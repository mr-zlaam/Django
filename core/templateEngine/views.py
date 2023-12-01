from django.shortcuts import render

# Create your views here.


def test_helloworld(request):
    return render(request, "index.html")
