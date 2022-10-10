from dataclasses import fields
from pyexpat import model
from xml.sax.handler import feature_external_ges
from rest_framework import serializers
from .models import Profile

class Profile_serializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['Address', 'County', 'State', 'City', 'zip_code']