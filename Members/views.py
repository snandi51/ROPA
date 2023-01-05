from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from Assessment.models import UserDetails, RopaType, BgMain, RopaMain, RopaAudit
from datetime import date
from django.conf import settings
from django.db import connection

import pandas as pd
import datetime
from django.forms.models import model_to_dict



# Create your views here.

def login_user(request):
    if request.method == 'POST':
        request.session['username'] = request.POST.get('username')
        password = request.POST.get('password')
        username = request.session.get('username')
        user = authenticate(request, username=username, password=password)

        # if request.user.is_authenticated:
        #     return render(request, 'dashboard.html')
        # else:
        #     return render(request, 'index.html')

        if user is not None:
            login(request, user)
            return render(request, 'index.html')
        else:
            context = {
                'text': 'Invalid Username or Password'
            }
            messages.success(request, 'Invalid Username or Password')
            return render(request, 'login.html', context)

    return render(request, 'login.html')

    # if request.user.is_authenticated:
    #     return render(request, 'dashboard.html')
    # else:
    #     return render(request, 'login.html')




@login_required
def logout_user(request):
    logout(request)
    return render(request, 'logout.html')

@login_required
def index(request):
    return render(request, 'index.html')


@login_required
def user(request):
    if request.method == "POST":
        organization = request.POST.get('organization')
        department = request.POST.get('department')
        date = request.POST.get('date')
        business_function_head = request.POST.get('business_function_head')
        business_function = request.POST.get('business_function')

        # import ipdb
        # ipdb.set_trace()
        user_detail = UserDetails(organization=organization, businessfunc=business_function, businessunithead=business_function_head, logintime=date)
        user_detail.save()
        request.session['user_detail'] = user_detail.userid

        ropaty = request.POST.get('ropaty')
        userid = request.POST.get('userid')
        # ropaty = request.POST.get('sap')
        ropaty = request.POST.get('ropaty1')

        name = request.POST.get('name')
        email = request.POST.get('email')
        telephone = request.POST.get('telephone')
        address = request.POST.get('address')
        dpo_name = request.POST.get('dpo_name')
        dpo_email = request.POST.get('dpo_email')
        dpo_telephone = request.POST.get('dpo_telephone')
        dpo_address = request.POST.get('dpo_address')
        rep_name = request.POST.get('rep_name')
        rep_email = request.POST.get('rep_email')
        rep_telephone = request.POST.get('rep_telephone')
        rep_address = request.POST.get('rep_address')
        # current_user = request.user
        # print(current_user.id)

        # user_detail = UserDetails.objects.get(userid= current_user.id)
        ropa_type = RopaType(userid=user_detail, ropaty=ropaty, name=name, email=email, telephone=telephone, address=address, dpo_name=dpo_name, dpo_email=dpo_email, dpo_phone=dpo_telephone, dpo_address=dpo_address, rep_name=rep_name, rep_email=rep_email, rep_phone=rep_telephone, rep_address=rep_address)
        ropa_type.save()

        # result = RopaType.objects.all()
        # bg = pd.DataFrame(list(BgMain.objects.all().values()))
        # # a=len(bg)
        # bg_dict = bg.to_dict('records')
        context = {
            'user_detail': user_detail,
        }
        return render(request, 'dashboard.html', context)
    return render(request, 'user.html')


# def userdetails(request):
#     organization = request.POST.get("title")
#     businessfunc = request.POST.get("department")
#     ropaty = request.POST.get("data_processing_project")
#
#     context = {
#         'org': organization,
#         'busi': businessfunc,
#         'ropty': ropaty
#     }
#     return render(request, 'test.html', context)


# def bussiness_glossary(request):
#     result = BgMain.objects.all()
#     # bgid = []
#     businessterm = []
#     definition = []
#     dataattribute = []
#     system = []
#     dataclassification = []
#     datadomain = []
#     lineofbusiness = []
#     status = []
#     createdby = []
#     create_timestamp = []
#     update_timestamp = []
#
#     for i in result:
#         # bgid.append(i.bgid)
#         businessterm.append(i.businessterm)
#         definition.append(i.definition)
#         dataattribute.append(i.dataattribute)
#         system.append(i.system)
#         dataclassification.append(i.dataclassification)
#         datadomain.append(i.datadomain)
#         lineofbusiness.append(i.lineofbusiness)
#         status.append(i.status)
#         createdby.append(i.createdby)
#         # create_timestamp.append(i.create_timestamp)
#         # update_timestamp.append(i.update_timestamp)
#     key_dict = {'businessterm': businessterm, 'definition': definition, 'dataattribute': dataattribute, 'system':system, 'dataclassification':dataclassification, 'datadomain':datadomain, 'lineofbusiness':lineofbusiness, 'status':status, 'createdby':createdby}
#     bussiness_glossary_df = pd.DataFrame(key_dict)
#     # import ipdb
#     # ipdb.set_trace()
#     bussiness_glossary_df.to_csv('Assessment/static/assets/bs_glossary_df.csv', index=False)
#     context = {
#         'bga': result
#     }
#     return render(request, 'bussiness_glossary.html', context)


def date(request):
    today = date.today()
    print("Today's date:", today)
    return today


def download(request):
    return render(request, 'download.html')


def workflow(request):
    return render(request, 'workflow.html')


def work(request):
    return render(request, 'work.html')


def temp(request):
    return render(request, 'temp.html')


def bussiness_glossary(request):

    context={
        'bga': BgAudit.objects.all()
    }
    return render(request, 'bussiness_glossary.html',context)


@login_required
def test(request):
    # import ipdb
    # ipdb.set_trace()


    if request.method == "POST":
        businessterm = request.POST.get('businessterm')
        definition = request.POST.get('definition')
        dataattribute = request.POST.get('dataattribute')
        system = request.POST.get('system')
        datadomain = request.POST.get('datadomain')
        lineofbusiness = request.POST.get('lineofbusiness')
        status = request.POST.get('status')
        # dataclassification= request.POST.get('dataclassification')
        createdby = request.POST.get('createdby')



# classification value pass pending.

        business_detail = BgMain(businessterm=businessterm, definition=definition, dataattribute=dataattribute, system=system, datadomain=datadomain,lineofbusiness=lineofbusiness,status=status,createdby=createdby)

        business_detail.save()

    result = BgMain.objects.all()
    bg = pd.DataFrame(list(BgMain.objects.all().values()))
    # a=len(bg)
    bg_dict = bg.to_dict('records')

    for i in bg_dict:

        i.update({'create_timestamp': str(i.get('create_timestamp'))})
        i.update({'update_timestamp': str(i.get('update_timestamp'))})
    # import ipdb
    # ipdb.set_trace()

    context = {
            'bga': result,
            'bg_dict': bg_dict
             }
    stored_proc(request)

    return render(request, 'test.html', context)


def addnew(request):
    return render(request, 'addnew.html')


def edit(request):
    # import ipdb
    # ipdb.set_trace()

    print('edit function')
    if request.method == "POST":
        #  form data fetching
        bgid = request.POST.get('bgid')
        businessterm = request.POST.get('businessterm')
        definition = request.POST.get('definition')
        dataattribute = request.POST.get('dataattribute')
        system = request.POST.get('system')
        datadomain = request.POST.get('datadomain')
        lineofbusiness = request.POST.get('lineofbusiness')
        status = request.POST.get('status')
        createdby = request.POST.get('createdby')

        # Id maapping with database then form updated data save to variables
        edit_db = BgMain.objects.get(bgid=bgid)
        edit_db_filter = BgMain.objects.filter(bgid=bgid)
        # check in  ipdb
        print(edit_db)
        print(edit_db_filter)
        edit_db.businessterm = businessterm
        edit_db.dataattribute = dataattribute
        edit_db.definition = definition
        edit_db.system = system
        edit_db.datadomain = datadomain
        edit_db.lineofbusiness = lineofbusiness
        edit_db.status = status
        edit_db.createdby = createdby
        edit_db.update_timestamp=datetime.datetime.now()
        # updates data save to new dict

        # check in  ipdb
        edit_db.save()
        print(edit_db)
        # check in  ipdb


        result = BgMain.objects.all()
        print(result)
        # check in  ipdb
        bg = pd.DataFrame(list(BgMain.objects.all().values()))
        print(bg)
        # check in  ipdb
        # a=len(bg)
        bg_dict = bg.to_dict('records')
        # check in  ipdb

        print(bg_dict)

        # bgid_update = request.POST.get('bgid')
        # print(bgid_update)
        #
        # bg_audit_result = BgAudit.objects.get(bgid=bgid_update)
        # print(bg_audit_result)
        # bg_audit_result.update_timestamp = datetime.datetime.now()
        # bg_audit_result.save()

        context = {
            'bga': result,
            'bg_dict': bg_dict
        }

        stored_proc_edit(request)

        return render(request, 'test.html', context)


def delete(request):
    # import ipdb
    # ipdb.set_trace()
    print('delete function')

    id_delete = request.GET.get('search')
    # Id maapping with database then form updated data save to variables
    delete_db = BgMain.objects.get(bgid=id_delete)
    print(delete_db)

    # updates data save to new dict
    delete_db.delete()

    result = BgMain.objects.all()
    bg = pd.DataFrame(list(BgMain.objects.all().values()))
    # a=len(bg)
    bg_dict = bg.to_dict('records')

    for i in bg_dict:

        i.update({'create_timestamp': str(i.get('create_timestamp'))})
        i.update({'update_timestamp': str(i.get('update_timestamp'))})

    context = {
        'bga': result,
        'bg_dict': bg_dict
    }

    # stored_proc_delete(request)

    return render(request, 'test.html', context)


def stored_proc(req):
    # import ipdb
    # ipdb.set_trace()
    cursor = connection.cursor()
    print('sp_add')
    try:
        cursor.execute('EXEC spauditinsertoperation')

        return render(req, 'test.html')
    finally:
        cursor.close()


def stored_proc_edit(req):
    # import ipdb
    # ipdb.set_trace()
    cursor = connection.cursor()
    print('sp_edit')
    try:
        cursor.execute('EXEC spauditupdateoperation')

        return render(req, 'test.html')
    finally:
        cursor.close()


# def stored_proc_delete(req):
#     # import ipdb
#     # ipdb.set_trace()
#     cursor = connection.cursor()
#     print('sp_delete')
#     try:
#         cursor.execute('EXEC spauditdeleteoperation')
#
#         return render(req, 'test.html')
#     finally:
#         cursor.close()


def dashboard(request):
    return render(request, 'dashboard.html')


@login_required
def record(request):
    if request.method == "POST":
        print("inside function")
        status = request.POST.get('status')
        processingactivityname = request.POST.get('processingactivityname')
        businessfunc = request.POST.get('businessfunc')
        processingactivitydesc = request.POST.get('processingactivitydesc')
        categoriesdatasubjects = request.POST.get('categoriesdatasubjects')
        controllername = request.POST.get('controllername')
        categoriesofrecepients = request.POST.get('categoriesofrecepients')
        categoriespersonaldata = request.POST.get('categoriespersonaldata')
        lawfulbasisofprocessing = request.POST.get('lawfulbasisofprocessing')
        dataprocessor = request.POST.get('dataprocessor')
        retentionschedule = request.POST.get('retentionschedule')
        linkcontractprocessor = request.POST.get('linkcontractprocessor')
        countriesdetailstransferred = request.POST.get('countriesdetailstransferred')
        safeguardsexternaltransfers = request.POST.get('safeguardsexternaltransfers')
        securitymeasures_desc = request.POST.get('securitymeasures_desc')
        linkscontracts = request.POST.get('linkscontracts')

        # import ipdb
        # ipdb.set_trace()

        user_detail = request.session['user_detail']
        # user_detail = UserDetails.objects.get(userid=current_user.id)
        ropa_id = RopaType.objects.get(userid=user_detail)
        print(ropa_id)
        ropa_id_dict = model_to_dict(ropa_id)
        print(ropa_id_dict)
        main_ropa_id = ropa_id_dict['ropaid']
        # ropa_type = RopaType()
        ropa_type = RopaType.objects.get(ropaid=main_ropa_id)
        # ropa_type = RopaType.objects.values('ropaid')
        ropa_type.save()

        ropa_bgmain = BgMain()
        ropa_bgmain.save()

        ropa_detail = RopaMain(ropaid=ropa_type, bgid=ropa_bgmain, status=status, processingactivityname=processingactivityname,
                               businessfunc=businessfunc, processingactivitydesc=processingactivitydesc,
                               categoriesdatasubjects=categoriesdatasubjects, controllername=controllername,
                               categoriesofrecepients=categoriesofrecepients,  categoriespersonaldata=categoriespersonaldata,
                               lawfulbasisofprocessing=lawfulbasisofprocessing, dataprocessor=dataprocessor,
                               retentionschedule=retentionschedule, linkcontractprocessor=linkcontractprocessor,
                               countriesdetailstransferred=countriesdetailstransferred, safeguardsexternaltransfers=safeguardsexternaltransfers,
                               securitymeasures_desc=securitymeasures_desc, linkscontracts=linkscontracts
                               )
        ropa_detail.save()

        # ropa_type = RopaType(ropaid=ropa_detail)
        # ropa_type.save()

    result = RopaMain.objects.all()
    print(result)
    # key_dict = {'businessfunc': businessfunc, 'processingactivityname': processingactivityname,
    #             'processingactivitydesc': processingactivitydesc, 'categoriesdatasubjects': categoriesdatasubjects,
    #             'categoriespersonaldata': categoriespersonaldata, 'status': status}
    # ropa_df = pd.DataFrame(key_dict)
    # ropa_df.to_csv('Assessment/static/assets/data_record_excel.csv', index=False)
    ropa_main = pd.DataFrame(list(RopaMain.objects.all().values('ropaid', 'businessfunc', 'processingactivityname','processingactivitydesc',
                                                                'categoriesdatasubjects', 'categoriespersonaldata', 'status', 'controllername',
                                                                'categoriesofrecepients', 'lawfulbasisofprocessing', 'dataprocessor',
                                                                'retentionschedule', 'linkcontractprocessor', 'countriesdetailstransferred',
                                                                'safeguardsexternaltransfers', 'securitymeasures_desc', 'linkscontracts')))
    ropa_main.to_csv('Assessment/static/assets/data_record_excel.csv', index=False)
    # a=len(bg)
    ropa_dict = ropa_main.to_dict('records')

    for i in ropa_dict:
        i.update({'create_timestamp': str(i.get('create_timestamp'))})
        i.update({'update_timestamp': str(i.get('update_timestamp'))})
    # import ipdb
    # ipdb.set_trace()

    ropa_stored_proc(request)
    context = {
        'result': result,
        'ropa_dict': ropa_dict,

    }
    return render(request, 'record.html', context)


def ropa_edit(request):
    print('inside edit function')
    if request.method == "POST":
        # import ipdb
        # ipdb.set_trace()
        #  form data fetching
        status = request.POST.get('status')
        processingactivityname = request.POST.get('processingactivityname')
        businessfunc = request.POST.get('businessfunc')
        processingactivitydesc = request.POST.get('processingactivitydesc')
        categoriesdatasubjects = request.POST.get('categoriesdatasubjects')
        controllername = request.POST.get('controllername')
        categoriesofrecepients = request.POST.get('categoriesofrecepients')
        categoriespersonaldata = request.POST.get('categoriespersonaldata')
        lawfulbasisofprocessing = request.POST.get('lawfulbasisofprocessing')
        dataprocessor = request.POST.get('dataprocessor')
        retentionschedule = request.POST.get('retentionschedule')
        linkcontractprocessor = request.POST.get('linkcontractprocessor')
        countriesdetailstransferred = request.POST.get('countriesdetailstransferred')
        safeguardsexternaltransfers = request.POST.get('safeguardsexternaltransfers')
        securitymeasures_desc = request.POST.get('securitymeasures_desc')
        linkscontracts = request.POST.get('linkscontracts')

        #ropa id added from record html which has none display style
        ropaid = request.POST.get('ropaid')


        # Id maapping with database then form updated data save to variables
        ropa_edit_db = RopaMain.objects.get(ropaid=ropaid)
        ropa_edit_db_filter = RopaMain.objects.filter(ropaid=ropaid)
        print(ropa_edit_db)
        print(ropa_edit_db_filter)
        ropa_edit_db.status = status
        ropa_edit_db.processingactivityname = processingactivityname
        ropa_edit_db.businessfunc = businessfunc
        ropa_edit_db.processingactivitydesc = processingactivitydesc
        ropa_edit_db.categoriesdatasubjects = categoriesdatasubjects
        ropa_edit_db.controllername = controllername
        ropa_edit_db.categoriesofrecepients = categoriesofrecepients
        ropa_edit_db.categoriespersonaldata = categoriespersonaldata
        ropa_edit_db.lawfulbasisofprocessing = lawfulbasisofprocessing
        ropa_edit_db.dataprocessor = dataprocessor
        ropa_edit_db.retentionschedule = retentionschedule
        ropa_edit_db.linkcontractprocessor = linkcontractprocessor
        ropa_edit_db.countriesdetailstransferred = countriesdetailstransferred
        ropa_edit_db.safeguardsexternaltransfers = safeguardsexternaltransfers
        ropa_edit_db.securitymeasures_desc = securitymeasures_desc
        ropa_edit_db.linkscontracts = linkscontracts
        ropa_edit_db.update_timestamp = datetime.datetime.now()
        # updates data save to new dict
        ropa_edit_db.save()
        print('ropa edit db:', ropa_edit_db)
        user_detail = request.session['user_detail']
        # user_detail = UserDetails.objects.get(userid=current_user.id)
        ropa_id = RopaType.objects.get(userid=user_detail)
        print(ropa_id)
        ropa_id_dict = model_to_dict(ropa_id)
        print(ropa_id_dict)
        main_ropa_id = ropa_id_dict['ropaid']
        # ropa_type = RopaType()
        ropa_type = RopaType.objects.get(ropaid=main_ropa_id)
        # ropa_type = RopaType.objects.values('ropaid')
        ropa_type.save()

        ropa_bgmain = BgMain()
        ropa_bgmain.save()

        result = RopaMain.objects.all()
        ropa_main = pd.DataFrame(list(RopaMain.objects.all().values()))
        print('ropa_main in edit', ropa_main)
        # a=len(bg)
        ropa_dict = ropa_main.to_dict('records')
        print('ropa_dict in edit', ropa_dict)

        context = {
            'result': result,
            'ropa_dict': ropa_dict
        }

        ropa_stored_proc_edit(request)
        return render(request, 'record.html', context)


def ropa_delete(request):
    # import ipdb
    # ipdb.set_trace()
    print('ropa delete function')

    id_delete = request.GET.get('search')
    # Id maapping with database then form updated data save to variables
    delete_db = RopaMain.objects.get(ropaid=id_delete)
    print(delete_db)


    # updates data save to new dict
    delete_db.delete()

    result = RopaMain.objects.all()
    ropa_delete = pd.DataFrame(list(RopaMain.objects.all().values()))
    # a=len(bg)
    ropa_dict = ropa_delete.to_dict('records')

    for i in ropa_dict:

        i.update({'create_timestamp': str(i.get('create_timestamp'))})
        i.update({'update_timestamp': str(i.get('update_timestamp'))})

    context = {
        'result': result,
        'ropa_dict': ropa_dict
    }

    # ropa_stored_proc_delete(request)
    return render(request, 'record.html', context)


def ropa_stored_proc(req):
    # import ipdb
    # ipdb.set_trace()
    cursor = connection.cursor()
    print('ropa_sp_add')
    try:
        cursor.execute('EXEC spauditinsertoperation_ropa')
        return render(req, 'record.html')
    finally:
        cursor.close()


def ropa_stored_proc_edit(req):
   # import ipdb
  #  ipdb.set_trace()
    cursor = connection.cursor()
    print('ropa_sp_edit')
    try:

        cursor.execute('EXEC spauditupdateoperation_ropa')

        return render(req, 'record.html')
    finally:
        cursor.close()


# def ropa_stored_proc_delete(req):
#     # import ipdb
#     # ipdb.set_trace()
#     cursor = connection.cursor()
#     print('ropa_sp_delete')
#     try:
#         cursor.execute('EXEC spauditdeleteoperation_ropa')
#
#         return render(req, 'record.html')
#     finally:
#         cursor.close()
