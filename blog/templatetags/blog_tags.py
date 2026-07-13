from django import template
from blog.models import Post

register = template.Library()

@register.inclusion_tag('popular-posts.html')
def popularposts() :
    posts = Post.objects.filter(status=1).order_by('-counted_views')
    return {'posts':posts}

