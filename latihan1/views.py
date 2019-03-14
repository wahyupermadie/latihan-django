from django.shortcuts import render

def index(request):
    context = {
        'judul':'kelas terbuka',
        'kontributor':'Wahyu Permadi',
        'banner':'img/banner_home.png',
        'nav': [
            ['/','Admin'],
            ['/about','About']
        ]
    }
    return render(request, 'index.html', context)