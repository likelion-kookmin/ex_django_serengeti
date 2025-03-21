from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect

from article.models import Article, Comment


def index(request):
    articles = Article.objects.all()

    return render(request, 'index.html', { 'articles': articles })


def show(request, pk):
    article = Article.objects.get(pk=pk)
    comments = article.comments.all()

    return render(request, 'show.html', { 'article': article, 'comments': comments })



def create(request):
    if request.method == 'POST':
        article = Article()
        article.author = request.user
        article.title = request.POST['title']
        article.content = request.POST['content']
        if 'image' in request.FILES:
            article.image = request.FILES['image']
        article.save()
        return redirect('article:show', pk=article.id)
    else:
        return render(request, 'new.html')


def update(request, pk):
    article = Article.objects.get(pk=pk)

    if request.user != article.author:
        return HttpResponseForbidden()

    if request.method == 'POST':
        article.title = request.POST['title']
        article.content = request.POST['content']
        if 'image' in request.FILES:
            article.image = request.FILES['image']
        article.save()
        return redirect('article:show', pk=article.id)
    else:
        return render(request, 'edit.html', { 'article': article })


def delete(request, pk):
    article = Article.objects.get(pk=pk)

    if request.user != article.author:
        return HttpResponseForbidden()

    article.delete()
    return redirect('article:index')


def create_comment(request, article_id):
    article = Article.objects.get(pk=article_id)
    content = request.POST['content']

    comment = Comment(author=request.user, article=article, content=content)
    comment.save()

    return redirect('article:show', pk=article_id)
