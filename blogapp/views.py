from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Blog
from .forms import NewBlog

def home(request):
    blog_list = Blog.objects.all()
    #페이지 3개로 자르기
    paginator = Paginator(blog_list, 3)
    #request된 페이지 변수에 담음
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'home.html', {'blogs':blog_list, 'posts':posts})

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'detail.html', {'blog':blog_detail})

#새로운 데이터 저장=POST
#글쓰기 페이지 띄워줌=GET
def create(request):
    if request.method == 'POST':
        form = NewBlog(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
        return redirect('home')
        # return redirect('/blog/'+str(blog.id))
    else:
        form = NewBlog()
        return render(request, 'create.html', {'form':form})

def update(request, pk):
    blog = get_object_or_404(Blog, pk = pk)

    form = NewBlog(request.POST, request.FILES, instance=blog)
    if form.is_valid():
        form.save()
        return redirect('home')
    else:
        form = NewBlog(instance=blog)
    return render(request, 'update.html', {'form':form})

def delete(request, pk):
    blog = get_object_or_404(Blog, pk = pk)
    blog.delete()
    return redirect('home')
