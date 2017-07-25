from django.shortcuts import render
import json
from .forms import StockForm
from .models import Stock
from .data import get_graph
# Create your views here.

def stock_create(request):
	return HttpResponse('<h1>create</h1>')

def stock_detail(request):
	return HttpResponse('<h1>detail</h1>')

def stock_info(request):
	form = StockForm(request.POST or None)
	stock = ""
	if form.is_valid():
		instance = form.save(commit=False)
		data = get_graph(form.cleaned_data.get('stock'))
		stock = json.dumps(data)
	#if request.method == 'POST':
	#	print (request.POST.get("title"))
	context = {
		'form': form,
		'stock_data_py' : stock
	}
	return render(request, 'stock_page/main_page.html', context)

def stock_update(request):
	return HttpResponse('<h1>update</h1>')

def stock_delete(request):
	return HttpResponse('<h1>delete</h1>')