from django.shortcuts import render, HttpResponse,get_object_or_404
from .models import article,ChapterImage,chapter
# Create your views here.
def index(request):
    post = article.objects.all()
    context = {
        "post": post
    }
    return render(request, "index.html",context)


def getdetails(request, id):
    post = article.objects.all()
    posts=get_object_or_404(article, pk=id)
    context = {
        "post": post,
        "posts":posts
    }
    return render(request, "details.html",context)

def getsimple(request):
    return render(request, "simple.html")

def getchapter(request,bid, cnum):
    chapters = chapter.objects.get(article__id=int(bid), chapter_number=int(cnum))
    images = ChapterImage.objects.filter(chapter_obj__id=chapters.id)
    all_chapter = chapter.objects.filter(article=chapters.article)
    context = {
        "chapter": article.objects.all(),
        "chapters": chapters,
        "images":images,
        "all_chapter":all_chapter
    }
    return render(request, "chapter.html", context)


def listview(request):
    post = article.objects.all()
    context = {
        "post": post
    }
    return render(request, "listview.html",context)