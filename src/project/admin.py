from django.contrib import admin
from project.models import Project, Sample, Seq

# Register your models here.

#custome admin interface
class ProjectAdmin(admin.ModelAdmin):
	list_display = ('name','desc','date_created', 'data_updated', 'owner')
	search_fields = ('name','owner',)
	readonly_fields=('date_created', 'data_updated')

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()

admin.site.register(Project)
admin.site.register(Sample)
admin.site.register(Seq)