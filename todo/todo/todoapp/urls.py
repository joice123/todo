
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('delete/<int:task_id>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('cvd/',views.Taskview.as_view(),name='cvd'),
    path('lc/<int:pk>/',views.Detailview.as_view(),name='lc'),
    path('cvu/<int:pk>/',views.Taskupdate.as_view(),name='cvu'),
    path('cv/<int:pk>/',views.Deleteview.as_view(),name='cv'),

]
