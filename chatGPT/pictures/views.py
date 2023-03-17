from pictures.forms import PictureForm
from django.shortcuts import render, redirect
from pictures.models import Pictures

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
        form.save()
        return redirect('pictures:list')
    return render(request, template, context)

def picture_view_list(request):
    objects = Pictures.objects.all()
    context = {
        'objects': objects
    }
    template = 'pictures/list.html'
    return render(request, template, context)