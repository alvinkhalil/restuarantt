from postbloq.forms import CommentForm
from django.shortcuts import redirect, render
from .models import Comments, Post, Category, ReplyComments
from django.contrib import messages
from taggit.models import Tag
from settings.models import Settings

# Create your views here.


def post_list(request):

    posts =Post.objects.all()
    settings = Settings.objects.all()

    context = {
        "posts":posts,
        "settings":settings
    }

    if request.method =="POST":

        search = request.POST['search']
        posts = Post.objects.filter(title__contains = search)

        context = {
        "search":search,
        "posts":posts,
        }
        if len(posts) == 0:

            messages.info(request, "Axtardığınız açar sözünə aid heç bir məqalə tapılmadı.")

            return render(request,"Blog/post_list.html",context)



        return render(request,"Blog/post_list.html",context)

    return render(request,"Blog/post_list.html",context)

def post_detail(request,id):

    post = Post.objects.get(id = id)
    tags = Tag.objects.all()
    categories = Category.objects.all()
    recentposts = Post.objects.all()[:5]
    comments = Comments.objects.filter(post = post)

    replys = ReplyComments.objects.filter(post = post)
    comment_form = CommentForm()
    settings = Settings.objects.all()

    if request.method == "POST":
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            
            newComment = comment_form.save(commit=False)

            newComment.post = post

            newComment.save()

    context = {
        "post":post,
        "categories":categories,
        "tags":tags,
        "recentposts":recentposts,
        'comments':comments,
        "comment_form":comment_form,
        "settings":settings,
        "replys":replys,
    }


    return render(request,"Blog/post_detail.html",context)


def post_tags(request,tag):

    post_tags = Post.objects.filter(tags__name__in =[tag])
    settings = Settings.objects.all()


    context = {
        "posts":post_tags,
        "settings":settings
   
    }

    return render(request,"Blog/post_list.html",context)

def post_category(request, category):

    post_category = Post.objects.filter(category__id = category)
    
    settings = Settings.objects.all()

    context = {
        "posts":post_category,
        "settings":settings
   
    }

    return render(request,"Blog/post_list.html",context)







