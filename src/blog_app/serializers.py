
from rest_framework import serializers
from .models import Post, Comment, Like, View



class CommentSerializer(serializers.ModelSerializer):
    user = serializers.CharField( source="user.username", read_only=True)
    
    class Meta:
        model = Comment
        fields = ( "content",  "user", "time") 
         
class PostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields=(
            'id',
            'title',
            'image',
            'publish_date',
            'update_date',
            'content',
            'author',
            'comment_count',
            'view_count',
            'like_count',
        )
        
         
class PostDetailSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many= True)
    class Meta:
        model = Post
        fields=(
            'id',
            'title',
            'image',
            'publish_date',
            'update_date',
            'content',
            'author',
            'comment_count',
            'view_count',
            'like_count',
            'comments'
        )
        
class CommentCreateSerializer(serializers.ModelSerializer):
    content = serializers.CharField()
    # author = serializers.CharField( source="author.username", read_only=True)
    class Meta:
        model = Comment
        fields = ( "content",)
        
class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = (
           'user',
           'post' 
        )
        
class PostViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = View
        fields = ("user", "post", "time")
    
  
             
        

