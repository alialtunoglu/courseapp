from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User

# Create your views here.

def user_login(request):
    if request.user.is_authenticated and  "next" in request.GET:
        return render(request, 'account/login.html', {'error': 'Yetkisiz kullanıcı erişimi'})

    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(request,username=username, password=password)
        if user is not None:
            login(request,user)
            nextUrl= request.GET.get("next",None)
            if nextUrl is None:
                return redirect('index')
            else:
                return redirect(nextUrl)
        else:
            return render(request, 'account/login.html', {'error': 'Parola veya username yanlış!'})
    else:
        return render(request, 'account/login.html')
        
def user_register(request):
    if request.method == 'POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        repassword=request.POST['repassword']
        if password != repassword:
            return render(request, 'account/register.html', {'error': 'Parola eşleşmiyor','username':username,'email':email})
        if User.objects.filter(username=username).exists():
            return render(request, 'account/register.html', {'error': 'Bu username daha önce kullanılmış!','username':username,'email':email})
        
        if User.objects.filter(email=email).exists():
            return render(request, 'account/register.html', {'error': 'Bu email daha önce kullanılmış!','username':username,'email':email})
        
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        # Kullanıcıyı otomatik giriş yaptır
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # Kullanıcıyı giriş yaptır
            return redirect('index')  # Ana sayfaya yönlendir    
    else:
        return render(request, 'account/register.html')

    
def user_logout(request):
    logout(request)
    return redirect('user_login')