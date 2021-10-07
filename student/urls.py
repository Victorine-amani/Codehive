from django.urls import path
from .views import delete_student, edit_student, register_student, student_list, student_profile
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    path("register/", register_student, name="register_student"),
    path("list/", student_list, name="student_list"),
    path("edit/<int:id>/", edit_student, name="edit_student"),
    path("profile/<int:id>/", student_profile, name="student_profile"),
    path("delete/<int:id>/", delete_student, name="delete_student"),
    
    
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)



