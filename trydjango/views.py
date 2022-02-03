"""
to render HTML Files
"""
import random
from django.http import HttpResponse
from django.template.loader import render_to_string
from articles.models import Article


#   routied to here  by /  from urls.py
def home_view(request, *args, **kwargs):
    """       take in a request  return an HTML reponse     """
    print('why are we in homer view   z z z z z z')
       
    
    article_obj = Article.objects.all().first()
    article_queryset = Article.objects.all()
    context = {
        "object_list": article_queryset,
        "object": article_obj,
       }
    # Django Templates
    HTML_STRING = render_to_string("home-view.html",context = context)
    # HTML_STRING = """  
    # <h1>{title} (id : {id}) ! </h1> 
    # <p> {content}  </p>
    # """ .format(**content)
    return HttpResponse(HTML_STRING)



