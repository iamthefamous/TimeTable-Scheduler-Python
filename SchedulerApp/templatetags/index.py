from django import template
from django.utils.safestring import mark_safe
from django.utils.html import escape

register = template.Library()

@register.filter
def dictKey(d, k):
    '''Returns the given key from a dictionary.'''

    return ', '.join(d[k]) or ''


@register.simple_tag
def sub(s, d, w, t):
    '''Returns the subject-teacher and room for a section, weekday and time period'''
    for c in s:
        if c.section == d and c.meeting_time.day == w and c.meeting_time.time == t:
            course_name = escape(c.course.course_name)
            instructor_name = escape(c.instructor.name)
            room_number = escape(c.room.r_number)
            room_html = f'<span class="room-number">Room: {room_number}</span>'
            return mark_safe(f'{course_name} ({instructor_name})<br>{room_html}')

    return ''

@register.tag
def active(parser, token):
    args = token.split_contents()
    template_tag = args[0]
    if len(args) < 2:
        raise (template.TemplateSyntaxError, f'{template_tag} tag requires at least one argument')
    return NavSelectedNode(args[1:])

class NavSelectedNode(template.Node):
    def __init__(self, patterns):
        self.patterns = patterns
    def render(self, context):
        path = context['request'].path
        for p in self.patterns:
            pValue = template.Variable(p).resolve(context)
            if path == pValue:
                return 'active'
        return ''