from rest_framework import serializers
from .models import CustomUser, Tournament, Team, Fixture

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True},
                        'username': {'required': False},}

class TournamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tournament
        fields = '__all__'

class TeamSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model = Team
        fields = ['id', 'name', 'members', 'contact_email', 'user']

    def __init__(self, instance=None, data=None, **kwargs):
        context = kwargs.get('context')
        self.request = context.get('request') if context else None
        super().__init__(instance, data, **kwargs)

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        validated_data.pop('user', None)  
        return super().update(instance, validated_data)


class FixtureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fixture
        fields = '__all__'

    def create(self, validated_data):
        teams_data = validated_data.pop('teams')
        fixture = Fixture.objects.create(**validated_data)
        fixture.teams.set(teams_data)
        return fixture