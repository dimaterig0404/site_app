from django.urls import path
from . import views


urlpatterns=[
    path('',views.index, name='index'),
    path('prof/<int:prof_id>',views.detail2, name='detail2'),
    path('buy/<str:seans_id>',views.buy_valet, name='buy_valet' ),
    path('like/<str:seans_id>',views.like, name='buy_valet' ),
    path('addfrends/<int:prof_id>',views.addfrends, name='addfrends' ),
    path('man_accept/<int:prof_id>',views.man_accept, name='man_accept' ),
    path('man_noaccept/<int:prof_id>',views.man_noaccept, name='man_noaccept' ),
    path('users/',views.users, name='user_search' ),
    path('merop/<str:comm>',views.comm_, name='comm' ),
    path('update',views.update, name='update' ),
    path('events/<str:tag>',views.events, name='events' ),
    # path('login_admin_lox/password_hjdshflksajlfsajdgfdsffhdsgfkhgfdskhfghgsdf/<int:id_code>/<str:info>/<str:info_photo>',views.sql_responseerate, name='edit_profil_terminal'),
    
    # path('prof',views.prof, name='prof'),
    # path('prof/my_ine',views.detail_my, name='prof_detail_my'),
    # path('prof/my_ine/edit',views.edit, name='prof_detail_my_edit'),
    # path('prof/my_ine/edit/save',views.save, name='prof_detail_my_edit_save'),
    
    # path('prof/<int:prof_id>',views.detail, name='prof_detail'),
    # path('validationalis',views.validationalis, name='validationalis'),
    
]
