from django.conf import settings
from django.conf.urls import include
from django.urls import path
from django.conf.urls.static import static
from django.contrib import admin


from .views import ProductDetailView, ProductListView,VariationListView 

urlpatterns = [
    # Examples:
    # url(r'^$', 'newsletter.views.home', name='home'),
    # path('', 'products.views.product_list', name='products'),
    # path('admin/', admin.site.urls),
    path('', ProductListView.as_view(), name='products'),
    path('<int:id>/', ProductDetailView.as_view(), name='product_detail'),
    path('(?P<pk>\d+)/inventory/', VariationListView.as_view(), name='product_inventory'),
    # path('(?P<id>\d+)', 'products.views.product_detail_view_func', name='product_detail_function'),
]