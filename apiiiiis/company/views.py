
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from bson.objectid import ObjectId
from .models import Company
from .serializers import CompanySerializer


class CompanyList(APIView):
    def get(self, request):
        companies = Company.get_all_companies()
        for company in companies:
            print(company['_id'])

            company["_id"] = str(company["_id"])
        return Response(companies)

    def post(self, request):
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            company_id = Company.create_company(serializer.validated_data)
            return Response({"_id": str(company_id.inserted_id)}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CompanyDetail(APIView):
    def get(self, request, company_id):
        company = Company.get_company(ObjectId(company_id))
        if company:
            company["_id"] = str(company["_id"])
            return Response(company)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, company_id):
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            updated_company = Company.update_company(ObjectId(company_id), serializer.validated_data)
            if updated_company.modified_count:
                return Response({"message": "Company updated successfully"})
            return Response({"message": "Company not found"}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, company_id):
        deleted_company = Company.delete_company(ObjectId(company_id))
        if deleted_company.deleted_count:
            return Response({"message": "Company deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        return Response({"message": "Company not found"}, status=status.HTTP_404_NOT_FOUND)



