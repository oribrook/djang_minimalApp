from rest_framework import serializers
from .models import Article, Site

# just example
def serialize_article(artic):

    return {
        'title': artic.title,
        'content': artic.content,
    }


class ArticleSerializer(serializers.Serializer):

    title = serializers.CharField(max_length=20)
    content = serializers.CharField()
    published = serializers.DateField(required=False)    

    def create(self, validated_data):        
        # title = validated_data.get('title')
        # content = validated_data.get('content')
        # published = validated_data.get('published')
        
        # return Article.objects.create(title=title, 
        #                        content=content,
        #                        published=published)
    
        return Article.objects.create(**validated_data)                
    
    
    def update(self, instance, validated_data):
        
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.published = validated_data.get('published', instance.published)
        instance.save()
        return instance


class ArticleMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ("title",)


class SiteSerializer(serializers.ModelSerializer):
    
    article_set = ArticleMiniSerializer(many=True)

    class Meta:
        model = Site
        fields = "__all__"                


class SiteMiniSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Site        
        fields = ("name",)
        

class ArticleModelSerializer(serializers.ModelSerializer):
    
    # site_id = serializers.IntegerField()
    # site = SiteMiniSerializer(read_only=True)

    class Meta:
        model = Article
        fields = "__all__"
   
        