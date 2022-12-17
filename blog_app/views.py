from django.shortcuts import render
from django.shortcuts import render, get_object_or_404,redirect
from blog_app.models import  Article,Category,Comment
from blog_app.models import Article
from django.shortcuts import render, get_object_or_404,redirect
from blog_app.models import  Article,Category
from django.core.paginator import Paginator
from django.contrib.auth.models import User
def home_app(request):
    articles = Article.objects.all().order_by("-updetad")
    page_number = request.GET.get('page')
    paginator = Paginator(articles , 10)
    objects_list = paginator.get_page(page_number)
    # print(request.user.username)

    return render(request,"blog_app/home_app.html",context={"article" :objects_list })
def post_detail(request,pk=None):
    article = get_object_or_404(Article, id=pk)
    article_list = Article.objects.order_by()[:4]
    if request.method == 'POST':
        try:
            parent_id = request.POST.get('parent_id')
            body = request.POST.get('body')
            Comment.objects.create(body=body, article=article, user=request.user, parent_id=int(parent_id))
        except:
            body = request.POST.get('body')
            Comment.objects.create(body=body, article=article, user=request.user)

    return render(request,"blog_app/blog_app.html",{"article" : article,'article_list':article_list })