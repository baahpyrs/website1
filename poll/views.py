from django.shortcuts import render

from django.http import HttpResponse
from .models import Item
from django.template import loader

def index(request):
	obj = Item.objects.order_by('id')[:9]
	template = loader.get_template('poll/index.html')
	content = {'obj' : obj,}
	return HttpResponse(template.render(content,request))

def detail(request, Item_id):
	obj = Item.objects.get(pk=Item_id)
	template = loader.get_template('poll/detail.html')
	return render(request, 'poll/detail.html', {'obj' : obj })


def style(request):
	return HttpResponse('<img src="abcd.jpg" height="400px" width="400px" alt="image not foundddd"><p style="color:red;">hey it works in red</p>')
	
	
def addItem(request):
	template = loader.get_template('poll/addItem.html')
	return render(request,'poll/addItem.html',{ 'head' : "<h1>Hello</h1>"})
	
def add(request):
	q = Item()
	q.name = request.POST['name']
	q.itemType = request.POST['itemType']
	q.itemimage = request.FILES['item_image']
	q.save()
	return render(request, 'poll/detail.html' , {'obj' : q,})


