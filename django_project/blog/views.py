from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Elay Maharramli',
        'title': 'Blog Post 1',
        'content':'First post content',
        'date_posted':'March 2, 2020'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content':'Second post content',
        'date_posted':'March 3, 2020'
    },
]



def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
