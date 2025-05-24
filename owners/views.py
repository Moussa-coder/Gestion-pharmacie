from rest_framework import viewsets
from .models import Owner
from .serializers import OwnerSerializer
# Create your views here.
class OwnerViewSet(viewsets.ModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer