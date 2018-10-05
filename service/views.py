from django.shortcuts import render

# Create your views here.


def yniScore(request):
    return render(request, 'service/yniScore.html')


def yniCompare(request):
    return render(request, 'service/yniCompare.html')


def yniAverage(request):
    return render(request, 'service/yniAverage.html')