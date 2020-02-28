from django.shortcuts import render
import datetime
# Create your views here.
def dateInfo(request):
    date=datetime.datetime.now()
    my_dict={'msg':date}
    return render(request,'testapp/test.html',context=my_dict)
