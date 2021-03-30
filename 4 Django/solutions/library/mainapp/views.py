from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import requests
import json
from .models import Book


def index(request):
    return render(request, 'mainapp/index.html')

# localhost:8000/search_books/?q=the+lord+of+the+rings&page=1
def search_books(request):
    '''searches openlibrary api and responds with json'''
    # http://openlibrary.org/search.json?q=the+lord+of+the+rings&page=1
    params = {
        'q': request.GET.get('search', ''),
        'page': request.GET.get('page', 1)
    }
    response = requests.get('http://openlibrary.org/search.json', params=params)
    api_data = json.loads(response.text)
    books = []
    for api_book in api_data['docs']:

        # only include books that have all required fields
        required_fields = ['title', 'author_name', 'cover_i', 'first_publish_year']
        has_required_fields = True
        for required_field in required_fields:
            if required_field not in api_book:
                has_required_fields = False
                break
        if not has_required_fields:
            continue
        
        key = api_book['key']
        favorited = Book.objects.filter(key=key).exists()
        book = {
            'key': key,
            'title': api_book['title'],
            'authors': ', '.join(api_book['author_name']),
            'cover_url': 'https://covers.openlibrary.org/b/id/' + str(api_book['cover_i']) + '-L.jpg',
            'year_published': api_book['first_publish_year'],
            'favorited': favorited# ????????
        }
        books.append(book)


        # if 'cover_i' in api_book:
        #     # https://covers.openlibrary.org/b/id/9255566-L.jpg
        #     book['cover_url'] = 'https://covers.openlibrary.org/b/id/' + str(api_book['cover_i']) + '-L.jpg'
        # else:
        #     book['cover_url'] = ''
        
        # if 'first_publish_year' in api_book:
        #     book['year_published'] = api_book['first_publish_year']
        # else:
        #     book['year_published'] = 0
        
        # if 'author_name' in api_book:
        #     book['authors'] = ', '.join(api_book['author_name'])
        # else:
        #     book['authors'] = ''

        
    return JsonResponse({'books': books})
    
    # params = {key: request.GET[key] for key in request.GET}
    # response = requests.get('http://openlibrary.org/search.json', params=request.GET)
    # return HttpResponse(response.text, content_type='application/json')


def favorite_book(request):
    # print(request.body)
    
    book_data = json.loads(request.body)
    # key = models.CharField(max_length=100)
    # title = models.CharField(max_length=200)
    # authors = models.CharField(max_length=200)
    # cover_url = models.CharField(max_length=100)
    # year_published = models.IntegerField()

    key = book_data['key']
    # get the book with the given key if it exists or None if it doesn't
    book = Book.objects.filter(key=key).first()
    if book is not None: # if the book is not None, delete it
        book.delete()
        favorited = False
    else: # otherwise, create it
        title = book_data['title']
        authors = book_data['authors']
        cover_url = book_data['cover_url']
        year_published = book_data['year_published']

        book = Book(key=key, title=title, authors=authors, cover_url=cover_url, year_published=year_published)
        book.save()

        favorited = True

    return JsonResponse({'favorited': favorited})


def favorites(request):
    favorited_books = Book.objects.all()
    books_data = []
    for book in favorited_books:
        books_data.append({
            'key': book.key,
            'title': book.title,
            'authors': book.authors,
            'cover_url': book.cover_url,
            'year_published': book.year_published,
            'favorited': True
        })
    return JsonResponse({'favorited_books': books_data})