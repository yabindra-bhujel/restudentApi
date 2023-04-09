from.models import Menu, Blog, Comment
from rest_framework import serializers

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'
    
    
    def create(self, validated_data):
        return super().create(validated_data)
    
    
    
class BlogSerialzier(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'
    
    
    def create(self, validated_data):
        return super().create(validated_data)
    


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'