from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "slug",'sub_title', 'full_name', "author", "created", "updated", 'active' )
    prepopulated_fields = {"slug": ("title",)}
    search_fields  = ['title', 'sub_title']
    #fields = ('title', 'sub_title')
    #def get_queryset(self, request):
    #    return Post.objects.filter(deleted=False)

#admin.site.register(Post, PostAdmin)
#admin.site.register(Post)
