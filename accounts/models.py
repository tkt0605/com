from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
class UserManager(BaseUserManager):
    def create_user(self,username , email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(email=self.normalize_email(email),username=username,)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self,username, email, password):
        user = self.create_user(username=username,email=email,password=password,)
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self,username, email, password):
        user = self.create_user(username,email,password=password,)
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    email = models.EmailField(verbose_name='Eメールアドレス',max_length=255,unique=True,null=True)
    username=models.CharField(verbose_name='フルネーム',max_length=255,unique=True,null=True)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False) 
    admin = models.BooleanField(default=False) 
    REQUIRED_FIELDS = ['username']
    USERNAME_FIELD = 'email'

    objects = UserManager()
    def __str__(self):             
        return self.email

    def has_perm(self, perm, obj=None):
        return self.admin

    def has_module_perms(self, app_label):
        return self.admin
    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active