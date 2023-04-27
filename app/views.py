from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .form import LoginForm, RegistartionForm,UserForm
from django.contrib.auth import authenticate, login, logout
from .models import User,Profile,Room,Conversation,Message
from django.core import serializers


def LoginView(request):
    form=LoginForm()
    if request.method =='POST':
        form=LoginForm(request.POST)
        
        if form.is_valid():
            user_name = form.cleaned_data['username']
            password = form.cleaned_data['password']
            if 'remeber_me' in request.POST:
                remeber_me = request.POST['remeber_me']
            else:
                remeber_me = None
            user = authenticate(username=user_name,password=password)
            if user is not None :
                login(request,user)
                if not remeber_me:
                    request.session.set_expiry(0)
                    request.session.save()
                return HttpResponseRedirect('/')
            else :
                return render(request,'Login.html',{'form':form , 'error': 'User name or passwor are wrong!!'})
            
    return render(request,'Login.html',{'form':form})


def RegisterView(request):
    form = RegistartionForm()
    form.set_up()
    if request.method =='POST':
        print(request.POST)
        form = RegistartionForm(request.POST)
        form.set_up()
        if 'TandC' not in request.POST:
            return render(request,'Register.html',{'form':form, 'error': 'Please agree to all the terms and condtition before creating an account!'})
        else:
            
            if form.is_valid():
                
                password=form.cleaned_data['password']
                confirm_password=form.cleaned_data['confirm_password']
                if password != confirm_password:
                    return render(request,'Register.html',{'form':form, 'error': 'Password does not match!'})
                user = User.objects.create_user(username=form.cleaned_data['username'],
                                                email=form.cleaned_data['email'],
                                                first_name=form.cleaned_data['first_name'],
                                                last_name=form.cleaned_data['last_name'],
                                                password=form.cleaned_data['password'])
                user.save()
                Profile.objects.create(user=user)
                login(request,user)
                request.session.set_expiry(0)
                request.session.save()
                return HttpResponseRedirect('/')
            else:
                return render(request,'Register.html',{'form':form, 'error': 'User already exists!'})
                
    return render(request,'Register.html',{'form':form})



@login_required(login_url='/login')
def Home(request):
    
    form = UserForm()
    form.set_up();
    try:
        user = Profile.objects.get(user= request.user)
    except User.DoesNotExist:
        return HttpResponseRedirect('/login')
    
    try:
        rooms=Room.objects.all()
    except Room.DoesNotExist:
        return render(request,'error.html')
    
    try:
        users= Profile.objects.exclude(user=user.user)
    except User.DoesNotExist:
        return render(request,'error.html')
    rn= []
    users = users.exclude(user__username__in = user.conversation.values_list('name'))
    
   
    
    if request.method=="POST":
        if "new_message" in request.POST:
            reciver = users.get(id=request.POST['new_message'])
            room=Room.objects.create()
            room.members.add(user,reciver)
            conf=Conversation.objects.create(name=str(reciver.user.username),room=room,avatar=reciver.avatar)
            conf1=Conversation.objects.create(name=str(user.user.username),room=room,avatar=user.avatar)
            user.conversation.add(conf)
            reciver.conversation.add(conf1)
            return HttpResponseRedirect('/')
            
    return render(request,'index.html',{'user':user,'roms': rooms,'contacts':users,'form':form})


def converastion(request,id):
    try:
        rooms=Room.objects.all()
    except Room.DoesNotExist:
        return render(request,'error.html')
    try:
        messages=Message.objects.filter(room=id);
    except Message.DoesNotExist:
        return render(request,'error.html')
    
    return JsonResponse({"messages":list(messages.values())})
        

def Send(request):

    try:
        room=Room.objects.get(id=request.POST['roomID']) 
    except Room.DoesNotExist:
        return HttpResponse('no oki');
    message = Message.objects.create(user=request.user.username,room=room,value=request.POST['value'])
    print(message)
    
    return HttpResponse('oki');