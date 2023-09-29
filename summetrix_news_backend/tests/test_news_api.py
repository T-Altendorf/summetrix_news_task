import unittest
from models.news import News
from app import create_app, db

class NewsAPITestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app('config.TestingConfig')
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_get_news_status_code(self):
        response = self.client.get('/api/news?search=test&language=en')
        self.assertEqual(response.status_code, 200)
        
    def test_add_favorite_news(self):
        data = {
            "title": "Test News",
            "url": "http://test.url",
            "description": "Test Description",
            "author": "Test Author",
            "content": "Test Content",
            "source": {"name": "Test Source"},
            "urlToImage": "http://test.image.url"
        }
        response = self.client.post('/api/news/favorite', json=data)
        self.assertEqual(response.status_code, 201)
        news_in_db = News.query.filter_by(title="Test News").first()
        self.assertIsNotNone(news_in_db)
        
    def test_add_favorite_news_with_insufficient_data(self):
        # Create JSON data with missing required fields (title and url)
        data = {
            "description": "Test Description",
            "author": "Test Author",
            "content": "Test Content",
            "source": {"name": "Test Source"},
            "urlToImage": "http://test.image.url"
        }

        response = self.client.post('/api/news/favorite', json=data)

        # Check that the response status code is 400 (Bad Request)
        self.assertEqual(response.status_code, 400)

        # Check that the response contains an error message
        response_data = response.get_json()
        self.assertIn('error', response_data)
        self.assertEqual(response_data['error'], 'Title and URL are required fields')
        
    
    def test_delete_favorite_news(self):
    # Given: A news entry exists in the database.
        test_url = "http://test.url"
        news_item = News(
            url=test_url,
            title="Test Title",
            description="Test Description",
            author="Test Author",
            content="Test Content",
            source={"name": "Test Source"},
            urlToImage="http://test.image.url"
            )
        db.session.add(news_item)
        db.session.commit()
        # When: We send a DELETE request to the endpoint.
        response = self.client.delete(f'/api/news/favorite/{test_url}')
        # Then: We expect a successful response.
        self.assertEqual(response.status_code, 200)
        # And: The news item should no longer exist in the database.
        deleted_news = News.query.get(test_url)
        self.assertIsNone(deleted_news)
        # Optionally: Validate the returned JSON (if necessary)
        # response_data = response.get_json()
        # self.assertEqual(response_data["title"], "Test Title")  # Or any other field you wish to validate.

if __name__ == '__main__':
    unittest.main()