# main_p/models.py

from oauth2_provider.models import AbstractApplication

class Application(AbstractApplication):
    class Meta:
        app_label = 'main_p'
