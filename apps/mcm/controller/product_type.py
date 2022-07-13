from django.contrib import admin
from django.contrib.auth.models import User
from django.urls import include, path
from rest_framework import generics, mixins, permissions, status, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.mcm.models.product_type import ProductType
from apps.mcm.serializer.product_type import ProductTypeSerializer
from utilities.env_manager import get_environ
from yaml import serialize


class ProductTypeViewSet(viewsets.ModelViewSet):

    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer
    permission_classes([permissions.IsAuthenticatedOrReadOnly])

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
