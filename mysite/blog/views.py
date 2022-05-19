from django.shortcuts import render
import random
from .models import MyHokku
from .models import Tokio_authors

from django.utils import timezone
from .models import Project


def main(request):
    this_hokkus = MyHokku.objects.all()
    this_names = Tokio_authors.objects.all()
    three_names = [random.randint(0, 201) for i in range(3)]
    three_hokkus = [random.randint(0, 539) for i in range(3)]
    tit_1 = this_names[three_names[0]]
    tit_2 = this_names[three_names[1]]
    tit_3 = this_names[three_names[2]]
    tex_1 = this_hokkus[three_hokkus[0]].text.split('\n')
    tex_2 = this_hokkus[three_hokkus[1]].text.split('\n')
    tex_3 = this_hokkus[three_hokkus[2]].text.split('\n')
    projects = Project.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    context_dict = {'tit_1': tit_1, 'tit_2': tit_2, 'tit_3': tit_3, 'tex_1': tex_1,
                    'tex_2': tex_2, 'tex_3': tex_3, 'projects': projects}
    return render(request, 'blog/main.html', context_dict)

def location(request):
    return render(request, 'blog/location.html', {})
# Create your views here.
