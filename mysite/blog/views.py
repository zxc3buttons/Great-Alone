from django.shortcuts import render
from django.utils import timezone
from .models import Project
from .parser import Pars


def main(request):
    new_obb = Pars()
    new_obb.make_good()
    tit_1 = new_obb.title_1
    tit_2 = new_obb.title_2
    tit_3 = new_obb.title_3
    tex_1 = new_obb.text_1.split('\n')
    tex_2 = new_obb.text_2.split('\n')
    tex_3 = new_obb.text_3.split('\n')
    projects = Project.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    context_dict = {'tit_1': tit_1, 'tit_2': tit_2, 'tit_3': tit_3, 'tex_1': tex_1,
                                            'tex_2': tex_2, 'tex_3': tex_3, 'projects': projects}
    return render(request, 'blog/main.html', context_dict)


def location(request):
    return render(request, 'blog/location.html', {})
# Create your views here.
