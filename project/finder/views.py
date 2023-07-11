from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpRequest

from .models import HousePlants
from .forms import CheckBoxForm
from finder import finder_services as fs


def displays_plants_by_filters(request: HttpRequest) -> HttpResponse:
    """
       Displays plants by filters
       :param request: http request
       :return: HTML page with plants by filters
       """
    form = CheckBoxForm(request.POST or None)
    page_number = request.GET.get("page")
    if request.method == "GET":
        page_obj = fs.generates_page_by_filters(page_number, fs.creates_default_filters_for_start_page())
    if request.method == "POST":
        if form.is_valid():
            page_obj = fs.generates_page_by_filters(page_number, fs.changing_value_of_filters(request))

    return render(request, 'finder/filtration_of_plants.html', {'form': form, 'page_obj': page_obj})


def displays_description_of_specific_plant(request: HttpRequest, pk: int) -> HttpResponse:
    """
       displays description of specific plant
       :param request: http request
       :param pk: id in model
       :return: HTML page with description of specific plant
       """
    plant = get_object_or_404(HousePlants, pk=pk)
    return render(request, 'finder/description_plant.html', {'plant': plant})
