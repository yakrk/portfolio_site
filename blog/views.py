from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Blog_post

# Create your views here.


def blogs_top(request):
    # pull blogs from db and show on page.
    posts = Blog_post.objects.order_by(
        "-created_date").filter(is_published=True)
    paginator = Paginator(posts, 5)  # 5 items per page
    page = request.GET.get('page')
    # includes gathered data plus pagination
    paged_posts = paginator.get_page(page)

    context = {
        "posts": paged_posts
    }
    # use pagenation
    return render(request, "blogs/blogs-top.html", context)


def post(request, post_id):
    # pull blog from
    post = get_object_or_404(Blog_post, pk=post_id)
    context = {
        "post": post
    }
    return render(request, "blogs/post.html", context)
