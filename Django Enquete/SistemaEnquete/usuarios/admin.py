from django.contrib import admin
from .models import Enquete
from .models import Opcao
from .models import Voto

admin.site.register(Enquete)
admin.site.register(Opcao)
admin.site.register(Voto)