from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MenuItemSerializer
from .models import Menu, MenuItem
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import api_view, permission_classes
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser


@api_view(['GET', 'POST'])
def menuapi(request, format=None):

    if request.method == 'GET':
        menu_items = MenuItem.objects.all()
        serializer = MenuItemSerializer(menu_items, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MenuItemSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def menuitem(request, id, format=None):

    try:
        menu_item = MenuItem.objects.get(pk=id)
    except MenuItem.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = MenuItemSerializer(menu_item)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = MenuItemSerializer(menu_item, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        menu_item.delete()
        return HttpResponse(status=204)







""" 
@api_view(["POST"])
def add_item(request):
    payload = json.loads(request.body)
    try:
        MenuItem = Menu.objects.get(id=pk)
        new = Menu.objects.create(
            Food_Code=payload["Food_Code"],

            )
        new.save()
        serializer = MenuSerializer(Menu)
        return JsonResponse({'Menu': serializer.data}, safe=False, status=status.HTTP_201_CREATED)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["PATCH"])
def update_item(request):
    payload = json.loads(request.body)
    try:

        MenuItem = Menu.objects.get(id=pk)
        new = Menu.objects.create(
            Food_Code=payload["title"],

            )
        new.save()
        serializer = MenuSerializer(Menu)
        return JsonResponse({'Menu': serializer.data}, safe=False, status=status.HTTP_201_CREATED)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        """