from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
from . import util
import markdown2
import random

class NewEntry(forms.Form):
    title = forms.CharField(required=True,label="title")
    content = forms.CharField(label="content",widget=forms.Textarea(attrs={'cols': 5, 'rows': 2}))



def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
def title(request, title):

    entries = util.list_entries()
    if title in entries:
        return render(request,"encyclopedia/content.html",{
            "content": markdown2.markdown(util.get_entry(title)), "title":title
        })
    else:
        return render(request, "encyclopedia/error.html", {"message": "No such entry found"})

def search(request):
    if request.method=="POST":
        query = request.POST['q']
        entries = util.list_entries()
        if query in entries:
            content = markdown2.markdown(util.get_entry(query))
            return render(request, "encyclopedia/content.html", {
            "content": content, "title" : query
            })
        else :
            lst=[]
            for entry in entries:
                if entry.startswith(query):
                    lst.append(entry)
            return render(request, "encyclopedia/index.html" , {
                "entries" : lst
            })

def create(request):
    if request.method=='POST':
        form = NewEntry(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            entries = util.list_entries()
            if title in entries:
                return render(request, "encyclopedia/error.html", {"message": "Page already exist"})
            else:
                util.save_entry(title,content)
                return render(request, "encyclopedia/content.html", {
                "content": content, "title" : title
                })

    return render(request, "encyclopedia/new.html", {
        "form" : NewEntry()
    })

def edit(request, title):
    #title is passed as we wrote <str:title> in url
    #title is passed as we wrote title with the url in edit.html
    if request.method == 'GET':
        page = util.get_entry(title)
        form = NewEntry(initial = {'content': page, 'title':title})
        return render(request,"encyclopedia/edit.html", {
        "form":form })

    else:
        NewEntry(request.POST)

        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            util.save_entry(title,content)
            content = markdown2.markdown(content)
            return render(request, "encyclopedia/content.html", {
            "content": content, "title" : title
            })


def ran(request):
    entries = util.list_entries()
    size = len(entries)
    get = random.randint(0,size-1)
    entry = entries[get]
    content = markdown2.markdown(util.get_entry(entry))
    return render(request, "encyclopedia/content.html", {
    "content": content, "title" : entry
    })
