# models/news.py
from extensions import db, ma


class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    description = db.Column(db.Text)
    author = db.Column(db.String(255))
    content = db.Column(db.Text)
    publishedAt = db.Column(db.String(255))
    source = db.Column(db.JSON)
    url = db.Column(db.String(255))
    urlToImage = db.Column(db.String(255))


class NewsSchema(ma.Schema):
    class Meta:
        fields = (
            "id",
            "title",
            "content",
            "author",
            "publishedAt",
            "source",
            "url",
            "urlToImage",
        )
        model = News


news_schema = NewsSchema()
newss_schema = NewsSchema(many=True)
