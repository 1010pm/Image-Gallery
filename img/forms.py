# في ملف myapp/forms.py
from django import forms
from .models import Image

# في ملف myapp/forms.py
from django import forms

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['description', 'image']

# استيراد SearchForm بشكل صحيح
class SearchForm(forms.Form):
    search_term = forms.CharField(label='Search', max_length=100, required=False)
