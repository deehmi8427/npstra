from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class GroupType(models.Model):
    group_type = models.CharField(max_length=100)
    description = models.CharField(max_length=100, default='No Description')

    def __str__(self):
        return "%s" % (self.group_type)


class Occupation(models.Model):
    occupation = models.CharField(max_length=100)
    description = models.CharField(max_length=100, default='No Description')

    def __str__(self):
        return "%s" % (self.occupation)


class Rank(models.Model):
    rank = models.CharField(max_length=100)
    description =models.CharField(max_length=100, default='No Description')

    def __str__(self):
        return "%s" % (self.rank)


class GroupAffl(models.Model):
    group_name = models.CharField(max_length=100)
    group_type = models.ForeignKey(GroupType, on_delete=models.CASCADE)

    def __str__(self):
        return "%s" % (self.group_name)


class MinisterialOffice(models.Model):
    ministry = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    def __str__(self):
        return "%s, %s" % (self.ministry, self.description)


class District(models.Model):
    district = models.CharField(max_length=100)
    description = models.TextField(default='No Description')

    def __str__(self):
        return "%s " % (self.district)


class Local(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    local = models.CharField(max_length=100)
    description = models.TextField(default='No Description')

    def __str__(self):
        return "%s " % (self.local)


class LocalType(models.Model):
    local = models.CharField(max_length=100)
    description = models.TextField(default='No Description')

    def __str__(self):
        return "%s " % (self.local)


class Location(models.Model):
    local = models.ForeignKey(Local,on_delete=models.CASCADE)
    localType = models.ForeignKey(LocalType,on_delete=models.CASCADE)
    description = models.TextField(default='No Description')


class GovernanceNetwork(models.Model):
    governance_level = models.CharField(max_length=100)
    description = models.CharField(max_length=100, default='No Description')

    def __str__(self):
        return "%s, %s" % (self.governance_level,self.description)


class ElectoralDivision(models.Model):
    constituency = models.CharField(max_length=100)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    description = models.CharField(max_length=100, default='No Description')

    def __str__(self):
        return "%s, %s" % (self.constituency,self.district)


class PolitcalRelation(models.Model):
    relation = models.CharField(max_length=100)
    description = models.CharField(max_length=100, default='No Description')

    def __str__(self):
        return "%s, %s" % (self.relation, self.description)


class Individual(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dob = models.DateField()
    political_affiliation = models.ForeignKey(GroupAffl, on_delete=models.CASCADE)
    rank = models.ForeignKey(Rank, on_delete=models.CASCADE)
    occupation = models.ForeignKey(Occupation, on_delete=models.CASCADE)

    def __str__(self):
        return "%s, %s" % (self.first_name, self.last_name)


class Publication(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)


class Article(models.Model):
    headline = models.CharField(max_length=100)
    pub_date = models.DateField()
    publications = models.ManyToManyField(Publication)

    def __str__(self):
        return self.headline

    class Meta:
        ordering = ('headline',)
