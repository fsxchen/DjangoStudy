from django.shortcuts import get_list_or_404, render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger
from apps.monapp.models import Host, HostGroup

PAGE_SIZE = 5

def index(request):
    host_list = get_list_or_404(Host.objects.all())

    paginator =  Paginator(host_list, PAGE_SIZE)
    page = request.GET.get('page')
    try:
        hosts = paginator.page(page)
    except PageNotAnInteger:
        hosts = paginator.page(1)
    except EmptyPage:
        hosts = paginator.page(paginator.num_pages)

    return render(request, 'monapp/index.html', {"hosts":hosts})


def host_detail(request, host_id):
    print host_id
    host = get_object_or_404(Host, 
                            pk=host_id, )
    print host.Pri_IP
    # host.access_count+=1
    # host.save()
    # return render(request, 'blog-post.html', {'blog':blog})
    return render(request, 'monapp/host-post.html', {'host':host})


# def index(request):
#     blog_list = get_list_or_404(Blog.objects.order_by('-publish_time'), )

#     print blog_list
#     paginator =  Paginator(blog_list, PAGE_SIZE)
#     page = request.GET.get('page')
#     try:
#         blogs = paginator.page(page)
#     except PageNotAnInteger:
#         blogs = paginator.page(1)
#     except EmptyPage:
#         blogs = paginator.page(paginator.num_pages)

#     return render(request, 'blogs/index.html', {"blogs": blogs})
