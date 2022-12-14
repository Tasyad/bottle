from django.shortcuts import render
from .models import Post
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView
    )
from django.urls import reverse_lazy


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'object_list'


class PostCreateViews(CreateView):
    model = Post
    fields = ['title', 'content', 'author', 'post_date', 'image']

    def form_valid(self, form):
        return super().form_valid(form)

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        return context

class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'content', 'image']

    def form_valid(self, form):
       return super().form_valid(form)

class PostDeleteView(DeleteView):
    model = Post
    template_name = "blog/post_confirm_delete.html"
    success_url = reverse_lazy('blog-home')