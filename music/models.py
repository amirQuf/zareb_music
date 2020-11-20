from django.db import models
from django.utils import timezone 
# Create your models here.

class Album(models.Model):
  name = models.CharField(max_length=200 ,verbose_name='نام البوم')
  rapper =models.CharField(max_length=200 ,verbose_name='نام خواننده')
  slug = models.SlugField(unique=True,verbose_name='ادرس')
  cover = models.ImageField(upload_to ='music-cover', verbose_name='کاور')
  publish_time = models.DateTimeField(default=timezone.now,verbose_name='زمان انتشار')
  created =models.DateTimeField(auto_now_add=True)
  update = models.DateTimeField(auto_now=True)
  label =models.CharField(max_length=50 ,verbose_name=' لیبل', blank =True , null =True)
  def __str__(self):
    return self.name
  
  class Meta:
    verbose_name='البوم'
    verbose_name_plural = 'البوم ها'
    ordering = ['publish_time']



class Music(models.Model):
  name = models.CharField(max_length=200 ,verbose_name='نام اهنگ')
  rapper =models.CharField(max_length=200 ,verbose_name='نام خواننده')
  album = models.ForeignKey(Album,blank =True , null =True,on_delete = models.CASCADE)
  label =models.CharField(max_length=50 ,verbose_name=' لیبل', blank =True , null =True)
  mix_mastering = models.CharField(max_length=200,blank =True , null =True)
  cover = models.ImageField(upload_to ='music-cover', verbose_name='کاور')
  cover_art = models.CharField(max_length=100 , blank =True , null =True)
  file = models.FileField(upload_to='music_file',verbose_name='فایل صوتی ')
  slug =models.SlugField(unique=True,verbose_name='ادرس')
  publish_time = models.DateTimeField(default=timezone.now,verbose_name='زمان انتشار')
  created =models.DateTimeField(auto_now_add=True)
  update = models.DateTimeField(auto_now=True)
  show =models.BooleanField(default = True,verbose_name='نمایش/عدم نمایش')
  des  = models.TextField(verbose_name = 'توضیحات', blank =True , null =True)

  def __str__(self):
    return self.name
  
  class Meta:
    verbose_name='موسیقی'
    verbose_name_plural = 'موسیقی ها'
    ordering = ['publish_time']