from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *

# Register your models here.
class TrainerAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['name', 'id', 'address', 'education', 'organization']
admin.site.register(Trainer, TrainerAdmin)  


       
    
class EventsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display= ['time','date','title','description','image','Location',]
    
admin.site.register(Events, EventsAdmin) 
        
        
     

class AttendesAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['name', 'id', 'college', 'education', 'address','training_location','phone','email','interest','basic_skill','date','time',]

admin.site.register(Attendes, AttendesAdmin)          
        


class RegistrationAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['name', 'id', 'college', 'education', 'district','training_location','age','phone','email','interest','basic_skill','date','time',]
   
        
        
admin.site.register(Registration, RegistrationAdmin)  

