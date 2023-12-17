from rest_framework import serializers
from rest_framework.generics import get_object_or_404

from catalog.models import Category


class CreateCategoryNodeSerializer(serializers.ModelSerializer):
    parent = serializers.IntegerField(required=False)

    class Meta:
        model = Category
        fields = ('id', 'title', 'description', 'is_public', 'slug', 'parent')

    def create(self, validated_data):
        parent = validated_data.pop('parent', None)
        if parent is None:
            instance = Category.add_root(**validated_data)
        else:
            parent_node = get_object_or_404(Category, pk=parent)
            instance = parent_node.add_child(**validated_data)
        return instance


class CategoryTreeSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()

    def get_children(self, obj):
        return CategoryTreeSerializer(obj.get_children(), many=True).data

    class Meta:
        model = Category
        fields = ('id', 'title', 'description', 'is_public', 'slug', 'parent')
