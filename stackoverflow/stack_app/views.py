from django.shortcuts import render,redirect
from .models import Answers,Questions
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.core.exceptions import ObjectDoesNotExist
from django import forms
from django.conf import settings
from django.db import IntegrityError
from django.contrib.auth.models import User
from .forms import RegisterForm
from django.core.mail import send_mail
# Create your views here.

def index(request):
    q=Questions.objects.order_by("date").reverse()
    return render(request,'index.html',{'questions':q})

def login_user(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            
            return redirect('stack_app:index')
        else:
            return render(request,'login.html',{'message':'Invalid credentials!'})
    else:
        return render(request,'login.html')

def signup(request):
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            if User.objects.filter(username=form.cleaned_data['username']).exists():
                    return render(request, 'signup.html', {
                        'form': form,
                        'error_message': 'Username already exists.'
                    })
            elif User.objects.filter(email=form.cleaned_data['email']).exists():
                    return render(request, 'signup.html', {
                        'form': form,
                        'error_message': 'Email already exists.'
                    })
            elif form.cleaned_data['password'] != form.cleaned_data['password_repeat']:
                    return render(request, 'signup.html', {
                        'form': form,
                        'error_message': 'Passwords do not match.'
                    })
            else:
                
                user = User.objects.create_user(
                        form.cleaned_data['username'],
                        form.cleaned_data['email'],
                        form.cleaned_data['password']
                    )
                subject='User Registration Successful'
                message=f"Hey {form.cleaned_data['username']}, you have successfully created an account in initOverflow. Thanks."
                from_addr=settings.EMAIL_HOST_USER
                to_addr=[form.cleaned_data['email']]
                user.save()
                send_mail(subject, message, from_addr, to_addr)
                    # Login the user
                login(request, user)
            return redirect('stack_app:index')
        
    else:
        form=RegisterForm()
    return render(request,'signup.html',{'form':form})

def logout_user(request):
    logout(request)
    q=Questions.objects.order_by('date').reverse()
    return render(request,'index.html',{'questions':q})

def create(request):
    if request.method=='POST':
        question=request.POST.get('question')
        try:
            a=Questions(question=question)
            a.user_id =request.user
            a.save()
            return redirect('stack_app:index')
        except IntegrityError:
            return render(request,'create.html',{'message':'This question is already been asked!'})
       
    return render(request,'create.html')
def my_ques(request):
    ques=Questions.objects.filter(user_id=request.user).order_by('date').reverse()  
    return render(request,'my_ques.html',{"a":ques})
def question(request,ques):
    if request.method=='POST':
        print(ques)
        answer=request.POST['answer']
        question=Questions.objects.filter(slug=ques).first()
        try:
            a=Answers(answer=answer)
            a.ques_id=question
            a.user_id=request.user
            a.save()

            questions=Questions.objects.filter(slug=ques).first()
            ques=questions.ques_id
            try:
                answer=Answers.objects.filter(ques_id=ques).order_by('date').reverse()
            except ObjectDoesNotExist:
                return render(request,'question.html',{'question':questions})
            return render(request,'question.html',{'question':questions,'answers':answer})
        except IntegrityError:
            questions=Questions.objects.filter(slug=ques).first()
            ques=questions.ques_id
            try:
                answer=Answers.objects.filter(ques_id=ques).order_by('date').reverse()
            except ObjectDoesNotExist:
                return render(request,'question.html',{'question':questions})
            return render(request,'question.html',{'question':questions,'answers':answer,'error':"Can't post an existing answer!"})

       
    
    else:
        questions=Questions.objects.get(slug=ques)
        ques=questions.ques_id
        try:
            answer=Answers.objects.filter(ques_id=ques).reverse()
        except ObjectDoesNotExist:
            return render(request,'question.html',{'question':questions})
    return render(request,'question.html',{'question':questions,'answers':answer})
