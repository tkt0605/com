from django.contrib import admin
from .models import Account, Group, Comment, Category,CommentCount, ReturnComment, Root, FollowCount, AccountRoot, FollowersCount, Rooter
# Register your models here.
admin.site.register(Account) 
admin.site.register(Comment) 
admin.site.register(Category)
admin.site.register(Group)
admin.site.register(CommentCount)
admin.site.register(ReturnComment)
admin.site.register(Root)
admin.site.register(FollowCount)
admin.site.register(AccountRoot)
admin.site.register(FollowersCount)
admin.site.register(Rooter)