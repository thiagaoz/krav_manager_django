from django.urls import path
from . import views 

urlpatterns  = [
    path('', views.home, name = 'home'),
    path('add_aluno', views.add_aluno, name='add-aluno'),
    path('lista_alunos', views.lista_alunos, name='lista-alunos'),
    path('add_plano', views.add_plano, name='add-plano'),
    path('lista_planos', views.lista_planos, name='lista-planos'),
    path('show_aluno/<id>', views.show_aluno, name='show-aluno'),
    path('update_aluno/<id>', views.update_aluno, name='update-aluno'),
    path('update_plano/<id>', views.update_plano, name='update-plano'),
    path('delete_plano/<id>',views.delete_plano,name='delete-plano'),
    path('show_aluno/delete_aluno/<id>', views.delete_aluno, name='delete-aluno'),
    path('busca_avancada', views.busca_avancada, name='busca-avancada'),
    path('relatorio', views.relatorio, name='relatorio'),
]