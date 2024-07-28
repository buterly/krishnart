from rest_framework.response import Response
from rest_framework.decorators import api_view
from krishnart.models import Drawings
from .serializers import DrawingsSerializer

@api_view(['GET'])
def getData(request):

    drawings = Drawings.objects.all()
    serializer = DrawingsSerializer(drawings, many=True)

    return Response(serializer.data)
