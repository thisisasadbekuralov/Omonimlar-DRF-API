from rest_framework import viewsets
from rest_framework.generics import ListAPIView

from .models import Homonyms
from .serializers import HomonymsDetailSerializer, HomonymsListSerializer


class HomonymsViewSet(viewsets.ModelViewSet):
    queryset = Homonyms.objects.all()
    serializer_class = HomonymsDetailSerializer


class HomonymsListView(ListAPIView):
    queryset = Homonyms.objects.all()
    serializer_class = HomonymsListSerializer

