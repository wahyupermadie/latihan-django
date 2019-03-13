from django.shortcuts import render

def index(request):
    context = {
        'judul':'kelas terbuka',
        'kontributor':'Wahyu Permadi',
        'nav': [
            ['/','Admin'],
            ['/about','About']
        ]
    }
    return render(request, 'index.html', context)