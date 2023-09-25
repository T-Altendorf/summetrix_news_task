import React, { Fragment, useState } from "react";

interface SearchBarProps {
  onSearch: (
    searchTerm: string,
    language: string,
    from?: string,
    to?: string
  ) => void;
  onViewingFavorites: (viewingFavorites: boolean) => void;
  viewingFavorites: boolean;
}

const SearchBar: React.FC<SearchBarProps> = ({
  onSearch,
  onViewingFavorites,
  viewingFavorites,
}) => {
  const [searchTerm, setSearchTerm] = useState("");
  const [language, setLanguage] = useState("en");
  const [fromDate, setFromDate] = useState(getOneMonthAgo());
  const [toDate, setToDate] = useState(new Date().toISOString().split("T")[0]);

  const handleSearch = () => {
    onSearch(searchTerm, language, fromDate, toDate);
  };

  function getOneMonthAgo() {
    const currentDate = new Date();
    currentDate.setMonth(currentDate.getMonth() - 1); // Subtract one month
    return currentDate.toISOString().split("T")[0]; // Format as yyyy-mm-dd
  }

  return (
    <Fragment>
      <div className="search-bar">
        <div className="row mb-4">
          <div className="col-md-4">
            Search term
            <input
              type="text"
              className="form-control"
              placeholder="Search..."
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
            />
          </div>

          <div className="col-md-2">
            From
            <input
              type="date"
              placeholder="From Date"
              className="form-control"
              min={getOneMonthAgo()}
              value={fromDate}
              onChange={(e) => setFromDate(e.target.value)}
            />
          </div>

          <div className="col-md-2">
            To
            <input
              type="date"
              placeholder="To Date"
              className="form-control"
              min={fromDate}
              value={toDate}
              onChange={(e) => setToDate(e.target.value)}
            />
          </div>
          <div className="col-md-2">
            Language
            <select
              className="form-select"
              value={language}
              onChange={(e) => setLanguage(e.target.value)}
            >
              <option value="en">English</option>
              <option value="de">German</option>
              {/* Add more language options */}
            </select>
          </div>
          <div className="col-md-2">
            <span className="invisible">Search</span>
            <button
              className="btn btn-primary btn-block"
              style={{ width: "100%" }}
              onClick={handleSearch}
            >
              Search
            </button>
          </div>
        </div>
        <div className="row mb-4  justify-content-right">
          <div className="col-md-10">
            {viewingFavorites ? (
              <h2>Favorite News:</h2>
            ) : (
              <h2>Search Results:</h2>
            )}
          </div>
          <div className="col-md-2">
            <button
              className="btn btn-secondary"
              style={{ width: "100%" }}
              onClick={() => onViewingFavorites(!viewingFavorites)}
            >
              {viewingFavorites ? "View Search Results" : "View Favorite News"}
            </button>
          </div>
        </div>
      </div>
    </Fragment>
  );
};

export default SearchBar;
