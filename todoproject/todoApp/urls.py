from django.urls import path
from . import views

urlpatterns=[
    path('',views.login),
     path('register_form',views.register_form),
    path('register',views.register),
    path('dashboard',views.dashboard),
    path('dashboard_taskview',views.dashboard_taskview),
    path('editbook/<int:id>',views.editbook),
    path('updatebook/<int:id>',views.updatebook),
    path('deletedata/<int:id>',views.deletedata),
]