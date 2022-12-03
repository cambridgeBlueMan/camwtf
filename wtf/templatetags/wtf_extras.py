from django import template


register = template.Library()


@register.filter
def duration(td):
    total_seconds = int(td.total_seconds())
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60

    if hours == 0 and minutes == 0:
        return ""
    elif hours == 1 and minutes == 0:
        return 'duration: {} hour'.format(hours)
    else:
        return 'duration: {} hour {} min'.format(hours, minutes)
        

