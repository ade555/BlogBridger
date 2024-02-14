from django.urls import path

from . import views

urlpatterns = [
    path('list/', views.PostListCreateView.as_view(), name="list_post"),
    path('create/', views.PostListCreateView.as_view(), name="create_post"),
    path('<int:post_id>/', views.RetrieveUpdateDeletePostView.as_view(), name='post_retrieve_delete_update'),
    path('<int:post_id>/comment/', views.CommentView.as_view(), name="create-comment")
]
