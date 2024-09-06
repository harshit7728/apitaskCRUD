from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets

from .models import Company, Department, CustomUser
from .Serializers import CompanySerializer, DepartmentSerializer, CustomUserSerializer, uploadserial


class CreateCompanyView(generics.CreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        company = self.serializer_class.Meta.model.objects.get(id=response.data['id'])  # Get the newly created company

        hr_department = Department.objects.create(name=Department.HR, company=company)
        sales_department = Department.objects.create(name=Department.SALES, company=company)

        return Response({
            "company": CompanySerializer(company).data,
            "departments": [
                DepartmentSerializer(hr_department).data,
                DepartmentSerializer(sales_department).data
            ]
        }, status=status.HTTP_201_CREATED)


class CreateUserView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    def create(self, request, *args, **kwargs):
        role = request.data.get('role')
        if role not in [CustomUser.STANDARD_USER, CustomUser.SUPER_USER]:
            return Response({"error": "Invalid role"}, status=status.HTTP_400_BAD_REQUEST)

        return super().create(request, *args, **kwargs)


class FileUploadView(APIView):

    def post(self, request):
        serializer = uploadserial(data=request.data)

        if serializer.is_valid():
            username = serializer.validated_data['name']
            try:
                csuser = CustomUser.objects.get(username=username)
                if csuser.role == 'SuperUser':
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                else:
                    return Response({'message': "Only SuperUser is allowed"}, status=status.HTTP_400_BAD_REQUEST)
            except CustomUser.DoesNotExist:
                return Response({'message': "User does not exist or only SuperUser is allowed"},
                                status=status.HTTP_400_BAD_REQUEST)
