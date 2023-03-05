from django.http import HttpResponse, JsonResponse
from tours_app.utils import get_db
from tours_app.serializers import TourSerializer


# Create your views here.

def index(request):
    db = get_db()
    tours_collection = db.tours
    results = tours_collection.find({})
    tour_serializer = TourSerializer(results, many=True)
    return JsonResponse(tour_serializer.data, safe=False)


def app_two(request):
    return HttpResponse('<em>Hello World!</em>')


def include_index(request):
    return HttpResponse('<b>Hello World!</b>')
