from django.urls import path,re_path
from .views import *

urlpatterns=[path("home/",home,name="intro"),
             path("add-task/",add_task,name="add_task"),
             path("create-task/",view_tasks,name="view_tasks"),
             path("edited/<int:task_id>/",update_task,name="edited"),
             path("deleted/<int:task_id>/",delete_task,name="deleted"),
             path("login/",login_view,name="login"),
             path("register/",register_view,name="register"),
             path("logout/",logout_view,name="logout")]