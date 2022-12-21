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
    path('delete', member_views.delete, name='delete')

 ]