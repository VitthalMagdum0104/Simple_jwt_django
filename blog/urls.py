from django.urls import path
from .views import BlogList, CreateBlog, RetrieveUpdateView, DestroyView

urlpatterns = [
    path('blogs/', BlogList.as_view(), name='blogs'),
    path('create_blog/', CreateBlog.as_view(), name='create'),
    path('fetch/', CreateBlog.as_view(), name='fetch'),
    path('edit_or_fetch/<int:pk>', RetrieveUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>', DestroyView.as_view(), name='delete')
]
