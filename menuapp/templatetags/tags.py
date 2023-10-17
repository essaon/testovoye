from django import template
from menuapp.models import MenuItem

register = template.Library()

@register.inclusion_tag('menuapp/menu.html')
def draw_menu(menu_name):
    menu_items = MenuItem.objects.filter(parent=None)
    return {'menu_items': menu_items, 'menu_name': menu_name}
@register.inclusion_tag('menuapp/submenu.html')
def draw_menu_recursive(menu_items):
    return {'menu_items': menu_items}
