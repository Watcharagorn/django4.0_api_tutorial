from rest_framework import permissions, viewsets, generics, mixins
from rest_framework.response import Response
from rest_framework.decorators import permission_classes, action
from apps.mcm.models.order import Order
from apps.mcm.serializer.order import OrderCreateSerializer, OrderListSerializer
from django.utils import timezone


class OrderViewSet(viewsets.ModelViewSet):

    queryset = Order.objects.all()
    write_serializer_class = OrderCreateSerializer
    read_serializer_class = OrderListSerializer
    permission_classes(
        [permissions.IsAuthenticated, permissions.IsAuthenticatedOrReadOnly]
    )

    def get_serializer_class(self):
        if self.request.method == "POST":
            return self.write_serializer_class

        return self.read_serializer_class

    def perform_create(self, serializer):
        serializer.save(
            created_by=self.request.user,
            product_id=serializer.validated_data["product_id"],
            status="WAIT",
        )

    @action(
        methods=["get"], detail=False, permission_classes=[permissions.IsAuthenticated]
    )
    def me(self, request):
        user = request.user
        queryset = self.get_queryset().filter(created_by=user)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


# class UserOrderView(generics.GenericAPIView):

#     queryset = Order.objects.all()
#     serializer_class = OrderListSerializer
#     permission_classes([permissions.IsAuthenticated])

#     def get(self):
#         user = self.request.user
#         queryset = self.get_queryset().filter(created_by=user)

#         page = self.paginate_queryset(queryset)
#         if page is not None:
#             serializer = self.get_serializer(page, many=True)
#             return self.get_paginated_response(serializer.data)

#         serializer = self.get_serializer(queryset, many=True)
#         return Response(serializer.data)
