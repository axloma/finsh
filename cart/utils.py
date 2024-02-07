from django.contrib import messages
from django.shortcuts import render,redirect,get_object_or_404
import re

def add_MSG(request):
    d_m = []
    for message in messages.get_messages(request):
        d_m.append({
            "level": message.level,
            "message": message.message,
            "extra_tags": message.tags,
    })
    return d_m 
        

def checkifo(request,name,email,address,city,phone):
    if not name or not email or not address or not city or not phone :
        print("func is working ")
        messages.error(request,"MISSING FIELD PLEASE MAKE SURE NES FIELD ARE NOT EMPTY  ")
        d_m = add_MSG(request)
        return False , d_m
    
    else:
        print(name,email,address,city,phone)
        d_m = add_MSG(request)
        return True,d_m

def checkemail(request,email):
   if not re.search(r"^[A-Za-z0-9_!#$%&'*+\/=?`{|}~^.-]+@[A-Za-z0-9.-]+$", email):
       print(f"The email address {email} is not valid")
       messages.error(request,("NOT VALID EMAIL "))
       d_m = add_MSG(request)
       return False ,d_m
   else:
       print("VALID EMAIL ")
       d_m = add_MSG(request)
       return True ,d_m
