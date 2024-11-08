from django.shortcuts import render,redirect
from .models import Post
from .forms import Postmodel
# Create your views here.
def post(request):
    if request.method == "POST":
        form = Postmodel(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('post')
    else:
        form = Postmodel()

    return render(request, 'post.html', {"form": form})

def search(request):
    query = request.GET.get('q')

    if query :
        results = Post.objects.filter(title__icontains=query)

    else:
        results = Post.objects.all()

    return render(request,'search.html',{'results':results})