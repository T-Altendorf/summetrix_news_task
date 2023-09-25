import React from "react";
//import style
import "./NewsItem.css";
import { addToFavorites } from "../api";

interface NewsItemProps {
  article: any; // Replace with the actual news article type
  addToFavorites?: (newsData: any) => void;
  removeFromFavorites?: (newsData: any) => void;
  isFavorite: boolean;
}

const NewsItem: React.FC<NewsItemProps> = ({
  article,
  addToFavorites,
  removeFromFavorites,
  isFavorite,
}) => {
  const formattedDate = new Date(article.publishedAt).toLocaleDateString(
    "en-US",
    {
      year: "numeric",
      month: "long",
      day: "numeric",
      hour: "2-digit",
      minute: "2-digit",
    }
  );

  return (
    <div className="container news-item">
      <div className="row">
        <div className="col-md-3 d-flex  justify-content-center align-items-center">
          <div>
            <img
              className="img-thumbnail"
              src={article.urlToImage}
              alt={article.title}
            />
          </div>
        </div>
        <div className="col-md-9">
          <div className="news-item-details">
            <a href={article.url} className="news-hyperlink" target="blank">
              <h3>{article.title}</h3>
            </a>
            <p>
              {formattedDate} by{" "}
              <a className="badge bg-light text-dark text-decoration-none">
                {article.source.name}
              </a>
            </p>
            <p>{article.content}</p>
            <div className="news-item-meta"></div>
            {addToFavorites !== undefined && !isFavorite && (
              <button
                className="btn btn-success"
                onClick={() => addToFavorites(article)}
              >
                Add to Favorites
              </button>
            )}
            {removeFromFavorites !== undefined && isFavorite && (
              <button
                className="btn btn-danger"
                onClick={() => removeFromFavorites(article)}
              >
                Delete from Favorites
              </button>
            )}
          </div>
        </div>
      </div>
    </div>
  );
};

export default NewsItem;
