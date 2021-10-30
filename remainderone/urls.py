from django.urls import path 
from remainderone.views import openpage,loginpage,signuppage,homepage,logoutpage,profilepage,updateprofilepage,roomformpage

from remainderone.viewsone import imageprob,updateroomformpage,deleteroompage,followhandler,unfollowhandler,roomchatpage,messagehandler
from django.conf.urls import (
handler400, handler403, handler404, handler500
)

handler404 = 'remainderone.viewsone.custom_page_not_found_view'
handler500 = 'remainderone.viewsone.custom_error_view'
handler403 = 'remainderone.viewsone.custom_permission_denied_view'
handler400 = 'remainderone.viewsone.custom_bad_request_view'
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
