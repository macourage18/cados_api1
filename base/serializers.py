from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import * 
from rest_framework import serializers




class CompanySerializer(ModelSerializer):
  employee_count = SerializerMethodField(read_only=True)
  class Meta:
    model = Company
    fields = '__all__'

  def get_employee_count(self, obj):
    count = obj.advocate_set.count()
    return count
  

class AdvocateSerializer(ModelSerializer):
  company = CompanySerializer(allow_null=True, required=False)
  profilePic = serializers.ImageField(use_url=True)
  profilePic = AdvocateProfile(ModelSerializer)
  class Meta:
    model = Advocate
    fields = ['profilePic','username','bio','company']


class AdvocateAllSerializer(ModelSerializer):
  advocates = AdvocateSerializer()
  class Meta:
    model = AdvocateAll
    fields ='__all__'