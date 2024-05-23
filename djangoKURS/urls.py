"""
URL configuration for djangoKURS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from rest_framework.routers import DefaultRouter
from kurs.views import dbViewSet
from django.contrib import admin

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView
)

urlpatterns = [
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path(
        'api/schema/swagger-ui/',
        SpectacularSwaggerView.as_view(url_name='schema'),
        name='swagger-ui'
    ),
    path(
        'api/schema/redoc/',
        SpectacularRedocView.as_view(url_name='schema'),
        name='redoc'
    ),
    path('admin/', admin.site.urls),
    path('api/add_stud/<str:nameSt>/<str:sur>/', dbViewSet.as_view({'post': 'v_add_student'}), name='v_add_student'),
    path('api/add_subj/<str:name>/<str:teacher>/', dbViewSet.as_view({'post': 'v_add_subj'}), name='v_add_subj'),
    path('api/set_mark/<str:nameSt>/<str:surSt>/<str:subj>/<int:markSt>/', dbViewSet.as_view({'post': 'v_set_mark'}), name='v_set_mark'),
    path('api/show_stud/', dbViewSet.as_view({'get': 'v_show_students'}), name='v_show_students'),
    path('api/show_subj/', dbViewSet.as_view({'get': 'v_show_subjects'}), name='v_show_subjects'),
    path('api/show_marks/<int:student_id>/', dbViewSet.as_view({'get': 'v_show_student_marks'}), name='v_show_subjects'),

]
