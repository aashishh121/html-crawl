import React, { useState } from "react";
import { Globe, Loader2, Search } from "lucide-react";
import SearchResult from "../SearchResult";

function SearchContent() {
  const [url, setUrl] = useState("");
  const [query, setQuery] = useState("");
  const [searchResults, setSearchResults] = useState([]);
  const [loading, setLoading] = useState(false);
  const [urlError, setUrlError] = useState("");

  const validateUrl = (url: string) => {
    const regex =
      /^(https?:\/\/)?([a-z0-9-]+\.)+[a-z0-9]{2,6}(\/[\w-]*)*(\?[a-z0-9&=]*)?(#[\w-]*)?$/i;
    return regex.test(url);
  };

  const getResults = async () => {
    if (!url || !query) {
      return;
    }

    if (!validateUrl(url)) {
      setUrlError("Please enter a valid URL.");
      return;
    } else {
      setUrlError("");
    }

    console.log("called");
    setLoading(true);
    try {
      const resp = await fetch("http://127.0.0.1:8000/api/v1/search", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          url: url,
          query: query,
        }),
      });

      if (!resp.ok) {
        throw new Error("Failed to fetch results");
      }

      const results = await resp.json();
      if (results) {
        console.log(results, "results");
        setSearchResults(results);
      }
    } catch (error) {
      console.error("Error fetching results:", error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <h1 className="text-2xl font-bold text-center">Website Content Search</h1>
      <p className="text-gray-500 text-sm mb-10 font-semibold text-center">
        Search through website content with precision
      </p>

      <div className="relative ">
        <span className="absolute inset-y-0 left-0 pl-3 flex items-center text-gray-400">
          <Globe className="h-5 w-5" />
        </span>
        <input
          type="text"
          placeholder="Enter Website URL"
          value={url}
          onChange={(e) => setUrl(e.target.value)}
          className="border p-2 pl-10 rounded-md w-full"
          required
        />
        {/* Show URL error message */}
      </div>
      {urlError && <p className="text-red-500 text-sm mb-2">{urlError}</p>}

      <div className="relative flex items-center mt-2">
        <span className="absolute inset-y-0 left-0 pl-3 flex items-center text-gray-400">
          <Search className="h-5 w-5" />
        </span>
        <input
          type="text"
          placeholder="Enter Search Query"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          className="border p-2 pl-10 pr-24 rounded-md w-full"
          required
        />
        <button
          type="submit"
          disabled={loading}
          onClick={() => getResults()}
          className="flex items-center gap-2 absolute right-1 py-1 bg-blue-500 text-white px-4 rounded-md hover:bg-blue-600"
        >
          {loading ? (
            <>
              <Loader2 className="h-4 w-4 animate-spin" /> Searching...
            </>
          ) : (
            "Search"
          )}
        </button>
      </div>

      <div>
        <SearchResult searchResults={searchResults} />
      </div>
    </div>
  );
}

export default SearchContent;
