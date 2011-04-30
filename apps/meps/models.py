from django.db import models

class Country(models.Model):
    code = models.CharField(max_length=2, unique=True)
    name = models.CharField(max_length=30, unique=True)

    def __unicode__(self):
        return u"%s - %s" % (self.code, self.name)

class Party(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __unicode__(self):
        return self.name

class Group(models.Model):
    abbreviation = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100, unique=True)

    def __unicode__(self):
        return u"%s - %s" % (self.abbreviation, self.name)

class Deleguation(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __unicode__(self):
        return self.name

class Committe(models.Model):
    name = models.CharField(max_length=255, unique=True)
    abbreviation = models.CharField(max_length=30, unique=True)

    def __unicode__(self):
        return u"%s: %s" % (self.abbreviation, self.name)

class Opinion(models.Model):
    title = models.CharField(max_length=255, unique=True)
    content = models.CharField(max_length=255, unique=True)
    url = models.URLField()

    def __unicode__(self):
        return self.title

class Mep(models.Model):
    key_name = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255, unique=True)
    gender = models.CharField(max_length=2, choices=((u'M', u'Male'), (u'F', u'Female')))
    picture = models.CharField(max_length=255, unique=True)
    birth_date = models.DateField()
    birth_place = models.CharField(max_length=255)
    ep_id = models.IntegerField()
    ep_opinions = models.URLField()
    ep_debates = models.URLField()
    ep_questions = models.URLField()
    ep_declarations = models.URLField()
    ep_reports = models.URLField()
    ep_motions = models.URLField()
    ep_webpage = models.URLField()
    bxl_building_name = models.CharField(max_length=255)
    bxl_building_abbreviation = models.CharField(max_length=255)
    bxl_office = models.CharField(max_length=255)
    bxl_fax = models.CharField(max_length=255)
    bxl_phone1 = models.CharField(max_length=255)
    bxl_phone2 = models.CharField(max_length=255)
    bxl_street = models.CharField(max_length=255)
    bxl_postcode = models.CharField(max_length=255)
    stg_building_name = models.CharField(max_length=255)
    stg_building_abbreviation = models.CharField(max_length=255)
    stg_office = models.CharField(max_length=255)
    stg_fax = models.CharField(max_length=255)
    stg_phone1 = models.CharField(max_length=255)
    stg_phone2 = models.CharField(max_length=255)
    stg_street = models.CharField(max_length=255)
    stg_postcode = models.CharField(max_length=255)
    party = models.ForeignKey(Party)
    group = models.ForeignKey(Group)
    group_role = models.CharField(max_length=63)
    country = models.ForeignKey(Country)
    deleguations = models.ManyToManyField(Deleguation, through='DeleguationRole')

    def __unicode__(self):
        return self.full_name

class Email(models.Model):
    email = models.EmailField()
    mep = models.ForeignKey(Mep)

class CV(models.Model):
    title = models.CharField(max_length=255)
    mep = models.ForeignKey(Mep)

class WebSite(models.Model):
    url = models.URLField()
    mep = models.ForeignKey(Mep)

    def __unicode__(self):
        return self.url

class DeleguationRole(models.Model):
    mep = models.ForeignKey(Mep)
    deleguation = models.ForeignKey(Deleguation)
    role = models.CharField(max_length=255)

class CommitteRole(models.Model):
    mep = models.ForeignKey(Mep)
    committe = models.ForeignKey(Committe)
    role = models.CharField(max_length=255)

class OpinionMep(models.Model):
    mep = models.ForeignKey(Mep)
    opinion = models.ForeignKey(Opinion)
    date = models.DateField()
