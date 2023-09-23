from django.shortcuts import render

# Create your views here.
def vision_list(request):
    return render(request, 'hallucination/vision_list.html', {})