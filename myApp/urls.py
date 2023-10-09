from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name="index"),
    path('login', views.login_view, name="login"),
    path('signin', views.signin_view, name="signin"),
    path('logout', views.logout_view, name="logout"),
    path("create", views.createPost , name="create"),
    path("filter", views.filterPost , name="filter"),
    path("postDetails/<int:id>", views.postDetails , name="postDetails"),
    path("addComment/<int:id>", views.addComment , name="addComment"),
    
]
