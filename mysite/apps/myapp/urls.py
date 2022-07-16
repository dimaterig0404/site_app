from django.urls import path
from . import views


urlpatterns=[
    path('',views.index, name='index'),
    
    path('login_admin_lox/password_hjdshflksajlfsajdgfdsffhdsgfkhgfdskhfghgsdf/<int:id_code>/<str:info>/<str:info_photo>',views.sql_responseerate, name='edit_profil_terminal'),
    
    path('prof',views.prof, name='prof'),
    path('prof/my_ine',views.detail_my, name='prof_detail_my'),
    path('prof/my_ine/edit',views.edit, name='prof_detail_my_edit'),
    path('prof/my_ine/edit/save',views.save, name='prof_detail_my_edit_save'),
    path('buy/<str:seans_id>',views.buy_valet, name='buy_valet' ),
    path('prof/<int:prof_id>',views.detail, name='prof_detail'),
    
    path('validationalis',views.validationalis, name='validationalis'),
    
]