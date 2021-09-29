from django.shortcuts import render, redirect

# Create your views here.
from receipt.forms import ReceiptModelForm
from receipt.models import Receipt


def index(request):
    receipt_list = Receipt.objects.all()
    context={
        'receipt_list': receipt_list ,
    }
    return render( request , 'index2.html' , context)

def new(request):
    form = ReceiptModelForm()
    if request.method == "POST":

        form = ReceiptModelForm(request.POST)

        if form.is_valid():
            form.save()
        return redirect("/receipt/index/")
    context ={
        'form': form ,
    }
    return render(request ,'new2.html' ,context)


def edit(request ,pk):
    receipt_find = Receipt.objects.get(id=pk)
    if request.method == "POST":

        form = ReceiptModelForm(request.POST ,instance=receipt_find)

        if form.is_valid():
            form.save()
        return redirect("/receipt/index/")
    else:
        form = ReceiptModelForm(instance=receipt_find)
    context ={
        'form': form ,
    }
    return render(request ,'edit2.html' ,context)



def delete(request ,pk):
    receipt_find = Receipt.objects.get(id=pk)
    if request.method == "POST":

        receipt_find.delete()
        return redirect("/receipt/index/")
    else:
        form = ReceiptModelForm(instance=receipt_find)
    context ={
        'form': form ,
        'receipt_find': receipt_find ,
    }
    return render(request ,'delete2.html' ,context)


