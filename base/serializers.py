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
  class Meta:
    model = Advocate
    fields = '__all__'

class AdvocateProfileSerializer(ModelSerializer):
  url = serializers.HyperlinkedIdentityField(view_name='profilePicDetail', read_only=True)
  advocate=AdvocateSerializer()
  class Meta:
    model= AdvocateProfile
    fields= ['profilePic','advocate','url']

        
class AdvocateAllSerializer(ModelSerializer):
  advocates = AdvocateProfileSerializer()
  class Meta:
    model = AdvocateAll
    fields ='__all__'