from django import template

register = template.Library()

@register.filter(name='format_name')
def format_name(full_name):
    if not full_name:
        return ''
    parts = full_name.split()
    if len(parts) == 1:
        return parts[0]
    first_name = parts[0]
    last_name = parts[-1]
    initials = f"{first_name[0].upper()}{last_name[0].upper()}"
    return f"{first_name} {last_name} ({initials})"


@register.filter
def initials(full_name):
    if not full_name:
        return ''
    parts = full_name.split()
    if len(parts) == 1:
        return parts[0][0].upper()
    initials = ''.join([part[0].upper() for part in parts if part])
    return initials.upper()