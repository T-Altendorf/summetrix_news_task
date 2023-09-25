# models/news.py
from datetime import datetime
from extensions import db, ma

class News(db.Model):
    title = db.Column(db.String(255))
    description = db.Column(db.Text)
    author = db.Column(db.String(255))
    content = db.Column(db.Text)
    published_at = db.Column(db.DateTime, default=datetime.utcnow)
    source = db.Column(db.JSON) 
    url = db.Column(db.String(255), primary_key=True)
    urlToImage = db.Column(db.String(255))
    
class NewsSchema(ma.Schema):
    class Meta:
        fields = ("title", "content", "author", "published_at", "source", "url", "urlToImage")
        model = News

news_schema = NewsSchema()
newss_schema = NewsSchema(many=True)
