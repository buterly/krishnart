from rest_framework.response import Response
from rest_framework.decorators import api_view
from krishnart.models import Drawings
from .serializers import DrawingsSerializer
from django.http import HttpResponse

@api_view(['GET'])
def getData(request):
    range = int(request.GET['range'])
    if range < len(Drawings.objects.all()):
        try:
            drawings = Drawings.objects.all()[range:range+5]
        except:
            drawings = Drawings.objects.all()[range:]

        finally:
            serializer = DrawingsSerializer(drawings, many=True)
            print(serializer.data)
            return Response(serializer.data)

    else:
        
        return HttpResponse(status=404)

