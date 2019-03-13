from django.shortcuts import render

def index(request):
    context = {
        'judul':'kelas terbuka',
        'kontributor':'Wahyu Permadi'
    }
    return render(request, 'index.html', context)