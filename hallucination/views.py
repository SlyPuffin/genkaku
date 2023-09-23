from django.shortcuts import render
from django.utils import timezone
from .models import Vision

# Create your views here.
def vision_list(request):
    visions = Vision.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'hallucination/vision_list.html', {'visions': visions})