from django.shortcuts import render

from . import util
import markdown2



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
        return render(request, "encyclopedia/error.html")

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
