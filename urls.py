from django.urls import path
from .views import *

urlpatterns = [
    path('', Dashboard.as_view(), name='dashboard-page'),
    path('product/list', writer_list, name='product-list'),
    path('writer/list', WriterListView.as_view(), name='writer-list'),
    path('writer/create', WriterCreateView.as_view(), name='writer-create'),
    path('writer/edit/<int:pk>', WriterEditView.as_view(), name='writer-edit'),
    path('writer/delete/<int:pk>', WriterDeleteView.as_view(), name='writer-delete'),
    path('writer/detail/<int:pk>', WriterDetailView.as_view(), name='writer-detail'),

    #book
    path('book/list', BookListView.as_view(), name='book-list'),
    path('book/detail/<int:pk>', BookDetailView.as_view(), name='book-detail'),
    path('book/buy/<int:pk>', BookEditView.as_view(), name='book-buy')
]