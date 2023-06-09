from django.shortcuts import render, redirect
from .models import Post
from django.shortcuts import get_object_or_404,HttpResponse
from django.views.generic import ListView
from .forms import EmailPostForm,CommentForm,UserRegistrationForm,LoginForm,PostAddForm,PostUpForm
from django.core.mail import send_mail
from django.views.decorators.http import require_POST
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.safestring import mark_safe

# Create your views here.

class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 2
    template_name = 'blog/post/list.html'

# @login_required(login_url='blog:user_login')
# def post_list(request):
#     posts = Post.published.all()
#     return render(request, 'blog/post/list.html', {'posts': posts})

@login_required(login_url='blog:user_login')
def post_add(request):
    if request.method == "GET":
        form = PostAddForm()
        return render(request, 'blog/post/post_add.html', {'form': form})
    elif request.method == "POST":
        form = PostAddForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Muvaffaqiyatli qo'shildi!")
            return redirect('blog:post_list')
        return render(request, 'blog/post/post_add.html', {'form': form})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, status=Post.Status.PUBLISHED,
                             slug=post,
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    comments = post.comments.filter(active=True)
    form = CommentForm()
    return render(request, 'blog/post/detail.html', {'post': post,'comments':comments,'form':form})


def post_share(request, post_id):
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    sent = False
    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(
                post.get_absolute_url())
            subject = f"{cd['name']} recommends you read" \
                      f"{post.title}"
            message = f" Read {post.title} at {post_url}\n\n" \
                      f"{cd['name']}\'s comments: {cd['comments']}"
            send_mail(subject, message, 'userpydj1@gmail.com', [cd['to']])
            sent = True

    else:
        form = EmailPostForm()
    return render(request, 'blog/post/share.html', {'post': post,
                                                    'form': form,
                                                    'sent': sent})

@require_POST
def post_comment_add(request,post_id):
    post = get_object_or_404(Post,id=post_id,status=Post.Status.PUBLISHED)
    comment = None
    form = CommentForm(data=request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post=post
        comment.save()
    return render(request,'blog/post/comment.html',{'post':post,'comment':comment,'form':form})


def user_register(request):
    if request.method=='POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user=user_form.save(commit=False)
            new_user.set_password(
                user_form.cleaned_data['password']
            )
            new_user.save()
            return redirect('blog:user_login')
            # return render(request,'account/register_done.html',{'new_user':new_user})
    else:
        user_form = UserRegistrationForm()
        return render(request,'account/register.html',{'user_form':user_form})


def user_login(request):
    if request.method=='POST':
        form_login = LoginForm(request.POST)
        if form_login.is_valid():
            data = form_login.cleaned_data
            user = authenticate(request,
                                username=data['username'],
                                password=data['password']
                                )
            if user is not None:
                if user.is_active:
                    login(request, user)
                    messages.success(request, "Muvaffaqiyatli kirdingiz!")
                    return redirect('blog:post_list')
                else:
                    return HttpResponse("Sizning hisobingiz faol emas!")
            else:
                return HttpResponse('login va parolda hatolik bor!')
    else:
        form = LoginForm()
        return render(request,'account/login.html',{'form':form })


@login_required(login_url='blog:user_login')
def profile(request):
    user = request.user
    context={
        'user': user
    }
    return render(request,'account/profile.html',context=context)

def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, mark_safe('<strong style="color: red;">Muvaffaqiyatli chiqdingiz!</strong>'))
        return redirect('blog:post_list')
    else:
        return HttpResponse("Foydalanuvchi avtorizatsiyadan o'tmagan.")

def post_delete(request, pk):
    delete = get_object_or_404(Post, id=pk)
    if request.user == delete.author:
        delete.delete()
        return redirect('blog:post_list')
    else:
        messages.error(request, mark_safe('<strong style="color: red;">Siz bu postni o\'chira olmaysiz!</strong>'))
        return redirect('blog:post_list')

@login_required(login_url='blog:user_login')
def post_update(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user == post.author:
        if request.method == 'GET':
            form = PostUpForm(instance=post)
            return render(request, 'blog/post/post_update.html', {'form': form, 'pt': post})
        elif request.method == 'POST':
            form = PostUpForm(instance=post, data=request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Muvaffaqiyatli yangilandi!")
                return redirect('blog:post_list')
            return render(request, 'blog/post/post_update.html', {'form': form, 'pt': post})
    else:
        messages.error(request, mark_safe('<strong style="color: red;">Siz bu postni yangilay olmaysiz!</strong>'))
        return redirect('blog:post_list')