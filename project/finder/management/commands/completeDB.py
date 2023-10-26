import random as rd

from django.core.management.base import BaseCommand

from finder import models
from finder.finder_services import Filters


def complete_db() -> None:
    """
    Fills the items with a value of None in the database: HousePlants,
    the random value of the possible values from the dictionary dict_filter.
    """
    dict_filters = Filters()
    list_update = []
    for item in models.HousePlants.objects.all():
        flag = False
        for key in dict_filters.converts_dictionary().keys():
            attribute = getattr(item, key)
            if attribute is None:
                flag = True
                setattr(item, key, rd.choice(dict_filters.converts_dictionary()[key]))
        if flag:
            list_update.append(item)
    models.HousePlants.objects.bulk_update(list_update, [*dict_filters.converts_dictionary().keys()])


class Command(BaseCommand):
    def handle(self, *args, **options):
        # complete_db()
