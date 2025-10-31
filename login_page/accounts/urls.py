# from django.urls import path
# from . import views

# urlpatterns = [
#     path('signup/', views.signup_view, name='signup'),
#     path('login/', views.login_view, name='login'),
#     path('success/', views.success_view, name='success'),
# ]


from django.urls import path
from . import views

urlpatterns = [
    path('accounts/login/', views.login_view, name='login'),  # 👈 add this
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('success/', views.success_view, name='success'),
    path('logout/', views.logout_view, name='logout'),
]
