
from django.http import HttpResponse
from django.template import loader
from .models import Member
# Create your views here.

def members(request):
    mymembers=Member.objects.all().values()
    #Creates a mymembers object with all the values of the Member model
    template= loader.get_template('allmembers.html')#Loads the all_members.html template.
    context={'mymembers':mymembers,
             }#Creates an object containing the mymembers object
    return HttpResponse(template.render(context,request))#Sends the object to the template.
#Outputs the HTML that is rendered by the template

def details(request, id):
  mymember = Member.objects.get(id=id)#Gets the id as an argument
  #Uses the id to locate the correct record in the Member table.
  template = loader.get_template('details.html')#loads the details.html template.
  context = {
    'mymember': mymember,
  }#Creates an object containing the member.
  return HttpResponse(template.render(context, request))#Sends the object to the template.
#Outputs the HTML that is rendered by the template
def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def testing(request):
  template = loader.get_template('template.html')
  context = {
    'fruits': ['Apple','Banana','Cherry'],
  }
  return HttpResponse(template.render(context, request))