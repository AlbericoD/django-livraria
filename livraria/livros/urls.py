from django.urls import path
from livros import views

urlpatterns = [
    path('', views.listar_livros, name='livro_list'),
    path('new', views.criar_livro, name='livro_new'),
    path('view/<int:pk>', views.detalhes_livros, name='livro_view'),
    path('edit/<int:pk>', views.alterar_livro, name='livro_edit'),
    path('delete/<int:pk>', views.deletar_livro, name='livro_delete'),
    path('home-page', views.home_page, name='home_page'),
]
