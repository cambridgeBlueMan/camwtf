# to run this from django shell

# >>> exec(open('soup/soup3.py').read())

from blog.models import Blog

b = Blog(name='stones blog', tagline='All the latest Stones news.')
b.save()