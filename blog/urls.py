from django.urls import path
from . import views

app_name = "blog"
urlpatterns = [
    path('blog/', views.BlogListView.as_view(), name="list_view"),
    path('blog/<slug:slug>', views.BlogDetailView.as_view(), name='detail_view'),
]