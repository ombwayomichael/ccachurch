from django.contrib import admin
from church.models import *
admin.autodiscover()
class SermonAdmin(admin.ModelAdmin):
	prepopulated_fields={'slug':('topic',)}
	list_display = ["__unicode__", "topic", "dateposted", "author"]
	list_filter = ["dateposted","author"]
	
class LeaderAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "firstname", "lastname", "picture"]
	list_filter = ["position"]
class MinistryAdmin(admin.ModelAdmin):
	prepopulated_fields={'slug':('title',)}

	
class EventAdmin(admin.ModelAdmin):
	prepopulated_fields={'slug':('title',)}
	list_display = ["__unicode__", "title", "venue", "eventDate"]
	list_filter = ["eventDate"]
	search_fiels=["eventDate"]
class SocialAdmin(admin.ModelAdmin):
	prepopulated_fields={'slug':('activity',)}
	
class NewAdmin(admin.ModelAdmin):
	prepopulated_fields={'slug':('title',)}
	
admin.site.register(SocialGallery)
admin.site.register(Event,EventAdmin)
admin.site.register(New,NewAdmin)
admin.site.register(Ministry,MinistryAdmin)
admin.site.register(MinistryCalender)
admin.site.register(Sermon,SermonAdmin)
admin.site.register(SermonComment)
admin.site.register(Resource)
admin.site.register(Service)
admin.site.register(Social,SocialAdmin)
admin.site.register(Leader,LeaderAdmin)