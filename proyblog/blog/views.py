from django.shortcuts import render
#from django.http import HttpResponse

posts = [
    {
        'autor':'Sebastian Daza',
        'titulo':'Hola Mundo',
        'contenido':'El primer post de la página',
        'fecha':'16 de mayo 2025'

    },
    {
        'autor':'Sebastian Daza',
        'titulo':'Hola Mundo',
        'contenido':'El primer post de la página',
        'fecha':'16 de mayo 2025'

    },
    {
        'autor':'Sebastian Daza',
        'titulo':'Hola Mundo',
        'contenido':'El primer post de la página',
        'fecha':'16 de mayo 2025'

    }
]

def home(request):
    context ={
        'post':posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')