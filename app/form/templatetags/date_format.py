from django import template
from datetime import datetime
from datetime import datetime, timezone, timedelta

register = template.Library()


@register.filter
def date2day(a):
    return datetime.strptime(str(a), '%Y-%m-%d').strftime('%A')



@register.filter
def check_past(a):
    dt = datetime.now()
    my_datetime = datetime.combine(a.date, a.time)
    return my_datetime > dt
