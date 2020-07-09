from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import login ,logout, authenticate
from testapp.models import Course_table
from testapp.forms import Course_tableForm


# Create your views here.
def admin_login(request):
    if request.method=='POST':
        un=request.POST['username']
        pwd=request.POST['password']
        user=authenticate(username=un,password=pwd) 
        if user:
            login(request,user)
            if user.is_superuser:
                return HttpResponseRedirect('/admin_welcome')
    return render(request,'admin_login.html')
def admin_logout(request):
    logout(request)
    return redirect('/')     

def admin_welcome(request):
    return render(request,'admin_welcome.html')
#admin can show all records
def view_all_scheduled(request):
    course_list=Course_table.objects.all()
    return render(request,'view_all_scheduled.html', {'course_list':course_list})

#admin can insert new course information

def insert_new_curese_info(request):
    form=Course_tableForm()
    if request.method=='POST':
        form=Course_tableForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/admin_welcome')
    return render(request,'insert_new_curese_info.html',{'form':form})

def delete_curese(request,id):
    course_itm=Course_table.objects.get(id=id)
    course_itm.delete()
    return redirect('/view_all_scheduled')

def update_course(request,id):
    course_itm=Course_table.objects.get(id=id)
    if request.method=='POST':
        form=Course_tableForm(request.POST,instance=course_itm)
        if form.is_valid():
            form.save()
            return redirect('/admin_welcome')
    return render(request,'update_course.html',{'course_itm':course_itm})        