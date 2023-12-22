from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import PermissionDenied
from .models import Article, Author, Tag
from .forms import ArticleForm
from django.core.paginator import Paginator
from django.db.models import F
# Create your views here.


def blog(request):
    # print('Show Data',request.GET)
    author_username = request.GET.get('author')
    articles = Article.objects.all()  # SELECT * FROM blog_article;
    authors = Author.objects.all()
    tags = Tag.objects.all()
    tag_title = request.GET.get('tag')
    page_number = int(request.GET.get('page', 1))
    if author_username:
        articles = articles.filter(author__user__username=author_username)
    if tag_title:
        articles = articles.filter(tags__title=tag_title)

    paginator = Paginator(articles, 2)
    page = paginator.page(page_number)
    articles = page.object_list

    return render(request, 'blog.html', context={'articles': articles, 'authors': authors, 'tags': tags, 'paginator': paginator, 'page': page})


def blog_detail(request, id):
    article = Article.objects.get(id=id)
    # article.view_count+=1 #UPDATE blog_article SET view_count = 16 WHERE id = 1
    # UPDATE blog_article SET view_count = view_count + 1 WHERE id = 1
    article.view_count = F('view_count') + 1
    article.refresh_from_db()
    article.save()
    return render(request, "blog-detail.html", context={'article': article})


def example(request):
    users = [
        {'name': 'orxan', 'age': 27, 'job': 'Sofware Developer'},
        {'name': 'eli', 'age': 24, 'job': 'Sofware Developer'},
        {'name': 'aysel', 'age': 21, 'job': 'Sofware Developer'},
        {'name': 'senan', 'age': 23, 'job': 'Sofware Developer'},
    ]
    return render(request, 'example.html', context={'user_list': users})


def add_article(request):
    if request.method == 'POST':
        data = request.POST.copy()
        form = ArticleForm(data=data, files=request.FILES)
        if form.is_valid():
            form.save(request.user.author)
            return redirect('blog:article-list')
        return render(request, 'article-form.html', {'form': form})
    else:
        form = ArticleForm()
        return render(request, 'article-form.html', {'form': form})


def edit_article(request, id):
    article = get_object_or_404(Article, id=id)
    if article.author.user != request.user:
        raise PermissionDenied()
    if request.method == 'POST':
        data = request.POST.copy()
        data['author'] = request.user.author.id
        form = ArticleForm(data=data, files=request.FILES, instance=article)
        if form.is_valid():
            form.save(request.user.author)
            return redirect('blog:article-list')
        return render(request, 'article-form.html', {'form': form})
    else:
        form = ArticleForm(instance=article)
        return render(request, 'article-form.html', {'form': form})


def delete_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if article.author.user != request.user:
        raise PermissionDenied()
    article.delete()
    return redirect("blog:article-list")
