from django.shortcuts import render,redirect
from .models import list
from .forms import listform
from django.contrib import messages
# Create your views here.

def home(request):
    if request.method == 'POST':
        form = listform(request.POST)

        if form.is_valid():
            form.save()
            all_items = list.objects.all()
            context={
                "items":all_items
            }
            messages.success(request,"Item has been added")
            return render(request,'home.html',context)
    else:
        all_items = list.objects.all()
        return render(request,'home.html',{"items":all_items})

def delete_item(request,list_id):
    item = list.objects.get(id=list_id)
    item.delete()
    messages.success(request,"Item has been deleted!!")
    return redirect('home')

def cross_off(request,list_id):
    item = list.objects.get(id=list_id)
    item.completed = True
    item.save()
    return redirect('home')

def uncross(request,list_id):
    item = list.objects.get(id=list_id)
    item.completed = False
    item.save()
    return redirect('home')

def edit_item(request,list_id):
    if(request.method == 'POST'):
        item = list.objects.get(id=list_id)

        form = listform(request.POST or None, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request,"Item has been edited!")
            return redirect('home')
    else:
        item = list.objects.get(id=list_id)
        return render(request,'edit.html',{'item':item})

