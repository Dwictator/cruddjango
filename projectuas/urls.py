
from django.contrib import admin
from django.urls import path
from inputproduct.views import createView, store, index, viewProduct, deleteProduct, updateView, update

urlpatterns = [
    path('create/', createView),
    path('store/', store, name='store'),
    path('admin/', admin.site.urls),
    path('',index),
    path('delete/<int:pk>', deleteProduct, name='deleteProduct'),
    path('update/<int:pk>', updateView, name='updateView'),
    path('edit/<int:pk>', update, name='update'),
]
