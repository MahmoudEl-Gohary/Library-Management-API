import json
from flask import Flask, request, jsonify
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

books = []

def save_books():
    with open('books.json', 'w') as f:
        json.dump(books, f)

def load_books():
    with open('books.json', 'r') as f:
        return json.load(f)
    
load_books()

# add a new book
@app.route('/books', methods=['POST'])
def add_book():
    data = request.json
    
    # check if the request data have all the required fields
    if 'isbn' not in data:
        return jsonify({'error': 'ISBN is required'}), 400
    if 'title' not in data:
        return jsonify({'error': 'Title is required'}), 400
    if 'author' not in data:
        return jsonify({'error': 'Author is required'}), 400
    if 'published_year' not in data:
        return jsonify({'error': 'Year is required'}), 400
    
    # check if the book is already in the list
    for book in books:
        if book['isbn'] == data['isbn']:
            return jsonify({'error': 'Book with this ISBN already exists'}), 400

    books.append(data)
    save_books()
    return jsonify({'message': 'Book added successfully'}), 201


# list all books
@app.route('/books', methods=['GET'])
def list_books():
    return jsonify(books), 200

# search for books
@app.route('/books/search', methods=['GET'])
def search_books():
    author = request.args.get('author')
    published_year = request.args.get('published_year')
    
    filtered_books = books

    if author:
        filtered_books = [book for book in filtered_books if book['author'].lower() == author.lower()]
    if published_year:
        filtered_books = [book for book in filtered_books if str(book['published_year']) == str(published_year)]
    if author and published_year:
        filtered_books = [book for book in filtered_books if book['author'].lower() == author.lower() and str(book['published_year']) == str(published_year)]
    elif not author and not published_year:
        return jsonify({'error': 'Please provide author or published_year to search'}), 400

    return jsonify(filtered_books), 200

# Delete a book
@app.route('/books/<isbn>', methods=['DELETE'])
def delete_book(isbn):
    global books
    books = [book for book in books if book['isbn'] != isbn]
    save_books()
    return jsonify({'message': 'Book deleted successfully'}), 200


# update a book
@app.route('/books/<string:isbn>', methods=['PUT'])
def update_book(isbn):
    data = request.json
    for book in books:
        if book['isbn'] == isbn:
            book.update(data)
            save_books()
            return jsonify({'message': 'Book updated successfully'}), 200

    return jsonify({'error': 'Book not found'}), 404

# Swagger documentation setup
SWAGGER_URL = '/api-docs'
API_URL = '/static/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,  
    API_URL,      
    config={
        'app_name': "Library Management API"
    }
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
