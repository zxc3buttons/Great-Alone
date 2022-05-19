from django.contrib import admin
from django.contrib import admin
from .models import Post
from .models import MyHokku
from .models import Tokio_authors
from .models import Project

admin.site.register(Post)
admin.site.register(MyHokku)
admin.site.register(Tokio_authors)
admin.site.register(Project)
# Register your models here.