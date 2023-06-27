from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Article
from .serializers import serialize_article, ArticleSerializer



@api_view(['GET', 'POST', 'PUT'])
def test_drf(request):
    # print(request.data)
    artic = Article.objects.first()
    res = serialize_article(artic)
    return Response(res)


@api_view(['GET', 'POST', 'PUT'])
def serve_article(request):
        
    if request.method == 'GET':
        id_ = request.query_params.get("id", False)
        if not id_:
            artics = Article.objects.all()
            res = ArticleSerializer(artics, many=True)
        else:
            artic = Article.objects.get(pk=id_)
            res = ArticleSerializer(instance=artic)

        return Response(res.data)
    
    if request.method == 'POST':
        artic_ser = ArticleSerializer(data=request.data)

        if artic_ser.is_valid():
            new_artic = artic_ser.save()
            return Response({'info': "Article added successfully",
                             'id': new_artic.id})
        else:
            return Response({'error': artic_ser.errors})
    
    if request.method == 'PUT':
        id_ = request.query_params.get("id", False)

        if not id_ :
            return Response({'error': 'you must specify id'})

        artic = Article.objects.get(pk=id_)
        artic_ser = ArticleSerializer(instance=artic, data=request.data)
        if artic_ser.is_valid():
            artic_ser.save()
            return Response({'info': "Article updated successfully"})
        else:
            return Response({'error': artic_ser.errors})