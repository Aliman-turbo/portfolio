from django.shortcuts import render,redirect,get_object_or_404
from .models import User,Message
from .forms import User_form, Message_form, MessageEditForm
from django.http import HttpResponse

def register(request):
    if request.method == 'POST':
        form = User_form(request.POST)
        if form.is_valid():
            user = form.save()
            request.session['user_id'] = user.id
            return redirect('chat')
    else:
        form = User_form()

    return render(request, 'register.html',{'form':form})
from django.shortcuts import render, redirect
from .models import User, Message
from .forms import Message_form

def chat(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('register')

    user = User.objects.get(id=user_id)
    messages = Message.objects.all().order_by('-timestamp')

    if request.method == 'POST':
        if 'edit_message_id' in request.POST:
            message_id=request.POST['edit_message_id']
            message = get_object_or_404(Message,id = message_id)
            if message.user == user:
                form = MessageEditForm(request.POST,instance=message)
                if form.is_valid():
                    form.save()
                    return redirect('chat')
        elif 'see_one' in request.POST:
            message_id=request.POST['see_one']
            message = get_object_or_404(Message,id = message_id)
            if message.user == user:
                form = MessageEditForm(request.POST,instance=message)
                if form.is_valid():
                    form.save()
                    return redirect('chat')

        elif 'delete_message_id' in request.POST:
            message_id = request.POST['delete_message_id']
            message=get_object_or_404(Message,id = message_id  )
            if message.user == user:
                message.delete()
                return redirect('chat')
        else:
            form = Message_form(request.POST)
            if form.is_valid():
                 message = form.save(commit=False)
                 message.user = user
                 message.save()
                 return redirect('chat')
    else:
        form = Message_form()
    return render(request, 'chat.html', {"user": user,"messages": messages,"form": form
         })






    #     form = Message_form(request.POST)
    #     if form.is_valid():
    #         message = form.save(commit=False)
    #         message.user = user
    #         message.save()
    #         return redirect('chat')
    # else:
    #     form = Message_form()
    #
    # return render(request, 'chat.html', {"user": user,"messages": messages,"form": form
    # })

