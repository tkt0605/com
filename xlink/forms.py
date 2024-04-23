from django import forms
from django.contrib.auth.models import User
from accounts.models import User
from .models import Account, Group, Comment, ReturnComment
class RegisterForm(forms.ModelForm):
	class Meta:
		model = User
		fields = "__all__"
	def save(self, commit=True):
		user = super().save(commit=False)
		user.name = self.cleaned_data["email"]
		if commit:
			user.save()
			return user.name  
class AccountForm(forms.ModelForm):
	class Meta:
		model = Account
		fields = ('__all__')
		exclude=['mainuser', 'name', 'image', 'icon', 'infomation', 'hobby', 'detail']
		widgets = {
            'infomation': forms.Textarea(
                attrs={'placeholder': 'ユーザーの自己紹介'}
            ),
			'explain': forms.Textarea(
                attrs={'placeholder': 'ユーザーの基本情報'}
            ),

        }
	def __init__(self,mainuser=None,name=None , *args, **kwargs):
		self.mainuser = mainuser
		self.name = name 
		super().__init__(*args, **kwargs)
	def save(self, commit=True):
		xlink_obj = super().save(commit=False)
		if self.mainuser:
			xlink_obj.mainuser = self.mainuser
			xlink_obj.name = self.name
			if commit==True:
				xlink_obj.save()
		return xlink_obj.mainuser
class ClassCreateForm(forms.ModelForm):
	class Meta:
		model = Group
		fields = '__all__'
		exclude=['mainuser', 'managername']
		widgets = {
			'name' : forms.TextInput(
				attrs={
			'placeholder': 'クラス名(dotto is not )',
			'min-length': 8,
			}
			),
			'explain': forms.Textarea(
				attrs={'placeholder': 'クラスの基本的な説明'}
			),
			'web_site':forms.TextInput(
			attrs={
			'placeholder': '@(サイトのリンク)',
			}
			),
			'index':forms.TextInput(
			attrs={
			'placeholder': '@(見出し/必須)',
			}
			),
			'root':forms.TextInput(
			attrs={
			'placeholder': '@(Your Approach class)',
			}
			),
		}
		# forms.widgets.Select
		required=True,
	def __init__(self,mainuser=None , managername=None, *args, **kwargs):
		self.managername = managername
		self.mainuser = mainuser
		super().__init__(*args, **kwargs)
	def save(self, commit=True):
		xlink_obj = super().save(commit=False)
		if self.managername:
			xlink_obj.managername = self.managername
			xlink_obj.mainuser = self.mainuser
			if commit==True:
				xlink_obj.save()
		return xlink_obj.managername
class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		exclude = ["user", "destination", 'mainuser']
		widgets = {
 			'text':forms.Textarea(
 			attrs={
			'placeholder': "what's goning on ?",
			'rows':5, 'cols':15,
			'id': 'text-bord',
			},
			),
		}
	def __init__(self,user=None , destination=None,*args, **kwargs):
		self.user = user
		self.destination = destination
		# self.mainuser = mainuser
		super().__init__(*args, **kwargs)
	def save(self, commit=True):
			kwargs = super(CommentForm, self).save(commit=False)
			if self.user:
				kwargs.user = self.user
				kwargs.destination = self.destination
				# kwargs.mainuser = self.mainuser
				if commit==True:
					kwargs.save()
			return kwargs.user
class ReturnCommentForm(forms.ModelForm):
	class Meta:
		model = ReturnComment
		exclude = ["user","comment", "class_name"]
		widgets = {
 			'text':forms.Textarea(
 			attrs={
			'placeholder': "what's goning on ?",
			'rows':5, 'cols':15,
			'id': 'text-bord',
			},				
 		),
		    'image': forms.TextInput(
			attrs={
			'id': 'image_bord',
			'class': 'mt-5',
			}
			)
		}
	def __init__(self,user=None ,comment=None,class_name=None, *args, **kwargs):
		self.user = user
		self.comment = comment
		self.class_name = class_name
		super().__init__(*args, **kwargs)
	def save(self, commit=True):
			kwargs = super(ReturnCommentForm, self).save(commit=False)
			if self.user:
				kwargs.user = self.user
				kwargs.comment = self.comment
				kwargs.class_name = self.class_name
				if commit==True:
					kwargs.save()
			return kwargs.user
class ProfileEditForm(forms.ModelForm):
	class Meta:
		model = Account
		exclude =["mainuser", "name"]
	def __init__(self,mainuser=None, name=None, *args, **kwargs):
		self.mainuser = mainuser
		self.name = name
		super().__init__(*args, **kwargs)
	def save(self, commit=True):
		kwargs = super(ProfileEditForm, self).save(commit=False)
		if self.mainuser:
			kwargs.mainuser = self.mainuser
			kwargs.name = self.name
			if commit == True:
				kwargs.save()
		return kwargs.name 