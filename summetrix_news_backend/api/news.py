# api/news.py
from flask import Blueprint, request, jsonify
import requests
from datetime import datetime, timedelta
from extensions import db
from models.news import news_schema, newss_schema
from models.news import News

news_api = Blueprint('news_api', __name__)
NEWS_API_KEY = '07a06d276cce4681a3351269be4a9074'  


@news_api.route('/news', methods=['GET'])
def get_news():
    # Get search term and language from query parameters
    search_term = request.args.get('search')
    language = request.args.get('language')
    
    # Get the 'from' and 'to' date query parameters (if provided)
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

    news_api_url = 'https://newsapi.org/v2/everything'
    params = {
        'apiKey': NEWS_API_KEY,
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
        return jsonify({'error': 'Failed to fetch news data','data':response.json()}), 500
    
@news_api.route('/news/favorite', methods=['POST'])
def add_to_favorites():
    try:
        # Get the news record data from the request
        news_data = request.get_json()

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

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
# Get All Favorite News
@news_api.route('/news/favorite', methods=['GET'])
def get_favorite_news():
    all_news = News.query.all()
    result = newss_schema.dump(all_news)
    return jsonify(result)

# Delete Favorite News
@news_api.route('/news/favorite', methods=['DELETE'])
def delete_favorite_news():
    news_data = request.get_json()
    print(news_data)
    news = News.query.get(news_data.get('url'))
    db.session.delete(news)
    db.session.commit()

    return news_schema.jsonify(news)