from django.urls import path
from . import views

app_name = 'todoapp'
urlpatterns = [
    path('',views.home,name='home'),
    # path('details/',views.details,name='details'),
    path('delete/<int:task_id>/',views.delete,name='delete'),
    path('update/<int:task_id>/',views.update,name='update'),
    path('listview/',views.List_View.as_view(),name='listview'),
    path('detailview/<int:pk>/',views.Detail_View.as_view(),name='detailview'),
    path('updateview/<int:pk>/',views.Update_View.as_view(),name='updateview'),
    path('deleteview/<int:pk>/',views.Delete_View.as_view(),name='deleteview')


]