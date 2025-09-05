from rest_framework import serializers
from .models import Feedback, Tag

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']

class FeedbackSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Feedback
        fields = ['id', 'message', 'submitted_at', 'is_resolved', 'tags']
