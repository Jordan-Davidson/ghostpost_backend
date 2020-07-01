from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action

from api.models import RoastBoast
from api.serializers import RoastBoastSerializer
# Create your views here.

class RoastBoastViewset(viewsets.ModelViewSet):
    queryset = RoastBoast.objects.all()
    serializer_class = RoastBoastSerializer
    
    @action(detail=True, methods=['post'])
    def upvote(self, request, id):
        roastboast = self.get_object()
        roastboast.upvotes += 1
        roastboast.save()

    @action(detail=True, methods=['post'])
    def downvote(self, request, id):
        roastboast = self.get_object()
        roastboast.downvotes -= 1
        roastboast.save()

