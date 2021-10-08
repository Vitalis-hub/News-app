from rest_framework import serializers
from newsapp.models import Newsapp

class NewsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Newsapp
        fields = ['name', 'date']

        