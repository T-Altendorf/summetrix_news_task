// App.tsx
import React, { useState, useEffect } from "react";
import Header from "./components/Header";
import SearchBar from "./components/SearchBar";
import NewsList from "./components/NewsList";
import { searchNews, addToFavorites, getFavorites } from "./api";

function App() {
  const [searchResults, setSearchResults] = useState([]);
  const [viewingFavorites, setViewingFavorites] = useState(false);
  const [favoriteNews, setFavoriteNews] = useState<any[]>([]);

  // Retrieve favorite news articles when the component mounts
  useEffect(() => {
    const fetchFavoriteNews = async () => {
      try {
        const data = await getFavorites();
        setFavoriteNews(data);
      } catch (error) {
        console.error(error);
      }
    };

    fetchFavoriteNews();
  }, []);

  const handleSearch = async (
    searchTerm: string,
    language: string,
    from?: string,
    to?: string
  ) => {
    viewingFavorites && setViewingFavorites(false);
    try {
      const data = await searchNews(searchTerm, language, from, to);
      setSearchResults(data);
    } catch (error) {
      console.error(error);
    }
  };

  const setFavoriteNewsWrapper = (favoriteNews: any[]) => {
    setFavoriteNews(favoriteNews);
    console.log(favoriteNews);
  };

  return (
    <div className="container text-light bg-dark d-flex flex-column vh-100">
      <Header />
      <SearchBar
        onSearch={handleSearch}
        onViewingFavorites={setViewingFavorites}
        viewingFavorites={viewingFavorites}
      />
      <div className="mb-4 pt-1 overflow-y-auto ">
        <NewsList
          articles={viewingFavorites ? favoriteNews : searchResults}
          favoriteNews={favoriteNews}
          setFavoriteNews={setFavoriteNewsWrapper}
        />
      </div>
    </div>
  );
}

export default App;
