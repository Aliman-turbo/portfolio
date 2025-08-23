from django.http import HttpResponse
from .models import Book
from django.shortcuts import render
def home(request):
    return HttpResponse('<h1>Привет!</h1>добро пожаловать')
def books(request):
    return HttpResponse('страница с книгами')
# def employee_info(request):
#     return HttpResponse('«Здесь будет полезная информация для сотрудников».')
def employee_detail(request,employee_id):
    response = f'<h1>employee:{employee_id}<h1>'
    return HttpResponse(response)
#ЭТО Я ДЕЛАЛ ДЗ
def book_detail(request,book_id):
    book = Book.objects.get(id = book_id)
    return render(request,'book_detail.html',{'book':book})


