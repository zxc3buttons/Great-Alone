from django.shortcuts import render


def main(request):
    return render(request, 'blog/main.html', {})
# Create your views here.
