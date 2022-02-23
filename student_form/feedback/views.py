from django.http import HttpResponse
from django.shortcuts import render
import sqlite3
# Create your views here.
def home(request):
    return render(request,'feedback_form.html')
def save(request):
    c=sqlite3.connect("db.sqlite3")
    cr=c.cursor()
    #cr.execute("create table reviews(roll_no NUMBER,name TEXT,email TEXT,review TEXT)")
    name=request.GET['name']
    roll_no=int(request.GET['roll'])
    email=request.GET['email']
    review=request.GET['review']

    cr.execute("insert into reviews values('%s','%s','%s','%s')"%(name,roll_no,email,review))
    c.commit()
    c.close()
    return HttpResponse('Save Succesfull')