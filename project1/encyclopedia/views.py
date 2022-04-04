from django.shortcuts import render, redirect
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect
import os
from markdown2 import markdown
from random import randint

from . import util



def index(request):
    if request.method == "POST":
        form = SearchEntryForm(request.POST)
        if form.is_valid():
            dataSearch = form.cleaned_data["dataSearch"]
            result = util.search(dataSearch)
            if result[0] :
                return render(request, "encyclopedia/content.html", {
                    "name": dataSearch,
                    "content": util.get_entry(dataSearch),
                    "form": SearchEntryForm()
                })
            else:
                return render(request, "encyclopedia/index.html", {
                    "entries": result[1],
                    "form" : SearchEntryForm()
                })
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "form" : SearchEntryForm()
    })

def entry(request, name):
    content = util.get_entry(name)
    content = markdown(content)
    return render(request, "encyclopedia/content.html", {
        "name": name,
        "content": content,
        "form": SearchEntryForm()
    })


def search(request):
    if request.method == "POST":
        form = SearchEntryForm(request.POST)
        if form.is_valid():
            dataSearch = form.cleaned_data["dataSearch"]
            result = util.search(dataSearch)
            if result[0] :
                return render(request, "encyclopedia/content.html", {
                    "name": dataSearch,
                    "content": util.get_entry(dataSearch),
                    "form": SearchEntryForm()
                })
            else:
                return render(request, "encyclopedia/index.html", {
                    "entries": result[1],
                    "form" : SearchEntryForm()
                })
            

def newpage(request):
    if request.method == "POST":
        form = CreateNewPageForm(request.POST)
        if form.is_valid():
            entry = form.cleaned_data['entry']
            content = form.cleaned_data['content']
            path = 'D:/ProgramFile/VS-Code/Web-Programming/wiki/entries/' + entry + '.md'
            if os.path.exists(path):
                return render(request, "encyclopedia/newpage.html", {
                    "entry" : entry,
                    "exist" : True,
                    "form" : SearchEntryForm(),
                    "formCreateNewPage" : CreateNewPageForm()
                })
            else:
                with open(path, 'w'): pass
                f = open(path, 'a')
                f.write(content)
                f.close()
                return render(request, "encyclopedia/content.html", {
                    "name": entry,
                    "content": util.get_entry(entry),
                    "form": SearchEntryForm()
                })


    return render(request, "encyclopedia/newpage.html", {
        "exist" : False,
        "form" : SearchEntryForm(),
        "formCreateNewPage" : CreateNewPageForm()
    })

def editpage(request, title):
    content = util.get_entry(title.strip())

    if request.method == "POST":
        content = request.POST.get("content").strip()
        util.save_entry(title, content)
        return render(request, "encyclopedia/content.html", {
        "name": title,
        "content": content,
        "form": SearchEntryForm()
    })

    return render(request, "encyclopedia/editpage.html", {'content' : content, 'title' : title})

def random_page(request):
    entries = util.list_entries()
    random_title = entries[randint(0, len(entries)-1)]
    return render(request, "encyclopedia/content.html", {
        "name": random_title,
        "content": util.get_entry(random_title),
        "form": SearchEntryForm()
        })



class SearchEntryForm(forms.Form):
    dataSearch = forms.CharField(label = "Search")

    def search(request):
        return render(request, "encyclopedia/index.html", {
            "form" : SearchEntryForm()
        })

class CreateNewPageForm(forms.Form):
    entry = forms.CharField(label = "entry")
    content = forms.CharField(widget=forms.Textarea(attrs={'name':'body', 'rows':'3', 'cols':'5'}))
    def search(request):
        return render(request, "encyclopedia/index.html", {
            "form" : SearchEntryForm()
        })

