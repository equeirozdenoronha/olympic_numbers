from rest_framework import serializers

from olympic.models import NOC, Athlete


class NOCSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        return NOC.objects.create(**validated_data)

    class Meta:
        model = NOC
        fields = ('noc', 'country_name', 'notes')


class AthleteSerializer(serializers.ModelSerializer):
    noc = serializers.SlugRelatedField(slug_field='noc', read_only=True)

    def create(self, validated_data):
        return Athlete.objects.create(**validated_data)

    class Meta:
        model = Athlete
        fields = '__all__'
