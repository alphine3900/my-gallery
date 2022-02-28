from django.shortcuts import render
from .models import  Location,Image,Category
# Create your views here.

def index(request):
    locations=Location.objects.all
    results=Image.objects.all()
    print(results)
    return render(request,'app2/index.html',{"results":results,"locations":locations})

def search_results(request):
    locations=Location.objects.all


    if 'search_term' in request.GET and request.GET["search_term"]:
        search_term = request.GET.get("search_term")
        searched_articles = Image.filter_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'app2/search.html',{"message":message,"results": searched_articles,"locations":locations})

    else:
        message = "You haven't searched for any term"
        return render(request, 'app2/search.html',{"message":message})

def searchLocation(request,term):
    locations=Location.objects.all

    results=Image.filter_by_location(term)

    return render(request,'app2/loc.html',{"results":results,"locations":locations})



