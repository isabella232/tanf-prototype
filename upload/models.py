from django.db import models
from datetime import date
import math


# Create your models here.

# https://www.acf.hhs.gov/sites/default/files/ofa/tanf_data_report_section1_10_2008.pdf
class Family(models.Model):
    # metadata
    imported_at = models.DateTimeField('time record was imported (metadata)')
    imported_by = models.CharField('who record was imported by (metadata)', max_length=64)

    # header data
    calendar_quarter = models.IntegerField('calendar quarter (header)')
    state_code = models.CharField('state fips code (header)', max_length=3)
    tribe_code = models.CharField('tribe code (header)', max_length=3)

    # record data
    recordtype = models.CharField('record type (T1)', max_length=2)
    reportingmonth = models.CharField('reporting month (item 4)', max_length=6)
    casenumber = models.CharField('case number (item 6)', max_length=11)
    countyfipscode = models.IntegerField('county fips code (item 2)')
    stratum = models.IntegerField('stratum (item 5)')
    zipcode = models.CharField('zipcode (item 7)', max_length=5)
    fundingstream = models.IntegerField('funding stream (item 8)')
    disposition = models.IntegerField('disposition (item 9)')
    newapplicant = models.IntegerField('new applicant (item 10)')
    numfamilymembers = models.IntegerField('number family members (item 11)')
    typeoffamilyforworkparticipation = models.IntegerField('type of family for work participation (item 12)')
    receivessubsidizedhousing = models.CharField('receives subsidized housing (item 13)', max_length=1)
    receivesmedicalassistance = models.CharField('receives medical assistance (item 14)', max_length=1)
    receivesfoodstamps = models.CharField('receives food stamps (item 15)', max_length=1)
    amtoffoodstampassistance = models.IntegerField('amount of food stamp assistance (item 16)')
    receivessubsidizedchildcare = models.CharField('receives food stamps (item 17)', max_length=1)
    amtofsubsidizedchildcare = models.IntegerField('amount of subsidized child care (item 18)')
    amtofchildsupport = models.IntegerField('amount of child support (item 19)')
    amtoffamilycashresources = models.IntegerField('amount of familys cash resources (item 20)')
    cash_amount = models.IntegerField('cash and cash equivalents amount (item 21a)')
    cash_nbr_month = models.IntegerField('cash and cash equivalents number of months (item 21b)')
    tanfchildcare_amount = models.IntegerField('TANF child care amount (item 22a)')
    tanfchildcare_children_covered = models.IntegerField('TANF child care children covered (item 22b)')
    tanfchildcare_nbr_months = models.IntegerField('TANF child care number of months (item 22c)')
    transportation_amount = models.IntegerField('transportation amount (item 23a)')
    transportation_nbr_months = models.IntegerField('transportation number of months (item 23b)')
    transitionalservices_amount = models.IntegerField('transitional services amount (item 24a')
    transitionalservices_nbr_months = models.IntegerField('transitional services number of months (item 24b)')
    other_amount = models.IntegerField('other amount (item 25a')
    other_nbr_months = models.IntegerField('other number of months (item 25b)')
    sanctionsreduction_amt = models.IntegerField('reason for and amount of assistance reduction: sanctions reduction_amount (item 26a)')
    workrequirementssanction = models.CharField('reason for and amount of assistance reduction: work requirements sanction (item 26a)', max_length=4)
    familysanctionforadultnohsdiploma = models.CharField('reason for and amount of assistance reduction: family sanction for adult, no high school diploma (item 26a)', max_length=1)
    sanctionforteenparentnotattendingschool = models.CharField('reason for and amount of assistance reduction: sanction for teen parent not attending school (item 26a)', max_length=1)
    noncooperatewithchildsupport = models.CharField('reason for and amount of assistance reduction: non-cooperation with child support (item 26a)', max_length=1)
    failuretocomploywithirp = models.CharField('reason for and amount of assistance reduction: failure to comply with individual responsibility plan (item 26a)', max_length=1)
    othersanction = models.CharField('reason for and amount of assistance reduction: other sanction (item 26a)', max_length=1)
    recoupmentofprioroverpayment = models.CharField('reason for and amount of assistance reduction: recourpment of prior overpayment (item 26b)', max_length=4)
    othertotalreductionamt = models.CharField('reason for and amount of assistance reduction: other total reduction amount (item 26c)', max_length=4)
    familycap = models.CharField('reason for and amount of assistance reduction: family cap (item 26c)', max_length=1)
    reductionbasedonlengthofreceiptofassistance = models.CharField('reason for and amount of assistance reduction: reduction based on length of receipt of assistance (item 26c)', max_length=1)
    othernonsanction = models.CharField('reason for and amount of assistance reduction: other, non-sanction (item 26c)', max_length=1)
    waiver_evaluation_control_gprs = models.CharField('waiver_evaluation_control_gprs (item 27)', max_length=1)
    tanffamilyexemptfromtimelimits = models.IntegerField('TANF family exempt from time_limits (item 28)')
    tanffamilynewchildonlyfamily = models.IntegerField('TANF family new child only family (item 29)')


# https://www.acf.hhs.gov/sites/default/files/ofa/tanf_data_report_section1_10_2008.pdf
class Adult(models.Model):
    # metadata
    imported_at = models.DateTimeField('time record was imported (metadata)')
    imported_by = models.CharField('who record was imported by (metadata)', max_length=64)

    # header data
    calendar_quarter = models.IntegerField('calendar quarter (header)')
    state_code = models.CharField('state fips code (header)', max_length=3)
    tribe_code = models.CharField('tribe code (header)', max_length=3)

    # record data
    recordtype = models.CharField('record type (T2)', max_length=2)
    reportingmonth = models.CharField('reporting month (item 4)', max_length=6)
    casenumber = models.CharField('case number (item 6)', max_length=11)
    familyafilliation = models.IntegerField('family affiliation (item 30)')
    noncustodialparent = models.IntegerField('noncustodial parent (item 31)')
    dateofbirth = models.DateField('date of birth (item 32)')
    socialsecuritynumber = models.CharField('social security number (item 33)', max_length=9)
    racehispanic = models.CharField('race/ethnicity: hispanic or latino (item 34a)', max_length=1)
    racenativeamerican = models.CharField('race/ethnicity: american indian or alaska native (item 34b)', max_length=1)
    # XXX many more fields need to be added here


# https://www.acf.hhs.gov/sites/default/files/ofa/tanf_data_report_section1_10_2008.pdf
class Child(models.Model):
    # metadata
    imported_at = models.DateTimeField('time record was imported (metadata)')
    imported_by = models.CharField('who record was imported by (metadata)', max_length=64)

    # header data
    calendar_quarter = models.IntegerField('calendar quarter (header)')
    state_code = models.CharField('state fips code (header)', max_length=3)
    tribe_code = models.CharField('tribe code (header)', max_length=3)

    # record data
    recordtype = models.CharField('record type (T3)', max_length=2)
    reportingmonth = models.CharField('reporting month (item 4)', max_length=6)
    casenumber = models.CharField('case number (item 6)', max_length=11)
    familyafilliation = models.IntegerField('family affiliation (item 67)')
    dateofbirth = models.DateField('date of birth (item 68)')
    socialsecuritynumber = models.CharField('social security number (item 69)', max_length=9)
    racehispanic = models.CharField('race/ethnicity: hispanic or latino (item 70a)', max_length=1)
    racenativeamerican = models.CharField('race/ethnicity: american indian or alaska native (item 70b)', max_length=1)
    # XXX many more fields need to be added here


# https://www.acf.hhs.gov/sites/default/files/ofa/tanf_data_report_section2.pdf
class ClosedCase(models.Model):
    # metadata
    imported_at = models.DateTimeField('time record was imported (metadata)')
    imported_by = models.CharField('who record was imported by (metadata)', max_length=64)

    # header data
    calendar_quarter = models.IntegerField('calendar quarter (header)')
    state_code = models.CharField('state fips code (header)', max_length=3)
    tribe_code = models.CharField('tribe code (header)', max_length=3)

    # record data
    recordtype = models.CharField('record type (T4)', max_length=2)
    reportingmonth = models.CharField('reporting month (item 4)', max_length=6)
    casenumber = models.CharField('case number (item 6)', max_length=11)
    countyfipscode = models.IntegerField('county fips code (item 2)')
    stratum = models.IntegerField('stratum (item 5)')
    zipcode = models.CharField('zipcode (item 7)', max_length=5)
    disposition = models.IntegerField('disposition (item 8)')
    closurereason = models.IntegerField('reason for closure (item 9)')
    receivessubsidizedhousing = models.CharField('receives subsidized housing (item 10)', max_length=1)
    receivesmedicalassistance = models.CharField('receives medical assistance (item 11)', max_length=1)
    receivesfoodstamps = models.CharField('receives food stamps (item 12)', max_length=1)
    receivessubsidizedchildcare = models.CharField('receives subsidized child care (item 13)', max_length=1)


# https://www.acf.hhs.gov/sites/default/files/ofa/tanf_data_report_section2.pdf
class ClosedPerson(models.Model):
    # metadata
    imported_at = models.DateTimeField('time record was imported (metadata)')
    imported_by = models.CharField('who record was imported by (metadata)', max_length=64)

    # header data
    calendar_quarter = models.IntegerField('calendar quarter (header)')
    state_code = models.CharField('state fips code (header)', max_length=3)
    tribe_code = models.CharField('tribe code (header)', max_length=3)

    # record data
    recordtype = models.CharField('record type (T5)', max_length=2)
    reportingmonth = models.CharField('reporting month (item 4)', max_length=6)
    casenumber = models.CharField('case number (item 6)', max_length=11)
    familyafilliation = models.IntegerField('family affiliation (item 14)')
    dateofbirth = models.DateField('date of birth (item 15)')
    socialsecuritynumber = models.CharField('social security number (item 16)', max_length=9)
    racehispanic = models.CharField('race/ethnicity: hispanic or latino (item 17a)', max_length=1)
    racenativeamerican = models.CharField('race/ethnicity: american indian or alaska native (item 17b)', max_length=1)
    raceasian = models.CharField('race/ethnicity: asian (item 17c)', max_length=1)
    raceblack = models.CharField('race/ethnicity: black or african american (item 17d)', max_length=1)
    racepacific = models.CharField('race/ethnicity: native hawaiian or other pacific islander (item 17e)', max_length=1)
    racewhite = models.CharField('race/ethnicity: white (item 17f)', max_length=1)
    gender = models.IntegerField('gender (item 18)')
    oasdibenefits = models.CharField('receives disability benefits: received federal disability insurance benefits under the oasdi program (item 19a)', max_length=1)
    nonssabenefits = models.CharField('receives disability benefits: receives benefits based on federal disability status under non-ssa programs (item 19b)', max_length=1)
    titlexivapdtbenefits = models.CharField('receives disability benefits: received aid to the permanently and totally disabled under title xiv-apdt (item 19c)', max_length=1)
    titlexviaabdbenefits = models.CharField('receives disability benefits: received aid to the aged, blind, and disabled under title xvi-aabd (item 19d)', max_length=1)
    titlexvissibenefits = models.CharField('receives disability benefits: received ssi under title xvi-ssi (item 19e)', max_length=1)
    maritalstatus = models.CharField('marital status (item 20)', max_length=1)
    relationshiptohh = models.IntegerField('relationship to head of household (item 21)')
    parentminorchild = models.CharField('parent with minor child in the family (item 22)', max_length=1)
    pregnantneeds = models.CharField('needs of a pregnant woman (item 23)', max_length=11)
    educationlevel = models.CharField('education level (item 24)', max_length=12)
    citizenship = models.CharField('citizenship/alienage (item 25)', max_length=1)
    countablemonths = models.IntegerField('number of countable months toward federal time limit (item 26)')
    countablemonthsremaining = models.IntegerField('number of countable months remaining under state/tribe limit (item 27)')
    employmentstatus = models.CharField('employment status (item 28)', max_length=1)
    earnedincome = models.IntegerField('amount of earned income (item 29)')
    unearnedincome = models.IntegerField('amount of unearned income (item 30)')


# https://www.acf.hhs.gov/sites/default/files/ofa/tanf_data_report_section3.pdf
class AggregatedData(models.Model):
    # metadata
    imported_at = models.DateTimeField('time record was imported (metadata)')
    imported_by = models.CharField('who record was imported by (metadata)', max_length=64)

    # header data
    calendar_quarter = models.IntegerField('calendar quarter (header)')
    state_code = models.CharField('state fips code (header)', max_length=3)
    tribe_code = models.CharField('tribe code (header)', max_length=3)

    # record data
    recordtype = models.CharField('record type (T6)', max_length=2)
    calendaryear = models.IntegerField('calendar year (item 3)')
    calendarquarter = models.IntegerField('calendar quarter (item 3)')
    firstmonthapps = models.IntegerField('total number of applicants: first month (item 4)')
    secondmonthapps = models.IntegerField('total number of applicants: second month (item 4)')
    thirdmonthapps = models.IntegerField('total number of applicants: third month (item 4)')
    firstmonthapprovals = models.IntegerField('total number of approved applications: first month (item 5)')
    secondmonthapprovals = models.IntegerField('total number of approved applications: second month (item 5)')
    thirdmonthapprovals = models.IntegerField('total number of approved applications: third month (item 5)')
    firstmonthdenied = models.IntegerField('total number of denied applications: first month (item 6)')
    secondmonthdenied = models.IntegerField('total number of denied applications: second month (item 6)')
    thirdmonthdenied = models.IntegerField('total number of denied applications: third month (item 6)')
    # XXX many more fields need to be added here


# https://www.acf.hhs.gov/sites/default/files/ofa/tanf_data_report_section4.pdf
class FamiliesByStratumData(models.Model):
    # metadata
    imported_at = models.DateTimeField('time record was imported (metadata)')
    imported_by = models.CharField('who record was imported by (metadata)', max_length=64)

    # header data
    calendar_quarter = models.IntegerField('calendar quarter (header)')
    state_code = models.CharField('state fips code (header)', max_length=3)
    tribe_code = models.CharField('tribe code (header)', max_length=3)

    # record data
    recordtype = models.CharField('record type (T7)', max_length=2)
    calendaryear = models.IntegerField('calendar year (item 3)')
    calendarquarter = models.IntegerField('calendar quarter (item 3)')
    # XXX many more fields need to be added here
