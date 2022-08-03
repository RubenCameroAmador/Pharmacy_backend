from rest_framework import status, views
from rest_framework.response import Response
from farmaciaApp.serializers.productSerializer import ProductSerializer


class ProductCreateView(views.APIView):
    def post(self,request, *args,**kwargs):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response ({'detail':'Producto guardado!!'}, status = status.HTTP_201_CREATED)
    
