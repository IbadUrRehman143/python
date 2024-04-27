from django.db.models import Model, CharField

# Create your models here.
class MyDb(Model):
    name = CharField(max_length=120)