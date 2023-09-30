// api.ts

const API_BASE_URL = import.meta.env.VITE_API_URL;

export const searchNews = async (
  searchTerm: string,
  language: string,
  from?: string,
  to?: string
) => {
  const url = `${API_BASE_URL}/news?search=${searchTerm}&language=${language}&from=${from}&to=${to}`;
  const response = await fetch(url);
  if (!response.ok) {
    throw new Error("Failed to fetch news");
  }
  const data = await response.json();
  if (data.status === "ok") {
    return data.articles; // Return only the 'articles' array
  } else {
    throw new Error("Failed to fetch news");
  }
};

export const getFavorites = async () => {
  const url = `${API_BASE_URL}/news/favorite`;
  const response = await fetch(url);
  if (!response.ok) {
    throw new Error("Failed to fetch news");
  }

  return response.json();
};

export const addToFavorites = async (newsData: any) => {
  const url = `${API_BASE_URL}/news/favorite`;
  const response = await fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(newsData),
  });
  if (!response.ok) {
    throw new Error("Failed to add news to favorites");
  }
  return response.json();
};

export const removeFromFavorites = async (newsData: any) => {
  const url = `${API_BASE_URL}/news/favorite/${newsData.id}`;
  const response = await fetch(url, {
    method: "DELETE",
    headers: {
      "Content-Type": "application/json",
    },
  });

  if (!response.ok) {
    throw new Error("Failed to remove news from favorites");
  }
  return response.json();
};
