from django.shortcuts import render
from .models import *

# Create your views here.


# API bult-in imports
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *







@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/task-list/',
		'Detail View':'/task-detail/<str:pk>/',
		'Create':'/task-create/',
		'Update':'/task-update/<str:pk>/',
		'Delete':'/task-delete/<str:pk>/',
		}

	return Response(api_urls)

@api_view(['GET'])
def registerList(request):
	registerer = Registers.objects.all().order_by('-id')
	serializer = RegistererSerializer(registerer, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def registerDetail(request, pk):
	registerer = Registers.objects.get(id=pk)
	serializer = RegistererSerializer(registerer, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def registerCreate(request):
	serializer = RegistererSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
def registerUpdate(request, pk):
	registerer = Registers.objects.get(id=pk)
	serializer = RegistererSerializer(instance=registerer, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def registerDelete(request, pk):
	registerer = Registers.objects.get(id=pk)
	registerer.delete()

	return Response('Item succsesfully deleted!')

