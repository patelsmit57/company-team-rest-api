from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import CompanySerializer, TeamSerializer
from home.models import Company, Team
# Create your views here.

class company(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            name = request.data['name']
            li = Company.objects.filter(name=name)
            if len(li):
                return Response({'msg':'This Company name already exists'})
            else:
                Camp = serializer.save()
                return Response({'msg':'Company Created','data' : serializer.data},status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class companyDetail(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        id=kwargs.get('uuid', None)
        projects = Company.objects.filter(UUID=id)
        serializer = CompanySerializer(projects, many=True)
        return Response(serializer.data)
    # def delete(self, request, format=None):
    #     try:
    #         fundraiser_others_obj = Company.objects.get(email_id = request.data[''])
    #         fundraiser_others_obj.delete()
    #         return Response({'status' : 200 , 'message' : 'your data is deleted'})
    #     except Exception as e:
    #         print(e)
    #         return Response({'status' : 403 , 'message' : 'invalid email_id'})



class team(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        print(kwargs.get('uuid', None))
        request.data['CompanyID'] = kwargs.get('uuid', None)
        serializer = TeamSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            teams = Company.objects.filter(name=request.data['CompanyID'])
            teams_data = teams.filter(name=request.data['Lead_Name'])
            if len(teams_data):
                return Response({'msg':'This Team name already exists'})
            else:
                te = serializer.save()
                return Response({'msg':'Team Created', 'data' : serializer.data},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class search(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        name = request.data['name']
        company_name = Company.objects.all()
        projects = company_name.filter(name__icontains=name)
        if len(projects)>=1:
            serializer = CompanySerializer(projects, many=True)
            print(projects)
            return Response(serializer.data)
        else:
            return Response({'msg':'No Data'})


class getTeam(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        projects = Team.objects.all()
        serializer = TeamSerializer(projects, many=True)
        return Response(serializer.data)