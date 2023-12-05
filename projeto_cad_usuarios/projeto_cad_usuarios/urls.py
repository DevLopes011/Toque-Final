from django.urls import path
from app_cad_usuarios import views


urlpatterns = [
path('',views.home,name='home'),

path('cadastro_usuarios',views.cadastro_usuarios,name='cadastro_usuarios'),

path('usuarios/', views.usuarios,name='listagem_usuarios'),

path('delete_item/<int:id_usuario>/', views.delete_item, name="delete_item"),

path('edit_item/<int:id_usuario>/', views.edit_item, name='edit_item'),


path('get_user/<int:id_usuario>/', views.get_user, name="get_user"), # GET

]
