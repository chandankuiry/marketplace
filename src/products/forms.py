from django import forms

PUBLISH_CHOICES = (
	('', ""),
	('publish', "Publish"),
	('draft', "Draft"),
)

class ProductAddForm(forms.Form):
	title = forms.CharField()
	#here we use widgets to make a charfield to textarea if you want to learn about widgets then 
	#https://docs.djangoproject.com/en/1.9/ref/forms/widgets/
	description = forms.CharField(widget=forms.Textarea) #this might be a problem if we give it a textfield like model.py
	price  = forms.DecimalField()
	publish = forms.ChoiceField(choices=PUBLISH_CHOICES, required=False)

	def clean_price(self):
		price = self.cleaned_data.get("price")
		if price <= 1.00:
			raise forms.ValidationError("Price must be greater than $1.00")
		elif price >= 99.99:
			raise forms.ValidationError("Price must be less than $100.00")
		else:
			return price

	def clean_title(self):
		title = self.cleaned_data.get("title")
		if len(title) > 3:
			return title
		else:
			raise forms.ValidationError("Title must be greater than 3 characters long.")