from django import forms

from .models import Stock

class StockForm(forms.ModelForm):
	stock = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Enter a Stock'}))
	class Meta:
		model = Stock
		fields = [
			'stock',
		]