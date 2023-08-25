from django.shortcuts import render,redirect
from  .forms import signupForm, ImageForm
from .models import signup,product,ImageModel
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.
def index(request):
    if request.method=='POST':
        if request.POST.get('signup')=='signup':
            newuser=signupForm(request.POST)
            if newuser.is_valid():
                newuser.save()
                print("signup successfully")
            
                #email sending
                sub='Welcome !'
                msg='Dear user '
                from_email='darshitgajjar2@gmail.com'
                to_email=[request.POST['Email']]
                send_mail(subject=sub,message=msg,from_email=from_email,recipient_list=to_email)
                return redirect('/')
            else:
                print(newuser.errors)
        elif request.POST.get('login')=='login':
                unm=request.POST['Email']
                pas=request.POST['Password']
                user=signup.objects.filter(Email=unm,Password=pas)
                uid=signup.objects.get(Email=unm)
                # print("userid:",uid.id)
                if user:
                    print('login successfully')
                    request.session['user']=unm
                    request.session['uid']=uid.id
                    return redirect('notes')
                    
                else:
                    print('Eror to Email and Password does not match')
    user = request.session.get('user')
    return render(request,'index.html',{'user':user})

#@login_required(login_url='/')
def about(request):
    return render(request,'about.html')

#@login_required(login_url='/')
def contact(request):
    return render(request,'contact.html')

#@login_required(login_url='/')
def news(request):
    return render(request,'news.html')

#@login_required(login_url='/')
def products(request):
    product1 = product.objects.all()
    return render(request,'products.html',{'products':product1})

#@login_required(login_url='/')
def fashion(request):
    return render(request,'fashion.html')

#@login_required(login_url='/')
def showdatapage(request):
    return render(request,'showdatapage.html')

def updateProfile(request):
    user=request.session.get('user')
    uid=request.session.get('uid')
    cilent=signup.objects.get(id=uid)
    if request.method=='POST':
        updateProfile=signupForm(request.POST,instance=cilent)
        if updateProfile.is_valid():
            updateProfile.save()
            print("Your profile has been updated!")
            return redirect('notes')
        else:
            print(updateProfile.errors)
    return render(request,'UpdateProfile.html',{'user':user,'uid':signup.objects.get(id=uid)})

#@login_required(login_url='/')
def notes(request):
    user=request.session.get('user')
    return render(request,'notes.html',{'user':user})

def emaillogout(request):
    logout(request)
    return redirect('/')


def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')  # Redirect to a view that lists images
    else:
        form = ImageForm()
    return render(request, 'upload_image.html', {'form': form})

def image_list(request):
    images = ImageModel.objects.all()
    return render(request, 'image_list.html', {'images': images})