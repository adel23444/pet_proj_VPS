from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from src.apps.api.serializers.vps import VPSSerializer
from src.apps.vps.models import VPS

'''

@method_decorator(
    name='list',
    decorator=swagger_auto_schema(
        operation_summary="Получение списка VPS",
        tags=["VPS"]
    )
)
@method_decorator(
    name='patrial_update',
    decorator=swagger_auto_schema(
        operation_summary='Обновление статуса VPS',
        tags=["VPS"]
    )
)
@method_decorator(
    name='create',
    decorator=swagger_auto_schema(
        operation_summary='Создание VPS-сервера',
        tags=["VPS"]
    )
)
@method_decorator(
    name='retrieve',
    decorator=swagger_auto_schema(
        operation_summary="Получение VPS по UID",
        tags=["VPS"]
    )
)
'''


class VPSViewSet(viewsets.ModelViewSet):
    authentication_classes = (SessionAuthentication,)
    serializer_class = VPSSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']
    my_tags = ['vps']
    queryset = VPS.objects.all()
