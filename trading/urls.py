from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('signup',views.signup,name='signup'),
    path('home',views.login,name='login'),
    path('trading',views.trading,name='trading'),
    path('wallets',views.wallets,name='wallets'),
    path('balances',views.balances,name='balances'),
    path('profit',views.profit,name='profit'),
    path('pooling',views.pooling,name='pooling'),
    path('trade_history',views.trade_history,name='trade_history'),
    path('edit_profile',views.edit_profile,name='edit_profile'),
    path('verification',views.verification,name='verification'),
    path('security',views.security,name='security'),
    path('logout',views.logout,name='logout'),
    path('account_verification',views.account_verification,name='account_verification'),
    path('verification',views.verification,name='verification'),
    
   
    
    
    ]