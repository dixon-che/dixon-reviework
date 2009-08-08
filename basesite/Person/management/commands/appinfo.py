from django.core.management.base import AppCommand
from django.db import models

class Command(AppCommand):
    help = "Prints the models in app, and count objects for each"

    def handle_app(self, app, **options):
        app_models = models.get_models(app)
        print "Models in: " + app.__name__
        for item_model in models.get_models(app):
            print item_model._meta.object_name, item_model.objects.all().count()

