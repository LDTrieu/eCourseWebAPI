from django.contrib import admin
from django.urls import path, include
from . import views
#from .admin import admin_site
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('courses',views.CourseViewSet)
router.register('lessons',views.LessonViewSet)

# /courses/ -GET
# /courses/ - POST
# /courses/{course_id}/ -GET
# /courses/{course_id}/ - PUT
# /courses/{courses_id}/ -DELETE

urlpatterns = [
    path('',include(router.urls)),
    #path('',views.index),

]
