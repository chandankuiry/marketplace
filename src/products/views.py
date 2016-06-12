from django.shortcuts import render


from .models import Product

# Create your views here.
def detail_view(request):
	#1 item
	print request.user
	product=Product.objects.all().first()
	template="detail_view.html"
	context= {
		"object":product
	}
	return render(request,template,context)



def list_view(request):
	#1 item
	print request
	queryset=Product.objects.all()
	template="list_view.html"
	context= {
		"queryset":queryset
	}
	return render(request,template,context)
