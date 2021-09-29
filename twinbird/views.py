from django.shortcuts import render, redirect

from receipt.models import Receipt
from twinbird.forms import TwinbirdModelForm
from twinbird.models import Twinbird
from wonder.models import Wonder


def index(request):
    form = TwinbirdModelForm()
    wonder_list = Wonder.objects.all().order_by('-xdate')
    receipt_list = Receipt.objects.all().order_by('-ydate')
    twinbird_list = Twinbird.objects.all()
    if request.method == "POST":
        form = TwinbirdModelForm(request.POST)
        if form.is_valid():
            savedform = form.save()
            if Wonder.objects.filter(id=savedform.wonderid).count() > 0:
                wonder_find = Wonder.objects.get(id=savedform.wonderid)
                wonder_find.twinbirdx_id = savedform.id
                wonder_find.save()
            if Receipt.objects.filter(id=savedform.dogid).count() > 0:
                dog_find = Receipt.objects.get(id=savedform.dogid)
                dog_find.twinbirdy_id = savedform.id
                dog_find.save()
            if Receipt.objects.filter(id=savedform.catid).count() > 0:
                cat_find = Receipt.objects.get(id=savedform.catid)
                cat_find.twinbirdy_id = savedform.id
                cat_find.save()
            if Receipt.objects.filter(id=savedform.eggid).count() > 0:
                egg_find = Receipt.objects.get(id=savedform.eggid)
                egg_find.twinbirdy_id = savedform.id
                egg_find.save()


        return redirect("/twinbird/index")
    context={
        'wonder_list': wonder_list ,
        'receipt_list': receipt_list ,
        'twinbird_list': twinbird_list ,
        'form': form ,
    }

    return render( request , 'index3.html' , context)



def list(request):
    form = TwinbirdModelForm()
    wonder_list = Wonder.objects.all().order_by('-xdate')
    receipt_list = Receipt.objects.all().order_by('-ydate')
    twinbird_list = Twinbird.objects.all()
    if request.method == "POST":
        form = TwinbirdModelForm(request.POST)
        if form.is_valid():
            form.save()


        return redirect("/twinbird/index")
    context={
        'wonder_list': wonder_list ,
        'receipt_list': receipt_list ,
        'twinbird_list': twinbird_list ,
        'form': form ,
    }

    return render( request , 'list.html' , context)



def dismiss(request,pk):
    twinbird_list = Twinbird.objects.all()
    twinbird_find = Twinbird.objects.get(id=pk)

    if Wonder.objects.filter(id=twinbird_find.wonderid).count() > 0:
        wonder_find = Wonder.objects.get(id=twinbird_find.wonderid)
    #     wonder_find是一筆wonder紀錄，而不是ID值
        wonder_find.twinbirdx_id = None
        wonder_find.save()

    if Receipt.objects.filter(id=twinbird_find.dogid).count() > 0:
        dog_find = Receipt.objects.get(id=twinbird_find.dogid)
        dog_find.twinbirdy_id = None
        dog_find.save()
    if Receipt.objects.filter(id=twinbird_find.catid).count() > 0:
        cat_find = Receipt.objects.get(id=twinbird_find.catid)
        cat_find.twinbirdy_id = None
        cat_find.save()
    if Receipt.objects.filter(id=twinbird_find.eggid).count() > 0:
        egg_find = Receipt.objects.get(id=twinbird_find.eggid)
        egg_find.twinbirdy_id = None
        egg_find.save()

    twinbird_find.delete()


    context={
        'twinbird_list': twinbird_list ,
    }

    return render( request , 'list.html' , context)
