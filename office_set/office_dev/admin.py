from django.contrib import admin

# Register your models here.
# Register your models here.
from django.contrib import admin
from .models import InputJournal,Signature
# Register your models here.
#from import_export.admin import ImportExportModelAdmin


class RegisterJournal(admin.ModelAdmin):
    list_display = ['signature', 'numberInput', 'dateReg','correspondent','content','executor','mark','nomenklatura']

class RegisterSignature(admin.ModelAdmin):
    list_display = [ 'numberInput', 'user','nomenklatura']

admin.site.register(InputJournal,RegisterJournal)
admin.site.register(Signature,RegisterSignature)
