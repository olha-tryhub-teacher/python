from django.urls import path
from .views import *

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
    path("<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path("task-create/", TaskCreateView.as_view(), name="task-create"),
    path("<int:pk>/complete/", TaskCompleteView.as_view(), name="task-complete"),
    path("comment/edit/<int:pk>/", CommentUpdateView.as_view(), name="edit_comment"),
    path("comment/delete/<int:pk>/", CommentDeleteView.as_view(), name="delete_comment"),
    path("comment/like/<int:pk>/", CommentLikeToggle.as_view(),
         name="comment-like-toggle"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", CustomLogoutView.as_view(), name="logout"),
    path("register/", RegisterView.as_view(), name="register"),
]

app_name = "tasks"
