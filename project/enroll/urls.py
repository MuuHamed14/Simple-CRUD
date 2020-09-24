from django.urls import path
from .import views 

app_name = 'enroll'
urlpatterns = [
    
    path('add_and_show_data/',views.add_show,name='add_and_show_data'),
     path('update_data/<int:id>/',views.update_data,name='update_data'),
    path('delete_student/<int:id>/',views.delete_data,name='delete_student'),
]
