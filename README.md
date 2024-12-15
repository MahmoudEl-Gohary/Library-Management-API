# Library Management API

A RESTful API for managing a collection of books.

## Prerequisites

- Python 3.10+
- Docker (optional for containerized deployment)
- Postman (for testing API endpoints, optional)

## Setup Instructions

### Run Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/MahmoudEl-Gohary/Library-Management-API.git
   cd library-management-api
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the API:
   ```bash
   python app.py
   ```

4. Access the API at:
   - Base URL: `http://127.0.0.1:5000`
   - Swagger UI: `http://127.0.0.1:5000/api-docs`

### Run with Docker

1. Build the Docker image:
   ```bash
   docker build -t library-api .
   ```

2. Run the Docker container:
   ```bash
   docker run -p 5000:5000 library-api
   ```

3. Access the API at:
   - Base URL: `http://127.0.0.1:5000`
   - Swagger UI: `http://127.0.0.1:5000/api-docs`

## API Endpoints

### Add a New Book
- **Method**: `POST`
- **URL**: `/books`
- **Body**:
  ```json
  {
    "isbn": "1234567890",
    "title": "Book Title",
    "author": "Author Name",
    "published_year": 2023
  }
  ```

### List All Books
- **Method**: `GET`
- **URL**: `/books`

### Search for Books
- **Method**: `GET`
- **URL**: `/books/search`
- **Query Parameters** (optional):
  - `author`
  - `published_year`

### Delete a Book
- **Method**: `DELETE`
- **URL**: `/books/<isbn>`

### Update a Book
- **Method**: `PUT`
- **URL**: `/books/<isbn>`
- **Body**:
  ```json
  {
    "title": "Updated Title",
    "author": "Updated Author",
    "published_year": 2024
  }
  ```

## Testing with Postman

- Import the `postman_collection.json` file into Postman.

## Data
- Books are stored in `books.json`. This file is created automatically if it doesn't exist.


