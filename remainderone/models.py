from django.db import models
from django.contrib.auth.models import User

class appuser(models.Model):
    username=models.OneToOneField(User,on_delete=models.CASCADE)
    email=models.EmailField(max_length=200)
    profilepic=models.ImageField(blank=True,null=True,upload_to='images/')
    first_name=models.CharField(max_length=200,null=True,blank=True)
    last_name=models.CharField(max_length=200,null=True,blank=True)
    user_joined=models.DateTimeField(auto_now=True)
    user_updated=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user_created.username
   


class Room(models.Model):
    user_created=models.ForeignKey(User,on_delete=models.CASCADE)
    room_name=models.CharField(max_length=200)
    room_created=models.DateTimeField(auto_now=True)
    room_updated=models.DateTimeField(auto_now_add=True)
    room_description=models.TextField()
    def __str__(self):
        return self.room_name + " "+self.user_created.username
class Follower(models.Model) :
    room=models.ForeignKey(Room,on_delete=models.CASCADE)
    followed_by=models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.room.room_name + "  C"+self.room.user_created.username +" "+self.followed_by.username
class message(models.Model):
    room_name=models.ForeignKey(Room,on_delete=models.CASCADE)
    message_sent=models.ForeignKey(User,on_delete=models.CASCADE)
    message=models.CharField(max_length=1000)
    message_date=models.DateField(auto_now=True)
    message_time=models.TimeField(auto_now=True)

    def __str__(self):
        return self.room_name.user_created.username+" "+self.room_name.room_name+" "+self.message_sent.username

class imageproblem(models.Model):
     title=models.CharField(max_length=200)
     image=models.ImageField()

    

# Create your models here.
