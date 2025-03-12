from django.urls import path
from .views import index, show, create, update, delete, create_comment

app_name = 'article'

urlpatterns = [
    path('', index, name='index'),
    path('<int:pk>', show, name='show'),
    path('create/', create, name='create'),
    path('<int:pk>/update/', update, name='update'),
    path('<int:pk>/delete/', delete, name='delete'),
    path('<int:article_id>/comments/create_comment/', create_comment, name='create_comment'),
]
