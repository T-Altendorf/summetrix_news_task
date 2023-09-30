# News Search Engine

This project is a simple News Search Engine with a Flask backend and a Node.js frontend.

It has the ability to save favorite articles to a database and to search for articles using the newsapi.org API.

Demo Hosted at [summetrix.timalti.com](https://summetrix.timalti.com)

## Getting Started

Follow these steps to set up and run the project locally.

### Backend (Flask)

1. Clone the repository:

   ```shell
   git clone https://github.com/T-Altendorf/summetrix_news_task
   cd summetrix_news_backend
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

   You can use the template given in "env_production_template.env" and then rename to ".env"

   ```
   SECRET_KEY='secret key'
   SQLALCHEMY_DATABASE_URI='database_uri'
   NEWS_API_KEY='news_api_key' # The news api key
   CORS_Origins="['*']" # allowed origins as a json list string
   ```
5. Initialize the database 
   ```shell
   python init_db.py
   ```

6. Run the Flask backend:

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

   The frontend should now be running on localhost. Check the port from the command line.

## Deployment

### Backend (Flask)

See the [Flask deployment guide](https://flask.palletsprojects.com/en/2.0.x/deploying/) for more information.

Make sure to set environment variables, including NEWS_API_KEY, in your hosting environment. There is a env_production_template.env file that needs to be renamed to .env and filled out with the appropriate values.

You can get a newsapi.org API key by signing up for a free account at https://newsapi.org/account.

After deploying, your Flask backend should be accessible via a public URL provided by the hosting platform.

### Frontend (Vite, React, TypeScript)

See the [Vite deployment guide](https://vitejs.dev/guide/build.html#command-line-interface) for more information.

Dont forget to set the VITE_API_URL environment variable to the URL of your Flask backend before building and then saving it to the .env.production file provided in the root folder.

You can then build using

```shell
npm run build
```

and then upload the files in the "dist" folder to your webspace.
