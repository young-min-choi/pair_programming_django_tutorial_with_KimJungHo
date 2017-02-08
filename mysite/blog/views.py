from django.shortcuts import render

from blog.models import Post


def post_list(request):
    post_list = Post.objects.all().order_by("-published_date")
    context = {"post_list": post_list}
    return render(request, "blog/post-list.html", context)

def post_detail(request, post_id):
    p = Post.objects.get(id=post_id)
    context = {"p": p}
    return render(request, "blog/post-detail.html", context)

