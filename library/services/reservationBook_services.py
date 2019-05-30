from django.shortcuts import render, redirect

from library.forms import ReservationBookForm
from library.models import Book, Category


def view(request, id):
    data = {'book': Book.objects.get(id=id), 'category': Category.objects.all()}
    return render(request, 'book/book_view.html', data)


def reserve(request):
    if request.method == 'POST':
        form = ReservationBookForm(request.POST, instance=Book)
        if form.is_valid():
            form.save()
            return redirect('book.list')
    else:
        form = ReservationBookForm()
        return render(request, 'book/book_view.html', {'form': form})