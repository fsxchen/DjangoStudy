from blog.models import Article, Tag, Classification
from django.shortcuts import render
            
def blog_list(request):
    blogs = Article.objects.order_by('-publish_time')[:2]
    context = {'blogs': blogs}
    return render(request, 'blog/index.html', context)
