from django.shortcuts import render
import markdown2
from django.shortcuts import redirect
import random


from . import util


def index(request):
    if request.method == "POST":
        search = request.POST
        return redirect('entry',search["title"])
    return render(request, "encyclopedia/index.html", {
        "heading": 'All Pages',
        "entries": util.list_entries()
    })

def wiki (request,title):
    if util.get_entry(title) == None:
        searchList = []
        for item in util.list_entries():
            if title in item.lower():
                searchList.append(item)
        if not searchList:
            pageTitle = '404 error'
            pageContent = f'Sorry, we couldn\'t find "{title}"'
        else:
            return render (request,"encyclopedia/index.html", {
                "heading": 'Did you mean?',
                "entries": searchList
            })
    else:
        pageTitle = title
        pageContent = markdown2.markdown(util.get_entry(title))
    return render(request,"encyclopedia/entry.html",{
        "title": pageTitle,
        "content": pageContent
    })

def createNew (request):
    if request.method == "POST":
        newPage = request.POST
        title = newPage["title"]
        if util.get_entry(title) == None:
            content = newPage["content"]
            util.save_entry(title,content)
            return redirect('entry',newPage["title"])
        else:
            return render(request,"encyclopedia/entry.html",{
                "title": 'Error',
                "content": 'This page alrealdy exists, try using another title'
            })
    return render (request,"encyclopedia/new.html")

def randomPage (self):
    choice = random.choice(util.list_entries())
    return redirect('entry',choice)

def editPage (request,title):
    if request.method == "POST":
        edited = request.POST
        title = edited["title"]
        content = edited["content"]
        util.save_entry(title,content)
        return redirect('entry',title)
    return render(request,"encyclopedia/edit.html",{
        "title":title,
        "content":util.get_entry(title)
    })

