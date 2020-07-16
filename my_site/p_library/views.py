from django.shortcuts import render, redirect
from p_library.models import Book, Publisher
from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('index.html')
    books = Book.objects.all()
    biblio_data = {
        "title":"мою библиотеку",
        "books":books,
        "rng3": [i for i in range(100)]
    }
    return HttpResponse(template.render(biblio_data,request))
    
def books_list(request):
    template = loader.get_template('slash.html')
    books = Book.objects.all().order_by('publisher')
    book_data = {
        "title":"Моя библиотека",
        "books":books
    }
    return HttpResponse(template.render(book_data, request))
# Create your views here.
# Код из модуля, улучшеный и почищеный от лишних ветвлений
def book_increment(request):
    if request.method =="POST":
        book_id = request.POST["id"]
        if book_id:
            book = Book.objects.filter(id=book_id).first()
            if book:
                book.copy_count +=1
                book.save()
    return redirect('/index/')

def book_decrement(request):
    if request.method =="POST":
        book_id = request.POST["id"]
        if book_id:
            book = Book.objects.filter(id=book_id).first()
            if book:
                if book.copy_count<1:
                    book.copy_count = 0
                else:
                    book.copy_count -=1
                book.save()
    return redirect('/index/')
# Выдача данных для ветки publishers
def publishers_index(request):
    template = loader.get_template('publishers.html')
    publishers = Publisher.objects.all()
    pub_data = {
        "title":"Мои издательства",
        "publishers":publishers
    }
    return HttpResponse(template.render(pub_data, request))

# Обработка POST запроса для увеличения рейтинга publishers
def publisher_increment(request):
    if request.method =="POST":
        pub_id = request.POST["id"]
        if pub_id:
            pub = Publisher.objects.filter(id=pub_id).first()
            if pub:
                pub.rating +=1
                pub.save()
    return redirect('/publishers/')

# Обработка POST запроса для уменьшения рейтинга publishers
def publisher_decrement(request):
    if request.method =="POST":
        pub_id = request.POST["id"]
        if pub_id:
            pub = Publisher.objects.filter(id=pub_id).first()
            if pub:
                pub.rating -=1
                pub.save()
    return redirect('/publishers/')
