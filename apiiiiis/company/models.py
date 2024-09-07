from django.db import models

# Create your models here.

import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['companies']
company = db['company']


class Company:

    @staticmethod
    def create_company(data):
        return company.insert_one(data)

    @staticmethod
    def get_all_companies():
        return list(company.find({}))

    @staticmethod
    def get_company(company_id):
        return company.find_one({"_id": company_id})

    @staticmethod
    def update_company(company_id, data):
        return company.update_one({"_id": company_id}, {"$set": data})

    @staticmethod
    def delete_company(company_id):
        return company.delete_one({"_id": company_id})
