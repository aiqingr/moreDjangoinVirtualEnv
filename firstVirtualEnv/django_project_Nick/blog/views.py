from django.shortcuts import render
# from django.http import HttpResponse

posts = [
    {
        'author': 'Nick',
        'title': 'Blog post1',
        'content': 'First post content',
        'date_posted': '05/13/2019'
    },
    {
        'author': 'Tongyang',
        'title': 'Blog post2',
        'content': 'Second post content',
        'date_posted': '05/14/2019'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About Blog'})
