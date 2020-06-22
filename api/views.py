from rest_framework.response import Response
from api import models,serializer
from rest_framework.generics import (
ListAPIView,
RetrieveAPIView,
UpdateAPIView,
RetrieveUpdateAPIView,
ListCreateAPIView,
DestroyAPIView
)

class StudentListView(ListCreateAPIView):
    queryset = models.Student.objects.all()
    serializer_class = serializer.StudentSerializer

class StudentDetailsView(UpdateAPIView):
    queryset = models.Student.objects.all()
    serializer_class = serializer.StudentSerializer

class StudentDeleteView(DestroyAPIView):
    queryset = models.Student.objects.all()
    serializer_class = serializer.StudentSerializer



