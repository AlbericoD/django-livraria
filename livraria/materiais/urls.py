from django.urls import path
from materiais import views

urlpatterns = [
    path('', views.listar_materiais, name='material_list'),
    path('new', views.criar_material, name='material_new'),
    path('view/<int:pk>', views.detalhes_material, name='material_view'),
    path('edit/<int:pk>', views.alterar_material, name='material_edit'),
    path('delete/<int:pk>', views.deletar_material, name='material_delete'),
]
