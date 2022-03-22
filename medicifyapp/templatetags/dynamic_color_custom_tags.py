from django import template
from ..models import dynamic_theme_color, footer_dynamic_theme_color

register = template.Library()


# reguler order count


@register.simple_tag
def count_active_campaign_product():
    all_color = dynamic_theme_color.objects.all()
    if all_color:
        all_color = dynamic_theme_color.objects.first()
        return all_color.color_code
    else:
        default_color_code='#07889E'
        return default_color_code


@register.simple_tag
def count_footer_color():
    all_color = footer_dynamic_theme_color.objects.all()
    if all_color:
        all_color = dynamic_theme_color.objects.first()
        return all_color.color_code
    else:
        default_color_code='#07889E'
        return default_color_code