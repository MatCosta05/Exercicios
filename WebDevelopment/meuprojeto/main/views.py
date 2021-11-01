from django.shortcuts import render
from .models import ProjFilm


# Create your views here.
def homepage(request):
    return render(
        request=request,
        template_name="home.html",
        context={"filmes": ProjFilm.objects.all}
    )
