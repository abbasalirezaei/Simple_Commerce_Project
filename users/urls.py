from django.urls import path,re_path
from .views import logout_view

# 


app_name='accounts'

urlpatterns = [
    # path('',home,name='home'),
    path('logout/',logout_view,name='logout'),
    # path('login/',AccountLoginView.as_view(),name='login'),
    # path('register/', SignUpCreateView.as_view(), name='register'),
    # path('activate/<slug:uidb64>/<slug:token>/',
    #      activate, name='activate'),

]