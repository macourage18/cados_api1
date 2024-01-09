from django.shortcuts import render, redirect
from django.http import JsonResponse
from rest_framework.decorators import  api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .serializers import *
from django.db.models import Q

from .models import *
# Create your views here.

@api_view(['GET'])
def endpoints(request):
  data=['/advocates', 'createAd','advocates/:username', 'companies', "compaines/:name", "token" ]
  return Response(data)


# @permission_classes([IsAuthenticated])
class AdvocatesView(APIView):
    def get(self, request):
        query = request.GET.get('query', '')

        advocates = AdvocateProfile.objects.filter(
          Q(advocate__username__icontains=query) | 
          Q(advocate__bio__icontains=query)| 
          Q(advocate__company__company__icontains=query))
        
        # Creating a list of AdvocateAll instances
        advocate_all_instances = [
            AdvocateAll(advocates=advocate)
            for advocate in advocates
        ]
        
        # Serializing the list of AdvocateAll instances
        serializer = AdvocateAllSerializer(advocate_all_instances, many=True, context={'request': request})
        print(serializer.data)
        return Response(serializer.data)

  

@api_view(["GET","POST"])
def advocate_create(request):
  if request.method == 'GET':
    query = request.GET.get('query', '')
    
    if query is None:
        query = ''

    profilePic = AdvocateProfile.objects.filter(
      Q(advocate__username__icontains=query)|
      Q(advocate__bio__icontains=query) |
      Q(advocate__company__company__icontains=query)
    )

    serializer = AdvocateProfileSerializer(profilePic, many=True, context={'request': request})
    print(serializer.data)

    return Response(serializer.data)

 
  
  if request.method == "POST":
    advocate = Advocate.objects.create(
       username=request.data['username'],
       bio = request.data['bio'],
       profilePic=request.data['profilePic']
       )
    serializer= AdvocateSerializer(advocate, many=False)

    return Response(serializer.data)
  
class ProfilePicDetailView(APIView):
    def get(self, request, *args, **kwargs):
        profile = AdvocateProfile.objects.all()
        serializer = AdvocateProfileSerializer(profile, many=True, context={'request': request})
        return Response(serializer.data)


class AdvocateDetial(APIView):

  def get_object(self, username):
    try:
      return Advocate.objects.get(username=username)
    except Advocate.DoesNotExist:
      raise Response('Advocate does not exit')

  def get(self, request, username):
    advocate = self.get_object(username)
    serializer = AdvocateSerializer(advocate, many=False)
    return Response(serializer.data)
  
  def put(self, request, username):
    advocate = self.get_object(username)
    advocate.username=request.data['username']
    advocate.bio=request.data['bio']
    advocate.save()
    serializer = AdvocateSerializer(advocate, many=False)
    return Response(serializer.data)
  
  def delete(self, request, username):
    advocate = self.get_object(username)
    advocate.delete()
    return Response('user was deleted')

@api_view(['GET', "POST"])
def companies_list(request):
  if request.method == 'GET':

    query= request.GET.get('query')
    
    if query == None:
      query=''

    
    companies = Company.objects.filter(Q(company__icontains=query) | Q(bio__icontains=query))
    serializer = CompanySerializer(companies, many=True)
    return Response(serializer.data)
  
  if request.method == "POST":
    company = Company.objects.create(
      company=request.data['company'],
      bio=request.data['bio']
    )

    serializer= CompanySerializer(company, many=False)
    return Response(serializer.data)


@api_view(['GET', "PUT", "DELETE"])
def companies_details(request, company):
  company=Company.objects.get(company=company)
  if request.method == 'GET':
    serializer = CompanySerializer(company, many=False)
    return Response(serializer.data)
  
  if request.method == "PUT":
    company.company=request.data['company']
    company.bio=request.data['bio']
    
    company.save()
    serializer=CompanySerializer(company, many=False)
    return Response(serializer.data)
  
  if request.method == "DELETE":
    company.delete()
    return Response('company has been deleted')
