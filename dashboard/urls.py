from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('dashboard/', views.dashboard, name= 'dashboard-page'),
    path('upload/', views.upload, name= 'upload-page'),
    path('edit/<int:pk>', views.edit, name= 'edit-page'),
    path('delete/<int:pk>', views.delete, name= 'delete-page'),
    path('allstudents/',views.allStudents, name= 'allStudent-page'),
    path('allreport/',views.allReports, name= 'allReports-page')
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)