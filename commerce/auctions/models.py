from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class AuctionListing(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=300)
    # time = models.TimeField()
    # photo = models.ImageField()
    def __str__(self):
        return f"{self.title}"

class Bid(models.Model):
    startingBid = models.IntegerField()
    currentPrice = models.IntegerField()
    # time = models.TimeField()
    listing = models.ForeignKey(AuctionListing, on_delete=models.CASCADE, related_name="bids")

    def __str__(self):
        return f"{self.listing.title}"

class Comment(models.Model):
    comment = models.CharField(max_length=2000)
    # time = models.TimeField()
    listing = models.ForeignKey(AuctionListing, on_delete=models.CASCADE, related_name="comments")
    


