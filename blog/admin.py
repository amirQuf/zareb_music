from django.contrib import admin

from .models import Blog , Category


class BlogAdmin(admin.ModelAdmin):
  list_display=('title','slug','publish_time','status','created',"cat_to_str")
  list_filter = ('status' , 'publish_time')
  search_fields =('slug','title', 'desc')
  ordering =['-publish_time', 'status'] 
  def cat_to_str(self ,obj):
    return ",".join([cat.body for cat in obj.category.all()])
  cat_to_str.short_description = "categorys"     
admin.site.register(Blog ,BlogAdmin )


class CatAmin(admin.ModelAdmin):
  list_display=('body','slug','status','created','position')
  list_filter = ('status' , 'created')
  search_fields =('slug', 'body')
  ordering =['-created', 'status'] 
admin.site.register(Category ,CatAmin)


