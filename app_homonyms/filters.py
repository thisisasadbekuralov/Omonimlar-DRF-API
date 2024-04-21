from django_filters import FilterSet

from .models import Homonyms

class HomonymsFilter(FilterSet):
    class Meta:
        model = Homonyms
        fields = {
            'word': ['exact', 'icontains'],
        }