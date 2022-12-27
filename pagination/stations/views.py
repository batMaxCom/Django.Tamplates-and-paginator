from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
import csv

from pagination.settings import BUS_STATION_CSV


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    with open(BUS_STATION_CSV, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        DATA = [{'Name':row['Name'], 'Street':row['Street'], 'District':row['District']} for row in reader]

        paginator = Paginator(DATA, 10)
        page_number = int(request.GET.get('page', 1))
        page_obj = paginator.get_page(page_number)

        context = {
            'bus_stations': page_obj.object_list,
            'page': page_obj,
        }
    return render(request, 'stations/index.html', context)
