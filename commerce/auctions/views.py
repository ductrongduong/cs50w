from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from PIL import Image
import datetime

from .models import *


def index(request):
    activeListings=AuctionListing.objects.all()
    return render(request, "auctions/index.html", {
        "activeListings" : activeListings
    })
    


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

def create(request):
    if request.method == "POST":
        title = request.POST.get("title").strip()
        description = request.POST.get("description").strip()
        starting = request.POST.get("starting").strip()
        images = request.FILES.getlist('images')

        # im = Image.open(r"C:\Users\PV\OneDrive - Hanoi University of Science and Technology\Pictures\cancelo.jpg")
        # im.show()
        # photo.show()
        # listing = AuctionListing.objects.create(title = title,
        #                         description = description,
        #                         time = datetime.datetime.now())
        for image in images:
            print(type(image))
            listing = AuctionListing.objects.create(
                title=title,
                description=description,
                time = datetime.datetime.now(),
                photo=image,
            )
            bid = Bid(startingBid = request.POST.get("starting").strip(),
                    currentPrice = 0,
                    listing = listing)
            bid.save()
    return render(request, "auctions/create.html")

def listing(request, pk):
    listing = AuctionListing.objects.get(id=pk)
    return render(request, "auctions/listing.html", {
        "pk" : pk,
        "listing" : listing
    })
