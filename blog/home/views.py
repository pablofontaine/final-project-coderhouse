from django.shortcuts import render

# Create your views here.


def index(request):
    return render(
        request=request,
        context=dict(),
        template_name="home/index.html",
    )
