from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Client
from .forms import PostForm

# Create your views here.
def post_list(request):
    clients = Client.objects.order_by('surname')
    return render(request, 'my_app/post_list.html', {'clients': clients})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
        return render(request, 'my_app/post_edit.html', {'form': form})
