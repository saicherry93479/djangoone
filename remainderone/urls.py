from django.urls import path 
from remainderone.views import openpage,loginpage,signuppage,homepage,logoutpage,profilepage,updateprofilepage,roomformpage

from remainderone.viewsone import imageprob,updateroomformpage,deleteroompage,followhandler,unfollowhandler,roomchatpage,messagehandler

urlpatterns=[
    path("",openpage,name="openpage"),
    path("loginpage/",loginpage,name="loginpage"),
    path("signuppage/",signuppage,name="signuppage"),
    path("home/",homepage,name="homepage"),
    path("logoutpage/",logoutpage,name="logoutpage"),
    path("home/profile/",profilepage,name="profile"),
    path("home/profile/updateprofile",updateprofilepage,name="updateprofile"),
    path("imageproblem/",imageprob,name="imageproblem"),
    path("home/roomformpage/",roomformpage,name="roomformpage"),
    path("home/profile/updateroomformpage/<str:pk>/",updateroomformpage,name="updateroomformpage"),
    path("home/profile/deleteroompage/<str:pk>/",deleteroompage,name="deleteroompage"),
    path("home/followHandler/<str:username>/<str:roomname>/",followhandler,name="followhandler"),
    path("home/unfollowHandler/<str:username>/<str:roomname>/",unfollowhandler,name="unfollowhandler"),
    path("home/room/<str:username>/<str:roomname>/",roomchatpage,name="roomchatpage"),
    path("home/room/messagehandler/<str:username>/<str:roomname>/",messagehandler,name='messagehandler')


]
