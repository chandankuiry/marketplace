from django.http import Http404
from django.shortcuts import render, get_object_or_404
# Create your views here.

from .forms import ProductAddForm
from .models import Product


def create_view(request): 
	# FORM
	form = ProductAddForm(request.POST or None)
	# if request.method == "POST": you can't print because it i security issue
	# 	print request.POST.get("price")
	if form.is_valid():
		data = form.cleaned_data
		title = data.get("title")
		description = data.get("description")
		price = data.get("price")
		#new_obj = Product.objects.create(title=title, description=description, price=price)
		new_obj = Product()
		new_obj.title = title
		new_obj.description = description
		new_obj.price = price
		new_obj.save()
	template = "create_view.html"
	context = {
			"form": form,
		}
	return render(request, template, context)




def detail_slug_view(request, slug=None):
	product = Product.objects.get(slug=slug)
	try:
		product = get_object_or_404(Product, slug=slug)
	except Product.MultipleObjectsReturned:
		product = Product.objects.filter(slug=slug).order_by("-title").first()
	# print slug
	# product = 1
	template = "detail_view.html"
	context = {
		"object": product
		}
	return render(request, template, context)


def detail_view(request, object_id=None):
	product = get_object_or_404(Product, id=object_id)
	template = "detail_view.html"
	context = {
		"object": product
		}
	return render(request, template, context)

	# if object_id is not None:
	# 	product = get_object_or_404(Product, id=object_id)
	# 	# product = Product.objects.get(id=object_id)
	# 	# try:
	# 	# 	product = Product.objects.get(id=object_id)
	# 	# except Product.DoesNotExist:
	# 	# 	product = None

		
	# else:
	# 	raise Http404


def list_view(request):
	# list of items
	print request
	queryset = Product.objects.all()
	template = "list_view.html"
	context = {
		"queryset": queryset
	}
	return render(request, template, context)