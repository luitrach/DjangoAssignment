from django.shortcuts import get_object_or_404, render, redirect
from .models import Book
from .forms import Bookform

def book_list(request):
    book = Book.objects.all()
    return render(request,'app1/book_list.html',{'object_list':book})

def book_view(request,pk):
    book = get_object_or_404(Book,pk=pk)
    return render(request,'app1/book_detail.html',{'object':book})

def book_update(request,pk):
    book = get_object_or_404(Book,pk=pk)
    form = Bookform (request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('book_list')
    return render(request, 'app1/book_form.html',{'form':form})

def book_delete(request,pk):
     book = get_object_or_404(Book,pk=pk)
     if request.method=='POST':
         book.delete()
         return redirect('book_list')
     return render(request, 'app1/book_delete.html',{'object':book})

