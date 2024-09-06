from django.urls import path
from .views import CreateCompanyView, CreateUserView, FileUploadView

urlpatterns = [
    path('create-company/', CreateCompanyView.as_view(), name='create-company'),
    path('create-user/', CreateUserView.as_view(), name='create-user'),
    path('create-upload/', FileUploadView.as_view(), name='upload-user'),
]
