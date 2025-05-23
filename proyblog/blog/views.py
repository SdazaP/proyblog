from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

#Infromación para pruebas
""" posts = [
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
] """

def home(request):
    context ={
        'post': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')

class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ["-date_posted"]


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

    # def test_func(self):
    #     post = self.get_object()
    #     if self.request.user == post.author:
    #         return True
    #     return False


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.autor:
            return True
        return False


class PostDeleteView(DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.autor:
            return True
        return False