from django.urls import path

from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib import admin

from accounts.views import GenericClientAPIView, ClientAPIView, CustomClientRegisterView, GenericDriverAPIView, DriverAPIView, CustomDriverRegisterView, CustomAuthToken

from carts.views import (
        CartAPIView,
        GenericCartAPIView,
        CustomCartRegisterView,

        CartItemAPIView,
        GenericCartItemAPIView,
        CustomCartItemRegisterView
        # CartView, 
        # CheckoutAPIView,
        # CheckoutFinalizeAPIView,
        # CheckoutView, 
        # CheckoutFinalView,
        # ItemCountView, 
        )

from orders.views import (
                    GenericOrderAPIView,
                    OrderAPIView,
                    CustomOrderRegisterView
                    )


from products.views import (
        APIHomeView,
        CategoryListAPIView,
        CategoryRetrieveAPIView,
        CategoryByProductListAPIView,
        CategoryByProductRetrieveAPIView,
        ProductListAPIView,
        ProductRetrieveAPIView,
        HomeCategoryListAPIView,
        HomeCategoryRetrieveAPIView, 
        SlideListAPIView,
        SlideRetrieveAPIView
    )
from rest_framework.authtoken import views

urlpatterns = [
    path('api-token-auth/', CustomAuthToken.as_view()),
    path('admin/', admin.site.urls),
    # path('products/', include('products.urls')),
    path('categories/', include('products.urls_categories')),
]

urlpatterns += [

    path('api/clients/', ClientAPIView.as_view(), name="clients_api"),
    path('api/clients/<int:id>', GenericClientAPIView.as_view(), name="client_detail_api"),
    path('api/client-register/', CustomClientRegisterView.as_view(), name="client_create_api"),


    path('api/drivers/', DriverAPIView.as_view(), name="drivers_api"),
    path('api/drivers/<int:id>', GenericDriverAPIView.as_view(), name="driver_detail_api"),
    path('api/driver-register/', CustomOrderRegisterView.as_view(), name="driver_create_api"),


    path('api/orders/', OrderAPIView.as_view(), name="orders_api"),
    path('api/orders/<int:id>', GenericOrderAPIView.as_view(), name="order_detail_api"),
    path('api/order-register/', CustomOrderRegisterView.as_view(), name="order_create_api"),


    path('api/carts/', CartAPIView.as_view(), name="carts_api"),
    path('api/carts/<int:id>', GenericCartAPIView.as_view(), name="cart_detail_api"),
    path('api/cart-register/', CustomCartRegisterView.as_view(), name="cart_create_api"),


    path('api/cartItems/', CartItemAPIView.as_view(), name="cartItems_api"),
    path('api/cartItems/<int:id>', GenericCartItemAPIView.as_view(), name="cartItem_detail_api"),
    path('api/cartItem-register/', CustomCartItemRegisterView.as_view(), name="cartItem_create_api"),



    path('api/', APIHomeView.as_view(), name='home_api'),
    # path('api/user/address/', UserAddressListAPIView.as_view(), name='user_address_list_api'),
    # path('api/user/address/create/', UserAddressCreateAPIView.as_view(), name='user_address_create_api'),
    # path('api/user/checkout/$', UserCheckoutAPI.as_view(), name='user_checkout_api'),
    # path('api/cart/', CartAPIView.as_view(), name='cart_api'),
    # path('api/checkout/', CheckoutAPIView.as_view(), name='checkout_api'),
    # path('api/checkout/finalize/', CheckoutFinalizeAPIView.as_view(), name='checkout_finalize_api'),
    path('api/categories/', CategoryListAPIView.as_view(), name='categories_api'),
    path('api/categories/<int:pk>/', CategoryRetrieveAPIView.as_view(), name='category_detail_api'),

    path('api/categoriesByProduct/', CategoryByProductListAPIView.as_view(), name='categories_by_product_api'),
    path('api/categoriesByProduct/<int:pk>/', CategoryByProductRetrieveAPIView.as_view(), name='category_by_product_detail_api'),

    path('api/home-categories/', HomeCategoryListAPIView.as_view(), name='homeCategories_api'),
    path('api/home-categories/<int:pk>/', HomeCategoryRetrieveAPIView.as_view(), name='homeCategory_detail_api'),
    # path('api/orders/', OrderListAPIView.as_view(), name='orders_api'),
    # path('api/orders/(?P<pk>\d+)/', OrderRetrieveAPIView.as_view(), name='order_detail_api'),
    path('api/products/', ProductListAPIView.as_view(), name='products_api'),
    path('api/products/<int:pk>/', ProductRetrieveAPIView.as_view(), name='products_detail_api'),

    path('api/slides/', SlideListAPIView.as_view(), name='slides_api'),
    path('api/slides/<int:pk>/', SlideRetrieveAPIView.as_view(), name='slides_detail_api'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
