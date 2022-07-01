import string
from xmlrpc.client import boolean
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import context, loader
from django.urls import reverse
from members.models import college






def index(request):
  myCollege = college.objects.all().values()
  return render(request, "index.html",{
    "myCollege": myCollege
  })




def add(request):
  myCollege = college.objects.all().values()
  return render(request, "add.html",{
    "myCollege": myCollege
  })



def addrecord(request):
  c = request.POST['collegeName']
  s = request.POST['subject']
  u = request.POST['numberOfUnits']
  t = request.POST['timeAndDate']
  collegeDetails = college(collegeName = c, subject = s, numberOfUnits = u, timeAndDate = t)
  collegeDetails.save()
  return HttpResponseRedirect(reverse('index'))




def delete(request, id):
  collegeDelete = college.objects.get(id=id)
  collegeDelete.delete()
  return HttpResponseRedirect(reverse('deletePage'))

def deletePage(request):
  myCollege = college.objects.all().values()
  return render(request,'delete.html',{
    "myCollege": myCollege
  })
  




def updatePage(request):
  myCollege = college.objects.all().values()
  return render(request,'updatePage.html',{
    "myCollege": myCollege
  })

  
def update(request, id):
  myCollege = college.objects.get(id=id)
  myCollege1 = college.objects.all().values()
  return render(request,'update.html',{
    'myCollege': myCollege,
    'myCollege1': myCollege1
  })



def updaterecord(request, id):
  c = request.POST['collegeName']
  s = request.POST['subject']
  u = request.POST['numberOfUnits']
  t = request.POST['timeAndDate']
  myCollege = college.objects.get(id=id)
  myCollege.collegeName = c
  myCollege.subject = s
  myCollege.numberOfUnits = u
  myCollege.timeAndDate = t
  myCollege.save()
  return HttpResponseRedirect(reverse('updatePage'))

