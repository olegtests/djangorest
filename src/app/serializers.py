from rest_framework import serializers

from src.app.models import Post, Reaction


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class ReactionSerializer(serializers.HyperlinkedModelSerializer):
    def create(self, validated_data):
        reaction_name = validated_data.pop('reaction')
        reaction = Reaction.objects.get_or_create(**validated_data)
        reaction.reaction = reaction_name
        return reaction

    class Meta:
        model = Reaction
        fields = 'reaction'
