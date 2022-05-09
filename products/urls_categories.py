from django.conf import settings
from django.conf.urls import include
from django.urls import path
from django.conf.urls.static import static
from django.contrib import admin


from .views import CategoryListView, CategoryDetailView, HomeCategoryListView, HomeCategoryDetailView

urlpatterns = [
    # Examples:
    # url(r'^$', 'newsletter.views.home', name='home'),
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('<str:slug>/', CategoryDetailView.as_view(), name='category_detail'),

    path('home-categories/', HomeCategoryListView.as_view(), name='homeCategories'),
    path('<str:slug>/', HomeCategoryDetailView.as_view(), name='homeCategories_api'),
    # url(r'^(?P<id>\d+)', 'products.views.product_detail_view_func', name='product_detail_function'),
]