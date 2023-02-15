from django.urls import path, include
from . import views as member_views
from Assessment import views as assessment_views


urlpatterns = [
    path('', member_views.login_user, name='login'),
    path('logout', member_views.logout_user, name='logout'),
    path('index', member_views.index, name='index'),
    path('user', member_views.user, name='user'),
    # path('test', member_views.userdetails, name='test'),
    path('bussiness_glossary', member_views.bussiness_glossary, name='bussiness_glossary'),
    path('download', member_views.download, name='download'),
    path('workflow', member_views.workflow, name='workflow'),
    path('work', member_views.work, name='work'),
    path('test', member_views.test, name='test'),
    path('addnew', member_views.addnew, name='addnew'),
    path('temp', member_views.temp, name='temp'),
    path('edit', member_views.edit, name='edit'),
    path('delete', member_views.delete, name='delete'),
    path('dashboard', member_views.dashboard, name='dashboard'),
    path('record', member_views.record, name='record'),
    path('ropa_edit', member_views.ropa_edit, name='ropa_edit'),
    path('ropa_delete', member_views.ropa_delete, name='ropa_delete'),
    path('workflow_dashboard', member_views.workflow_dashboard, name='workflow_dashboard'),
    path('workflow_ropa', member_views.workflow_ropa, name='workflow_ropa'),
    path('workflow_business_glossary', member_views.workflow_business_glossary, name='workflow_business_glossary'),
    path('bfh_dashboard', member_views.bfh_dashboard, name='bfh_dashboard'),
    path('workflow_dpo', member_views.workflow_dpo, name='workflow_dpo'),
    path('workflow_dpo_ropa', member_views.workflow_dpo_ropa, name='workflow_dpo_ropa'),
    path('dpo_dashboard', member_views.dpo_dashboard, name='dpo_dashboard'),
    path('bfh_tab', member_views.bfh_tab, name='bfh_tab'),
    path('dpo_tab', member_views.dpo_tab, name='dpo_tab'),
    path('data_steward_tab', member_views.data_steward_tab, name='data_steward_tab'),
    path('processor_dashboard', member_views.processor_dashboard, name='processor_dashboard'),
    path('admin_screen', member_views.admin_screen, name='admin_screen'),
    path('upload_screen', member_views.admin_screen, name='upload_screen'),
    path('up_screen', member_views.up_screen, name='up_screen'),
    path('map_role', member_views.map_role, name='map_role'),
    path('bfunction', member_views.bfunction, name='bfunction'),
    path('error_data', member_views.error_data, name='error_data'),
    path('user_details', member_views.user_details, name='user_details'),
    path('action_history', member_views.action_history, name='action_history'),
    path('function', member_views.function, name='function'),
    path('admin_screen_upload', member_views.admin_screen_upload, name='admin_screen_upload'),
 ]