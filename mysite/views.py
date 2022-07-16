from django.shortcuts import render
# from .apps.myapp2.views import detail2
#from .apps.myapp.models import USER,II,SEANS 





def eror404(request):
    return render(request, 'ProDos/eror404.html', status=404)

