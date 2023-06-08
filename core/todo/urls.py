from django.urls import path
from . import views


urlpatterns = [
    path("", views.TaskList.as_view() , name="list_task"),
    path("create/", views.TaskCreate.as_view(), name="create_task"),
    path('update/<int:pk>/', views.TaskUpdate.as_view(), name='update_task'),
    path('delete/<int:pk>/', views.TaskDelete.as_view(), name='delete_task'),
    path('done/<int:pk>/', views.TaskDone.as_view(), name='done_task'),

]