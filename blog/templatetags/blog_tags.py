from django import template
from blog.models import Post,Category
from django.utils import timezone

register = template.Library()

@register.inclusion_tag('popular-posts.html')
def popularposts() :
    posts = Post.objects.filter(status=1).order_by('-counted_views')
    return {'posts':posts}

@register.inclusion_tag('blog-categories.html')
def postcategories() :
    posts = Post.objects.filter(status=1)
    categories = Category.objects.all()
    cat_dict = {}
    for title in categories :
        cat_dict[title]=posts.filter(category=title).count()
    return {'categories':cat_dict}

@register.inclusion_tag('latest-posts.html')
def latestposts() :
    posts = Post.objects.filter(status=1,published_date__lte=timezone.now()).order_by('-published_date')
    return {'posts':posts}




