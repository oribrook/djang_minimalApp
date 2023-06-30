from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Article, Site
from .serializers import serialize_article, SiteSerializer
from .serializers import ArticleModelSerializer as ArticleSerializer
from rest_framework import status


@api_view(['GET', 'POST', 'PUT'])
def test_drf(request):
        
    artic = Article.objects.all()    
    res = serialize_article(artic)    
    return Response(res.data)        


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
        

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def serve_site(request):
    try:
        if request.method == 'GET':
            id_ = request.query_params.get("id", False)
            if id_:                
                site = Site.objects.get(pk=id_)
                res = SiteSerializer(instance=site)
                return Response(res.data)
            else:
                sites = Site.objects.all()
                res = SiteSerializer(instance=sites, many=True)
                return Response(res.data)
            
        if request.method == 'POST':                        
            site_ser = SiteSerializer(data=request.data)
            if site_ser.is_valid():
                site_ser.save()
                return Response({'status': 'ok', 'info': 'site added'}, 
                                status=status.HTTP_201_CREATED)
            else:
                return Response({'status': 'error', 'info': site_ser.errors}, 
                                status=status.HTTP_400_BAD_REQUEST)
        
        if request.method == 'PUT':
            id_ = request.query_params.get("id", False)
            if not id_:                
                return Response({'status': 'error', 'info': "ID is missing"}, 400)
            site = Site.objects.get(pk=id_)
            site_ser = SiteSerializer(instance=site, data=request.data, partial=True)
            if site_ser.is_valid():
                site_ser.save()
                return Response({'status': 'ok', 'info': 'site updated'}, 
                                status=200)
            else:
                return Response({'status': 'error', 'info': site_ser.errors}, 
                                status=status.HTTP_400_BAD_REQUEST)
        
        if request.method == 'DELETE':
            id_ = request.query_params.get("id", False)
            if not id_:                
                return Response({'status': 'error', 'info': "ID is missing"}, 400)
            site = Site.objects.get(pk=id_)
            site.delete()            
            return Response({'status': 'ok', 'info': 'site deleted'}, 
                                status=200)


    except Exception as e:
        # todo: send email bal balba
        return Response({'status': 'error', 'info': str(e)}, 
                        status.HTTP_500_INTERNAL_SERVER_ERROR)
