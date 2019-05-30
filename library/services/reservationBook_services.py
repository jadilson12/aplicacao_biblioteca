from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from library.forms import ReservationBookForm
from library.models import Book, Category, ReservationBook


def reserve_list(request):
    data = {
        # 'books': ReservationBook.objects.all(),
        'form': ReservationBookForm(),
        # 'category': Category.objects.all(),
        # 'user': User.objects.all()
    }
    return render(request, 'reserve/reserve.list.html', data)


def view(request, id):
    data = {
        'book': Book.objects.get(id=id),
        'category': Category.objects.all(),
        'form': ReservationBookForm()
    }
    return render(request, 'book/book_view.html', data)


def reserve(request):
    if request.method == 'POST':
        form = ReservationBookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book.list')
    else:
        form = ReservationBookForm()
        return render(request, 'book/book_reserve.html', {'form': form})
