from django.shortcuts import render,get_object_or_404
from django.http import JsonResponse
from .models import Book
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
def book_list(request):
    books = list(Book.objects.values())
    return JsonResponse(books, safe=False)


@csrf_exempt  # Disable CSRF just for this demo (not for production!)
def book_create(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        title = data.get('title')
        author = data.get('author')

        book = Book.objects.create(title=title, author=author)
        return JsonResponse({'message': 'Book created', 'book_id': book.id})
    return JsonResponse({'error': 'Invalid method'}, status=400)

@csrf_exempt  # Disable CSRF just for this demo (not for production!)
def book_update(request, book_id):
    
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST' or request.method == 'PUT':
        data = json.loads(request.body)
        book.title = data.get('title',book.title)
        book.author = data.get('author',book.author)
        book.save()
        return JsonResponse({'updated': True})
    return JsonResponse({'error': 'Invalid method'}, status=400)

@csrf_exempt  # Disable CSRF just for this demo (not for production!)
def book_delete(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    book.delete()
    return JsonResponse({'deleted': True})