from django.shortcuts import render


def ping(request):
    return render(request, 'ping.html')
