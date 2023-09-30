# api/news.py
from flask import Blueprint, abort, request, jsonify, current_app
import requests
from datetime import datetime, timedelta
from extensions import db
from models.news import news_schema, newss_schema
from models.news import News

news_api = Blueprint('news_api', __name__)


@news_api.route('/news', methods=['GET'])
def get_news():
    try:
        # Get search term and language 
        search_term = request.args.get('search')
        language = request.args.get('language')
        
        # Get the 'from' and 'to' date 
        from_date_str = request.args.get('from')
        to_date_str = request.args.get('to')

        # Calculate the default 'from' and 'to' dates for the previous month
        default_to_date = datetime.now()
        default_from_date = default_to_date - timedelta(days=30)

        # Parse the 'from' and 'to' dates if provided, or use the default dates
        if from_date_str and to_date_str:
            from_date = datetime.strptime(from_date_str, '%Y-%m-%d')
            to_date = datetime.strptime(to_date_str, '%Y-%m-%d')
        else:
            from_date = default_from_date
            to_date = default_to_date

        # Validate query parameters (e.g., search term and language)
        if not search_term:
            raise ValueError("Search term is required")
        if not language:
            raise ValueError("Language is required")
        
        news_api_url = 'https://newsapi.org/v2/everything'
        params = {
            'apiKey': current_app.config['NEWS_API_KEY'],
            'q': search_term,  # Search term
            'language': language,  # Language
            'from': from_date.strftime('%Y-%m-%d'),  # Convert dates to string
            'to': to_date.strftime('%Y-%m-%d'),
        }

        # Make the request to the News API
        response = requests.get(news_api_url, params=params)

        if response.status_code == 200:
            news_data = response.json()
            return jsonify(news_data)
        else:
            # Handle API request errors with appropriate HTTP status code and description
            return jsonify({'error': 'Failed to fetch news data', 'data': response.json()}), response.status_code
            
    except ValueError as ve:
        abort(400, description=str(ve))
    except Exception as e:
        abort(500, description=str(e))
    
@news_api.route('/news/favorite', methods=['POST'])
def add_to_favorites():
    try:
        # Get the news record data from the request
        news_data = request.get_json()
        
        # Validate required fields
        if 'title' not in news_data or 'url' not in news_data:
            # Raise a custom exception for validation error
            raise ValueError("Title and URL are required fields")

        # Create a new favorite news record and add it to the database
        favorite_news = News(
            title=news_data.get('title'),
            description=news_data.get('description'),
            author=news_data.get('author'),
            content=news_data.get('content'),
            source=news_data.get('source'),
            url=news_data.get('url'),
            urlToImage=news_data.get('urlToImage')
        )

        # Add the new record to the database
        db.session.add(favorite_news)
        db.session.commit()

        # Serialize the newly added favorite news record
        result = news_schema.dump(favorite_news)

        return jsonify({'message': 'News added to favorites successfully', 'data': result}), 201

    except ValueError as ve:
        abort(400, description=str(ve))
    except Exception as e:
        abort(500, description=str(e))
    
# Get All Favorite News
@news_api.route('/news/favorite', methods=['GET'])
def get_favorite_news():
    all_news = News.query.all()
    result = newss_schema.dump(all_news)
    return jsonify(result)

# Delete Favorite News
@news_api.route('/news/favorite/<path:url>', methods=['DELETE'])
def delete_favorite_news(url):
    news = News.query.get(url)
    
    if news is None:
        # Handle the case where the news item does not exist with a 404 Not Found response
        return jsonify({'error': 'News item not found'}), 404
    
    db.session.delete(news)
    db.session.commit()

    return news_schema.jsonify(news)


# Error handling for 404 Not Found (resource not found)
@news_api.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e.description), message="The requested resource was not found"), 404

# Error handling for 400 Bad Request (client error)
@news_api.errorhandler(400)
def bad_request(e):
    return jsonify(error=str(e.description), message="Bad request"), 400

# Error handling for 500 Internal Server Error (server error)
@news_api.errorhandler(500)
def internal_server_error(e):
    return jsonify(error=str(e.description), message="Internal server error"), 500