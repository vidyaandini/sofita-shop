from django import template

register = template.Library()

@register.filter
def rupiah(value):
    try:
        value = int(value)
        return f"Rp {value:,.0f}".replace(",", ".")
    except (ValueError, TypeError):
        return value
