from django.shortcuts import render,redirect,get_object_or_404
from.models import Task
from django.http import HttpResponse
from  .forms import UserForm
# def index(request):
#     task = Task.objects.all()
#     return render(request,"tasks/index.html",{"tasks":task})
# def view_task(request,task_id):
#     task =get_object_or_404(Task,pk=task_id)
#     return render(request,"tasks/view_task.html",{"task":task})
# def create_task(request):
#     if request.method == "POST":
#         title = request.POST["title"]
#         description = request.POST.get("description",'')
#
#         Task.objects.create(title=title,description=description)
#         return redirect("index")
#     return render(request,"tasks/create_task.html")
# def edit_task(request,task_id):
#     task = get_object_or_404(Task,pk=task_id)
#     if request.method =="POST":
#         task.title = request.POST["title"]
#         task.description = request.POST.get("description", '')
#         task.discription2 = request.POST.get("description2", '')
#         task.completed = "completed" in request.POST
#         task.save()
#         return redirect("index")
#     return render(request,"tasks/edit_task.html",{"task":task})
# def delete_task(request,task_id):
#     task = get_object_or_404(Task,pk=task_id)
#     if request.method == "POST":
#         task.delete()
#         return redirect("index")
#     return render(request, "tasks/delete_task.html", {"task": task})
# def index(request):
#     return render(request,"index.html",context={"body":"<h1>Hello world!</h1>"})
def index(request):
    # data = {"n":5}
    # langs = ["Сделать дз","выучить java","пойти на улицу"]
    # data = {"langs":langs}
    # return render(request,"index.html",context=data)
    # return render(request,'index.html')
    # user_form = UserFor
    # return render(request,'index.html',{'form':user_form})
    # if request.method == 'POST':
    #     # name = request.POST.get('name')
    #     # age = request.POST.get('age')
    #     # return HttpResponse(f"Hello{name } age:{age}")
    #     name = request.POST.get('name', 'undefind')
    #     age = request.POST.get('age', 1)
    #     lang = request.POST.getlist('languages', ["Python"])
    #     return HttpResponse(f'<div> Name:{name} Age:{age} <div><div>Languages{lang}</div>')
    # else:
    #     user_form = UserForm()
    #     return render(request,'index.html',{'forms':user_form})

    # user_form = UserForm()
    # return render(request,'index.html',{"form":user_form})
    user_form = UserForm()
    if request.method == "POST":
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            name = user_form.cleaned_data['name']
            password = user_form.cleaned_data['password']
            email = user_form.cleaned_data['email']
            return  HttpResponse(f'Hello{name} {password} {email}')
    return render(request, 'index.html', {"form": user_form})


    # if request.method == "POST":
    #     user_form=UserForm(request.POST)
    #     if user_form.is_valid():
    #         name=user_form.cleaned_data['name']
    #     else:
    #         return HttpResponse("INVALID DATA")
    #     # age = request.POST.get("age")
    #     # name = request.POST.get("name")
    #     # date = request.POST.get("date")
    #     # email = request.POST.get("email")
    #     # file = request.POST.get("file")
    #     # return HttpResponse(f"NAME:{name} date:{date} email:{email} age:{age} file:{file}")
    #     return HttpResponse(f"NAME:{name}")
    # else:
    #     user_form=UserForm()
    #     return render(request, 'index.html', {"form": user_form})


# def contacs(request):
#     return render(request,'Contacs.html')



# def post_user(request):
#     name=request.POST.get('name','undefind')
#     age = request.POST.get('age',1)
#     lang=request.POST.getlist('languages',["Python"])
#     return HttpResponse(f'<div> Name:{name} Age:{age} <div><div>Languages{lang}</div>')