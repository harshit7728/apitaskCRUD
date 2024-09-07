
from django.urls import path
from .views import CompanyList, CompanyDetail

urlpatterns = [
    path("companies/", CompanyList.as_view(), name="company-list"),
    path("companies/<str:company_id>/", CompanyDetail.as_view(), name="company-detail"),
]
