from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('add/',views.add,name='add'),
    path('add/addrecord/',views.addrecord, name='addrecord'),
    path('deletePage/delete/<int:id>',views.delete, name='delete'),
    path('deletePage/',views.deletePage, name='deletePage'),
    path('updatePage/',views.updatePage, name='updatePage'),
    path('updatePage/update/<int:id>',views.update, name='update'),
    path('updatePage/update/updaterecord/<int:id>',views.updaterecord, name='updaterecord'),
]