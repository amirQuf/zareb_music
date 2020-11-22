from django.db import models
from django.utils import timezone 

class Category(models.Model):
  #parent  = models.ForeignKey(Category)
  body =models.CharField(max_length= 30)
  slug = models.SlugField(unique=True)
  status =models.BooleanField()
  position = models.IntegerField()
  created = models.DateTimeField(auto_now_add =True)    
  def __str__(self):
    return self.body
  class Meta:
    verbose_name='دستهبندی'
    verbose_name_plural = 'دسته بندی ها'
    ordering =('position',)



class Blog(models.Model):
  STATUS_CHOICIES=(('p', 'انتشار'),('d', 'پیش نویس'))
  title =models.CharField(max_length=200 ,verbose_name='عنوان')
  cover = models.ImageField(upload_to ='blog-cover', verbose_name='عکس بندانگشتی')
  desc  = models.TextField(verbose_name = 'توضیحات', blank =True , null =True)
  slug =models.SlugField(unique=True,verbose_name='ادرس')
  publish_time = models.DateTimeField(default=timezone.now,verbose_name='زمان انتشار')
  created =models.DateTimeField(auto_now_add=True)
  update = models.DateTimeField(auto_now=True)
  status = models.CharField(max_length=1, choices= STATUS_CHOICIES)
  pin = models.BooleanField(default=False)
  category = models.ManyToManyField(Category)
  def __str__(self):
    return self.title
  class Meta:
    verbose_name='وبلاگ'
    verbose_name_plural = 'وبلاگ ها'
    ordering = ['publish_time']