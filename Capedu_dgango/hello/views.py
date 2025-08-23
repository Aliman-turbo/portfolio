from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.http import HttpResponseNotFound
from django.http import JsonResponse
def set_cookie_view(request):
    # response = HttpResponse("Cokie установлена")
    # response.set_cookie("user_id","12345",max_age=3600)
    # return response
    username = request.GET.get("username","UNDEFIND")
    responce = HttpResponse(f"Hello{username}")
    responce.set_cookie("username",username)
    return responce
def get_cookie_view(request):
    user_id = request.COOKIES.get('user_id','Неизвестный пользховател')
    return HttpResponse(f"id Пользователя:{user_id}")
def json_responce(request):
    data = {"NAME":"TOM","AGE":"41"}
    return JsonResponse(data)
def error_404(request,exception):
    return HttpResponseNotFound("Страница не найдена")
def redirect_func(request):
    return redirect("/contact")

def index(request,id):
    host = request.META["HTTP_HOST"]
    user_agent = request.META["HTTP_USER_AGENT"]#Browzer info
    path = request.path

    return HttpResponse(f"<h2>Hello Ваш Host:{host}</h2><p>Ваш user_agent{user_agent}</p><p>Ваш path:{path}</p>")
# Create your views here.
def contact(request):
    return HttpResponse("http://127.0.0.1:8000/about")

def about(reques,name,age):
    return HttpResponse(f"<h2>Школа программирования</h2><p>Имя:{name}</p><p>Возраст:{age}</p>")
def about_us(request):
    return HttpResponse("Школа программирования учит пайтон")
def users(request,name):
    return HttpResponse(f"<h1>Ваше имя:{name}</h1>")
def request_info(request):
    method = request.method
    path = request.path
    user_agent  = request.headers.get("User-agent")
    host = request.get_host()
    responce_answer = f"Метод:{method} Url{path}  user_agent:{user_agent} host:{host}"
    return HttpResponse(responce_answer)
def products(request,id):
    return HttpResponse(f"<h2>Продукты id{id}</h2>")
def products_new(request,id):
    return HttpResponse(f"<h2>Новые продукты {id}</h2>")
def products_top(request,id):
    return HttpResponse(f"<h2>Топовые Продукты id{id}</h2>")
def stat(request,id):
    return HttpResponse(f"<h2> Id Статьи{id}</h2>")
def stat_new(request,id):
    return HttpResponse(f"<h2>Новая Статья  её id{id}</h2>")
def stat_top(request):
    id = request.GET.get("id","Не указан id")
    return HttpResponse(f"<h2>Топовой Статьи id{id}</h2>")
def stat1(request,id):
    return HttpResponse(f"<h2> Id Статьи{id}</h2>")
def stat_new1(request):
    id = request.GET.get("id", "Не указан id")
    return HttpResponse(f"<h2>Новая Статья  её id{id}</h2>")
def stat_top1(request):
    id = request.GET.get("id", "Не указан id")
    return HttpResponse(f"<h2>Топовой Статьи id{id}</h2>")
def user(request):
    age = request.GET.get("age","Неизвестно")
    name = request.GET.get("name","Неизвестно")
    return HttpResponse(f"Name:{name} age:{age}")

def custom_answer(request):
    responce = HttpResponse("Secret code:",content_type="text/plain; charset=utf-8")
    responce["Secret_code"] = "123471"
    return responce
def custom_answer1(request):
    return HttpResponse("Hello",headers={"Secret_code":"149364"})

