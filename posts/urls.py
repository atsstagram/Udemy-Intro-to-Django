from django.urls import path

from . import views #同じ階層を表す"."

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.index, name='index'),
]