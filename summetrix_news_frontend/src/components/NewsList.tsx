import React, { Fragment } from "react";
import NewsItem from "./NewsItem";
import { addToFavorites, removeFromFavorites } from "../api";

interface NewsListProps {
  articles: any[];
  favoriteNews: any[];
  setFavoriteNews: (favoriteNews: any[]) => void;
  setError: (error: string | null) => void;
  emptyResult: boolean;
}

const NewsList: React.FC<NewsListProps> = ({
  articles,
  favoriteNews,
  setFavoriteNews,
  setError,
  emptyResult,
}) => {
  const handleAddToFavorites = async (newsData: any) => {
    try {
      setError(null);
      const data = await addToFavorites(newsData);
      // Update favorite news list
      setFavoriteNews([...favoriteNews, data.data]);
    } catch (error) {
      setError("There was an error adding the news to your favorites.");
      console.error(error);
    }
  };

  const handleRemoveFromFavorites = async (newsData: any) => {
    try {
      setError(null);
      const data = await removeFromFavorites(newsData);
      // Update your favorite news list
      setFavoriteNews(
        favoriteNews.filter((article) => article.url !== newsData.url)
      );
    } catch (error) {
      setError("There was an error removing the news from your favorites.");
      console.error(error);
    }
  };

  if (articles.length === 0) {
    return (
      <div className="text-light bg-dark d-flex justify-content-center align-items-center flex-column">
        {favoriteNews === articles ? ( // If the user is viewing favorites
          <Fragment>
            <h3>You have no favorite news articles</h3>
            <p>Click on the "Add to Favorites" button to add news articles</p>
          </Fragment> // If the user is not viewing favorites
        ) : emptyResult ? (
          <h3>There were no results for your search term.</h3>
        ) : (
          <h3>Search for news to display the here</h3>
        )}
      </div>
    );
  }

  return (
    <div className="text-light bg-dark d-flex justify-content-center align-items-center flex-column">
      {articles.map((article, index) => (
        <NewsItem
          key={index}
          article={article}
          addToFavorites={handleAddToFavorites}
          removeFromFavorites={handleRemoveFromFavorites}
          isFavorite={favoriteNews.some(
            (favoriteArticle) => favoriteArticle.url === article.url
          )}
        />
      ))}
    </div>
  );
};

export default NewsList;
