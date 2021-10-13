from django import template
from remainderone.models import Follower
register=template.Library()

def add(value):
    if value == "sai" :
        return "yes"
    else :
        return "no"
def following(room,user):
    is_following=False
    followers=Follower.objects.filter(room=room)
    print("followers are ",followers)
    for follower in followers :
        if follower.followed_by == user:
            is_following=True
            break
    return is_following

register.filter("add",add)
register.filter("following",following)
    