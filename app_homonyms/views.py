from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.generics import ListAPIView

from .filters import HomonymsFilter
from .models import Homonyms
from .serializers import HomonymsDetailSerializer, HomonymsListSerializer
from .filters import HomonymsFilter


class HomonymsViewSet(viewsets.ModelViewSet):
    queryset = Homonyms.objects.all()
    serializer_class = HomonymsDetailSerializer
    # filter_backends = (DjangoFilterBackend,)
    # filterset_class = HomonymsFilter

class HomonymsListView(ListAPIView):
    queryset = Homonyms.objects.all()
    serializer_class = HomonymsListSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = HomonymsFilter

