from api import views
from django.urls import path

urlpatterns = [
    path('students/',views.StudentListView.as_view()),
    path('students/<int:pk>',views.StudentDetailsView.as_view()),
    path('delete/<int:pk>',views.StudentDeleteView.as_view())

]