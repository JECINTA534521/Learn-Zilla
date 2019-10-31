import urllib.request, json
from .models import Book

# Getting api key
api_key = None

# Getting the book base url
base_url = None


def configure_request(app):
    global api_key, base_url
    api_key = app.config["BOOKS_API_KEY"]
    base_url = app.config["BOOKS_API_BASE_URL"]


def get_books(category):
    """
    Function that gets the json response to our url request
    """
    get_books_url = base_url.format(category, api_key)
    with urllib.request.urlopen(get_books_url) as url:
        get_books_data = url.read()
        get_books_response = json.loads(get_books_data)

        books_results = None

        if get_books_response['results']:
            books_results_list = get_books_response['results']
            books_results = process_results(books_results_list)

    return books_results


def process_results(books_list):
    """
    Function  that processes the book result and transform them to a list of Objects
    Args:
        books_list: A list of dictionaries that contain book details
    Returns :
        books_results: A list of book objects
    """
    books_results = []
    for books_item in book_list:
        id = book_item.get('id')
        title = book_item.get('original_title')
        overview = book_item.get('overview')
        poster = book_item.get('poster_path')
        vote_average = book_item.get('vote_average')
        vote_count = book_item.get('vote_count')

        if poster:
            book_object = Book(id, title, overview, poster, vote_average, vote_count)
            book_results.append(book_object)

    return book_results


def get_books(id):
    get_books_details_url = base_url.format(id, api_key)
    with urllib.request.urlopen(get_books_details_url) as url:
        books_details_data = url.read()
        books_details_response = json.loads(books_details_data)

        books_object = None
        if books_details_response:
            id = books_details_response.get('id')
            title = books_details_response.get('original_title')
            overview = books_details_response.get('overview')
            poster = books_details_response.get('poster_path')
            vote_average = books_details_response.get('vote_average')
            vote_count = books_details_response.get('vote_count')

            book_object = Book(id, title, overview, poster, vote_average, vote_count)

    return book_object


def search_book(boook_name):
    search_book_url = 'https://www.googleapis.com/books/v1/volumes/zyTCAlFPjgYC?&key={}'.format(api_key, book_name)
    with urllib.request.urlopen(search_book_url) as url:
        search_book_data = url.read()
        search_book_response = json.loads(search_book_data)

        search_book_results = None

        if search_book_response['results']:
            search_book_list = search_book_response['results']
            search_boook_results = process_results(search_book_list)

    return search_book_results