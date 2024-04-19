from rest_framework import serializers


from .models import Homonyms, WordType

class HomonymsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Homonyms
        fields = '__all__'
        depth = 1


class HomonymsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Homonyms
        fields = ['id', 'word']
