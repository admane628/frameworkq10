from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from collec_management.forms import CollecForm
from collec_management.models import Collec
# Create your views here.
def about(request):
    return render(request, 'collec_management/about.html')

def collection_detail(request ,id) :
    collectionInexistant= get_object_or_404(Collec , id=id) 
    return render(request ,'collec_management/collection_detail.html', {'collectionInexistant' : collectionInexistant})

def new( request ) :
 if request.method == "POST" :
    form=CollecForm(request.POST)
    if form.is_valid () :
       collec=form.save(commit = False ) 
       collec.save () # Sauvegarde en base de donnees
       return HttpResponseRedirect(reverse('collection' ,args=[collec.id] ))
 else :
    form = CollecForm() # Formulaire vide
 return render(request,"collec_management/formulaireNew.html" ,
               {"form" :form })

def all(request):
    collections=Collec.objects.all()
    return render(request, "collec_management/colleclist.html", {"collections":collections})

def delete(request , collec_id) :
   collec=get_object_or_404(Collec , pk=collec_id)
   if request.method=="POST" :
      collec.delete()
      return redirect("all")
   
   return render (request , "collec_management/collec_delete.html",{"collec" :collec})


def check_save(form) :
   if form.is_valid() :
      collec=form.save(commit = False ) 
      collec.save ()
   return collec.id 
      
def change(request , collec_id) :
   collec = get_object_or_404(Collec , pk=collec_id)
   if request.method == "POST" :
      form =CollecForm(request.POST , instance=collec)
      collecModif_id = check_save(form)
      return redirect("collection" , id = collecModif_id)
   else :
      form =CollecForm(instance=collec)
   return render(request,
                 "collec_management/collec_modifier.html"
                 ,{"form": form})
def menu(request):
    return render(request, 'collec_management/menu.html')
