# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.conf import settings


class BgAudit(models.Model):
    auditid = models.BigAutoField(db_column='AuditId', primary_key=True)  # Field name made lowercase.
    bgid = models.BigIntegerField(db_column='BGId')  # Field name made lowercase.
    businessterm = models.CharField(db_column='BusinessTerm', max_length=30)  # Field name made lowercase.
    definition = models.CharField(db_column='Definition', max_length=100)  # Field name made lowercase.
    dataattribute = models.CharField(db_column='DataAttribute', max_length=30)  # Field name made lowercase.
    system = models.CharField(db_column='System', max_length=30)  # Field name made lowercase.
    dataclassification = models.CharField(db_column='DataClassification', max_length=30)  # Field name made lowercase.
    datadomain = models.CharField(db_column='DataDomain', max_length=30)  # Field name made lowercase.
    lineofbusiness = models.CharField(db_column='LineOfBusiness', max_length=30)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=30)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=30)  # Field name made lowercase.
    create_timestamp = models.DateTimeField(db_column='Create_Timestamp')  # Field name made lowercase.
    update_timestamp = models.DateTimeField(db_column='Update_Timestamp')  # Field name made lowercase.
    auditaction = models.CharField(db_column='AuditAction', max_length=1)  # Field name made lowercase.
    auditdate = models.DateTimeField(db_column='AuditDate')  # Field name made lowercase.
    audituser = models.CharField(db_column='AuditUser', max_length=50)  # Field name made lowercase.
    auditapp = models.CharField(db_column='AuditApp', max_length=128)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BG_AUDIT'


class BgMain(models.Model):
    bgid = models.BigAutoField(db_column='BGId', primary_key=True)  # Field name made lowercase.
    businessterm = models.CharField(db_column='BusinessTerm', max_length=30)  # Field name made lowercase.
    definition = models.CharField(db_column='Definition', max_length=100)  # Field name made lowercase.
    dataattribute = models.CharField(db_column='DataAttribute', max_length=30)  # Field name made lowercase.
    system = models.CharField(db_column='System', max_length=30)  # Field name made lowercase.
    dataclassification = models.CharField(db_column='DataClassification', max_length=30)  # Field name made lowercase.
    datadomain = models.CharField(db_column='DataDomain', max_length=30)  # Field name made lowercase.
    lineofbusiness = models.CharField(db_column='LineOfBusiness', max_length=30)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=30)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=30)  # Field name made lowercase.
    create_timestamp = models.DateTimeField(db_column='Create_Timestamp',auto_now_add=True)  # Field name made lowercase.
    update_timestamp = models.DateTimeField(db_column='Update_Timestamp',auto_now_add=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BG_MAIN'


class BusinessFunction(models.Model):
    businessfuncid = models.BigAutoField(db_column='BusinessFuncId', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey('UserDetails', models.DO_NOTHING, db_column='UserId')  # Field name made lowercase.
    organization = models.CharField(db_column='Organization', max_length=8000)  # Field name made lowercase.
    businessfunc = models.CharField(db_column='BusinessFunc', max_length=30)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BUSINESS_FUNCTION'


class Roles(models.Model):
    roleid = models.BigAutoField(db_column='RoleId', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey('UserDetails', models.DO_NOTHING, db_column='UserId')  # Field name made lowercase.
    organization = models.TextField(db_column='Organization')  # Field name made lowercase.
    role = models.CharField(db_column='Role', max_length=50)  # Field name made lowercase.
    role_description = models.TextField(db_column='Role_Description', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ROLES'


class RopaAudit(models.Model):
    auditid = models.BigAutoField(db_column='AuditId', primary_key=True)  # Field name made lowercase.
    ropamainid = models.BigIntegerField(db_column='ROPAMAINId')  # Field name made lowercase.
    ropaid = models.BigIntegerField(db_column='ROPAId')  # Field name made lowercase.
    bgid = models.BigIntegerField(db_column='BGId')  # Field name made lowercase.
    ropaty = models.CharField(db_column='ROPATy', max_length=30)  # Field name made lowercase.
    businessfunc = models.CharField(db_column='BusinessFunc', max_length=50)  # Field name made lowercase.
    processingactivityname = models.TextField(db_column='ProcessingActivityName', blank=True, null=True)  # Field name made lowercase.
    processingactivitydesc = models.TextField(db_column='ProcessingActivityDesc', blank=True, null=True)  # Field name made lowercase.
    categoriesdatasubjects = models.CharField(db_column='CategoriesDataSubjects', max_length=50)  # Field name made lowercase.
    categoriespersonaldata = models.CharField(db_column='CategoriesPersonalData', max_length=50)  # Field name made lowercase.
    controllername = models.CharField(db_column='ControllerName', max_length=50)  # Field name made lowercase.
    categoriesofrecepients = models.CharField(db_column='CategoriesofRecepients', max_length=50)  # Field name made lowercase.
    lawfulbasisofprocessing = models.CharField(db_column='LawfulBasisOfProcessing', max_length=50)  # Field name made lowercase.
    retentionschedule = models.CharField(db_column='RetentionSchedule', max_length=50)  # Field name made lowercase.
    dataprocessor = models.TextField(db_column='DataProcessor', blank=True, null=True)  # Field name made lowercase.
    linkcontractprocessor = models.TextField(db_column='LinkContractProcessor')  # Field name made lowercase.
    countriesdetailstransferred = models.CharField(db_column='CountriesDetailsTransferred', max_length=50)  # Field name made lowercase.
    safeguardsexternaltransfers = models.CharField(db_column='SafeguardsExternalTransfers', max_length=50)  # Field name made lowercase.
    securitymeasures_desc = models.TextField(db_column='SecurityMeasures_Desc')  # Field name made lowercase.
    linkscontracts = models.TextField(db_column='LinksContracts')  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=30)  # Field name made lowercase.
    create_timestamp = models.DateTimeField(db_column='Create_Timestamp')  # Field name made lowercase.
    update_timestamp = models.DateTimeField(db_column='Update_Timestamp')  # Field name made lowercase.
    auditaction = models.CharField(db_column='AuditAction', max_length=1)  # Field name made lowercase.
    auditdate = models.DateTimeField(db_column='AuditDate')  # Field name made lowercase.
    audituser = models.CharField(db_column='AuditUser', max_length=50)  # Field name made lowercase.
    auditapp = models.CharField(db_column='AuditApp', max_length=128)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ROPA_AUDIT'


class RopaMain(models.Model):
    ropamainid = models.BigAutoField(db_column='ROPAMAINId', primary_key=True)  # Field name made lowercase.
    ropaid = models.ForeignKey('RopaType', models.DO_NOTHING, db_column='ROPAId')  # Field name made lowercase.
    bgid = models.ForeignKey(BgMain, models.DO_NOTHING, db_column='BGId')  # Field name made lowercase.
    ropaty = models.CharField(db_column='ROPATy', max_length=30)  # Field name made lowercase.
    businessfunc = models.CharField(db_column='BusinessFunc', max_length=50)  # Field name made lowercase.
    processingactivityname = models.TextField(db_column='ProcessingActivityName', blank=True, null=True)  # Field name made lowercase.
    processingactivitydesc = models.TextField(db_column='ProcessingActivityDesc', blank=True, null=True)  # Field name made lowercase.
    categoriesdatasubjects = models.CharField(db_column='CategoriesDataSubjects', max_length=50)  # Field name made lowercase.
    categoriespersonaldata = models.CharField(db_column='CategoriesPersonalData', max_length=50)  # Field name made lowercase.
    controllername = models.CharField(db_column='ControllerName', max_length=50)  # Field name made lowercase.
    categoriesofrecepients = models.CharField(db_column='CategoriesofRecepients', max_length=50)  # Field name made lowercase.
    lawfulbasisofprocessing = models.CharField(db_column='LawfulBasisOfProcessing', max_length=50)  # Field name made lowercase.
    retentionschedule = models.CharField(db_column='RetentionSchedule', max_length=50)  # Field name made lowercase.
    dataprocessor = models.TextField(db_column='DataProcessor', blank=True, null=True)  # Field name made lowercase.
    linkcontractprocessor = models.TextField(db_column='LinkContractProcessor')  # Field name made lowercase.
    countriesdetailstransferred = models.CharField(db_column='CountriesDetailsTransferred', max_length=50)  # Field name made lowercase.
    safeguardsexternaltransfers = models.CharField(db_column='SafeguardsExternalTransfers', max_length=50)  # Field name made lowercase.
    securitymeasures_desc = models.TextField(db_column='SecurityMeasures_Desc')  # Field name made lowercase.
    linkscontracts = models.TextField(db_column='LinksContracts')  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=30)  # Field name made lowercase.
    create_timestamp = models.DateTimeField(db_column='Create_Timestamp')  # Field name made lowercase.
    update_timestamp = models.DateTimeField(db_column='Update_Timestamp')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ROPA_MAIN'


class UserDetails(models.Model):
    userid = models.BigAutoField(db_column='UserId', primary_key=True)  # Field name made lowercase.
    # id = models.ForeignKey(auth_user, on_delete=models.DO_NOTHING, db_column='id', null=True)
    organization = models.CharField(db_column='Organization', max_length=8000)  # Field name made lowercase.
    businessfunc = models.CharField(db_column='BusinessFunc', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ropaty = models.CharField(db_column='ROPATy', max_length=30)  # Field name made lowercase.
    dpo_name = models.CharField(db_column='DPO_Name', max_length=50)  # Field name made lowercase.
    businessunithead = models.CharField(db_column='BusinessUnitHead', max_length=30, blank=True, null=True)  # Field name made lowercase.
    logintime = models.DateTimeField(db_column='LoginTime')  # Field name made lowercase.


    class Meta:
        managed = False
        db_table = 'USER_DETAILS'





# class auth_users(models.model):
#     id = models.BigAutoField(db_column='id', primary_key=True, null=True)
#     # password nvarchar(128) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
#     last_login = models.DateTimeField(db_column='logintime')
#     # is_superuser bit NOT NULL,
#     username = models.CharField(db_column='username', max_length=30, blank=True, null=True)
#     first_name = models.CharField(db_column='first_name', max_length=30, blank=True, null=True)
#     last_name = models.CharField(db_column='last_name', max_length=30, blank=True, null=True)
#     email = models.CharField(db_column='email', max_length=100, blank=True, null=True)
#     # is_staff bit NOT NULL,
#     # is_active bit NOT NULL,
#     # date_joined datetime2(7) NOT NULL,
#     class Meta:
#         managed = False
#         db_table = 'auth_user'
#




class RopaType(models.Model):
    ropaid = models.BigAutoField(db_column='ROPAId', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey(UserDetails, models.DO_NOTHING, db_column='UserId', null=True)  # Field name made lowercase.
    ropaty = models.CharField(db_column='ROPATy', max_length=30, null=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name')  # Field name made lowercase.
    address = models.TextField(db_column='Address', blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=100, blank=True, null=True)  # Field name made lowercase.
    country_code = models.IntegerField(db_column='Country_Code', blank=True, null=True)  # Field name made lowercase.
    telephone = models.IntegerField(db_column='Telephone', blank=True, null=True)  # Field name made lowercase.
    dpo_name = models.TextField(db_column='DPO_Name', blank=True, null=True)  # Field name made lowercase.
    dpo_address = models.TextField(db_column='DPO_Address', blank=True, null=True)  # Field name made lowercase.
    dpo_email = models.CharField(db_column='DPO_Email', max_length=100, blank=True, null=True)  # Field name made lowercase.
    dpo_country_code = models.IntegerField(db_column='DPO_Country_Code', blank=True, null=True)  # Field name made lowercase.
    dpo_phone = models.IntegerField(db_column='DPO_Phone', blank=True, null=True)  # Field name made lowercase.
    rep_name = models.TextField(db_column='Rep_Name', blank=True, null=True)  # Field name made lowercase.
    rep_address = models.TextField(db_column='Rep_Address', blank=True, null=True)  # Field name made lowercase.
    rep_email = models.CharField(db_column='Rep_Email', max_length=100, blank=True, null=True)  # Field name made lowercase.
    rep_country_code = models.IntegerField(db_column='Rep_Country_Code', blank=True, null=True)  # Field name made lowercase.
    rep_phone = models.IntegerField(db_column='Rep_Phone', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ROPA_TYPE'
