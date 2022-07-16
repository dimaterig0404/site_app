
def pasword(sours):
    import hashlib
    h = hashlib.sha1(f"{sours}".encode('utf-8'))
    h.digest()
    return h.hexdigest()


#from myapp.request_db import pasword
#from myapp.models import USER
#admin.save()
#admin = USER(login='adminis',password=pasword('Dimaz04042'),isGreen=False,info_vac='',sopose='<18',email='dima.terig@gmail.com',list_frends='')


