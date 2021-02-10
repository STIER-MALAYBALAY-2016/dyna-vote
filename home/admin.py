from django.contrib import admin
from home import models
# Register your models here.

admin.site.register(models.User)
admin.site.register(models.Position)


class CandidateAdmin(admin.ModelAdmin):
    #search_fields = ('title',)
    list_display = ('candidate','position', 'getNumVotes')
    list_filter = ('position',)
admin.site.register(models.Candidate, CandidateAdmin)

admin.site.register(models.Tally)
