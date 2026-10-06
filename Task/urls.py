from django.urls import path,re_path
from .views import *

urlpatterns=[path("home/",home,name="intro"),
             path("add-task/",add_task,name="add_task"),
             path("create-task/",view_tasks,name="view_tasks"),
             re_path(r"^edited/([0-9]+)/$",update_task,name="edited")]