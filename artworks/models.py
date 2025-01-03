from django.db import models
from django.contrib.auth.models import User


# Categories for artworks
class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['name']

    def __str__(self):
        return self.name


# Artists who create and sell artworks
class Artist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='artist_profile')
    bio = models.TextField(blank=True, null=True)
    portfolio_url = models.URLField(blank=True, null=True)
    subscription_status = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Artists"

    def __str__(self):
        return self.user.username


# Patrons who buy artworks and request commissions
class Patron(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='patron_profile')
    wishlist = models.ManyToManyField('Artwork', related_name='wishlisted_by', blank=True)
    purchase_history = models.ManyToManyField('Artwork', related_name='purchased_by', blank=True)

    class Meta:
        verbose_name_plural = "Patrons"

    def __str__(self):
        return self.user.username


# Artworks available for purchase
class Artwork(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='artworks')
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='artworks', default=1)
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='artworks/')
    is_featured = models.BooleanField(default=False)
    availability = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title


# Commissions for custom artwork
class Commission(models.Model):
    STATUS_CHOICES = [
        ('open', 'Open'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    patron = models.ForeignKey(Patron, on_delete=models.CASCADE, related_name='commissions')
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='commissions')
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    due_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='open')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Commission by {self.patron.user.username} to {self.artist.user.username} - {self.status}"


# Transactions for purchases, subscriptions, and commissions
class Transaction(models.Model):
    TRANSACTION_TYPES = [
        ('purchase', 'Purchase'),
        ('subscription', 'Subscription'),
        ('commission', 'Commission'),
    ]

    TRANSACTION_STATUS_CHOICES = [
        ('success', 'Success'),
        ('failed', 'Failed'),
        ('pending', 'Pending'),
    ]

    patron = models.ForeignKey(Patron, on_delete=models.CASCADE, related_name='transactions')
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='transactions', null=True, blank=True)
    artwork = models.ForeignKey(Artwork, on_delete=models.SET_NULL, null=True, blank=True, related_name='transactions')
    commission = models.ForeignKey(Commission, on_delete=models.SET_NULL, null=True, blank=True, related_name='transactions')
    transaction_type = models.CharField(max_length=20, choices=TRANSACTION_TYPES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=TRANSACTION_STATUS_CHOICES, default='success')

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Transaction ({self.transaction_type}) - £{self.amount} by {self.patron.user.username}"
