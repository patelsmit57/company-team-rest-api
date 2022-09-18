from rest_framework.views import APIView  # FOR CLASS BASE VIEW
# from rest_framework.permissions import IsAuthenticated  # FOR  AUTHORIZATION
from rest_framework.response import Response


class getRoutes(APIView):
    def get(self, request):
        routes = [

            {'POST': '/api/token'},
            {'POST': '/api/refresh_token'},

            {'POST': '/api/company'},
            {'GET': '/api/team'},
            {'POST': '/api/company/uuid/team'},
            {'POST' : 'api/search'},
            {'GET': 'api/company/uuid'},

        ]
        return Response(routes)
