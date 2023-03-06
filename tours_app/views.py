from django.http import HttpResponse, JsonResponse
from tours_app.utils import get_tour_collection, get_not_found_response
from tours_app.serializers import TourSerializer
from rest_framework import mixins, generics
from rest_framework.decorators import api_view
from .mixins import TourQuerysetMixin
from tours_app.models import Tour


# Create your views here.
class TourMixinView(TourQuerysetMixin,
                    mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    generics.GenericAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


tour_mixin_view = TourMixinView.as_view()


@api_view(['GET', 'POST'])
def tours(request):
    method = request.method
    if method == 'GET':
        tours_collection = get_tour_collection()
        results = tours_collection.find({})  # TODO pagination
        tour_serializer = TourSerializer(results, many=True)
        return JsonResponse({'data': tour_serializer.data}, safe=False)
    elif method == 'POST':
        tour_serializer = TourSerializer(data=request.data)
        if tour_serializer.is_valid(raise_exception=True):
            get_tour_collection().insert_one(tour_serializer.data)
            return JsonResponse({'data': tour_serializer.data})  # TODO deal with duplicate. e.g., name...

        return JsonResponse({"Invalid": "Invalid input"}, status=400)


@api_view(['GET', 'POST', 'DELETE'])
def tours_with_id(request, pk=None):
    method = request.method
    if method == 'GET':
        tour = get_tour(pk)
        tour_serializer = TourSerializer(tour, many=True)
        if len(tour_serializer.data) == 0:
            return get_not_found_response(f'Tour with id: {pk} not found')
        return JsonResponse({'data': tour_serializer.data}, safe=False)

    elif method == 'DELETE':
        result = get_tour_collection().delete_one({'id': pk})
        if result.deleted_count == 1:
            return HttpResponse(status=204)
        else:
            return get_not_found_response(f'Tour with id: {pk} not found')


def get_tour(pk):
    tours_collection = get_tour_collection()
    tour = tours_collection.find({'id': pk})
    return tour


def index(request):
    return HttpResponse('<em>Hello World!</em>')


def include_index(request):
    return HttpResponse('<b>Hello World!</b>')
