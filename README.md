# News Search Engine

This project is a News Search Engine with a Flask backend and a Node.js frontend.

## Getting Started

Follow these steps to set up and run the project locally.

### Backend (Flask)

1. Clone the repository:

   ```shell
   git clone <repository_url>
   cd news-search-engine
   ```

2. Create a virtual environment (optional but recommended):

   ```shell
    python -m venv venv
    source venv/bin/activate # On Windows, use `venv\Scripts\activate`

   ```

3. Install Python dependencies:

   ```shell
   pip install -r requirements.txt
   ```

4. Set up environment variables:

   TODO - add instructions for environments

   ```shell
   NEWS_API_KEY=<your_api_key>
   ```

5. Run the Flask backend:

   ```shell
   python app.py
   ```

The backend should now be running at http://localhost:5000.

### Frontend (Vite, React, TypeScript)

1. Install Node.js:

   Install Node.js from https://nodejs.org/en/download/

2. Navigate to the `frontend` directory:

   ```shell
   cd summetrix_news_frontend
   ```

3. Install Node.js dependencies:

   ```shell
   npm install
   ```

4. Start the development server:

   ```shell
   npm run dev
   ```

   The frontend should now be running at http://localhost:3000.
