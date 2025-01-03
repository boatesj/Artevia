from django.contrib import admin
from .models import Category, Artwork

# Custom Admin for Artwork
@admin.register(Artwork)
class ArtworkAdmin(admin.ModelAdmin):
    list_display = ('title', 'price_display', 'category', 'is_featured', 'created_at')
    list_filter = ('category', 'is_featured', 'created_at')
    search_fields = ('title', 'description')

    def price_display(self, obj):
        """Display price formatted in GBP."""
        return f"£{obj.price:.2f}"
    price_display.short_description = "Price (GBP)"


# Default Admin for Category
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

