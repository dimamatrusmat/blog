from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from  blog.models import Post
 
def home(request):
    postList = Post.objects.filter(visible=1)
    paginator = Paginator(postList, 4)
    page = request.GET.get('page')
    querysetGoods = paginator.get_page(page)

    context = {
        'posts': postList,
        'title': 'Главная страница блога',
        'desc': 'Описание для главной страницы',
        'key': 'ключевые слова',
    }

    return render(request, "partial\\home.html", context)

def single(request, id=None):
    post = get_object_or_404(Post, id=id)
    post.views += 1
    post.save()

    print(post.views)
 
    context = {
        "post": post,
    }
    return render(request, "partial\\single.html", context)