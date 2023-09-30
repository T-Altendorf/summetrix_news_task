// App.tsx
import React, { useState, useEffect } from "react";
import Header from "./components/Header";
import SearchBar from "./components/SearchBar";
import NewsList from "./components/NewsList";
import { searchNews, getFavorites } from "./api";

function App() {
  const [searchResults, setSearchResults] = useState([]);
  const [viewingFavorites, setViewingFavorites] = useState(false);
  const [favoriteNews, setFavoriteNews] = useState<any[]>([]);
  const [error, setError] = useState<string | null>(null); // State for error messages
  const [emptyResult, setEmptyResult] = useState<boolean>(false); // State for error messages

  // Retrieve favorite news articles when the component mounts
  useEffect(() => {
    const fetchFavoriteNews = async () => {
      try {
        setError(null);
        const data = await getFavorites();
        setFavoriteNews(data);
      } catch (error) {
        setError("There was an error fetching your favorite news.");
        console.error(error);
      }
    };

    fetchFavoriteNews();
  }, []);

  const clearError = () => {
    setError(null);
  };

  const handleSearch = async (
    searchTerm: string,
    language: string,
    from?: string,
    to?: string
  ) => {
    viewingFavorites && setViewingFavorites(false);
    try {
      setError(null);
      const data = await searchNews(searchTerm, language, from, to);
      setSearchResults(data);
      if (data.length == 0) {
        setEmptyResult(true);
      } else {
        setEmptyResult(false);
      }
    } catch (error) {
      setError("There was an error fetching your search results.");
      console.error(error);
    }
  };

  return (
    <div className="container text-light bg-dark d-flex flex-column vh-100">
      <Header />
      {error && (
        <div className="alert alert-danger d-flex justify-content-between align-items-center">
          <div className="error-text text-center">{error}</div>
          <button className="btn btn-danger" onClick={clearError}>
            Clear
          </button>
        </div>
      )}
      <SearchBar
        onSearch={handleSearch}
        onViewingFavorites={setViewingFavorites}
        viewingFavorites={viewingFavorites}
        setError={setError}
      />
      <div className="mb-4 pt-1 overflow-y-auto ">
        <NewsList
          articles={viewingFavorites ? favoriteNews : searchResults}
          favoriteNews={favoriteNews}
          setFavoriteNews={setFavoriteNews}
          setError={setError}
          emptyResult={emptyResult}
        />
      </div>
    </div>
  );
}

export default App;
