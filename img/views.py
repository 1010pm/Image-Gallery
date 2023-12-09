# في ملف myapp/views.py
from django.shortcuts import render, redirect
from .models import Image
from .forms import ImageForm, SearchForm

def home(request):
    images = Image.objects.all()
    search_form = SearchForm(request.GET)

    if search_form.is_valid():
        search_term = search_form.cleaned_data['search_term']
        if search_term:
            images = images.filter(description__icontains=search_term)

    return render(request, 'home.html', {'images': images, 'search_form': search_form})


def delete_image(request, image_id):
    image = Image.objects.get(pk=image_id)
    image.delete()
    return redirect('home')



def upload_image(request):
    uploaded_image = None
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_image = form.save()
            # بمجرد رفع الصورة بنجاح، قم بتحويل المستخدم إلى الصفحة الرئيسية
            return redirect('home')
    else:
        form = ImageForm()

    return render(request, 'upload_image.html', {'form': form, 'uploaded_image': uploaded_image})

