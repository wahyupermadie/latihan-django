from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'judul':'kelas terbuka',
        'kontributor':'Wahyu Permadi',
        'banner':'about/img/banner_blog.png',
    }
    return render(request, 'about/about.html', context)

def news(request):
    context = {
        'judul':'kelas news',
        'kontributor':'Wahyu Ganteng',
        'banner':'about/img/banner_blog.png',
    }
    return render(request, 'about/about.html', context)

def cerita(request):
    context = {
        'judul':'kelas cerita',
        'kontributor':'Wahyu Boy',
        'banner':'about/img/banner_blog.png',
    }
    return render(request, 'about/about.html', context)