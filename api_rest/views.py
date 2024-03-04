from django.shortcuts import render

# Create your views here.
from .serializer import ComidaSerializer, BebidaSerializer, SnackSerializer
from .models import Comida, Bebida, Snack
from rest_framework import viewsets


class ComidaViewset(viewsets.ModelViewSet):
    queryset = Comida.objects.all()
    serializer_class= ComidaSerializer
    

class BebidaViewset(viewsets.ModelViewSet):
    queryset = Bebida.objects.all()
    serializer_class= BebidaSerializer
    

class SnackViewset(viewsets.ModelViewSet):
    queryset = Snack.objects.all()
    serializer_class= SnackSerializer