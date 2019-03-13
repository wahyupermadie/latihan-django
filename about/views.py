from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'judul':'kelas terbuka',
        'kontributor':'Wahyu Permadi'
    }
    return render(request, 'about/about.html', context)

def news(request):
    context = {
        'judul':'kelas news',
        'kontributor':'Wahyu Ganteng'
    }
    return render(request, 'about/about.html', context)

def cerita(request):
    context = {
        'judul':'kelas cerita',
        'kontributor':'Wahyu Boy'
    }
    return render(request, 'about/about.html', context)