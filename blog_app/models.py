from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify
class Category(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    is_published = models.DurationField(default=timezone.timedelta(days=23,hours=21,minutes=43,seconds=54))
    slug = models.SlugField(unique=True, blank=True, null=True)
    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.title)
        super(Category, self).save()
    def __str__(self):
        return f"{self.title} "

class Article(models.Model):
    # author = models.ForeignKey(User,on_delete=models.SET_NULL , null= True , blank= True)
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name="user_name_author")
    category = models.ManyToManyField(Category,related_name="category_name")
    title = models.CharField(max_length=70)
    short_description = models.CharField(max_length=200)
    body = models.TextField()
    # image = models.ImageField(upload_to="images/articles")
    created = models.DateTimeField(auto_now_add=True)
    updetad = models.DateTimeField(auto_now=True)
    is_published = models.DurationField(default=timezone.timedelta(days=23,hours=21,minutes=43,seconds=54))
    slug = models.SlugField(unique= True,blank=True,null=True )
    class Meta:
        ordering =  ("-updetad","-created")
    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.title)
        super(Article, self).save()
    def __str__(self):
        return f"{self.title} - {self.body[:30]}"
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete= models.CASCADE,related_name= "comments")
    parent = models.ForeignKey("self", on_delete=models.CASCADE,null=True ,blank=True,related_name="replies")
    user = models.ForeignKey(User , on_delete= models.CASCADE ,related_name="comments")
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.article} - {self.body[:50]}"