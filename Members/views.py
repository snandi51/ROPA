from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.models import User
from Assessment.models import UserDetails, RopaType, BgMain, RopaMain, RopaAudit, BusinessFunction, BgAudit
from datetime import date
from django.conf import settings
from django.db import connection

import pandas as pd
import datetime
from django.forms.models import model_to_dict
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import Group
# from Assessment.views import group_required
# from IPython.display import display, HTML
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
# import pdfkit as pdf


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
            # import ipdb
            # ipdb.set_trace()
            login(request, user)
            print('user', request.user)
            print('user_id', request.user.id)
            userid = request.user.id

            # result = UserDetails.objects.all().filter()
            result = UserDetails.objects.all().values().filter(userid=userid)
            bg = pd.DataFrame(list(UserDetails.objects.all().values().filter(userid=userid)))
            bg_dict = bg.to_dict('records')[0]
            print(result)
            print(bg_dict)
            print(bg_dict['ropaty'])
            output = bg_dict['ropaty']
            print(output)
            request.session['output'] = output
            if output is not None:
                if output == 'Processor':
                    print(output, 'function inner dashboard')
                    return render(request, 'processor_dashboard.html')
                else:
                    print('else function inner dashboard')
                    return render(request, 'dashboard.html')
            else:
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


# @login_required
def index(request):
    return render(request, 'index.html')


# @login_required
def user(request):
    if request.method == "POST":
        id = request.user.id
        organization = request.POST.get('organization')
        department = request.POST.get('department')
        date = request.POST.get('date')
        business_function_head = request.POST.get('business_function_head')
        business_function = request.POST.get('business_function')

        # import ipdb
        # ipdb.set_trace()

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

        # user_detail = UserDetails(id=id, organization=organization, businessfunc=business_function,
        #                           businessunithead=business_function_head, logintime=date)
        # user_detail.save()
        #
        # request.session['user_detail'] = user_detail.userid

        userdetail = UserDetails.objects.get(userid=id)
        userdetail.ropaty = ropaty
        userdetail.save()

        # user_detail = UserDetails.objects.get(userid= current_user.id)
        ropa_type = RopaType(userid=userdetail, ropaty=ropaty, name=name, email=email, telephone=telephone, address=address, dpo_name=dpo_name, dpo_email=dpo_email, dpo_phone=dpo_telephone, dpo_address=dpo_address, rep_name=rep_name, rep_email=rep_email, rep_phone=rep_telephone, rep_address=rep_address)
        ropa_type.save()

        # result = RopaType.objects.all()
        # bg = pd.DataFrame(list(BgMain.objects.all().values()))
        # # a=len(bg)
        # bg_dict = bg.to_dict('records')
        context = {
            'user_detail': userdetail,
        }

        bg = pd.DataFrame(list(UserDetails.objects.all().values().filter(userid=id)))
        bg_dict = bg.to_dict('records')[0]

        print(bg_dict)

        output = bg_dict['ropaty']
        print('Ropa Type:', output)
        request.session['output'] = output
        if output is not None:
            if output == 'Processor':
                print(output, 'function inner dashboard')
                return render(request, 'processor_dashboard.html', context)
            else:
                print('else function inner dashboard')
                return render(request, 'dashboard.html', context)
        else:
            return render(request, 'index.html')

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
    is_data_loaded = False
    if request.method == "POST":
        businessterm = request.POST.get('businessterm')
        definition = request.POST.get('definition')
        dataattribute = request.POST.get('dataattribute')
        system = request.POST.get('system')
        datadomain = request.POST.get('datadomain')
        lineofbusiness = request.POST.get('lineofbusiness')
        status = 'Awaiting Approval'


        dataclassification_list = request.POST.getlist('dataclassification')
        print(dataclassification_list)
        dataclassification = ' , '.join([str(elem) for elem in dataclassification_list])
        dataclassification = dataclassification.upper()
        print(dataclassification)

        createdby = request.POST.get('createdby')

        is_data_loaded = True

        # classification value pass pending.
        business_detail = BgMain(businessterm=businessterm, definition=definition, dataclassification=dataclassification, dataattribute=dataattribute,
                                 system=system, datadomain=datadomain,
                                 lineofbusiness=lineofbusiness, status=status, createdby=createdby)
        business_detail.save()

    result = BgMain.objects.all()
    bg1 = pd.DataFrame(list(BgMain.objects.all().values()))
    # bg1 = pd.DataFrame(list(BgMain.objects.all().values('businessterm', 'definition','dataclassification', 'dataattribute', 'system', 'datadomain', 'lineofbusiness', 'status', 'createdby')))
    # bg1 = bg1.drop(['bgid'])
    # bg2 = pd.DataFrame(bg1)
    bg2 = bg1.copy()
    # bg1 = bg1.rename(columns={'businessterm': 'business_term', 'dataclassification': 'data_classification',
    #                           'datadomain': 'data_domain', 'lineofbusiness':'line_of_business', 'createdby':'created_by'}, inplace=True)
    bg2.columns = bg2.columns.str.replace('businessterm', 'business_term')
    bg2.columns = bg2.columns.str.replace('dataclassification', 'data_classification')
    bg2.columns = bg2.columns.str.replace('datadomain', 'data_domain')
    bg2.columns = bg2.columns.str.replace('lineofbusiness', 'line_of_business')
    bg2.columns = bg2.columns.str.replace('createdby', 'created_by')
    bg2.columns = bg2.columns.str.replace('dataattribute', 'data_attribute')
    bg2.to_csv('Assessment/static/assets/bs_glossary_df.csv', index=False)
    # a=len(bg)
    bg = bg1.sort_values(by='update_timestamp', ascending=False)
    bg_dict = bg.to_dict('records')

    for i in bg_dict:

        i.update({'create_timestamp': str(i.get('create_timestamp'))})
        i.update({'update_timestamp': str(i.get('update_timestamp'))})
        i.update({'comments': str(i.get('comments'))})
    # import ipdb
    # ipdb.set_trace()

    output = request.session.get('output')

    new_data = str(is_data_loaded).lower()

    context = {
            'bga': result,
            'bg_dict': bg_dict,
            'output': output,
            'is_data_loaded': is_data_loaded,
            'new_data': new_data

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

        dataclassification_list = request.POST.getlist('dataclassification')
        print(dataclassification_list)
        dataclassification = ' , '.join([str(elem) for elem in dataclassification_list])
        dataclassification = dataclassification.upper()
        print(dataclassification)

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
        edit_db.dataclassification = dataclassification
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

        for i in bg_dict:
            i.update({'create_timestamp': str(i.get('create_timestamp'))})
            i.update({'update_timestamp': str(i.get('update_timestamp'))})
            i.update({'comments': str(i.get('comments'))})

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
        i.update({'comments': str(i.get('comments'))})

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
        cursor.execute('EXEC spauditinsertoperation_bg')

        return render(req, 'test.html')
    finally:
        cursor.close()


def stored_proc_edit(req):
    # import ipdb
    # ipdb.set_trace()
    cursor = connection.cursor()
    print('sp_edit')
    try:
        cursor.execute('EXEC spauditupdateoperation_bg')

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

# @login_required(login_url='/index/')
def dashboard(request):
    return render(request, 'dashboard.html')


# @login_required
def record(request):
    is_data_loaded = False
    if request.method == "POST":
        print("inside function")
        status = 'Awaiting Approval'
        processingactivityname = request.POST.get('processingactivityname')
        businessfunc = request.POST.get('businessfunc')
        processingactivitydesc = request.POST.get('processingactivitydesc')
        categoriesdatasubjects = request.POST.get('categoriesdatasubjects')
        controllername = request.POST.get('controllername')
        categoriesofrecepients = request.POST.get('categoriesofrecepients')
        categoriespersonaldata_list = request.POST.getlist('categoriespersonaldata')
        print(categoriespersonaldata_list)
        categoriespersonaldata = ' , '.join([str(elem) for elem in categoriespersonaldata_list])
        categoriespersonaldata = categoriespersonaldata.upper()
        print(categoriespersonaldata)
        lawfulbasisofprocessing = request.POST.get('lawfulbasisofprocessing')
        dataprocessor = request.POST.get('dataprocessor')
        retentionschedule = request.POST.get('retentionschedule')
        linkcontractprocessor = request.POST.get('linkcontractprocessor')
        countriesdetailstransferred = request.POST.get('countriesdetailstransferred')
        safeguardsexternaltransfers = request.POST.get('safeguardsexternaltransfers')
        securitymeasures_desc = request.POST.get('securitymeasures_desc')
        linkscontracts = request.POST.get('linkscontracts')

        is_data_loaded = True

        # user_detail = request.session['user_detail']
        # id = request.user.id
        # user_detail = RopaType.objects.get(userid=id)
        # # user_detail.ropaid = ropaid
        # user_detail.save()

        userid = request.user.id
        print(userid)
        ropa_obj = RopaType.objects.get(userid=userid)
        print('ropa_obj', ropa_obj)
        ropa_id_dict = model_to_dict(ropa_obj)
        print('ropa_id_dict', ropa_id_dict)
        main_ropa_id = ropa_id_dict['ropaid']
        print('main_ropa_id', main_ropa_id)
        ropa_type = RopaType.objects.get(ropaid=main_ropa_id)
        ropa_type.save()

        # ropa_bgmain = BgMain.objects.get(bgid=user_detail)
        # print('ropa_bgmain', ropa_bgmain)
        # ropa_bgmain.save()

        ropa_detail = RopaMain(ropaid=ropa_type, status=status, processingactivityname=processingactivityname,
                               businessfunc=businessfunc, processingactivitydesc=processingactivitydesc,
                               categoriesdatasubjects=categoriesdatasubjects, controllername=controllername,
                               categoriesofrecepients=categoriesofrecepients,  categoriespersonaldata=categoriespersonaldata,
                               lawfulbasisofprocessing=lawfulbasisofprocessing, dataprocessor=dataprocessor,
                               retentionschedule=retentionschedule, linkcontractprocessor=linkcontractprocessor,
                               countriesdetailstransferred=countriesdetailstransferred, safeguardsexternaltransfers=safeguardsexternaltransfers,
                               securitymeasures_desc=securitymeasures_desc, linkscontracts=linkscontracts)
        ropa_detail.save()

        # ropa_type = RopaType(ropaid=ropa_detail)
        # ropa_type.save()

    result = RopaMain.objects.all()
    print('result of ropamain', result)
    # key_dict = {'businessfunc': businessfunc, 'processingactivityname': processingactivityname,
    #             'processingactivitydesc': processingactivitydesc, 'categoriesdatasubjects': categoriesdatasubjects,
    #             'categoriespersonaldata': categoriespersonaldata, 'status': status}
    # ropa_df = pd.DataFrame(key_dict)
    # ropa_df.to_csv('Assessment/static/assets/data_record_excel.csv', index=False)
    ropa_main1 = pd.DataFrame(list(RopaMain.objects.all().values('ropamainid','ropaid', 'businessfunc', 'processingactivityname','processingactivitydesc',
                                                                'categoriesdatasubjects', 'categoriespersonaldata', 'status', 'controllername',
                                                                'categoriesofrecepients', 'lawfulbasisofprocessing', 'dataprocessor',
                                                                'retentionschedule', 'linkcontractprocessor', 'countriesdetailstransferred',
                                                                'safeguardsexternaltransfers', 'securitymeasures_desc', 'linkscontracts', 'update_timestamp')))
    ropa_csv = pd.DataFrame(list(RopaMain.objects.all().values('ropaid', 'businessfunc', 'processingactivityname','processingactivitydesc',
                                                                'categoriesdatasubjects', 'categoriespersonaldata', 'status', 'controllername',
                                                                'categoriesofrecepients', 'lawfulbasisofprocessing', 'dataprocessor',
                                                                'retentionschedule', 'linkcontractprocessor', 'countriesdetailstransferred',
                                                                'safeguardsexternaltransfers', 'securitymeasures_desc', 'linkscontracts')))
    ropa_csv = ropa_csv.drop(['ropaid'], axis=1)

    # fig, ax = plt.subplots(figsize=(12, 4))
    # ax.axis('tight')
    # ax.axis('off')
    # the_table = ax.table(cellText=ropa_csv.values, colLabels=ropa_csv.columns, loc='center')
    #
    # pp = PdfPages("Assessment/static/assets/data_record_pdf.pdf")
    # pp.savefig(fig, bbox_inches='tight')
    # pp.close()

    # ropa_csv.to_html('f.html')
    # ropa_pdf = 'Assessment/static/assets/data_record_pdf.pdf'
    # pdf.from_file('f.html', ropa_pdf)
    # style = ropa_csv.style.set_table_styles(
    #     [{"selector": "", "props": [("border", "1px solid grey")]},
    #      {"selector": "tbody td", "props": [("border", "1px solid grey")]},
    #      {"selector": "th", "props": [("border", "1px solid grey")]}
    #      ])
    # ropa_csv.style.set_table_styles(style).to_csv('Assessment/static/assets/data_record_excel.csv', index=False)
    table1 = ropa_csv.style.set_precision(2).background_gradient().hide_index().to_excel('Assessment/static/assets/data_record_excel1.xlsx', engine='openpyxl')
    ropa_main = ropa_main1.sort_values(by='update_timestamp', ascending=False)
    # a=len(bg)
    ropa_dict = ropa_main.to_dict('records')
    # print('ropa_dict:', ropa_dict)

    user_id = request.user.id
    user_detail = pd.DataFrame(list(RopaType.objects.all().values().filter(userid=user_id)))
    user_detail = user_detail.drop(['ropaid', 'userid_id', 'ropaty', 'country_code', 'dpo_country_code', 'rep_country_code'], axis=1)
    table2 = user_detail.style.set_precision(2).background_gradient().hide_index().to_excel('Assessment/static/assets/data_record_excel2.xlsx', engine='openpyxl')

    # result = pd.concat([ropa_table, user_table])
    # table_combined = ropa_csv.merge(user_detail, left_on='ropaid', right_on='ropaid', how='left')
    # table_combined =  user_detail.append(ropa_csv, ignore_index = True)
    # table_combined.to_excel("Assessment/static/assets/data_record_excel3.xlsx", index=False)

    # writer = pd.ExcelWriter(r'Assessment/static/assets/data_record_excel.xlsx', engine='xlsxwriter')
    # table_combined.to_excel(writer, index=False, sheet_name='report')

    # workbook = writer.book
    # worksheet = writer.sheets['report']

    writer = pd.ExcelWriter('Assessment/static/assets/data_record_excel.xlsx', engine='xlsxwriter')
    workbook = writer.book
    worksheet = workbook.add_worksheet('report')
    writer.sheets['report'] = worksheet

    user_detail.to_excel(writer, sheet_name='report', startrow=3, startcol=0)
    ropa_csv.to_excel(writer, sheet_name='report', startrow=9, startcol=0)
    # Now we have the worksheet object. We can manipulate it
    worksheet.set_zoom(90)
    #header formatting
    header_format = workbook.add_format({
        "valign": "vcenter",
        "bold": True,
        'border': 1,
        'text_wrap': True,
        'fg_color': '#D7E4BC',
        'border_color': 'black'
    })
    # Full border formatting for conditional formatted cells
    full_border = workbook.add_format({"border": 1, "border_color": "#D3D3D3"})
    # add title
    title = "Controller "
    title2 = 'Records of Processing Activity'
    # merge cells
    format = workbook.add_format()
    format.set_font_size(20)
    format.set_font_color("#333333")
    #
    subheader = "Article 30 Record of Processing Activities"
    subheader1 = 'Name and contact details'
    subheader2 = 'Data Protection Officer (if applicable)'
    subheader3 = 'Representative (if applicable)'
    worksheet.merge_range('A1:M1', title, format)
    worksheet.merge_range('A7:Q7', title2, format)
    worksheet.merge_range('B9:Q9', subheader)
    worksheet.merge_range('B3:E3', subheader1)
    worksheet.merge_range('F3:I3', subheader2)
    worksheet.merge_range('J3:M3', subheader3)
    worksheet.set_row(2, 15)  # Set the header row height to 15
    # puting it all together
    # Write the column headers with the defined format.
    for col_num, value in enumerate(user_detail.columns.values):
        # print(col_num, value)
        worksheet.write(3, col_num+1, value, header_format)

    for col_num, value in enumerate(ropa_csv.columns.values):
        # print(col_num, value)
        worksheet.write(9, col_num+1, value, header_format)

    writer.save()

    for i in ropa_dict:
        i.update({'create_timestamp': str(i.get('create_timestamp'))})
        i.update({'update_timestamp': str(i.get('update_timestamp'))})
        i.update({'comments': str(i.get('comments'))})
        i.update({'categoriesdatasubjects': str(i.get('categoriesdatasubjects'))})
        i.update({'processingactivityname': str(i.get('processingactivityname'))})


    ropa_stored_proc(request)

    # import ipdb
    # ipdb.set_trace()

    distinct_values = BgMain.objects.order_by().values('businessterm').distinct()
    print(distinct_values)

    output = request.session.get('output')

    new_data = str(is_data_loaded).lower()

    context = {
        'distinct_values': distinct_values,
        'result': result,
        'ropa_dict': ropa_dict,
        'output': output,
        'new_data': new_data
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


        categoriespersonaldata_list = request.POST.getlist('categoriespersonaldata')
        print(categoriespersonaldata_list)
        categoriespersonaldata = ' , '.join([str(elem) for elem in categoriespersonaldata_list])
        categoriespersonaldata = categoriespersonaldata.upper()
        print(categoriespersonaldata)

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
        ropamainid = request.POST.get('ropamainid')


        # Id maapping with database then form updated data save to variables
        ropa_edit_db = RopaMain.objects.get(ropamainid=ropamainid)
        ropa_edit_db_filter = RopaMain.objects.filter(ropamainid=ropamainid)
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

        # user_detail = request.session['user_detail']
        # user_detail = UserDetails.objects.get(userid=current_user.id)
        user_detail = request.user.id
        ropa_id = RopaType.objects.get(userid=user_detail)
        print(ropa_id)
        ropa_id_dict = model_to_dict(ropa_id)
        print(ropa_id_dict)
        main_ropa_id = ropa_id_dict['ropaid']
        # ropa_type = RopaType()
        ropa_type = RopaType.objects.get(ropaid=main_ropa_id)
        # ropa_type = RopaType.objects.values('ropaid')
        ropa_type.save()

        # ropa_bgmain = BgMain()
        # ropa_bgmain.save()

        result = RopaMain.objects.all()
        print('result of edit ropa', result)
        ropa_main = pd.DataFrame(list(RopaMain.objects.all().values('ropamainid', 'ropaid', 'businessfunc', 'processingactivityname',
                                          'processingactivitydesc','categoriesdatasubjects', 'categoriespersonaldata', 'status',
                                          'controllername', 'categoriesofrecepients', 'lawfulbasisofprocessing', 'dataprocessor',
                                          'retentionschedule', 'linkcontractprocessor', 'countriesdetailstransferred',
                                          'safeguardsexternaltransfers', 'securitymeasures_desc', 'linkscontracts')))
        print('ropa_main in edit', ropa_main)
        # a=len(bg)
        ropa_dict = ropa_main.to_dict('records')
        print('ropa_dict in edit', ropa_dict)

        for i in ropa_dict:
            i.update({'create_timestamp': str(i.get('create_timestamp'))})
            i.update({'update_timestamp': str(i.get('update_timestamp'))})
            i.update({'comments': str(i.get('comments'))})
            i.update({'categoriesdatasubjects': str(i.get('categoriesdatasubjects'))})
            i.update({'processingactivityname': str(i.get('processingactivityname'))})

        distinct_values = BgMain.objects.order_by().values('businessterm').distinct()
        print(distinct_values)

        context = {
            'distinct_values': distinct_values,
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
    delete_db = RopaMain.objects.get(ropamainid=id_delete)
    print(delete_db)


    # updates data save to new dict
    delete_db.delete()

    result = RopaMain.objects.all()
    ropa_delete = pd.DataFrame(list(RopaMain.objects.all().values('ropamainid', 'ropaid', 'businessfunc', 'processingactivityname',
                                          'processingactivitydesc','categoriesdatasubjects', 'categoriespersonaldata', 'status',
                                          'controllername', 'categoriesofrecepients', 'lawfulbasisofprocessing', 'dataprocessor',
                                          'retentionschedule', 'linkcontractprocessor', 'countriesdetailstransferred',
                                          'safeguardsexternaltransfers', 'securitymeasures_desc', 'linkscontracts')))
    # a=len(bg)
    ropa_dict = ropa_delete.to_dict('records')

    for i in ropa_dict:

        i.update({'create_timestamp': str(i.get('create_timestamp'))})
        i.update({'update_timestamp': str(i.get('update_timestamp'))})
        i.update({'comments': str(i.get('comments'))})
        i.update({'categoriesdatasubjects': str(i.get('categoriesdatasubjects'))})
        i.update({'processingactivityname': str(i.get('processingactivityname'))})

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

def bfh_dashboard(request):
    return render(request, 'bfh_dashboard.html')


# @login_required
def workflow_dashboard(request):
    user1 = request.user
    print('user1:', user1)
    user_id = request.user.id
    print('user_id:', user_id)
    group1 = request.user.groups.all()
    print('group1:', group1)
    dahboard_df = pd.DataFrame(list(request.user.groups.all().values()))
    print(dahboard_df)
    print(dahboard_df['name'].to_string(index=False))
    result = dahboard_df['name'].to_string(index=False)
    output = request.session.get('output')
    if result == "Business Function Head":
        if request.method == 'POST':
            ropa_main = pd.DataFrame(
                list(RopaMain.objects.all().values('ropamainid', 'ropaid', 'businessfunc', 'processingactivityname',
                                                   'processingactivitydesc', 'categoriesdatasubjects',
                                                   'categoriespersonaldata',
                                                   'status', 'controllername', 'categoriesofrecepients',
                                                   'lawfulbasisofprocessing',
                                                   'dataprocessor', 'retentionschedule', 'linkcontractprocessor',
                                                   'countriesdetailstransferred',
                                                   'safeguardsexternaltransfers', 'securitymeasures_desc',
                                                   'linkscontracts', 'comments')))
            # a=len(bg)
            ropa_dict = ropa_main.to_dict('records')

            for i in ropa_dict:
                i.update({'create_timestamp': str(i.get('create_timestamp'))})
                i.update({'update_timestamp': str(i.get('update_timestamp'))})
                i.update({'comments': str(i.get('comments'))})
                i.update({'categoriesdatasubjects': str(i.get('categoriesdatasubjects'))})
                i.update({'processingactivityname': str(i.get('processingactivityname'))})

            if request.POST["act"] == "approve":
                bgid = request.POST.get('bgid')
                edit_bg_db = BgMain.objects.get(bgid=bgid)
                ropamainid = request.POST.get('ropamainid')
                edit_bg_db.status = 'Approved'
                edit_bg_db.comments = request.POST.get('comments')
                edit_bg_db.save()
                edit_ropa_db = RopaMain.objects.get(ropamainid=ropamainid)
                edit_ropa_db.status = 'Approved'
                edit_ropa_db.comments = request.POST.get('comments')
                edit_ropa_db.save()
            else:
                bgid = request.POST.get('bgid')
                edit_bg_db = BgMain.objects.get(bgid=bgid)
                ropamainid = request.POST.get('ropamainid')
                edit_bg_db.status = 'Rejected'
                edit_bg_db.comments = request.POST.get('comments')
                edit_bg_db.save()
                edit_ropa_db = RopaMain.objects.get(ropamainid=ropamainid)
                edit_ropa_db.status = 'Approved'
                edit_ropa_db.comments = request.POST.get('comments')
                edit_ropa_db.save()
        result = BgMain.objects.all()
        bg = pd.DataFrame(list(BgMain.objects.all().values()))
        # a=len(bg)
        bg_dict = bg.to_dict('records')

        result1 = RopaMain.objects.all()
        ropa_main = pd.DataFrame(
            list(RopaMain.objects.all().values('ropamainid', 'ropaid', 'businessfunc', 'processingactivityname',
                                               'processingactivitydesc', 'categoriesdatasubjects',
                                               'categoriespersonaldata',
                                               'status', 'controllername', 'categoriesofrecepients',
                                               'lawfulbasisofprocessing',
                                               'dataprocessor', 'retentionschedule', 'linkcontractprocessor',
                                               'countriesdetailstransferred',
                                               'safeguardsexternaltransfers', 'securitymeasures_desc', 'linkscontracts',
                                               'comments')))
        # a=len(bg)
        ropa_dict = ropa_main.to_dict('records')

        for i in bg_dict:
            i.update({'create_timestamp': str(i.get('create_timestamp'))})
            i.update({'update_timestamp': str(i.get('update_timestamp'))})
            i.update({'comments': str(i.get('comments'))})

        for i in ropa_dict:
            i.update({'create_timestamp': str(i.get('create_timestamp'))})
            i.update({'update_timestamp': str(i.get('update_timestamp'))})
            i.update({'comments': str(i.get('comments'))})

        # import ipdb
        # ipdb.set_trace()
        context = {
            'bga': result,
            'bg_dict': bg_dict,
            'result1': result1,
            'ropa_dict': ropa_dict,
            'output': output
        }
        return render(request, 'bfh_tab.html', context)
    elif result == "DPO":
        bg1 = pd.DataFrame(list(BgMain.objects.all().values()))
        # a=len(bg)
        bg = bg1.sort_values(by='update_timestamp', ascending=False)
        bg_dict = bg.to_dict('records')

        for i in bg_dict:
            i.update({'create_timestamp': str(i.get('create_timestamp'))})
            i.update({'update_timestamp': str(i.get('update_timestamp'))})
            i.update({'comments': str(i.get('comments'))})

        ropa_main1 = pd.DataFrame(
            list(RopaMain.objects.all().values('ropamainid', 'ropaid', 'businessfunc', 'processingactivityname',
                                               'processingactivitydesc', 'categoriesdatasubjects',
                                               'categoriespersonaldata',
                                               'status', 'controllername', 'categoriesofrecepients',
                                               'lawfulbasisofprocessing',
                                               'dataprocessor', 'retentionschedule', 'linkcontractprocessor',
                                               'countriesdetailstransferred',
                                               'safeguardsexternaltransfers', 'securitymeasures_desc', 'linkscontracts',
                                               'comments', 'update_timestamp')))
        # a=len(bg)
        ropa_main = ropa_main1.sort_values(by='update_timestamp', ascending=False)
        ropa_dict = ropa_main.to_dict('records')

        for i in ropa_dict:
            i.update({'create_timestamp': str(i.get('create_timestamp'))})
            i.update({'update_timestamp': str(i.get('update_timestamp'))})
            i.update({'comments': str(i.get('comments'))})

        context = {
            'bg_dict': bg_dict,
            'ropa_dict': ropa_dict,
            'output': output
        }
        return render(request, 'dpo_tab.html', context)
    elif result == "Data Steward":
        bg = pd.DataFrame(list(BgMain.objects.all().values()))
        # a=len(bg)
        bg_dict = bg.to_dict('records')

        for i in bg_dict:
            i.update({'create_timestamp': str(i.get('create_timestamp'))})
            i.update({'update_timestamp': str(i.get('update_timestamp'))})
            i.update({'comments': str(i.get('comments'))})

        ropa_main = pd.DataFrame(
            list(RopaMain.objects.all().values('ropamainid', 'ropaid', 'businessfunc', 'processingactivityname',
                                               'processingactivitydesc', 'categoriesdatasubjects',
                                               'categoriespersonaldata',
                                               'status', 'controllername', 'categoriesofrecepients',
                                               'lawfulbasisofprocessing',
                                               'dataprocessor', 'retentionschedule', 'linkcontractprocessor',
                                               'countriesdetailstransferred',
                                               'safeguardsexternaltransfers', 'securitymeasures_desc', 'linkscontracts',
                                               'comments')))
        # a=len(bg)
        ropa_dict = ropa_main.to_dict('records')

        for i in ropa_dict:
            i.update({'create_timestamp': str(i.get('create_timestamp'))})
            i.update({'update_timestamp': str(i.get('update_timestamp'))})
            i.update({'comments': str(i.get('comments'))})

        context = {
            'bg_dict': bg_dict,
            'ropa_dict': ropa_dict,
            'output': output
        }
        return render(request, 'data_steward_tab.html', context)
    else:
        return render(request, 'workflow_dashboard.html')
    return render(request, 'workflow_dashboard.html')


def workflow_business_glossary(request):
    if request.method == 'POST':
        if request.POST["act"] == "approve":
            # import ipdb
            # ipdb.set_trace()
            bgid = request.POST.get('bgid')
            edit_db = BgMain.objects.get(bgid=bgid)
            edit_db.status = 'Approved'
            edit_db.comments = request.POST.get('comments')
            edit_db.save()
        else:
            bgid = request.POST.get('bgid')
            edit_db = BgMain.objects.get(bgid=bgid)
            edit_db.status = 'Rejected'
            edit_db.comments = request.POST.get('comments')
            edit_db.save()
    result = BgMain.objects.all()
    bg = pd.DataFrame(list(BgMain.objects.all().values()))
    # a=len(bg)
    bg_dict = bg.to_dict('records')

    for i in bg_dict:
        i.update({'create_timestamp': str(i.get('create_timestamp'))})
        i.update({'update_timestamp': str(i.get('update_timestamp'))})
        i.update({'comments': str(i.get('comments'))})

    context = {
        'bga': result,
        'bg_dict': bg_dict
    }
    return render(request, 'bfh_tab.html', context)
    # return render(request, 'workflow_business_glossary.html')


def workflow_ropa(request):
    if request.method == 'POST':
        if request.POST["act"] == "approve":
            ropamainid = request.POST.get('ropamainid')
            edit_db = RopaMain.objects.get(ropamainid=ropamainid)
            edit_db.status = 'Approved'
            edit_db.comments = request.POST.get('comments')
            edit_db.save()
        else:
            ropamainid = request.POST.get('ropamainid')
            edit_db = RopaMain.objects.get(ropamainid=ropamainid)
            edit_db.status = 'Rejected'
            edit_db.comments = request.POST.get('comments')
            edit_db.save()
    result = RopaMain.objects.all()
    ropa_main = pd.DataFrame(list(RopaMain.objects.all().values('ropamainid', 'ropaid', 'businessfunc', 'processingactivityname',
                                           'processingactivitydesc', 'categoriesdatasubjects', 'categoriespersonaldata',
                                           'status', 'controllername', 'categoriesofrecepients', 'lawfulbasisofprocessing',
                                           'dataprocessor', 'retentionschedule', 'linkcontractprocessor', 'countriesdetailstransferred',
                                           'safeguardsexternaltransfers', 'securitymeasures_desc', 'linkscontracts', 'comments')))
    # a=len(bg)
    ropa_dict = ropa_main.to_dict('records')
    # ropa_dict.status = 'Approve'

    for i in ropa_dict:
        i.update({'create_timestamp': str(i.get('create_timestamp'))})
        i.update({'update_timestamp': str(i.get('update_timestamp'))})
        i.update({'comments': str(i.get('comments'))})

    context = {
        'result': result,
        'ropa_dict': ropa_dict
    }
    return render(request, 'workflow_ropa.html', context)


def workflow_dpo(request):
    bg = pd.DataFrame(list(BgMain.objects.all().values()))
    # a=len(bg)
    bg_dict = bg.to_dict('records')

    for i in bg_dict:
        i.update({'create_timestamp': str(i.get('create_timestamp'))})
        i.update({'update_timestamp': str(i.get('update_timestamp'))})
        i.update({'comments': str(i.get('comments'))})

    context = {
        'bg_dict': bg_dict
    }
    return render(request, 'workflow_dpo.html', context)


def dpo_dashboard(request):
    return render(request, 'dpo_dashboard.html')


def workflow_dpo_ropa(request):

    context = {
        'ropa_dict': ropa_dict
    }
    return render(request, 'workflow_dpo_ropa.html', context)


# @allowed_users(allowed_roles=['Business Function Head'])
# @group_required('Business Function Head')
def bfh_tab(request):
    if request.method == 'POST':
        ropa_main = pd.DataFrame(list(RopaMain.objects.all().values('ropamainid', 'ropaid', 'businessfunc', 'processingactivityname',
                                           'processingactivitydesc', 'categoriesdatasubjects', 'categoriespersonaldata',
                                           'status', 'controllername', 'categoriesofrecepients',
                                           'lawfulbasisofprocessing',
                                           'dataprocessor', 'retentionschedule', 'linkcontractprocessor',
                                           'countriesdetailstransferred',
                                           'safeguardsexternaltransfers', 'securitymeasures_desc', 'linkscontracts', 'comments')))
    # a=len(bg)
        ropa_dict = ropa_main.to_dict('records')

        for i in ropa_dict:
            i.update({'create_timestamp': str(i.get('create_timestamp'))})
            i.update({'update_timestamp': str(i.get('update_timestamp'))})
            i.update({'comments': str(i.get('comments'))})

        if request.POST["act"] == "approve":
            bgid = request.POST.get('bgid')
            edit_bg_db = BgMain.objects.get(bgid=bgid)
            ropamainid = request.POST.get('ropamainid')
            edit_bg_db.status = 'Approved'
            edit_bg_db.comments = request.POST.get('comments')
            edit_bg_db.save()
            edit_ropa_db = RopaMain.objects.get(ropamainid=ropamainid)
            edit_ropa_db.status = 'Approved'
            edit_ropa_db.comments = request.POST.get('comments')
            edit_ropa_db.save()
        else:
            bgid = request.POST.get('bgid')
            edit_bg_db = BgMain.objects.get(bgid=bgid)
            ropamainid = request.POST.get('ropamainid')
            edit_bg_db.status = 'Rejected'
            edit_bg_db.comments = request.POST.get('comments')
            edit_bg_db.save()
            edit_ropa_db = RopaMain.objects.get(ropamainid=ropamainid)
            edit_ropa_db.status = 'Approved'
            edit_ropa_db.comments = request.POST.get('comments')
            edit_ropa_db.save()
    result = BgMain.objects.all()
    bg = pd.DataFrame(list(BgMain.objects.all().values()))
    # a=len(bg)
    bg_dict = bg.to_dict('records')

    result1 = RopaMain.objects.all()
    ropa_main = pd.DataFrame(list(RopaMain.objects.all().values('ropamainid', 'ropaid', 'businessfunc', 'processingactivityname',
                                           'processingactivitydesc', 'categoriesdatasubjects', 'categoriespersonaldata',
                                           'status', 'controllername', 'categoriesofrecepients',
                                           'lawfulbasisofprocessing',
                                           'dataprocessor', 'retentionschedule', 'linkcontractprocessor',
                                           'countriesdetailstransferred',
                                           'safeguardsexternaltransfers', 'securitymeasures_desc', 'linkscontracts', 'comments')))
    # a=len(bg)
    ropa_dict = ropa_main.to_dict('records')

    for i in bg_dict:
        i.update({'create_timestamp': str(i.get('create_timestamp'))})
        i.update({'update_timestamp': str(i.get('update_timestamp'))})
        i.update({'comments': str(i.get('comments'))})

    for i in ropa_dict:
        i.update({'create_timestamp': str(i.get('create_timestamp'))})
        i.update({'update_timestamp': str(i.get('update_timestamp'))})
        i.update({'comments': str(i.get('comments'))})

    # import ipdb
    # ipdb.set_trace()
    context = {
        'bga': result,
        'bg_dict': bg_dict,
        'result1': result1,
        'ropa_dict': ropa_dict
    }
    return render(request,'bfh_tab.html', context)


# @allowed_users(allowed_roles=['DPO'])
def dpo_tab(request):
    bg = pd.DataFrame(list(BgMain.objects.all().values()))
    # a=len(bg)
    bg_dict = bg.to_dict('records')

    for i in bg_dict:
        i.update({'create_timestamp': str(i.get('create_timestamp'))})
        i.update({'update_timestamp': str(i.get('update_timestamp'))})
        i.update({'comments': str(i.get('comments'))})

    ropa_main = pd.DataFrame(list(RopaMain.objects.all().values('ropamainid', 'ropaid', 'businessfunc', 'processingactivityname',
                                           'processingactivitydesc', 'categoriesdatasubjects', 'categoriespersonaldata',
                                           'status', 'controllername', 'categoriesofrecepients',
                                           'lawfulbasisofprocessing',
                                           'dataprocessor', 'retentionschedule', 'linkcontractprocessor',
                                           'countriesdetailstransferred',
                                           'safeguardsexternaltransfers', 'securitymeasures_desc', 'linkscontracts','comments')))
    # a=len(bg)
    ropa_dict = ropa_main.to_dict('records')

    for i in ropa_dict:
        i.update({'create_timestamp': str(i.get('create_timestamp'))})
        i.update({'update_timestamp': str(i.get('update_timestamp'))})
        i.update({'comments': str(i.get('comments'))})

    context = {
        'bg_dict': bg_dict,
        'ropa_dict': ropa_dict
    }
    return render(request, 'dpo_tab.html', context)


# @allowed_users(allowed_roles=['Data Steward'])
def data_steward_tab(request):
    bg = pd.DataFrame(list(BgMain.objects.all().values()))
    # a=len(bg)
    bg_dict = bg.to_dict('records')

    for i in bg_dict:
        i.update({'create_timestamp': str(i.get('create_timestamp'))})
        i.update({'update_timestamp': str(i.get('update_timestamp'))})
        i.update({'comments': str(i.get('comments'))})

    ropa_main = pd.DataFrame(
        list(RopaMain.objects.all().values('ropamainid', 'ropaid', 'businessfunc', 'processingactivityname',
                                           'processingactivitydesc', 'categoriesdatasubjects', 'categoriespersonaldata',
                                           'status', 'controllername', 'categoriesofrecepients',
                                           'lawfulbasisofprocessing',
                                           'dataprocessor', 'retentionschedule', 'linkcontractprocessor',
                                           'countriesdetailstransferred',
                                           'safeguardsexternaltransfers', 'securitymeasures_desc', 'linkscontracts', 'comments')))
    # a=len(bg)
    ropa_dict = ropa_main.to_dict('records')

    for i in ropa_dict:
        i.update({'create_timestamp': str(i.get('create_timestamp'))})
        i.update({'update_timestamp': str(i.get('update_timestamp'))})
        i.update({'comments': str(i.get('comments'))})

    context = {
        'bg_dict': bg_dict,
        'ropa_dict': ropa_dict
    }
    return render(request, 'data_steward_tab.html', context)


def processor_dashboard(request):
    return render(request, 'processor_dashboard.html')


def admin_screen(request):
    result = RopaType.objects.all()
    ropaty = []
    name = []
    address = []
    email = []
    country_code = []
    telephone = []
    dpo_name = []
    dpo_address = []
    dpo_email = []
    dpo_country_code = []
    dpo_phone = []
    rep_name = []
    rep_address = []
    rep_email = []
    rep_country_code = []
    rep_phone = []

    # import ipdb
    # ipdb.set_trace()
    for i in result:

        ropaty.append(i.ropaty)
        name.append(i.name)
        address.append(i.address)
        email.append(i.email)
        country_code.append(i.country_code)
        telephone.append(i.telephone)
        dpo_name.append(i.dpo_name)
        dpo_address.append(i.dpo_address)
        dpo_email.append(i.dpo_email)
        dpo_country_code.append(i.dpo_country_code)
        dpo_phone.append(i.dpo_phone)
        rep_name.append(i.rep_name)
        rep_address.append(i.rep_address)
        rep_email.append(i.rep_email)
        rep_country_code.append(i.rep_country_code)
        rep_phone.append(i.rep_phone)

        # result = RopaType.objects.all()
        key_dict = {'ropaty': ropaty, 'name': name,'address':address, 'email':email, 'country_code': country_code, 'telephone':telephone,'dpo_name':dpo_name, 'dpo_address':dpo_address, 'dpo_email': dpo_email,'dpo_country_code': dpo_country_code, 'dpo_phone': dpo_phone, 'rep_name':rep_name,'rep_address': rep_address, 'rep_email': rep_email, 'rep_country_code': rep_country_code,'rep_phone': rep_phone}
        user_roll_mapping_df = pd.DataFrame(key_dict)
        user_roll_mapping_df.to_csv('Assessment/static/assets/user_roll_mapping_excel.csv', index=False)

    result1 = RopaMain.objects.all()
    ropa_main = pd.DataFrame(list(RopaMain.objects.all().values()))
    ropa_main.to_csv('Assessment/static/assets/record_register_excel.csv', index=False)

    result2 = BgMain.objects.all()
    bg = pd.DataFrame(list(BgMain.objects.all().values()))
    bg.to_csv('Assessment/static/assets/bs_glossary_excel (2).csv', index=False)

    result3 = BusinessFunction.objects.all()
    bu = pd.DataFrame(list(BusinessFunction.objects.all().values()))
    bu.to_csv('Assessment/static/assets/business_function_excel.csv', index=False)

    if request.method == 'POST':
        # BgMain_resource = BgMainResource()
        # dataset = Dataset()
        print('inside debugger')
        # import ipdb
        # ipdb.set_trace()
        new_BgMain = request.FILES['document']
        # imported_data = dataset.load(new_BgMain.read(),format='csv')
        try:
            imported_data = pd.read_csv(new_BgMain)
            print(imported_data)
            # df = list(imported_data.columns)
            # print(df)
            # ideal_list=['businessterm','definition','dataattribute','system','datadomain','lineofbusiness','status','dataclassification','createdby']
            #
            # if df==ideal_list:
            #     print('matched')
            # else:
            #     return render(request, 'error_data.html')


        except:
            print('error due to incorrect format')
            return render(request, 'error_data.html')

        count = 0
        for i in range(len(imported_data)):
            try:
                a = BgMain.objects.bulk_create([
                    BgMain(businessterm=imported_data["businessterm"][count],
                           definition=imported_data["definition"][count],
                           dataattribute=imported_data["dataattribute"][count],
                           system=imported_data["system"][count],
                           datadomain=imported_data["datadomain"][count],
                           lineofbusiness=imported_data["lineofbusiness"][count],
                           status=imported_data["status"][count],
                           dataclassification=imported_data["dataclassification"][count],
                           createdby=imported_data["createdby"][count],
                           )])
                print(a)
                count += 1
            except:

                return render(request, 'error_data.html')

        if a is not None:
            print('Success', a)
            success = '1'
        else:
            print('Failure', a)

        print('success', success)

        output = request.session.get('output')
        context = {
            'success': success,
            'result': result,
            'result1': result1,
            'result2': result2,
            'result3': result3,
            'output': output
        }
        return render(request, 'upload_screen.html', context)
    return render(request, 'admin_screen.html')


def map_role(request):
    if request.method == 'POST':
        # BgMain_resource = BgMainResource()
        # dataset = Dataset()
        print('inside debugger')
        # import ipdb
        # ipdb.set_trace()
        new_RopaType = request.FILES['document']
        # imported_data = dataset.load(new_BgMain.read(),format='csv')
        imported_data = pd.read_csv(new_RopaType)
        print(imported_data)

        count = 0
        for i in range(len(imported_data)):
            a = RopaType.objects.bulk_create([
                RopaType(ropaty=imported_data["ropaty"][count],
                         name=imported_data["name"][count],
                         address=imported_data["address"][count],
                         email=imported_data["email"][count],
                         country_code=imported_data["country_code"][count],
                         telephone=imported_data["telephone"][count],
                         dpo_name=imported_data["dpo_name"][count],
                         dpo_address=imported_data["dpo_address"][count],
                         dpo_email=imported_data["dpo_email"][count],
                         dpo_country_code=imported_data["dpo_country_code"][count],
                         dpo_phone=imported_data["dpo_phone"][count],
                         rep_name=imported_data["rep_name"][count],
                         rep_address=imported_data["rep_address"][count],
                         rep_email=imported_data["rep_email"][count],
                         rep_country_code=imported_data["rep_country_code"][count],
                         rep_phone=imported_data["rep_phone"][count],

                         )
            ])
            print(a)
            count += 1

        if a is not None:
            print('Success', a)
            success = '1'
        else:
            print('Failure', a)

        print('success', success)

        context = {
            'success': success,
        }
        return render(request, 'upload_screen.html', context)
    return render(request, 'map_role.html')


def bfunction(request):
    bfunc = pd.DataFrame(list(BusinessFunction.objects.all().values()))
    bfunc_dict = bfunc.to_dict('records')
    context = {

        'bfunc_dict': bfunc_dict
    }

    if request.method == 'POST':
        # BgMain_resource = BgMainResource()
        # dataset = Dataset()
        print('inside debugger bfunction')
        bfunc = pd.DataFrame(list(BusinessFunction.objects.all().values()))
        bfunc_dict = bfunc.to_dict('records')
        print("bfunc", bfunc)
        print("bfunc_dict", bfunc_dict)
        new_BusinessFunction = request.FILES['document']
        imported_data = pd.read_csv(new_BusinessFunction)
        print(imported_data)
        count = 0
        for i in range(len(imported_data)):
            a = BusinessFunction.objects.bulk_create([
                BusinessFunction(
                    organization=imported_data["organization"][count],
                    businessfunc=imported_data["businessfunc"][count],
                    description=imported_data["description"][count])])
            print(a)
            count += 1



        if a is not None:
            print('Success', a)
            success = '1'
        else:
            print('Failure', a)

        print('success', success)

        context = {
            'success': success,
            'bfunc_dict': bfunc_dict
        }

        return render(request, 'function.html', context)
    return render(request, 'bfunction.html',context)


def up_screen(request):
    if request.method == 'POST':
        # import ipdb
        # ipdb.set_trace()
        print('inside debugger')

        new_RopaMain = request.FILES['document']
        # imported_data = dataset.load(new_BgMain.read(),format='csv')
        try:
            imported_data = pd.read_csv(new_RopaMain)
            print(imported_data)

        except:
            print('error due to incorrect format')
            return render(request, 'error_data.html')

        count = 0
        for i in range(len(imported_data)):
            try:
                a = RopaMain.objects.bulk_create([
                    RopaMain(
                             ropaty=imported_data["ropaty"][count],
                             businessfunc=imported_data["businessfunc"][count],
                             processingactivityname=imported_data["processingactivityname"][count],
                             processingactivitydesc=imported_data["processingactivitydesc"][count],
                             categoriesdatasubjects=imported_data["categoriesdatasubjects"][count],
                             categoriespersonaldata=imported_data["categoriespersonaldata"][count],
                             controllername=imported_data["controllername"][count],
                             categoriesofrecepients=imported_data["categoriesofrecepients"][count],
                             lawfulbasisofprocessing=imported_data["lawfulbasisofprocessing"][count],
                             retentionschedule=imported_data["retentionschedule"][count],
                             dataprocessor=imported_data["dataprocessor"][count],
                             countriesdetailstransferred=imported_data["countriesdetailstransferred"][count],
                             securitymeasures_desc=imported_data["securitymeasures_desc"][count],
                             status=imported_data["status"][count])])
                print(a)
                count += 1

            except:
                return render(request, 'error_data.html')

        if a is not None:
            print('record_success', a)
            record_success = '1'
        else:
            print('Failure', a)

        print('record_success', record_success)

        context = {
            'record_success': record_success,

        }
        return render(request, 'admin_screen_upload.html', context)
    return render(request, 'admin_screen.html')


def error_data(request):
    return render(request, 'error_data.html')


def map_role(request):
    cursor = connection.cursor()
    print('sp_admin_map_roles_edit')
    try:
        cursor.execute('EXEC sp_admin_map_roles')
        result_set = cursor.fetchall()

        context = {
            'admin_dict': result_set,
        }
        return render(request, 'map_role.html', context)

    finally:
        cursor.close()


def map_role_upload(request):
    print('map_role_upload')
    cursor1 = connection.cursor()
    try:
        cursor1.execute('EXEC sp_admin_map_roles')
        result_set1 = cursor1.fetchall()
        context1 = {
            'admin_dict': result_set1,
        }

        if request.method == 'POST':

            print('inside map_role_upload')
            # import ipdb
            # ipdb.set_trace()
            uploaded_data = request.FILES['document']
            df = pd.read_csv(uploaded_data)
            print(df)
            for temp in df.index:
                print(df['username'][temp], df['roles'][temp], df['email'][temp], df['password'][temp])
                user_final = User.objects.create_user(username=df['username'][temp],
                                                email=df['email'][temp],
                                                password=df['password'][temp])
                print('user :', user_final)

                group_final = df['roles'][temp]
                # import ipdb
                # ipdb.set_trace()

                my_group = Group.objects.get(name=group_final)
                print(my_group)
                my_group.user_set.add(user_final)

                # user_final.groups.add(group_final)
                cursor = connection.cursor()
            try:
                cursor.execute('EXEC sp_admin_map_roles')
                result_set = cursor.fetchall()

                print(result_set)

                context = {
                     'admin_dict': result_set,
                    }
                return render(request, 'map_role.html', context)

            finally:
                cursor.close()

        return render(request, 'map_role.html', context1)

    finally:
        cursor1.close()


def map_role_edit(request):
    # from django.contrib.auth.models import User, Group
    #
    # # retrieve the user
    # user = User.objects.get(username='user_name')
    #
    # # retrieve the group
    # group = Group.objects.get(name='group_name')
    #
    # # add the user to the group
    # user.groups.add(group)
    #
    # # save the changes
    # user.save()
    cursor = connection.cursor()

    if request.method == 'POST':

        roles = request.POST.getlist('roles')
        print(roles)
        roles_df=pd.DataFrame(roles)

        print('sp_admin_map_roles_edit')
        try:
            cursor.execute('EXEC sp_admin_map_roles')
            result_set = cursor.fetchall()

            print(result_set)
            df = pd.DataFrame(result_set)
            print(df[0])

            df[4]=roles_df
            print(df)

            for index, x in df.iterrows():
                # import ipdb
                # ipdb.set_trace()

                # retrieve the user
                user = User.objects.get(username=df[0][index])
                # print(user)

                old_group = Group.objects.get(user=user.id)
                # print('old_group =',old_group)

                user_final = User.objects.get(id=df[5][index])
                # print('user_final=',user_final)
                group_final = Group.objects.get(id=df[4][index])
                # print('group_final =',group_final)




                if old_group != group_final:
                    user_final.groups.remove(old_group)

                    user_final.groups.add(group_final)




                # group.user_set.remove(user)
                # group.user_set.add(user)
                # add the user to the group
                # user.groups.add(group)
                # save the changes


            cursor.execute('EXEC sp_admin_map_roles')
            final_result = cursor.fetchall()
            context = {
                'admin_dict': final_result,
            }
            return render(request, 'map_role.html',context)

        finally:
            cursor.close()


def user_details(request):
    print('inside user details page')
    user_id = request.user.id
    # group = Group.objects.get(id=user_id)
    # print('group', group)
    user_detail = pd.DataFrame(list(RopaType.objects.all().values().filter(userid=user_id)))
    user_dict = user_detail.to_dict('records')[0]
    print('user_dict', user_dict)
    output = request.session['output']
    context = {
        'user_dict': user_dict,
        'output': output
    }
    return render(request, 'user_details.html', context)


def action_history(request):
    # import ipdb
    # ipdb.set_trace()
    bg_audit = pd.DataFrame(list(BgAudit.objects.all().values('auditaction', 'auditdate', 'audituser','businessterm','bgid')))
    # a=len(bg)
    bg_audit_dict = bg_audit.to_dict('records')


    ropa_audit = pd.DataFrame(list(RopaAudit.objects.all().values('auditaction', 'auditdate', 'audituser','businessfunc','ropaid')))
    # a=len(bg)
    ropa_audit_dict = ropa_audit.to_dict('records')


    output = request.session['output']

    context={
        'bg_audit_dict': bg_audit_dict,
        'ropa_audit_dict':ropa_audit_dict,
        'output': output
    }

    return render(request, 'action_history.html', context)


def function(request):
    bfunc = pd.DataFrame(list(BusinessFunction.objects.all().values()))
    bfunc_dict = bfunc.to_dict('records')
    context = {

        'bfunc_dict': bfunc_dict
    }

    if request.method == 'POST':
        # BgMain_resource = BgMainResource()
        # dataset = Dataset()
        print('inside debugger bfunction')
        bfunc = pd.DataFrame(list(BusinessFunction.objects.all().values()))
        bfunc_dict = bfunc.to_dict('records')
        print("bfunc", bfunc)
        print("bfunc_dict", bfunc_dict)
        new_BusinessFunction = request.FILES['document']
        imported_data = pd.read_csv(new_BusinessFunction)
        print(imported_data)
        count = 0
        for i in range(len(imported_data)):
            a = BusinessFunction.objects.bulk_create([
                BusinessFunction(
                    organization=imported_data["organization"][count],
                    businessfunc=imported_data["businessfunc"][count],
                    description=imported_data["description"][count])])
            print(a)
            count += 1

        if a is not None:
            print('Success', a)
            success = '1'
        else:
            print('Failure', a)

        print('success', success)

        context = {
            'success': success,
            'bfunc_dict': bfunc_dict
        }
    return render(request, 'function.html',context)


def admin_screen_upload(request):
    return render(request, 'admin_screen_upload.html')