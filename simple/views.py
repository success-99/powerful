from django.shortcuts import render, redirect, get_object_or_404
from .models import Book,Author
from .forms import BookForm,BookUpdateForm
# Create your views here.

def list_view(request):
    books = Book.objects.all()
    authors = Author.objects.all()
    return render(request, 'simple/index.html', { 'books': books, 'authors': authors })

def post_detail(request, pk):
    books = Book.objects.get(id=pk)
    authors = books.author.all()
    print(authors)
    return render(request,'simple/list.html',{'posts':books, 'authors': authors })

def create(request):
    if request.method=='POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('simple:index')
        context = {
            "form": form
        }
        return render(request, 'simple/create.html', context)
    else:
        form=BookForm()
        return render(request, 'simple/create.html', {'form':form})

def update(request, pk):
    if request.method=='POST':
        book_up = get_object_or_404(Book, id=pk)
        form = BookUpdateForm(request.POST, instance=book_up)
        if form.is_valid():
            instance= form.save(commit=False)
            instance.save()
            return redirect('simple:index')
        context = {
            "form": form,
        }
        return render(request, 'simple/update.html', context)
    else:
        books = get_object_or_404(Book, id=pk)
        form = BookUpdateForm(instance=books)
        return render(request, 'simple/update.html', {'form':form})



def delete(request, pk):
    delete = get_object_or_404(Book, id=pk)
    delete.delete()
    return redirect('simple:index')