from django.shortcuts import render

# Create your views here.


def test_helloworld(request):
    titles = ["S.No", "Name", "Age", "Role"]
    people = [
        {"name": "Zlaam", "role": "FullstackDev", "age": 23},
        {"name": "Siraj", "role": "Frontend-Devloper", "age": 20},
        {"name": "Khan", "role": "Backend-Developer", "age": 21},
    ]
    return render(request, "index.html", context={"peoples": people, "titles": titles})
