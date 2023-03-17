from pictures.forms import PictureForm
from django.shortcuts import render, redirect
from pictures.models import Pictures
from pictures.gpt import GPT_function
import urllib.request


def picture_view(request):
    template = 'pictures/index.html'
    form = PictureForm
    context = {
        'form': form
    }
    if request.method != 'POST':
        form = PictureForm()
        return render(request, template, context)
    form = PictureForm(request.POST)
    if form.is_valid():
        name = form.data['name']
        form.save()
        my_picture = Pictures.objects.filter(name=name)[0]
        result = urllib.request.urlretrieve(GPT_function('name'))
        my_picture.picture = result
        # my_picture.picture = GPT_function(name)
        my_picture.save()
        return redirect('pictures:list')
    return render(request, template, context)

def picture_view_list(request):
    objects = Pictures.objects.all()
    context = {
        'objects': objects
    }
    template = 'pictures/list.html'
    return render(request, template, context)