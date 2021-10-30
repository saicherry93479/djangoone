from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
# from django.http import HtttpResponse
from django.http import HttpResponse
from remainderone.profileform import profileupdate
from remainderone.models import appuser,Room,Follower
from remainderone.roomform import roomform
from django.db.models import Count

@login_required(login_url='openpage')
def roomformpage(request):
    form=roomform()
    context={
        'Dshow':True,
        'form':form
    }

   

    if request.method=='POST' :
        form=roomform()
        data = {
            'user_created':request.user,
            'room_name':request.POST.get('room_name'),
            'room_description':request.POST.get('room_description')
        }
        current_room=Room.objects.filter(user_created=request.user)
     
        create =True
        for room in current_room :
            if room.room_name == request.POST.get('room_name') :
                create=False
                break



       
        if create :
            form_save=roomform(data)
            if form_save.is_valid():
                form_save.save()
                return redirect("homepage")
            else :
                return HttpResponse("your form is not valid")
        else :
            return HttpResponse("your are not allowed to create room with same name twice")
        


    return render(request,'roomformpage.html',context)

@login_required(login_url='openpage')
def profilepage(request):
    
    user=User.objects.filter(username=request.user.username).first()
    context={
        'Dshow':True,
        'userDetails':appuser.objects.filter(username=user).first(),
        'rooms':Room.objects.filter(user_created=request.user)
    }
    return render(request,'profilepage.html',context)
@login_required(login_url='openpage')    
def updateprofilepage(request):
    form=profileupdate()
    
    
    user_exist=User.objects.filter(username=request.user.username).first()
    app_user=appuser.objects.filter(username=user_exist).first()
    
    context={
         'Dshow':True,
          'form':form,
          'appuser':app_user

    }
    if request.method == 'POST' :
        user=User.objects.filter(username=request.user.username).first()
        user.first_name=request.POST.get('first_name')
        user.last_name=request.POST.get('last_name')
        user.save() 
       
        user_app=appuser.objects.filter(username=user).first()
        data={
            'username':user,
            'email':user.email,
            'profilepic':request.POST.get('profilepic'),
          
            'first_name':request.POST.get('first_name'),
            'last_name':request.POST.get('last_name')
        }
      
        appuser_exist=profileupdate(data,request.FILES,instance=user_app)
      
        
        if appuser_exist.is_valid():
                
             user_app=appuser_exist.save(commit=False)
            #  user_app.profilepic=request.FILES.get('profilepic')

             user_app.save()
             return redirect("profile")
        else :
            return HttpResponse("no form is not valid")
       
    
    return render(request,'updateprofilepage.html',context)

@login_required(login_url='openpage')
def homepage(request):
        rooms=Room.objects.values('room_name').annotate(dcount=Count('room_name')).order_by()

        # print("top followers are ",top_followers_rooms)
        rooms_all=Room.objects.all()
       
        
        context={
            'rooms_left':rooms,
            'rooms':rooms_all,
            'recentrooms':Room.objects.all().order_by('-id')[:10],
            # 'top_followers_rooms':top_followers_rooms

        }
        return render(request,"home.html",context)
def logoutpage(request):
    logout(request)
    return redirect("openpage")
def openpage(request):
    context={
        "name":"charan"
    }
    if request.user.is_anonymous:
         return render(request,'openpage.html',context)
    else :
        return redirect("homepage")


def loginpage(request):
    
   
    if request.user.is_anonymous:
        context={'Dshow':True}
        if request.method == 'POST':
            username=request.POST.get("username")
            password=request.POST.get("password")
            user_auth=authenticate(username=username,password=password)
            if user_auth is not None :
                login(request,user_auth)
               
                return redirect("homepage")
    else :
        return redirect("homepage")

    return render(request,'loginpage.html',context)

def signuppage(request):
    if  request.user.is_anonymous:
   
        form=UserCreationForm()
        context={
            'Dshow':True,
            'form':form,
            'redirected':False,
            
        }
    
        if request.method=='POST':

            
            username=request.POST.get('username')
            password1=request.POST.get('password1')
            password2=request.POST.get('password2')
            email=request.POST.get('email') 
           
            
            if password1 != password2 :
               
                context['redirected']=True
               
                # form=UserCreationForm(request.POST)
            
                context['redirect']={
                        'username':username,
                        'password1':password1,
                        'password2':password2,
                        'email':email
                    }
                context['error']="passworderror"
                
            
            else :
            
                user_presence=User.objects.filter(email=email).first()
                if user_presence is not None :
                    context['redirected']=True
                    context['redirect']={
                            'username':username,
                            'password1':password1,
                            'password2':password2,
                            'email':email
                        }
                    context['error']="emailerror"
                else :
                    username_presence=User.objects.filter(username=username).first()
                    if username_presence is not None :
                        context['redirected']=True
                        context['redirect']={
                        'username':username,
                        'password1':password1,
                        'password2':password2,
                        'email':email
                    }
                        context['error']="usernameerror"
                    else :
                        
                        form_save=UserCreationForm(request.POST)
                        if form_save.is_valid() :
                            form_save.save()
                            user=User.objects.filter(username=username).first()
                            user.email=email
                            user.save()
                            app_user=appuser(username=user,email=email)
                            app_user.save()
                            login(request,user)
                            return redirect("homepage")
                        else :
                            return HttpResponse("no there is a problem")
    else :
        return redirect("homepage")
                    
    return render(request,'signuppage.html',context)
    
   

# Create your views here.
