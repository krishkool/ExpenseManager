from django.urls.resolvers import URLPattern
from .import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/login/', views.login_view, name='login'),
    path('logout', views.logout_view),
    path('home', views.home, name='home'),
    path('viewexpense', views.expenseView, name='viewexpense'),
    path('viewwallet', views.walletView, name='viewwallet'),
    path('viewtotexpense', views.totexpenseView, name='viewtotexpense'),
    path('reset', views.reset_view, name='reset'),
    path('passwordreset', views.passReset),

    path('addbalance', views.addBalance),
    path('showbalance', views.showBalance),
    path('showexpense', views.showExpenses),
    path('addexpensedata', views.addExpense)


]