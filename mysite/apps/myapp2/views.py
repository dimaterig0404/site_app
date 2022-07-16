import re
from collections import Counter
import random
from this import s
import cv2
import face_recognition
from turtle import pen
from django.shortcuts import render
from .models import II,USER,SEANS,DATA_ALL_SEANSES,Tegs
from django.http import Http404
from validate_email import validate_email
from .forms import UploadFileForm
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .infos import *
import numpy as np
from PIL import Image
import hashlib

grade_list = grade_list_()
grade_list_city = grade_list_city_()
grade_list_pol = grade_list_pol_()


def seans_all():
    seans = DATA_ALL_SEANSES.objects.all()
    for x in seans:
        x.class_seans_name = grade_list[x.class_seans-1][1]
    return seans

def delete_None(mas):
    new_words = []
    for i in mas:
        if i != "":
            new_words.append(i)
    return new_words

def password_create(sours):
    
    h = hashlib.sha1(f"{sours}".encode('utf-8'))
    h.digest()
    return h.hexdigest()
      
def checher(email,password):
    user_all_data = [f'{el.email}|{el.password}' for el in USER.objects.all()]
    print(password_create(password) )
    if email+"|"+password_create(password) in user_all_data:
        return [True,user_all_data.index(email+"|"+password_create(password))]
    else:
        return [False,'-']

def make_po_foto_code(img_str):
    
    img_str.seek(0)
    img_array = np.asarray(bytearray(img_str.read()), dtype=np.uint8)
    
    image = cv2.imdecode(img_array, 0) 
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    boxes = face_recognition.face_locations(rgb, model='hog')
    encodings = face_recognition.face_encodings(rgb, boxes)
    knownEncodings = []
    for encoding in encodings:
        knownEncodings.append(encoding)
    print('&'.join([str(x) for x in knownEncodings[0]]))
    return '&'.join([str(x) for x in knownEncodings[0]])




def index(request):
    seans_all_def = seans_all()
    if request.META['PATH_INFO'] == '/':
        
        MINE =  request.COOKIES.get('user','').split('/') 
        print(MINE)  
        if MINE != [''] or len(MINE)>1:
            info = checher(MINE[0],MINE[1])
            if info[0]:
                user = USER.objects.all()[info[1]]
                seans = SEANS.objects.all()[info[1]]
                like_cat = [x.class_seans for x in user.likes.all() ] + [x.class_seans for x in seans.seanses.all() ]
                user.loock_like = max(Counter(like_cat).items() ,key=lambda i : i[1],default=str(user.loock_like))[0]
                user.save()
                
                old = seans_all_def
                new = []
                for i in old.reverse():
                    print(grade_list[0])
                    
                    print(user.loock_like)
                    if i.class_seans == user.loock_like:
                        new.insert(0,i)
                    else:
                        new.append(i)
                for x in new:
                    x.class_seans_name = grade_list[x.class_seans-1][1]
        else:
            print('Eror')
            return render(request,'ProDos/index.html',{'seanses':seans_all_def})
        
        # Поработать с фото лица
        # Красивые ошибки 
        # Супер стараница 404 
        for x in new:
            x.class_seans_name = grade_list[x.class_seans-1][1]
        
        return render(request,'ProDos/index.html',{'seanses':new})
    
    elif request.META['PATH_INFO'] == '/eror404/':
        return render(request,'ProDos/eror404.html')
    
    elif request.META['PATH_INFO'] == '/merop/':
        MINE =  request.COOKIES.get('user','').split('/') 
        print(MINE)  
        if MINE != [''] or len(MINE)>1:
            info = checher(MINE[0],MINE[1])
            if info[0]:
                user = USER.objects.all()[info[1]]
                seans = SEANS.objects.all()[info[1]]
                
                
                
                
                
                
                
                
                
                
                
                # Тут обработка категорий
                # like_cat = [int(x) for x in user.likes.split(',') if x] + [int(x.split('!')[-1]) for x in seans.seanses.split('|') if x] 
                like_cat = [x.class_seans for x in user.likes.all() ] + [x.class_seans for x in seans.seanses.all() ]
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                user.loock_like = max(Counter(like_cat).items() ,key=lambda i : i[1],default=str(user.loock_like))[0]
                user.save()
                
                old = seans_all_def
                new = []
                for i in old.reverse():
                    print(grade_list[0])
                    
                    print(user.loock_like)
                    if i.class_seans == user.loock_like:
                        new.insert(0,i)
                    else:
                        new.append(i)
                for x in new:
                    x.class_seans_name = grade_list[x.class_seans-1][1]
        else:
            print('Eror')
            num = len(seans_all_def)//10 if  len(seans_all_def) >= 10 else 1 
            return render(request,'ProDos/merop_all.html',{'seanses':seans_all_def,'range':range(num),'catt_all':grade_list,'tegs':Tegs.objects.all(),'name_main':'Все мероприятия'})
        num = len(new)//10 if  len(new) >= 10 else 1
        
        return render(request,'ProDos/merop_all.html',{'seanses':new,'range':range(num),'catt_all':grade_list,'tegs':Tegs.objects.all(),'name_main':'Все мероприятия'})
    
    elif request.META['PATH_INFO'] == '/logout/':
        return render(request,'ProDos/logout.html')
    
    elif request.META['PATH_INFO'] == '/prof/my_ine/edit':
        
        MINE =  request.COOKIES.get('user','').split('/')   
        idis = int(MINE[2])
        
        try:

            uaser = USER.objects.all()[idis]
            ii = II.objects.all()[idis]
            try:
                seans = SEANS.objects.all()[idis]
            except:
                seans = []
        except:
            raise Http404('Тут нет ничего ')
        

        USER_SOURS = str(uaser).split('/')
        

        if password_create(MINE[1]) == USER_SOURS[2] and MINE[0] == USER_SOURS[1]:
            isMine = True
        else:
            isMine = False
        list_seans =[]
        if seans != []:
            list_seans = [x.split('!') for x in list(filter(None, str(seans.seanses).split('|')))]
        
            
        
        return render(request,'profile/edit.html',{'uaser':uaser,'ii':ii,'seans':seans,'isMine':isMine,'id':idis,'list_seans':list_seans})
    
    elif request.META['PATH_INFO'] == '/prof/my_ine/edit/save':
        MINE =  request.COOKIES.get('red','').split('/')  
        MINE_user =  request.COOKIES.get('user','').split('/')  
        idis = int(MINE[-1])
        
        try:

            uaser = USER.objects.all()[idis]
            ii = II.objects.all()[idis]
            try:
                seans = SEANS.objects.all()[idis]
            except:
                seans = []
        except:
            raise Http404('Тут нет ничего ')
        

        USER_SOURS = str(uaser).split('/')
        

        if password_create(MINE_user[1]) == USER_SOURS[2] and MINE_user[0] == USER_SOURS[1]:
            print(MINE)
            name = MINE[0] if MINE[0] != uaser.login else uaser.login
            sopose = MINE[1] if len(MINE[1]) >= 2 else uaser.sopose
            email = MINE[2] if MINE[2] != uaser.email else uaser.email
            
            password = password_create(MINE[3]) if len(MINE[3]) > 3 else uaser.password
            password_clear = MINE[3] if len(MINE[3]) > 3  else MINE_user[1]
            
            
            tipe_new =  False if MINE[4]=='0' else True if MINE[4] == '0' or MINE[4] == '1' else uaser.isGreen
            
        
            
            
            
            
            word = list('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')
            
            code_Face_id = str(random.randint(100000000,99999999999)) if  not ii.code.isdigit() else ii.code
            code_Phone_id = ''.join(random.sample(word, len(word))[:11]) if  ii.code.isdigit() else ii.code
            finish_tip = code_Face_id if tipe_new else code_Phone_id
            
            print(name,sopose,email,finish_tip,password,password_clear)
            uaser.login = name
            uaser.email = email
            uaser.sopose = sopose
            uaser.password = password
            uaser.isGreen = tipe_new
            ii.code = finish_tip
            uaser.save()
            ii.save()
            
            return render(request,'profile/save.html',{'email':email,'pass':password_clear,'id':idis})
        
    elif request.META['PATH_INFO'] == '/login/':
        if request.GET != {}:
            
            if validate_email(request.GET["email"]) and len(request.GET['password']) >=8:
                print('AC')
                ans = checher(request.GET['email'],request.GET['password'])
                if ans[0]:
                    print(request.GET['email']+'/'+request.GET['password']+'/'+str(ans[1]))
                    print(request.COOKIES) 
                    return render(request,'ProDos/setCoke.html',{'name':'user','cok':request.GET['email']+'/'+request.GET['password']+'/'+str(ans[1])})
            else:
                print('EROR')
              
        return render(request,'ProDos/login.html')
    
    elif request.META['PATH_INFO'] == '/reg/':
        print(request.GET)
        user = USER()
        ii = II(id_user=user)
        seans = SEANS(id_user=user)
        if request.method == 'POST':
            if 'face' in request.FILES:
                print(request.FILES)
                file = request.FILES['face']
                print(file)
                info = make_po_foto_code(file)
                
                
                
                ii.info_photo = info
                ii.code = str(random.randint(100000000,99999999999)) 
            if 'ico' in request.FILES:
                print(request.FILES)
                ico = request.FILES['ico']
                
                
                user.ico = ico
        
        if request.GET!={}:
            
            form = UploadFileForm(request.GET, request.FILES)
            print(form.is_valid())
            
            name = request.GET['name']
            if name == '':
                print(1)
                return render(request,'ProDos/register.html',{'eror':"Name",'grade_list_city':grade_list_city})
            
            category = request.GET['category']
            
            age = -1 if not request.GET['age'].isdigit() else int(request.GET['age'])
            if age<=0 or age>= 125 or age == '':
                print(2)
                return render(request,'ProDos/register.html',{'eror':"age",'grade_list_city':grade_list_city})
            
            email = request.GET['email']
            if not validate_email(email):
                print(3)
                return render(request,'ProDos/register.html',{'eror':"age",'grade_list_city':grade_list_city})
            
            password = request.GET['password']
            confirmPassword = request.GET['confirmPassword']
            
            if len(password) < 8 or len(confirmPassword) < 8 :
                return render(request,'ProDos/register.html',{'eror':"<8",'grade_list_city':grade_list_city})
            elif password != confirmPassword:
                return render(request,'ProDos/register.html',{'eror':"!=",'grade_list_city':grade_list_city})
            
            print('0k')
 
            user.login = name
            user.city = request.GET['city']
            user.pol = request.GET['pol']
            user.password = password_create(password)
            user.age = age
            user.email=email
            user.isGreen = True if category == '2' else False
            if age<18:
                user.sopose = '18'
            
            
            print(request.FILES=={})
            
            if category == '2' and not request.method == 'POST':
                return render(request,'ProDos/register2.html',{'category':category})
            elif category == '1' and request.FILES == {}:
                return render(request,'ProDos/register2.html',{'category':category})
            
            elif category == '1':
                code_Phone_id = ''.join(random.sample(list('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'), 52))[:11] 
                ii.code = code_Phone_id

            if not checher(email,password)[0]:
                print('save')
                seans.seanses = ''
                print(user.ico)
                user.save()
                ii.save()
                seans.save()
                
            return HttpResponseRedirect('../login')
        
        
             
        return render(request,'ProDos/register.html',{'grade_list_city':grade_list_city})
    
    

    
    elif request.META['PATH_INFO'] == '/prof/my_ine':
        MINE =  request.COOKIES.get('user','').split('/')   
        
        
        try:
            idis = int(MINE[2])
            uaser = USER.objects.all()[idis]
            ii = II.objects.all()[idis]
            try:
                seans = SEANS.objects.all()[idis]
            except:
                seans = []
        except:
            return HttpResponseRedirect('../')
        mass_users = [x for x in USER.objects.all()]
        frends = uaser.list_frends.all()
        frends_new = uaser.list_req_frends.all()
        for x in frends:
            x.ids = mass_users.index(x)
        for x in frends_new:
            x.ids = mass_users.index(x)
        USER_SOURS = str(uaser).split('/')
        if password_create(MINE[1]) == USER_SOURS[2] and MINE[0] == USER_SOURS[1]:
            isMine = True
            myFrend = False
        else:
            isMine = False
            myFrend = False
            print(myFrend)
        list_seans =[]
        if seans != []:
            list_seans = [x.split('!') for x in list(filter(None, str(seans.seanses).split('|')))]

          
        
        user = [el for i,el in enumerate(USER.objects.all()) if i in  [1,7,8,9]]
        for i,el in enumerate(user):
            el.ids = [1,7,8,9][i]
            

       
        return render(request,'profile/profile.html',{'uaser':uaser,'ii':ii,'seans':seans,'isMine':isMine,'id':idis,'list_seans':list_seans,'frends_new':frends_new,'frends':frends,'prof_id':idis,'myFrend':myFrend,'frends_temp_nado_del_eto_kastil':user,'all_seans':DATA_ALL_SEANSES.objects.all()})

    else:
        return HttpResponseRedirect('../eror404')
    
    
def detail2(request,prof_id):
    try:
        uaser = USER.objects.all()[prof_id]
        ii = II.objects.all()[prof_id]
        try:
            seans = SEANS.objects.all()[prof_id]
        except:
            seans = []
    except:
        raise Http404('Тут нет ничего ')
    

    USER_SOURS = str(uaser).split('/')
    MINE =  request.COOKIES.get('user','').split('/')    
    list_seans = []
    if seans != []:
        list_seans = [x.split('!') for x in list(filter(None, str(seans.seanses).split('|')))]
    isMine = False
    mass_users = [x for x in USER.objects.all()]
    frends = uaser.list_frends.all()
    frends_new = uaser.list_req_frends.all()
    for x in frends:
        x.ids = mass_users.index(x)
    for x in frends_new:
        x.ids = mass_users.index(x)
                
    myFrend = False
    if MINE!=['']:
        
        myFrend = True if USER.objects.all()[checher(MINE[0],MINE[1])[1]] in [x for x in frends] else False
        
        if password_create(MINE[1]) == USER_SOURS[2] and MINE[0] == USER_SOURS[1]:
            isMine = True
            idis = MINE[2]
            myFrend = False
            user = [el for i,el in enumerate(USER.objects.all()) if i in  [1,7,8,9]]
            for i,el in enumerate(user):
                el.ids = [1,7,8,9][i]
            
            return render(request,'profile/profile.html',{'uaser':uaser,'ii':ii,'seans':seans,'isMine':isMine,'id':idis,'list_seans':list_seans,'prof_id':prof_id,'frends':frends,'frends_new':frends_new,'myFrend':myFrend,'frends_temp_nado_del_eto_kastil':user})
    
    # user = [el for i,el in enumerate(USER.objects.all()) if i in  [1,7,8,9]]
    # for i,el in enumerate(user):
    #     el.ids = [1,7,8,9][i]
    return render(request,'profile/profile.html',{'uaser':uaser,'ii':ii,'seans':seans,'isMine':isMine,'list_seans':list_seans,'prof_id':prof_id,'frends':frends,'frends_new':frends_new,'myFrend':myFrend })

def addfrends(request,prof_id):
    
    MINE =  request.COOKIES.get('user','').split('/')
    if len(MINE)>1:
        info = checher(MINE[0],MINE[1])
        user_at = USER.objects.all()[info[1]]
        user_to = USER.objects.all()[prof_id]
        user_to.list_req_frends.add(user_at)
        user_to.save()
        return HttpResponseRedirect('../prof/'+str(prof_id))
    else:
        return HttpResponseRedirect('../login/')

def man_accept(request,prof_id):
    
    MINE =  request.COOKIES.get('user','').split('/') 
    info = checher(MINE[0],MINE[1])
    user_send = USER.objects.all()[prof_id]
    user_to = USER.objects.all()[info[1]]
    if user_send in user_to.list_req_frends.all():
        user_to.list_req_frends.remove(user_send)
        user_to.list_frends.add(user_send)
        user_to.save()
               
    return HttpResponseRedirect('../prof/my_ine')

def man_noaccept(request,prof_id):
    MINE =  request.COOKIES.get('user','').split('/') 
    info = checher(MINE[0],MINE[1])
    user_send = USER.objects.all()[prof_id]
    user_to = USER.objects.all()[info[1]]
    
    user_to.list_req_frends.remove(user_send)
    
    user_to.save()
    return HttpResponseRedirect('../prof/my_ine')


# СУУУУКА ManyToMAny ТОП

def buy_valet (request,seans_id):
    
    try:
        
        MINE_user =  request.COOKIES.get('user','').split('/')  
        idis = int(MINE_user[-1])
        
        

        ii = II.objects.all()[idis]
        
        try:
            seans = SEANS.objects.all()[idis]
        except:
            seans = []
            raise Http404('Этого чисто физически не должно было произойти  ')
        
        
        seans_key= [x.ident_key for x in DATA_ALL_SEANSES.objects.all()]
        
        seans.seanses.add(DATA_ALL_SEANSES.objects.all()[seans_key.index(seans_id)])
        
        
        

        
        
        ii.now.add(DATA_ALL_SEANSES.objects.all()[seans_key.index(seans_id)])
        ii.save()
        seans.save()
        return HttpResponse('Все гуд ')
    except Exception as e:
        print(e)
        
        # raise 
        return HttpResponseRedirect('../login')







# Все ок
def like(request,seans_id):
    cookie = request.COOKIES.get('user','').split('/') 
    
    try:
        if cookie[-1] == str(checher(cookie[0],cookie[1])[1]):
        
            user = USER.objects.all()[int(cookie[-1])]
            seans_key= [x.ident_key for x in DATA_ALL_SEANSES.objects.all()]
            print(user)
            user.likes.add(DATA_ALL_SEANSES.objects.all()[seans_key.index(seans_id)])
            
            user.save()
            
            return HttpResponseRedirect('../merop/')
        else:
            
            return HttpResponseRedirect('../reg/')
    except:
        seans = []
        raise Http404('Этого чисто физически не должно было произойти... HakHer')
    
    
def users(request):
    
    
    return render(request,'ProDos/category.html',{'user':USER.objects.all(),'citiz':list(set([grade_list_city[x.city-1][1] for x in USER.objects.all()])),'list_cat_users':list(set([grade_list[x.loock_like-1][1] for x in USER.objects.all()]))})

def comm_(request,comm):

    seans_all_def = seans_all()
    name_cat = [x[1] for x in grade_list ]
    comm_proc = '' if comm not in name_cat else name_cat.index(comm)+1 
    if not comm.isdigit() and comm in [x[1] for x in grade_list] and comm_proc != '' :
        
        seans_all_def = DATA_ALL_SEANSES.objects.filter(class_seans=comm_proc)#comm - название меропр надо  число 
        print(seans_all_def)
    else:
        print(comm)
        print( [x[1] for x in grade_list]) 
    MINE =  request.COOKIES.get('user','').split('/') 
    print(MINE)  
    if MINE != [''] or len(MINE)>1:
        info = checher(MINE[0],MINE[1])
        if info[0]:
            user = USER.objects.all()[info[1]]
            seans = SEANS.objects.all()[info[1]]
            like_cat = [x.class_seans for x in user.likes.all() ] + [x.class_seans for x in seans.seanses.all() ]
            user.loock_like = max(Counter(like_cat).items() ,key=lambda i : i[1],default=str(user.loock_like))[0]
            user.save()
            
            old = seans_all_def
            new = []
            for i in old.reverse():
                print(grade_list[0])
                
                print(user.loock_like)
                if i.class_seans == user.loock_like:
                    new.insert(0,i)
                else:
                    new.append(i)
            for x in new:
                x.class_seans_name = grade_list[x.class_seans-1][1]
    else:
        print('Eror')
        num = len(seans_all_def)//10 if  len(seans_all_def) >= 10 else 1 
        return render(request,'ProDos/merop_all.html',{'seanses':seans_all_def,'range':range(num),'catt_all':grade_list,'tegs':Tegs.objects.all(),'name_main':comm})
    num = len(new)//10 if  len(new) >= 10 else 1
    
    return render(request,'ProDos/merop_all.html',{'seanses':new,'range':range(num),'catt_all':grade_list,'tegs':Tegs.objects.all(),'name_main':comm})

def update(request):
    return render(request,'ProDos/index.html',{'seanses':seans_all()})

def events(request,tag):
    tags = Tegs.objects.filter(name=tag)
    
    seans_all_def = tags[0].events.all()
    for x in seans_all_def:
        x.class_seans_name = grade_list[x.class_seans-1][1]
    num = len(seans_all_def)//10 if  len(seans_all_def) >= 10 else 1 
    return render(request,'ProDos/merop_all.html',{'seanses':seans_all_def,'range':range(num),'catt_all':grade_list,'tegs':Tegs.objects.all(),'name_main':tag})
    