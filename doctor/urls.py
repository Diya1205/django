from django.urls import path
from . import views

urlpatterns = [
    path('doctors/', views.doctor_list, name='doctor_list'),
    path('doctors/add/', views.add_doctor, name='add_doctor'),
    path('doctors/edit/<int:pk>/', views.edit_doctor, name='edit_doctor'),
    path('doctors/delete/<int:pk>/', views.delete_doctor, name='delete_doctor'),
    path('ajax-doctors/', views.ajax_doctor_list, name='ajax_doctor_list'),
    path('ajax-doctors/add/', views.ajax_doctor_add, name='ajax_doctor_add'),
    path('ajax-doctors/update/<int:pk>/', views.ajax_doctor_update, name='ajax_doctor_update'),
    path('ajax-doctors/delete/<int:pk>/', views.ajax_doctor_delete, name='ajax_doctor_delete'),
]
