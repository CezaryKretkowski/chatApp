from ..models import Profile
from django import template

register = template.Library()

@register.filter(name="fitreByName")
def fitreByName(list,str):
    try:
        users=list.filter(user__username__contains=str)
    except Profile.DoesNotExist:
        users=[]
    print(users)
    return users