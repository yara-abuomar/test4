from django.shortcuts import render ,redirect 
from .models import *
from django.contrib import messages

def method(request):
    return render(request ,'form.html' )

def method1 (request):
    print("hiii")
    print(request.POST['releasedate'])
    errors=Show.objects.basic_validator(request.POST)
    if len(errors)>0:
        for key ,values in errors.items():
            messages.error(request,values)
        return redirect('/shows/new')

    show1=Show.creatshow(title1=request.POST['tname'],network1=request.POST['net'],description1=request.POST['desc'],reldate=request.POST['releasedate'])
    return redirect('/shows/'+ str(show1.id))
def method2(request):
    context={
        'show':Show.readone()
    }
    return render(request ,'show.html' ,context)

def method3(request):
    context={
        'all':Show.readshow(),
    }
    return render(request ,'all.html' ,context)
def method4(request,id):
    ss=Show.objects.get(id=int(id))
    ss.delete()
    return redirect('/shows')

def method5(request,num):
    context={
         'show':Show.objects.get(id=int(num))
     }
    return render(request ,'show.html' ,context)

def method6(request,num2):
    errors1=Show.objects.basic_validator2(request.POST)
    if len(errors1)>0:
        for key ,values in errors1.items():
            messages.error(request,values)
        return redirect('/shows/' + str(num2) + '/edit')
    else:
        up=Show.objects.get(id=int(num2))
        up.title=request.POST['ttname']
        up.network=request.POST['nett']
        up.description=request.POST['descr']
        up.releasedate=request.POST['releasedatee']
        up.save()
        messages.success(request, "Show successfully updated")
        return redirect('/shows/' + str(num2))
    
def method7(request,num1):
    
    context={
         'edit':Show.objects.get(id=int(num1))
     }
    return render(request ,'update.html' ,context)
