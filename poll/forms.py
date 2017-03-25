from django import forms


class form_add(forms.Form):
	item_name = forms.CharField(label='Item Name', max_length=100)
	item_type = forms.CharField(label='Item Type', max_length=100)
	item_image = forms.FileField(label='Item Image',)