from ast import arg
from gc import get_objects
from multiprocessing import context
from pyexpat import model
from re import template
from turtle import title
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import View, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import PostCreateForm
from .models import Post
# Create your views here.
class BlogListView(View):
    def get(self, request,*args, **kwargs):
        posts= Post.objects.all()

        context={
            'posts':posts
        }
        return render(request,'blog_list.html',context)

class BlogCreateView(View):
    def get(self,request,*args, **kwargs):
        form = PostCreateForm()
        context={
            'form':form
        }
        return render(request,'blog_create.html',context)

    def post(self,request,*args, **kwargs):
        if request.method=="POST":
            form=PostCreateForm(request.POST)
            if form.is_valid():
                title=form.cleaned_data.get('title')
                content=form.cleaned_data.get('content')

                p, created= Post.objects.get_or_create(title=title, content=content)
                p.save()
                return redirect('blog:Home')
        context={

        }
        return render(request,'blog_create.html',context)

class BlogDetailView(View):

    def get (self, request,pk,*args, **kwargs):
        post=get_object_or_404(Post,pk=pk)
        context={
            'post':post
        }
        return render(request,'blog_detail.html',context)

class UpdateView(UpdateView):
    model=Post  ##pasar el modelo que se quiere editar
    fields=['title','content'] #pasar los campos a editar
    template_name='blog_update.html'
    ##enviar la vista de editar o la misma de crear

    def get_success_url(self):
        pk=self.kwargs['pk']
        return reverse_lazy('blog:Detail',kwargs={'pk':pk})

class BlogDeleteView(DeleteView):
    model=Post
    template_name= 'blog_delete.html'
    success_url= reverse_lazy('blog:Home')



