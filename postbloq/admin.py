from django.contrib import admin
from postbloq.models import Category, Comments, Post, ReplyComments
# Register your models here.

admin.site.register(Post)
admin.site.register(Category)


class CommentsAd(admin.ModelAdmin):

    list_display = ["content","created","post"]

admin.site.register(Comments,CommentsAd)

admin.site.register(ReplyComments)