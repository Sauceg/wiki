from django import forms
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.utils.translation import gettext_lazy as _
from . import util
import random


   
   
class NewEntryForm(forms.Form):
    title = forms.CharField(label="title", max_length=100)
    content = forms.CharField(label = "Content", max_length= 400,widget=forms.Textarea)

    def clean_title(self):
        data = self.cleaned_data.get('title')
        if data in util.list_entries():
            raise forms.ValidationError("This title already Exists")
        return data 

def index(request):
    return render(request, "encyclopedia/index.html", {
        'entries' : util.list_entries()

    })
def title(request,tit):
    return render(request, "encyclopedia/pages.html",{
    "title" : tit,
    "content" :util.get_entry(tit)})

def search_box(request):
    search  = request.GET.get('q','w') 
    entries =  util.list_entries()
    if search in  entries:
        return title(request,search)
    else:
        ent =  [x for x in entries if str(search) in x]
        return render(request, "encyclopedia/index.html", {
        'entries' : ent 

    })

def make_entry(request):
    # Take in the data the user submitted and save it as form
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = NewEntryForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
        # Isolate the entry from the 'cleaned' version of form data
            tit = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            # Add the new entry to our list of entries 
            util.save_entry(tit,content)
            # Redirect user to entry just created 
            return title(request,tit)

        
    return render(request, "encyclopedia/make_entry.html",{
                "form" : NewEntryForm(),
            
})

def editpage(request,title):
    #title = request.GET.get('q','w') 
    #content =  util.get_entry(title)
    return render(request, "encyclopedia/edit.html",{
        "title" : title,
        "content" :util.get_entry(title)})

def random(request):
    import random
    randompage = random.choice(util.list_entries())
    return title(request,randompage)

def save_new_entry(request):
     if request.method == "POST":
        content  = request.GET.get('t') 
        