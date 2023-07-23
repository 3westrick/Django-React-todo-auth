from rest_framework import serializers
from .models import Todo


class UserInlineSerializer(serializers.Serializer):
    username = serializers.CharField(read_only=True)


class TodoSerializer(serializers.ModelSerializer):
    owner = UserInlineSerializer(source="user", read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookup_field='pk',
    )

    class Meta:
        model = Todo
        fields = ['id', 'title', 'created', 'updated', 'done', 'owner', 'url']
