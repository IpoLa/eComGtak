from django.urls import path

from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib import admin

from accounts.views import GenericClientAPIView, ClientAPIView, CustomClientRegisterView, GenericDriverAPIView, DriverAPIView, CustomDriverRegisterView

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
        ProductListAPIView,
        ProductRetrieveAPIView,
    )


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('products/', include('products.urls')),
    path('categories/', include('products.urls_categories')),
]

urlpatterns += [

    path('api/clients/', ClientAPIView.as_view()),
    path('api/client/<int:id>', GenericClientAPIView.as_view()),
    path('api/client-register/', CustomClientRegisterView.as_view()),


    path('api/drivers/', DriverAPIView.as_view()),
    path('api/driver/<int:id>', GenericDriverAPIView.as_view()),
    path('api/driver-register/', CustomOrderRegisterView.as_view()),


    path('api/orders/', OrderAPIView.as_view()),
    path('api/order/<int:id>', GenericOrderAPIView.as_view()),
    path('api/order-register/', CustomOrderRegisterView.as_view()),


    path('api/carts/', CartAPIView.as_view()),
    path('api/cart/<int:id>', GenericCartAPIView.as_view()),
    path('api/cart-register/', CustomCartRegisterView.as_view()),


    path('api/cartItems/', CartItemAPIView.as_view()),
    path('api/cartItem/<int:id>', GenericCartItemAPIView.as_view()),
    path('api/cartItem-register/', CustomCartItemRegisterView.as_view()),



    path('api/', APIHomeView.as_view(), name='home_api'),
    # path('api/user/address/', UserAddressListAPIView.as_view(), name='user_address_list_api'),
    # path('api/user/address/create/', UserAddressCreateAPIView.as_view(), name='user_address_create_api'),
    # path('api/user/checkout/$', UserCheckoutAPI.as_view(), name='user_checkout_api'),
    # path('api/cart/', CartAPIView.as_view(), name='cart_api'),
    # path('api/checkout/', CheckoutAPIView.as_view(), name='checkout_api'),
    # path('api/checkout/finalize/', CheckoutFinalizeAPIView.as_view(), name='checkout_finalize_api'),
    path('api/categories/', CategoryListAPIView.as_view(), name='categories_api'),
    path('api/categories/<int:pk>/', CategoryRetrieveAPIView.as_view(), name='category_detail_api'),
    # path('api/orders/', OrderListAPIView.as_view(), name='orders_api'),
    # path('api/orders/(?P<pk>\d+)/', OrderRetrieveAPIView.as_view(), name='order_detail_api'),
    path('api/products/', ProductListAPIView.as_view(), name='products_api'),
    path('api/products/<int:pk>/', ProductRetrieveAPIView.as_view(), name='products_detail_api'),
]

