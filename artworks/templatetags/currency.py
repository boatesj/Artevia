from django import template

register = template.Library()

@register.filter
def currency(value):
    """Format a value as GBP."""
    return f"£{value:.2f}"
