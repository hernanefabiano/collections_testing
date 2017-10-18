from __future__ import absolute_import, division, print_function, unicode_literals

from django.db.models import F
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.http import Http404
from django.utils.decorators import method_decorator

from rest_framework import viewsets
from rest_framework import exceptions
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

from .models import CarCollection
from .serializer import CarSerializer

class CarModelListViewSet(viewsets.ModelViewSet):
    """
    A simple ModelViewSet for display of change order of car listings.
    
    params: color: red | blue | ...

    Object Oriented Programming(Inheritance and Polymorphism)
     - Inherit ModelViewSet from viewsets class to display and manage all cars.
     - Override list, partial_udpate and queryset methods to filter data and change order of listings.
    """
    serializer_class = CarSerializer
    
    def get_queryset(self):
        queryset = CarCollection.objects.all()
        color = self.request.GET.get('color')
        if color:
            queryset = queryset.filter(color__icontains=color)
        return queryset.order_by('position')

    def list(self, request):
        queryset = self.get_queryset()
        serializer = CarSerializer(queryset, many=True)
        return Response(serializer.data)

    def partial_update(self, request, pk=None):
        """
        Move car explicitly to a certain position.
        
        Select a car and use it as param to identify the current position 
        of the car to be moved and swap the position.
        """
        queryset = self.get_queryset()
        car_to_swap_pk = request.data.get('car', None)
        card_to_move_pk = pk

        if not car_to_swap_pk and not card_to_move_pk:
            return Response({
                'error': 'API required card-id/position to be swapped is needed to proceed.'
                })
        
        car_to_swap = get_object_or_404(queryset, pk=car_to_swap_pk) 
        car_to_swap_position = car_to_swap.position

        car_to_move = get_object_or_404(queryset, pk=pk) 
        car_to_move_position = car_to_move.position

        car_to_swap.position = car_to_move_position
        car_to_move.position = car_to_swap_position

        car_to_move.save()
        car_to_swap.save()
        
        return Response({"status": "successfully moved and change position of the car."})
