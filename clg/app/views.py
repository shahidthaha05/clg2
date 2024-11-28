from django.shortcuts import render,redirect
from .forms import *
from .models import *


# Create your views here.
def home(req):
    return render(req,'home.html',)
def about(req):
    return render(req,'about.html',)
def contact(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect(contact)  
    else:
        form = MessageForm()

    return render(request, 'contact.html', {'form': form})
    
def course(req):
    if req.method=='POST':
        form=course_form(req.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            phone=form.cleaned_data['phone']
            email=form.cleaned_data['email']
            message=form.cleaned_data['message']
            coursee=form.cleaned_data['coursee']
            data=Students.objects.create(name=name,phone=phone,email=email,message=message,coursee=coursee)
            data.save()
            return redirect(course)
    form=course_form()
    return render(req,'course.html',{'form':form})

# coursess

def course1(req):
    if req.method=='POST':
        form=course_form(req.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            phone=form.cleaned_data['phone']
            email=form.cleaned_data['email']
            message=form.cleaned_data['message']
            coursee=form.cleaned_data['coursee']
            data=Students.objects.create(name=name,phone=phone,email=email,message=message,coursee=coursee)
            data.save()
            return redirect(thanks)
    form=course_form()
    return render(req,'course1.html',{'form':form})



def course2(req):
    if req.method=='POST':
        form=course_form(req.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            phone=form.cleaned_data['phone']
            email=form.cleaned_data['email']
            message=form.cleaned_data['message']
            coursee=form.cleaned_data['coursee']
            data=Students.objects.create(name=name,phone=phone,email=email,message=message,coursee=coursee)
            data.save()
            return redirect(thanks)
    form=course_form()
    return render(req,'course2.html',{'form':form})

def course3(req):
    if req.method=='POST':
        form=course_form(req.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            phone=form.cleaned_data['phone']
            email=form.cleaned_data['email']
            message=form.cleaned_data['message']
            coursee=form.cleaned_data['coursee']
            data=Students.objects.create(name=name,phone=phone,email=email,message=message,coursee=coursee)
            data.save()
            return redirect(thanks)
    form=course_form()
    return render(req,'course3.html',{'form':form})


def course4(req):
    if req.method=='POST':
        form=course_form(req.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            phone=form.cleaned_data['phone']
            email=form.cleaned_data['email']
            message=form.cleaned_data['message']
            coursee=form.cleaned_data['coursee']
            data=Students.objects.create(name=name,phone=phone,email=email,message=message,coursee=coursee)
            data.save()
            return redirect(thanks)
    form=course_form()
    return render(req,'course4.html',{'form':form})



def course5(req):
    if req.method=='POST':
        form=course_form(req.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            phone=form.cleaned_data['phone']
            email=form.cleaned_data['email']
            message=form.cleaned_data['message']
            coursee=form.cleaned_data['coursee']
            data=Students.objects.create(name=name,phone=phone,email=email,message=message,coursee=coursee)
            data.save()
            return redirect(thanks)
    form=course_form()
    return render(req,'course5.html',{'form':form})

def thanks(req):
    return render(req,'thanks.html')