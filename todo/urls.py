from django.urls import path
from .views import RegisterView, LoginView, TodoListView, TodoDetailView, TodoShareView, TodoAccessLogView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('todos/', TodoListView.as_view(), name='todo-list'),
    path('todos/<str:pk>/', TodoDetailView.as_view(), name='todo-detail'),
    path('todos/<str:pk>/share/', TodoShareView.as_view(), name='todo-share'),
    path('todos/<str:pk>/access-log/', TodoAccessLogView.as_view(), name='todo-access-log'),
]
