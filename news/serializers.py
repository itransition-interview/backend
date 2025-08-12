from rest_framework import serializers
from news.models import News


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ["uuid", "title", "content", "image", "created_at", "updated_at"]
        read_only_fields = ['uuid', 'created_at', 'updated_at']