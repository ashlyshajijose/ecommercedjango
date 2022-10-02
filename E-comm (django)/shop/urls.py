from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('Eadmin/',views.Eadmin,name='Eadmin'),
    path('Euser/',views.Euser,name='Euser'),
    path('loginpage/',views.loginpage,name='loginpage'),
    path('signuppage/',views.signuppage,name='signuppage'),
    path('uprofile/',views.uprofile,name='uprofile'),
    path('add_product',views.add_product,name='add_product'),
    path('edit_product/<int:od>',views.edit_product,name='edit_product'),
    path('add_category',views.add_category,name='add_category'),
    path('edit_category/<int:od>',views.edit_category,name='edit_category'),
    path('showproduct',views.showproduct,name='showproduct'),
    path('show_category',views.show_category,name='show_category'),
    path('show_user',views.show_user,name='show_user'),

    path('cart/',views.cart,name='cart'),
    path('Login/',views.Login,name='Login'),
    path('Signup/',views.Signup,name='Signup'),
    path('Logout/',views.Logout,name='Logout'),
    path('eprofile/',views.eprofile,name='eprofile'),
    path('a_product',views.a_product,name='a_product'),
    path('e_product/<int:od>',views.e_product,name='e_product'),
    path('a_category',views.a_category,name='a_category'),
    path('e_category/<int:od>',views.e_category,name='e_category'),
    path('deletecust/<int:od>',views.deletecust,name='deletecust'),
    path('add_cart/<int:od>',views.add_cart,name='add_cart'),
    path('delete_product/<int:od>',views.delete_product,name='delete_product'),
]