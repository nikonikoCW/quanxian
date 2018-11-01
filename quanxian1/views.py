from django.shortcuts import render,redirect,HttpResponse

# Create your views here.
def check_login(func):
    def inner(request,*args,**kwargs):
        user_cookies = request.get_signed_cookie('chenwei', default='0', salt='sa10nb')
        if user_cookies == 'henshuai':
            return func(request, *args, **kwargs)
        else:
            next_url = request.path_info
            print(next_url)
            return redirect('/login/?next={}'.format(next_url))
    return inner



def login(request):
    if request.method == "POST":
        user = request.POST.get("user")
        password = request.POST.get('password')
        next_url = request.GET.get('next')
        if user =='cw' and password =='123123':
            if next_url:
                rep = redirect(next_url)
            else:
                rep = redirect('/home/')
            rep.set_signed_cookie('chenwei','henshuai',salt='sa10nb',max_age = 10)
            return rep
        else:
            return HttpResponse("cuole")
    return render (request,'login.html')
def home(request):
    #user_cookies = request.COOKIES['chenwei']
    user_cookies = request.get_signed_cookie('chenwei',default='0',salt='sa10nb')
    if user_cookies =='henshuai':
        return render (request,'home.html')
    else:
        return redirect('/login/')

@check_login
def index(request):
    return render(request,'index.html')


def logout(request):

    rep = redirect('/login/')
    rep.delete_cookie('chenwei')
    return rep