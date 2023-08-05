from django.shortcuts import render,redirect,get_object_or_404,Http404
from blogs.models import Post,Comment
from blogs.forms import PostForm,CommentForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    context = {
        'title': 'Blogs'
    }
    return render(request,'blogs/index.html',context)

@login_required
def posts_list(request):
    posts = Post.objects.all()

    return render(request, 'blogs/posts_list.html', {'posts': posts})
@login_required
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = Comment.objects.filter(post = post)
    comment_form = CommentForm()

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('blogs:post_detail', post_id=post.id)
    context = {
        'post': post,
        'comment_form': comment_form,
        'comments':comments,
    }
    return render(request, 'blogs/post_detail.html', context)
@login_required
def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.owner = request.user
            post.save()
            return redirect('blogs:posts_list')
    else:
        form = PostForm
    return render(request,'blogs/create_post.html',{'form':form})
@login_required
def edit_post(request,post_id):
    post = get_object_or_404(Post,id = post_id)

    if post.owner != request.user:
        raise Http404

    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES,instance=post)
        if form.is_valid():
            form.save()
            return redirect('blogs:posts_list')
    else:
        form = PostForm(instance=post)

    return render(request,'blogs/post_edit.html',{'form':form,'post':post})

@login_required
def delete_post(request,post_id):
    post = get_object_or_404(Post,id = post_id)
    if post.owner != request.user:
        raise Http404

    post.delete()
    return redirect('blogs:posts_list')
