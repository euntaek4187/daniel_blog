from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

# Create your views here.

# CBV 스타일
# Listview를 받아 사용하는 CBV 스타일은 모델명 뒤에 _list가 붙은 html 파일이여야 리드가 된다.
# 혹은 views에서 template_name을 지정해서 변경해주는 방식이 사용 가능하다.
class PostList(ListView):
    model = Post
    ordering = "-pk"
    # Listview 사용방법으로써, 기존에 사용하던 파일명 변경하기 싫을 때, 지정해준다.
    # template_name = "blog/post_list.html"


# FBV 스타일
"""
def index(request):
    posts = Post.objects.all().order_by("-pk")

    return render(
        request, 'blog/post_list.html',
        {
            'posts':posts
        }
    )

def single_post_page(request, pk):
    post = Post.objects.get(pk=pk)

    return render(
        request, "blog/single_post_page.html",
        {
            'post':post
        }
    )
"""