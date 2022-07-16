# from multiprocessing import context
# from tkinter import SE
# from django.shortcuts import get_object_or_404
# from .forms import UserInfo
# from django.http import request

from mimetypes import MimeTypes
import random
from django.http import Http404, HttpResponse#,HttpResponseRedirect
from django.shortcuts import render
from .models import II,USER,SEANS,DATA_ALL_SEANSES



def index(request):
    
    print(request.META['PATH_INFO'])
    if request.META['PATH_INFO'] == '/reg/Qr':
        
        MINE =  request.COOKIES.get('info','').split('/') 
        if str(MINE[3]) == '0':
            return render(request,'Phone_id/check.html')
        else:
            return render(request,'Phone_id/check.html')
    
        
    
    elif request.META['PATH_INFO'] == '/reg/info':
        
        MINE =  request.COOKIES.get('info','').split('/') 
        if str(MINE[3]) == '0':
            
            return render(request,'Phone_id/qr_code.html',{'status':MINE[4]})
        else:
            
            return render(request,'Face_id/qr_code.html',{'status':MINE[4]})
        
    elif request.META['PATH_INFO'] == '/reg/valid':
        MINE =  request.COOKIES.get('info','').split('/') 
        
        isGreen = True if str(MINE[3]) == '1' else False 
        
        user = USER(login=MINE[0],email=MINE[1],isGreen=isGreen,sopose=MINE[4],password=password_create(MINE[2]))
        ii = II(id_user=user,code=MINE[-1])
        seans = SEANS(id_user=user,seanses='')
        user.save()
        ii.save()
        seans.save()
        idis=[x for x in USER.objects.all()]
        
        idis=idis.index(user)
        
        return render(request,'Face_id/valid.html',{'id':idis,'pass':MINE[2],'name':MINE[1]})
    
    
    # response.set_cookie('user', '', max_age = 5000000)
    
    elif  request.META['PATH_INFO'] == '/':
        try:
            MINE =  request.COOKIES.get('user','').split('/')    
            idis = int(MINE[-1])
            
            uaser = USER.objects.all()[idis]
            USER_SOURS = str(uaser).split('/')
            
            if uaser.sopose == '18':
                data = [x for x in DATA_ALL_SEANSES.objects.filter() if int(x.categori)<18]
                
            else:
                data = [x for x in DATA_ALL_SEANSES.objects.filter()] 
        except:
            data = [x for x in DATA_ALL_SEANSES.objects.filter()] 
        n = 3 
        
        
        def take_second(elem):
            if elem.class_seans == uaser.loock_like:
                print(elem)
                return elem.class_seans
            else:
                return 1

        random.shuffle(data)    
        print(data)
        
        
        ar = [sorted(data[:len(data)//n], key=take_second,reverse=True)] + [sorted(data[len(data)//n:][:-len(data)//n] , key=take_second,reverse=True)] + [sorted(data[-len(data)//n:], key=take_second,reverse=True)]
         
        
        try:
            if password_create(MINE[1]) == USER_SOURS[2] and MINE[0] == USER_SOURS[1]:
                print(uaser.sopose)
                seans_info=SEANS.objects.all()[idis]
                print(seans_info.seanses.split('|'))
                list_interisting_user = [x.split('!')[3] for x in seans_info.seanses.split('|') if len(x)>0 ]
                import collections
                print(list_interisting_user)
                
                print(uaser.loock_like)
                def two_el_chech(el):
                    return el[1]
                uaser.loock_like = int(max(collections.Counter(list_interisting_user).items(),key=two_el_chech)[0])
                uaser.save()
                
                
                return render(request,'index.html', {'catalog':ar,'user':uaser}) 
        
        except Exception as e:
            print(e)    
            return render(request,'index.html', {'catalog':ar}) 
    
    elif  request.META['PATH_INFO'] == '/login/':
        
        
        return render(request,'other/login.html')
    
    
    

def validationalis(request):
    if request.method == 'GET':
        
        MINE =  request.COOKIES.get('user','').split('/') 
        MINE[1] = "/"+ password_create(MINE[1])
        MINE = ''.join(MINE)
        
        
        
        uaser = USER.objects.all()
        clear_user_info = [x.email +"/"+ x.password for x in uaser]
        
        print(clear_user_info)
        print(MINE)
        
        if MINE in clear_user_info:
            id_user = clear_user_info.index(MINE)
            return render(request,'profile/validationalis.html',{"id":id_user})
             
        return render(request,'profile/validationalis_no.html')
        

def password_create(sours):
    import hashlib
    h = hashlib.sha1(f"{sours}".encode('utf-8'))
    h.digest()
    return h.hexdigest()
    


def prof(request):
    return render(request,'profile/profile_admin.html')



def detail(request,prof_id):
    
    try:

        uaser = USER.objects.all()[prof_id]
        ii = II.objects.all()[prof_id]
        try:
            seans = SEANS.objects.all()[prof_id]
        except:
            seans = None
    except:
        
        raise Http404('Тут нет ничего ')
    

    USER_SOURS = str(uaser).split('/')
    MINE =  request.COOKIES.get('user','').split('/')    

    if password_create(MINE[1]) == USER_SOURS[2] and MINE[0] == USER_SOURS[1]:
        isMine = True
    else:
        isMine = False
    
    idis = MINE[2]
    list_seans = [x.split('!') for x in list(filter(None, str(seans.seanses).split('|')))]
    
    print(list_seans)
    return render(request,'profile/profile.html',{'uaser':uaser,'ii':ii,'seans':seans,'isMine':isMine,'id':idis,'list_seans':list_seans})



def detail_my(request):
    MINE =  request.COOKIES.get('user','').split('/')   
    idis = int(MINE[2])
    
    try:

        uaser = USER.objects.all()[idis]
        ii = II.objects.all()[idis]
        try:
            seans = SEANS.objects.all()[idis]
        except:
            seans = None
    except:
        raise Http404('Тут нет ничего ')
    

    USER_SOURS = str(uaser).split('/')
     

    if password_create(MINE[1]) == USER_SOURS[2] and MINE[0] == USER_SOURS[1]:
        isMine = True
    else:
        isMine = False
    
    list_seans = [x.split('!') for x in list(filter(None, str(seans.seanses).split('|')))]
    
    print(list_seans)
    return render(request,'profile/profile.html',{'uaser':uaser,'ii':ii,'seans':seans,'isMine':isMine,'id':idis,'list_seans':list_seans})
    
    
def edit(request):
    MINE =  request.COOKIES.get('user','').split('/')   
    idis = int(MINE[2])
    
    try:

        uaser = USER.objects.all()[idis]
        ii = II.objects.all()[idis]
        try:
            seans = SEANS.objects.all()[idis]
        except:
            seans = None
    except:
        raise Http404('Тут нет ничего ')
    

    USER_SOURS = str(uaser).split('/')
     

    if password_create(MINE[1]) == USER_SOURS[2] and MINE[0] == USER_SOURS[1]:
        isMine = True
    else:
        isMine = False
    
    list_seans = [x.split('!') for x in list(filter(None, str(seans.seanses).split('|')))]
    
    print(list_seans)
    return render(request,'profile/edit.html',{'uaser':uaser,'ii':ii,'seans':seans,'isMine':isMine,'id':idis,'list_seans':list_seans})


def save(request):
    MINE =  request.COOKIES.get('red','').split('/')  
    MINE_user =  request.COOKIES.get('user','').split('/')  
    idis = int(MINE[-1])
    
    try:

        uaser = USER.objects.all()[idis]
        ii = II.objects.all()[idis]
        try:
            seans = SEANS.objects.all()[idis]
        except:
            seans = None
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
    else:
        raise Http404('Тут нет ничего ')
    


def buy_valet (request,seans_id):
    # if request.method == 'POST':
    #     print('ON')
    try:
        all = DATA_ALL_SEANSES.objects.all()
        info_po_cody = [str(x).split('|')[0] for x in all]
        id = info_po_cody.index(seans_id)
        info_po_id = all[id]
        MINE_user =  request.COOKIES.get('user','').split('/')  
        idis = int(MINE_user[-1])
        
        try:

            ii = II.objects.all()[idis]
            
            try:
                seans = SEANS.objects.all()[idis]
            except:
                seans = None
                raise Http404('Этого чисто физически не должно было произойти  ')
        except:
            raise Http404('Тут нет ничего ,kz ')
        
        
        print(str(info_po_id.img.name))
        seans.seanses = f'{str(seans.seanses)}{info_po_id.name.replace("!",".").replace("|",".")}!{info_po_id.discription.replace("!",".").replace("|",".")}!{str(info_po_id.img.name.replace("!",".").replace("|","."))}!{info_po_id.class_seans}|'
        
        
        ii.now=f'{ii.now}{info_po_id.name}!{info_po_id.discription.replace("!",".").replace("|",".")}!{info_po_id.img.name.replace("!",".").replace("|",".")}!{info_po_id.class_seans}|'
        ii.save()
        seans.save()
        return HttpResponse('Все гуд ')
    except Exception as e:
        print(e)
        print(info_po_id.class_seans)
        
        raise Http404('Войдите в аккакунт ')
    
    
    
    
def sql_responseerate (request,id_code,info,info_photo):
    print('0k')
    if id_code == 1:
        print(info,info_photo)
        ii = II.objects.all()[int(info)]
        
        ii.info_photo = info_photo
        ii.save()
        
    elif id_code == 0 :
        
        #+ '|' + str(x.id)
        names = [x.login for x in USER.objects.all()]
        codes = [x.code for x in II.objects.all()]
        print(names)
        print(codes)
        
        return render(request,'other/admin_do.html',{'names':'/'.join(names),'codes':'/'.join(codes)})
    
    elif id_code == 3 :
        
        #+ '|' + str(x.id) 
        names = [x.login for x in USER.objects.all()]
        codes = [x.info_photo for x in II.objects.all()]
        print(names)
        print(codes)
        
        return render(request,'other/admin_do.html',{'names':'/'.join(names),'codes':'/'.join(codes)})
    elif id_code == 4 :
        
        #+ '|' + str(x.id) 
        names = [x.sopose for x in USER.objects.all()]
        codes = [x.now for x in II.objects.all()]
        print(names)
        print(codes)
        
        return render(request,'other/admin_do.html',{'names':'/'.join(names),'codes':'/'.join(codes)})
    
    raise Http404()
    