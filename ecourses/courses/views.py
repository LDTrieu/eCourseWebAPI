from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from rest_framework import viewsets,permissions
from .models import Course, Lesson
from .serializers import CourseSerializer,LessonSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.filter(active=True)
    serializer_class = CourseSerializer
    #permission_classes = [permissions.IsAuthenticated]
    # list --> xem danh sach khoa hoc
    # ... (POST) --> them khoa hoc
    # detail ->> xem chi tiet 1 khoa hoc
    # ... (PUT) --> cap nhat
    # ... (DELETE) --> Xoa khoa hoc

    def get_permissions(self):
        if self.action=='list':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]

class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.filter(active=True)
    serializer_class = LessonSerializer

    # an lesson (active=false)




def index(request):
    return render(request,
                  template_name='index.html',
                  context={'name':'Dinh Trieu'
                           })
