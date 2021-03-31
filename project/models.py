from django.db.models import *

class Photographs(Model):
    name = CharField(max_length=80)
    surname = CharField(max_length=80)
    img = ImageField(upload_to='images/', null= True, blank=True)
    text = TextField(default= ' ')
    created_at = DateTimeField('creation timestamp', auto_now_add=True)

    def __str__(self):
        return str(self.name)
