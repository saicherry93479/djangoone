from django.shortcuts import render,redirect
from django.http import HttpResponse
from remainderone.models import imageproblem,Room,Follower,message
from remainderone.roomform import roomform
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from threading import Timer
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core import serializers
import json
@receiver(post_save,sender=message)
def message_loop(sender,instance,created,**kwargs):
    if created :
         # messages=sender.objects.filter(room_name=host_room)[::-1]
         print("new messsage is created")
         print("message created is ",instance.message)
         room=instance.room_name
         username=room.user_created.username
         roomname=room.room_name

         url="/home/room/"+username+"/"+roomname
         return redirect(url)

@login_required(login_url='openpage')
def messagehandler(request,username,roomname):
    # return HttpResponse("this is message")
   if request.method == 'POST': 
        user=User.objects.filter(username=username).first()
        room=Room.objects.filter(user_created=user,room_name=roomname).first()
        new_message=message(room_name=room,message_sent=request.user,message=request.POST.get('message'))
        new_message.save()
        url="/home/room/"+username+"/"+roomname
        return redirect(url)
   else :
        return HttpResponse("message is not sent properly")


# host_room=None     
@login_required(login_url='openpage')
def roomchatpage(request,username,roomname):
    user_created=User.objects.filter(username=username).first()
    host_room=Room.objects.filter(user_created=user_created,room_name=roomname).first()
    
    messages=message.objects.filter(room_name=host_room)[::-1]
    host_room_f=serializers.serialize("json",messages)
    print("start messages length is ",len(messages))
    room_name={
        "user_created":host_room.user_created.username,
        "room_name":host_room.room_name
    }
    

   


    
   
    context={
        'host_room':host_room,
        'Dshow':True,
        'messages':messages,
        'host_room_f':host_room_f,
        'roomname':room_name
        
    }

    return render(request,'chatroom.html',context)
# @receiver(post_save,sender=message)
# def message_loop(sender,instance,created,**kwargs):
#     if created :
#        messages=sender.objects.filter(room_name=host_room)[::-1]
#        print("messages length is ",len(messages))
#        print("message created is ",instance.message)

@login_required(login_url='openpage')
def followhandler(request,username,roomname):
    user=User.objects.filter(username=username).first()
    room=Room.objects.filter(user_created=user,room_name=roomname).first()
    # follower=Follower.objects.filter(room=room,followed_by=request.user).first()
    # if follower is None :
    follower_create=Follower(room=room,followed_by=request.user)
    follower_create.save()
    return redirect("homepage")
    # else :
    #     return HttpResponse("again u fucked this in making follow")
@login_required(login_url='openpage')
def unfollowhandler(request,username,roomname):
    user=User.objects.filter(username=username).first()
    room=Room.objects.filter(user_created=user,room_name=roomname).first()
    follower=Follower.objects.filter(room=room,followed_by=request.user).first()
    if follower is not None :
        follower.delete()
        # print("follower delete ",follower.delete())
        
        return redirect("homepage")
    else :
        return HttpResponse("again u fucked this in making unfollow")
    # return HttpResponse("u have clicked on Unfollow ")

    

@login_required(login_url='openpage')
def deleteroompage(request,pk):
    room_delete=Room.objects.filter(user_created=request.user,room_name=pk).first()
    if room_delete is not None :
        room_delete.delete()
        return redirect("profile")
    else :
        return HttpResponse("u are  fucked .. it was impossible to get here ")
def updateroomformpage(request,pk):
    print("room to be updated ",pk)
    current_room=Room.objects.filter(user_created=request.user,room_name=pk).first()
    form =roomform(instance=current_room)
    # print("form  is ",form)

    context={
        'Dshow':True,
        'form' :form,
        'update':True
    }
    if request.method=='POST' :
        form=roomform()
        data = {
            'user_created':request.user,
            'room_name':request.POST.get('room_name'),
            'room_description':request.POST.get('room_description')
        }
        current_room=Room.objects.filter(user_created=request.user,room_name=pk)
        print("room length in update ",len(current_room))
        if len(current_room) ==1 :
             current_room=Room.objects.filter(user_created=request.user,room_name=pk).first()
             form_save=roomform(data,instance=current_room)
             if form_save.is_valid():
                    form_final=form_save.save(commit=False)
                    form_final.save()
                    return redirect("homepage")
             else :
                    return HttpResponse("your form is not valid in updating room")
        else :
            return HttpResponse("your are not allowed to have same room_names in update form")
        

        
    return render(request,'roomformpage.html',context)


def imageprob(request):
    images=imageproblem.objects.all()

    context={
        'images':images
    }
    if request.method == 'POST':
        print("request post values are ",request.POST)
        print("the files are ",request.FILES.get('image'))
        imagemodel=imageproblem(title=request.POST.get('title'),image=request.FILES.get('image'))
        imagemodel.save()
        return redirect("imageproblem")
    return render(request,'iamgeproblem.html',context)