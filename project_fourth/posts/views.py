from django.shortcuts import render
from .models import Articles
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView
from django.views.generic.edit import UpdateView,DeleteView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
# Create your views here.

class ArticleListView(ListView):
    model=Articles
    template_name='article_list.html'
    
    
class ArticleUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Articles
    template_name='article_update.html'
    fields=('title','summary','body','photo',)
    
    def test_func(self):
        obj=self.get_object()
        return obj.author==self.request.user
    
class ArticleCreateView(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    model=Articles
    template_name='article_create.html'
    fields=('title','summary','body','photo')
    
    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        return self.request.user.is_superuser
    
    
class ArticleDetailView(LoginRequiredMixin,DetailView):
    model=Articles
    template_name='article_detail.html'
    
class ArticleDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Articles
    template_name='article_delete.html'
    success_url=reverse_lazy('article_list')
    
    def test_func(self):
        obj=self.get_object()
        return obj.author==self.request.user
    
    

    

