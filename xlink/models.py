from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.template.defaultfilters import slugify # new
from django.contrib.auth.models import AbstractUser, UserManager
from django.conf import settings
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse, reverse_lazy
User = get_user_model()
# from accounts.models import User
class Category(models.Model):
    name = models.CharField('カテゴリー', max_length=100)

    def __str__(self):
        return self.name
class Account(models.Model):
    HOBBIES ={
        ('読書', '読書'),
        ('ゲーム', 'ゲーム'),
        ('映画', '映画'),
        ('TV', 'TV'),
        ('運動', '運動'),
        ('PC', 'PC'),
        ('VR/AR', 'VR/AR'),
        ('プログラミング', 'プログラミング')
    }
    DETAILS = {
        ('小学生', '小学生'),
        ('中学生', '中学生'),
        ('高校生', '高校生'),
        ('大学生', '大学生'),
        ('社会人', '社会人'),
    }
    mainuser = models.ForeignKey(User,  on_delete=models.PROTECT, verbose_name="メインユーザー", blank=True, null=True)
    # name = models.ForeignKey(User,on_delete=models.CASCADE, verbose_name='ユーザー名', blank=True, null=True)
    name = models.CharField(max_length=15, verbose_name='ユーザー名', blank=True, null=True, default="")
    image = models.ImageField(upload_to='image/', verbose_name="バックイメージ")
    icon = models.ImageField(upload_to='icon/', verbose_name="アイコン")
    infomation = models.TextField(max_length=180, verbose_name="紹介文",blank=True, null=True)
    hobby =  models.CharField(max_length=8, choices=HOBBIES)
    detail = models.CharField(max_length=8, choices=DETAILS)
    created_at = models.DateTimeField(auto_now_add=True,null=True  ,verbose_name='作成日')
    def __str__(self):
        return str(self.name)
    class Meta:
        verbose_name_plural = 'Account'
class Group(models.Model):
    # managername = models.ForeignKey(Account,blank=True, null=True,on_delete=models.PROTECT ,verbose_name="管理者名", default="")
    mainuser = models.ForeignKey(User,  on_delete=models.PROTECT, verbose_name="メインユーザー", blank=True, null=True)
    managername = models.ForeignKey(Account, null=True,on_delete=models.CASCADE,verbose_name="管理者")
    name = models.CharField(max_length=30, blank=True, null=True, verbose_name="Class名")
    category = models.ForeignKey(Category, verbose_name="ジャンル", on_delete=models.PROTECT)
    web_site = models.URLField(blank=True)
    backimage = models.ImageField(upload_to='backimage/', verbose_name="BackImage")
    icon = models.ImageField(upload_to='classicon/', verbose_name="クラスアイコン", null=True)
    index = models.CharField(max_length=50, blank=False, null=True, verbose_name = "見出し")
    explain = models.TextField(max_length=180, blank=True, verbose_name="explain")
    created_at = models.DateField(null=True ,auto_now_add=True, blank=True, verbose_name='作成日')
    def __str__(self):
        return str(self.name)
    class Meta:
        verbose_name_plural = 'ClassName'
class Comment(models.Model):
    destination = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="投稿先", null=True, blank=True)
    mainuser = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="メインユーザー", blank=True, null=True)
    user = models.ForeignKey(Account,on_delete=models.CASCADE, null=True)
    text = models.TextField(max_length=200, null=True, verbose_name=None)
    image = models.FileField(upload_to='post/',null=True,blank=True , verbose_name=None)
    video = models.FileField(upload_to='video/', null=True, blank=True, verbose_name=None)
    created_at = models.DateTimeField(auto_now_add=True,null=True  ,verbose_name='作成日')
    def __str__(self):
        return str(self.text)
    class Meta:
        verbose_name_plural = 'Comments'
class FollowersCount(models.Model):
    user = models.CharField(max_length=10000)
    follower= models.CharField(max_length=10000)
    # このfollowerは現在ログインしている方
    def __str__(self):
        return self.user
#         # return '%s - [ %s ]' % (self.user, self.follower)
class CommentCount(models.Model):
    # このgroupはcommentを送ったところ
    classname = models.CharField(max_length=1000000)
    # このcommentは投稿したcomment数
    comment = models.CharField(max_length=100000)
    def __str__(self):
        return self.classname
class ReturnComment(models.Model):
    # コメントモデルからテキストを取得する。(テキストが唯一の単一で判別できるもの)
    class_name = models.ForeignKey(Group, on_delete=models.CASCADE, blank=True, verbose_name="class先")
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True,related_name="returncomments")
    user = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
    text = models.TextField(max_length=158, null=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True  ,verbose_name='作成日')
    def __str__(self):
        return str(self.comment)
    class Meta:
        verbose_name_plural = 'ReturnComments'
class Root(models.Model):
    group = models.CharField(max_length=10000000)
    rooter = models.CharField(max_length=1000000)
    # rooter = models.ForeignKey(Group, on_delete=models.CASCADE, null=True, related_name="ルーター")
    user = models.CharField(max_length=10000000)
    def __str__(self):
        return self.group
class FollowCount(models.Model):
    follower = models.CharField(max_length=1000000)
    user = models.CharField(max_length=10000000)
    def __str__(self): 
        return str(self.follower)
class AccountRoot(models.Model):
    rooter = models.CharField(max_length=100000)
    user = models.CharField(max_length=100000)
    def __str__(self): 
        return str(self.rooter)
class Recommendation(models.Model):
    recommending_user = models.ForeignKey(User, on_delete=models.CASCADE)
    recommended_group = models.ForeignKey(Group, on_delete=models.CASCADE)
class Rooter(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name