from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'newsApp/index.html')

def moviesinfo(request):
    head_msg="Latest movies information"
    msg1='sonali fighting with cancer!!!!!!!'
    msg2='arjun reddy audio launch released on 22 aprl!!!!!!'
    msg3='salman gng to get married!!!with katrina'
    my_dict={'head_msg':head_msg,'msg1':msg1,'msg2':msg2,'msg3':msg3,}
    return render(request,'newsApp/news.html',context=my_dict)

def sportsinfo(request):
    return render(request,'newsApp/news.html')

def politicsinfo(request):
    return render(request,'newsApp/news.html')
