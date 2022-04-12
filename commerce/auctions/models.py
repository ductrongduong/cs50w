from django.contrib.auth.models import AbstractUser
from django.db import models



class AuctionListing(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=300)
    time = models.TimeField(null=True )
    photo = models.ImageField(null=True, blank=False)
    def __str__(self):
        return f"{self.title}"

class User(AbstractUser):
    listings = models.ManyToManyField(AuctionListing, blank=True, related_name="watchlist")
    pass

class Bid(models.Model):
    id = models.AutoField(primary_key=True)
    startingBid = models.IntegerField()
    currentPrice = models.IntegerField()
    time = models.TimeField(null=True)
    listing = models.ForeignKey(AuctionListing, on_delete=models.CASCADE, related_name="bids")

    def __str__(self):
        return f"{self.listing.title}"

class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    comment = models.CharField(max_length=2000)
    time = models.TimeField(null=True)
    listing = models.ForeignKey(AuctionListing, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bids")

    


