from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils import timezone

from .models import Keyword, Flag
from .serializers import KeywordSerializer, FlagSerializer
from .services import run_scan


# ✅ Create Keyword
class KeywordCreateView(generics.CreateAPIView):
    queryset = Keyword.objects.all()
    serializer_class = KeywordSerializer


# ✅ Get all Flags
class FlagListView(generics.ListAPIView):
    queryset = Flag.objects.all()
    serializer_class = FlagSerializer


# ✅ Update Flag (review step)
class FlagUpdateView(generics.UpdateAPIView):
    queryset = Flag.objects.all()
    serializer_class = FlagSerializer

    def perform_update(self, serializer):
        serializer.save(reviewed_at=timezone.now())


# ✅ Run Scan (calls your logic)
class ScanView(APIView):
    def post(self, request):
        run_scan()
        return Response({"message": "Scan completed"})