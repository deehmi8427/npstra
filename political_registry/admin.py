from django.contrib import admin
from .models import MinisterialOffice, GroupAffl, GroupType, District, Local, \
    LocalType, Location, PolitcalRelation, ElectoralDivision, GovernanceNetwork, \
    Individual, Rank, Occupation, Publication, Article


# Register your models here.


class MinistryAdmin(admin.ModelAdmin):
    list_display = ('ministry', 'description')


class GroupAfflAdmin(admin.ModelAdmin):
    list_display = ('group_name', 'group_type')


class GroupTypeAdmin(admin.ModelAdmin):
    list_display = ('group_type', 'description')


class DistrictAdmin(admin.ModelAdmin):
    list_display = ('district', 'description')


class LocalAdmin(admin.ModelAdmin):
    list_display = ('local', 'district', 'description')


class LocalTypeAdmin(admin.ModelAdmin):
    list_display = ('local', 'description')


class LocationAdmin(admin.ModelAdmin):
    list_display = ('local', 'localType', 'description')


class ElectoralDivisionAdmin(admin.ModelAdmin):
    list_display = ('constituency', 'district')


class PolitcalRelationAdmin(admin.ModelAdmin):
    list_display = ('relation', 'description')


class GovernanceNetworkAdmin(admin.ModelAdmin):
    list_display = ('governance_level', 'description')


class IndividualAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'political_affiliation')


class RankAdmin(admin.ModelAdmin):
    list_display = ('rank', 'description',)


class OccupationAdmin(admin.ModelAdmin):
    list_display = ('occupation', 'description')


class PubAdmin(admin.ModelAdmin):
    list_display = ('title',)


admin.site.register(MinisterialOffice, MinistryAdmin)
admin.site.register(GroupAffl, GroupAfflAdmin)
admin.site.register(GroupType, GroupTypeAdmin)
admin.site.register(District, DistrictAdmin)
admin.site.register(Local, LocalAdmin)
admin.site.register(LocalType, LocalTypeAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(GovernanceNetwork, GovernanceNetworkAdmin)
admin.site.register(PolitcalRelation, PolitcalRelationAdmin)
admin.site.register(ElectoralDivision, ElectoralDivisionAdmin)
admin.site.register(Individual, IndividualAdmin)
admin.site.register(Rank, RankAdmin)
admin.site.register(Occupation, OccupationAdmin)
admin.site.register(Publication, PubAdmin)
admin.site.register(Article)

