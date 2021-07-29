# from src.views import Home,register_product,register_bcustmer,login_bcustomer,order_product
from django.urls import path
from src import views
urlpatterns = [
    path('',views.Home,name='home'),
    path('register_product',views.register_product,name = 'register_product'),
    path('register_bcustomer',views.register_bcustmer,name = 'register_bcustomer'),
    path('login_bcustomer',views.login_bcustomer,name = 'login_bcustomer'),
    path('view_product',views.view_product,name = 'view_product'),
    path("delete_product",views.product_delete,name="product_delete"),
    path("update_product/<int:pid>/",views.update_product,name="update_product"),
    path("payment",views.payment,name="payment"),





    # path("ordered_product",views.ordered,name="ordered_p"),

    # path("o/<int:ord_id>/",views.ord,name="ord"),
    # path("o/<int:ord_id>/",views.ord,name="ord"),

    # path("order",views.)

]
