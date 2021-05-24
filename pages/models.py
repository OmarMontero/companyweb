from django.db import models
# from ckeditor.fields import RichTextField

# Create your models here.
class Page(models.Model):
    title = models.CharField( max_length=200)
    content = models.TextField()  # RichTextField --> en lugar de TextField
    slug = models.SlugField(max_length=20, default="None")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "page"
        verbose_name_plural= "pages"
        ordering = ['title']

    def __str__(self):
        return self.title