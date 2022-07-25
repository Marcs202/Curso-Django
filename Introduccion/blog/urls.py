from django.urls import path
from .views import BlogDetailView, BlogListView, BlogCreateView, UpdateView, BlogDeleteView

app_name="blog"

urlpatterns = [
    path('',BlogListView.as_view(),name='Home'), #!manera de agregar las url que estan dentro de la misma app
    #ese espacio sin texto representa el nombre que llevaria despues de 
    #" nombreAsignadoenURLdeCore/ nombre que se asigna en este url"
    path('create/',BlogCreateView.as_view(),name='Create'),
    path("<int:pk>/", BlogDetailView.as_view(), name="Detail"),
    path("<int:pk>/update/ ", UpdateView.as_view(), name="Update"),
    path("<int:pk>/delete/",BlogDeleteView .as_view(), name="Delete"),
]
