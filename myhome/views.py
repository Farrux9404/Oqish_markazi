from django.shortcuts import render, redirect
from django.views.generic import ListView, DeleteView
from .models import Post, Contacts
from django.db.models import Q
from django.contrib import messages
from requests import *
class VlogListView(ListView):
    model = Post
    template_name = 'home.html'


class VlogDetailView(DeleteView):
    model = Post
    template_name = 'post.html'

def home(request):
    post = Post.objects.all()
    context = {
        'post': post
    }
    return render(request, 'home.html', context)

def About(request):
    tex = {}
    return render(request,'about.html',tex)


def Contact(request):
    if request.method =='POST':
        fname = request.POST.get("name")
        femail = request.POST.get("email")
        fnumber = request.POST.get("tel")
        body = request.POST.get("subject")
        rey = Contacts(name = fname, email=femail, number =fnumber, body =body)
        rey.save()
        messages.info(request,"Ma'lumotingiz yuborildi...")
        return redirect('/contact')
    return render(request,'contact.html')


def Services(request):
    tex = {}
    return render(request,'services.html',tex)

def Partfifolio(request):
    tex = {}
    return render(request,'partifolio.html',tex)


def Pricing(request):
    tex = {}
    return render(request,'pricing.html',tex)



def Question(request):
    tex = {}
    return render(request,'question.html',tex)


def Section(request):
    tex = {}
    return render(request,'section.html',tex)


def Talaba(request):
    tex = {}
    return render(request,'talaba.html',tex)












# def Search(request):
# if request.method == 'POST':
#     search_text = request.POST['q']
#     if search_text:
#         post = Post.objects.filter(title__icontains=search_text) | Q(discrition__icontains=search_text)
#         context = {
#             'post': post
#         }
#         return render(request, 'blog/view_posts.html found')
#     else:
#         messages.error(request, 'Siz qdirgan malumot topilmadi!')
#         return redirect('view-posts')
# else:
#     return redirect('view-posts')
