from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from Assessment.models import UserDetails, RopaType, BgMain
from datetime import date
from django.conf import settings

import pandas as pd
import datetime




# Create your views here.

def login_user(request):
    if request.method == 'POST':
        request.session['username'] = request.POST.get('username')
        password = request.POST.get('password')
        username = request.session.get('username')
        user = authenticate(request, username=username, password=password)

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



@login_required
def logout_user(request):
    logout(request)
    return render(request, 'logout.html')

@login_required
def index(request):
    return render(request, 'index.html')


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


def bussiness_glossary(request):
    result = BgMain.objects.all()
    # bgid = []
    businessterm = []
    definition = []
    dataattribute = []
    system = []
    dataclassification = []
    datadomain = []
    lineofbusiness = []
    status = []
    createdby = []
    create_timestamp = []
    update_timestamp = []

    for i in result:
        # bgid.append(i.bgid)
        businessterm.append(i.businessterm)
        definition.append(i.definition)
        dataattribute.append(i.dataattribute)
        system.append(i.system)
        dataclassification.append(i.dataclassification)
        datadomain.append(i.datadomain)
        lineofbusiness.append(i.lineofbusiness)
        status.append(i.status)
        createdby.append(i.createdby)
        # create_timestamp.append(i.create_timestamp)
        # update_timestamp.append(i.update_timestamp)
    key_dict = {'businessterm': businessterm, 'definition': definition, 'dataattribute': dataattribute, 'system':system, 'dataclassification':dataclassification, 'datadomain':datadomain, 'lineofbusiness':lineofbusiness, 'status':status, 'createdby':createdby}
    bussiness_glossary_df = pd.DataFrame(key_dict)
    # import ipdb
    # ipdb.set_trace()
    bussiness_glossary_df.to_csv('Assessment/static/assets/bs_glossary_df.csv', index=False)
    context = {
        'bga': result
    }
    return render(request, 'bussiness_glossary.html', context)


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


def test(request):
    import ipdb
    ipdb.set_trace()
    if request.method == "POST":
        businessterm = request.POST.get('businessterm')
        definition = request.POST.get('definition')
        dataattribute = request.POST.get('dataattribute')
        system = request.POST.get('system')
        datadomain = request.POST.get('datadomain')
        lineofbusiness = request.POST.get('lineofbusiness')
        status = request.POST.get('status')
        # dataclassification= request.POST.get('dataclassification')
        createdby=request.POST.get('createdby')

        business_detail = BgMain(businessterm=businessterm, definition=definition, dataattribute=dataattribute, system=system,datadomain=datadomain,lineofbusiness=lineofbusiness,status=status,createdby=createdby)
        business_detail.save()

    result = BgMain.objects.all()
    bg = pd.DataFrame(list(BgMain.objects.all().values()))
    # a=len(bg)
    bg_dict=bg.to_dict('records')

    for i in bg_dict:

        i.update({'create_timestamp': str(i.get('create_timestamp'))})
        i.update({'update_timestamp': str(i.get('update_timestamp'))})
    import ipdb
    ipdb.set_trace()

    context = {
            'bga' : result,
            'bg_dict':bg_dict
             }

    return render(request, 'test.html', context)


def addnew(request):
    return render(request, 'addnew.html')


def temp(request):
    return render(request, 'temp.html')


def delete(request):
    return render(request, 'delete.html')


def edit(request):
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
        print(edit_db)
        edit_db.businessterm = businessterm
        edit_db.dataattribute = dataattribute
        edit_db.definition = definition
        edit_db.system = system
        edit_db.datadomain = datadomain
        edit_db.lineofbusiness = lineofbusiness
        edit_db.status = status
        edit_db.createdby = createdby

        # updates data save to new dict
        edit_db.save()

        result = BgMain.objects.all()
        bg = pd.DataFrame(list(BgMain.objects.all().values()))
        # a=len(bg)
        bg_dict = bg.to_dict('records')

        context = {
            'bga': result,
            'bg_dict': bg_dict
        }
        return render(request, 'test.html', context)


def dashboard(request):
    return render(request, 'dashboard.html')


