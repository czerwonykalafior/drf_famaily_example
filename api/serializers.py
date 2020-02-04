from rest_framework import serializers

from api import models


class FamilySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Family
        fields = '__all__'


class PapaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Papa
        fields = '__all__'


class MamaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Mama
        fields = '__all__'


class KidSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Kid
        fields = '__all__'


class ToySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Toy
        fields = '__all__'


class ToyOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ToyOwner
        fields = '__all__'
