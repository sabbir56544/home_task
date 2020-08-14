from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, View, UpdateView, DeleteView
from django.views.generic.edit import FormView
from .models import Writer, Book, Publication
from .forms import WriterForm
from django.urls import reverse_lazy



class Dashboard(View):
    def get(self, request):
        return render(request, 'dashboard/dashboard.html')


def writer_list(request):
    writers = Writer.objects.all()
    context = {
        'writers' : writers
    }
    return render(request, 'dashboard/writer_list.html', context)


class WriterListView(ListView):
    model = Writer
    context_object_name = 'writers'


class WriterDetailView(DetailView):
    model = Writer
    template_name = 'dashboard/writer_detail.html'
    context_object_name = 'writer'


class WriterCreateView(FormView):
    form_class = WriterForm
    template_name = 'dashboard/writer_form.html'

    def form_valid(self, form):
        form.save()
        return redirect('writer-list')


class WriterEditView(UpdateView):
    model = Writer
    template_name = 'dashboard/writer_form.html'
    fields = '__all__'


class WriterDeleteView(DeleteView):
    model = Writer
    template_name = 'dashboard/writer_delete.html'
    success_url = reverse_lazy('writer-list')


class BookListView(ListView):
    model = Book
    template_name = 'dashboard/book_list.html'
    context_object_name = 'books'


class BookDetailView(DetailView):
    model = Book
    template_name = 'dashboard/book_detail.html'
    context_object_name = 'book'


class BookEditView(UpdateView):
    model = Book
    template_name = 'dashboard/book_buy.html'
    fields = '__all__'