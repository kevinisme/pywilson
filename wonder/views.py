from django.shortcuts import render, redirect

# Create your views here.
from wonder.forms import WonderModelForm
from wonder.models import Wonder


def index(request):
    wonder_list = Wonder.objects.all()
    context={
        'wonder_list': wonder_list ,
    }
    return render( request , 'index.html' , context)

def new(request):
    form = WonderModelForm()
    if request.method == "POST":

        form = WonderModelForm(request.POST)

        if form.is_valid():
            form.save()
        return redirect("/wonder/index/")
    context ={
        'form': form ,
    }
    return render(request ,'new.html' ,context)


def edit(request ,pk):
    wonder_find = Wonder.objects.get(id=pk)
    if request.method == "POST":

        form = WonderModelForm(request.POST ,instance=wonder_find)

        if form.is_valid():
            form.save()
        return redirect("/wonder/index/")
    else:
        form = WonderModelForm(instance=wonder_find)
    context ={
        'form': form ,
    }
    return render(request ,'edit.html' ,context)



def delete(request ,pk):
    wonder_find = Wonder.objects.get(id=pk)
    if request.method == "POST":

        wonder_find.delete()
        return redirect("/wonder/index/")
    else:
        form = WonderModelForm(instance=wonder_find)
    context ={
        'form': form ,
        'wonder_find': wonder_find ,
    }
    return render(request ,'delete.html' ,context)


