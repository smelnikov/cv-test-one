from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework import permissions, response, viewsets
from rest_framework.decorators import action

from . import models, serializers


BASIC_SECURITY = [{'Basic': []}]


@method_decorator(name='list', decorator=swagger_auto_schema(security=BASIC_SECURITY))
@method_decorator(name='create', decorator=swagger_auto_schema(security=BASIC_SECURITY))
@method_decorator(name='retrieve', decorator=swagger_auto_schema(security=BASIC_SECURITY))
@method_decorator(name='update', decorator=swagger_auto_schema(security=BASIC_SECURITY))
@method_decorator(name='partial_update', decorator=swagger_auto_schema(security=BASIC_SECURITY))
@method_decorator(name='destroy', decorator=swagger_auto_schema(security=BASIC_SECURITY))
class ApplicationViewset(viewsets.ModelViewSet):
    """
    Приложения
    """
    permission_classes = (permissions.IsAuthenticated,)
    queryset = models.Application.objects
    serializer_class = serializers.Application

    @swagger_auto_schema(security=BASIC_SECURITY)
    @action(detail=True, methods=['post'])
    def refresh(self, request, pk=None):
        """
        Обновляет токен приложения
        """
        application = self.get_object()
        application.refresh()
        serializer = self.get_serializer(application)
        return response.Response(serializer.data)
