from django.shortcuts import render
from rest_framework import viewsets
from .models import Feedback
from .serializers import FeedbackSerializer

class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all().order_by('-submitted_at')
    serializer_class = FeedbackSerializer

