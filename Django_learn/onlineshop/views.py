from django.shortcuts import render

from .models import Order
from .serializers import OrderSerializer

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
class OrderView(APIView):
    def get(slef, request):
        try:
            orders = Order.objects.all()
            serializer = OrderSerializer(orders, many = True)

            return Response({
                'data': serializer.data,
                'message': 'Order data retrieved successfully'
            },
            status = status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({
                'data': {},
                'message': 'Failed to retrieve order data'
            }, status = status.HTTP_400_BAD_REQUEST)
        
    def post(self, request):
        try:
            data = request.data
            serializer = OrderSerializer(data = data)

            if not serializer.is_valid():
                return Response({
                    'data': serializer.errors,
                    'message': 'Invalid data to insert'
                }, status = status.HTTP_400_BAD_REQUEST)
            
            serializer.save()

            return Response({
                'data': serializer.data,
                'message': 'Order data saved successfully'
            }, status = status.HTTP_201_CREATED)
        
        except Exception as e:
            return Response({
                'data': {},
                'message': 'Failed to save order data'
            }, status = status.HTTP_400_BAD_REQUEST)
        

    def patch(self, request):
        try:
            data = request.data
            order = Order.objects.filter(id = data['id'])

            if not order.exists():
                return Response({
                    'data': {},
                    'message': 'Order data not found to update'
                }, status = status.HTTP_404_NOT_FOUND)
            
            serializer = OrderSerializer(order[0], data = data, partial = True)

            if not serializer.is_valid():
                return Response({
                    'data': serializer.errors,
                    'message': 'Something went Wrong'
                }, status = status.HTTP_500_BAD_REQUEST)

            serializer.save()

            return Response({
                'data': serializer.data,
                'message': 'Order data updated successfully'
            }, status = status.HTTP_200_OK)
        
        except Exception as e:
            return Response({
                'data': {},
                'message': 'Failed to update order data'
            }, status = status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request):
        try:
            data = request.data
            order = Order.objects.filter(id = data['id'])

            if not order.exists():
                return Response({
                    'data': {},
                    'message': 'Order data not found to delete'
                }, status = status.HTTP_404_NOT_FOUND)
            
            order.delete()

            return Response({
                'data': {},
                'message': 'Order data deleted successfully'
            }, status = status.HTTP_200_OK)
        
        except Exception as e:
            return Response({
                'data': {},
                'message': 'Failed to delete order data'
            }, status = status.HTTP_400_BAD_REQUEST)