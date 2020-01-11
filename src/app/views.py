from drf_yasg.utils import swagger_auto_schema
from rest_framework import permissions, response, views

from . import authentication, serializers


TOKEN_SECURITY = [{'ApiKey': []}]


class TestView(views.APIView):
    """
    Получает данные о текущем приложении
    """
    authentication_classes = (authentication.ApplicationAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    http_method_names = ['get']

    @swagger_auto_schema(security=TOKEN_SECURITY)
    def get(self, request):
        serializer = serializers.Application(request.auth)
        return response.Response(serializer.data)
