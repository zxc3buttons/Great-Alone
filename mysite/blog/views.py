from django.shortcuts import render


def main(request):
    return render(request, 'blog/main.html', {})
def location(request):
    return render(request, 'blog/location.html', {})
# Create your views here.
