from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from api import serializers

from api import models


class FamilyViewSet(viewsets.ModelViewSet):
    queryset = models.Family.objects.all()
    serializer_class = serializers.FamilySerializer

    @action(detail=True)
    def members(self, request, pk=None):
        kids = models.Kid.objects.filter(family__id=pk)
        kid_serializer = serializers.KidSerializer(kids, many=True)

        papa = models.Papa.objects.filter(family__id=pk)
        papa_serializer = serializers.PapaSerializer(papa, many=True)

        mama = models.Mama.objects.filter(family__id=pk)
        mama_serializer = serializers.MamaSerializer(mama, many=True)

        return Response({'papa': papa_serializer.data,
                         'mama': mama_serializer.data,
                         'kids': kid_serializer.data})


class PapaViewSet(viewsets.ModelViewSet):
    queryset = models.Papa.objects.all()
    serializer_class = serializers.PapaSerializer

    @action(detail=True)
    def kids(self, request, pk=None):
        kids = models.Kid.objects.filter(papa__id=pk)
        serializer = serializers.KidSerializer(kids, many=True)
        return Response(serializer.data)


class MamaViewSet(viewsets.ModelViewSet):
    queryset = models.Mama.objects.all()
    serializer_class = serializers.MamaSerializer

    @action(detail=True)
    def kids(self, request, pk=None):
        kids = models.Kid.objects.filter(mama__id=pk)
        serializer = serializers.KidSerializer(kids, many=True)
        return Response(serializer.data)


class KidViewSet(viewsets.ModelViewSet):
    queryset = models.Kid.objects.all()
    serializer_class = serializers.KidSerializer

    @action(detail=True, methods=['get'])
    def toys(self, request, pk=None):
        toys_lookup = models.ToyOwner.objects.filter(owner__pk=pk)
        toys_pk = [toy.id for toy in toys_lookup.all()]
        toys = models.Toy.objects.filter(pk__in=toys_pk)
        serializer = serializers.ToySerializer(toys, many=True)
        return Response(serializer.data)


class ToyViewSet(viewsets.ModelViewSet):
    queryset = models.Toy.objects.all()
    serializer_class = serializers.ToySerializer

    @action(detail=True, methods=['get'])
    def owners(self, request, pk=None):
        toys_lookup = models.ToyOwner.objects.filter(toy__pk=pk)
        owners_pk = [toy.id for toy in toys_lookup.all()]
        owners = models.Kid.objects.filter(pk__in=owners_pk)
        serializer = serializers.KidSerializer(owners, many=True)
        return Response(serializer.data)


class ToyOwnerViewSet(viewsets.ModelViewSet):
    queryset = models.ToyOwner.objects.all()
    serializer_class = serializers.ToyOwnerSerializer
