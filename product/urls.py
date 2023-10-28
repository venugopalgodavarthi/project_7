from django.urls import path
from product.views import create_view, list_view, details_view, update_view, delete_view, register_view

urlpatterns = [
    path(route='create/<str:pname>/<str:desc>/<int:price>/',
         view=create_view, name="create"),
    path(route='list/', view=list_view, name="list"),
    path(route='details/<int:pk>/', view=details_view, name="details"),
    path(route='update/<int:pk>/<int:value>/', view=update_view, name="update"),
    path(route='delete/<int:pk>/', view=delete_view, name="delete"),
    path(route='register/', view=register_view, name="register"),
]
