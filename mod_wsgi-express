from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import  render, redirect
from .forms import AccountForm, ClassCreateForm, CommentForm, ReturnCommentForm
from django.contrib import messages
from django.contrib.auth import login
from .models import Account, Group, Comment, Category, FollowersCount, CommentCount, ReturnComment, Root, FollowCount, AccountRoot
from django.views import generic
from django.views.generic import ListView
from django.db.models import Q
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
User = get_user_model()
def index(request):
    template = loader.get_template('index.html')
    context_instance = {
        'csrf_token': '',
    }
    return HttpResponse(template.render(context_instance, request))
# def home(request):
#     template = loader.get_template('home.html')
#     context = {
#         'csrf_token': '',
#     }
#     return HttpResponse(template.render(context, request))
def rooms(request):
	rooms = Account.objects.order_by('-name')[:10000]
	template=loader.get_template('header.html', 'home.html')
	context={
		'csrf_token': '',
		'rooms': rooms,
	}
	return HttpResponse(template.render(context, request))
def accounts(request):
	accounts = Group.objects.order_by('-created_at')[:1000000]
	rooms = Account.objects.order_by('-name')[:10000]
	template=loader.get_template('home.html')
	context={
		'csrf_token': '',
		'accounts': accounts,
		'rooms': rooms
	}
	return HttpResponse(template.render(context, request))
def account(request,name):
	account= Group.objects.get(name=name)
	template = loader.get_template('class.html')
	context={
		'account': account,
	}
	return HttpResponse(template.render(context, request))
def profiles(request):
	template = loader.get_template('header.html', 'profile.html')
	rooms = Account.objects.order_by('-name')[:10000]
	context ={
		'rooms': rooms
	}
	return HttpResponse(template.render(context, request))
def groups(request):
	groups =Account.objects.order_by('name')[:100000]
	template=loader.get_template('class.html')
	context={
		'csrf_token': '',
		'groups': groups,
	} 
	return HttpResponse(template.render(context, request))
def comments(request):
	comments=Comment.objects.order_by('-created_at')[:10000]
	accounts = Account.objects.order_by('name')[:10000]
	template=loader.get_template('room.html')
	context={
		'comments':comments,
		'accounts': accounts,
	}
	return HttpResponse(template.render(context, request))
def room(request, name):
	name = Account.objects.get(name=name)
	group = Group.objects.filter(managername=name)
	accounts = Account.objects.order_by('-created_at')[:1000]
	comments = Comment.objects.order_by('-created_at')[:10000]
	rooms = Account.objects.order_by('-name')[:10000]
	# notifications = AccountNotification.objects.order_by('-created_at')[:100000]
	current_user = request.GET.get('user')
	logged_in_user = request.user.username
	user_followers = len(FollowCount.objects.filter(user=name))	
	user_following = len(FollowCount.objects.filter(follower=name))
	user_followers0 = FollowCount.objects.filter(user=name)
	followers = FollowCount.objects.filter(user=name)
	followings = FollowCount.objects.filter(follower=name)
	user_root0 = AccountRoot.objects.filter(rooter=name)
	rooters = AccountRoot.objects.filter(user=name)
	roots = AccountRoot.objects.filter(rooter=name)
	root_class=[]
	user_followers1 = []
	for i in user_followers0:
		user_followers0 = i.follower
		user_followers1.append(user_followers0)
	if logged_in_user in user_followers1:
		follow_button_value = 'following'
	else:
		follow_button_value = 'follow'
	for x in user_root0:
		user_root0 = x.user
		root_class.append(user_root0)
	if logged_in_user in root_class:
		root_button_value = 'rooting'
	else:
		root_button_value = 'root'
	template = loader.get_template('profile.html')
	context={
		'rooms':rooms, 
		'room': name,
		'comments': comments,
		'roots': roots,
		# 'notifications': notifications,
		'followers': followers,
		'followings': followings,
		'groups': group,
		'accounts': accounts,
		'rooters': rooters,
		'user_root0': user_root0,
		'user_followers0': user_followers0,
		'current_user': current_user,
		'logged_in_user': logged_in_user,
		'user_followers': user_followers,
		'user_following': user_following,
		'follow_button_value': follow_button_value,
		'root_button_value':root_button_value,
	}
	return HttpResponse(template.render(context, request))
def communitys(request):
	rooms = Account.objects.order_by('-name')[:10000]
	template=loader.get_template('header.html', 'class.html')
	context={
		'csrf_token': '',
		'rooms': rooms,
	}
	return HttpResponse(template.render(context, request))
def community(request,name):
	current_user = request.GET.get('user')
	logged_in_user = request.user.username
	groups= Group.objects.order_by('-created_at')[:10000]
	rooms = Account.objects.order_by('-created_at')[:1000]
	comments = Comment.objects.order_by('-created_at')[:100000]
	return_comments = ReturnComment.objects.order_by('-created_at')[:10000]
	# notifications = Notification.objects.order_by('-created_at')[:100000]
	manages=Group.objects.filter(mainuser=request.user)
	name = Group.objects.get(name=name)
	user_followers = len(FollowersCount.objects.filter(user=name))	
	user_following = len(FollowersCount.objects.filter(follower=current_user))
	user_comments=len(CommentCount.objects.filter(classname=name))
	# return_comments_numbers = len(ReturnComment.objects.get(class_name = name))
	user_followers0 = FollowersCount.objects.filter(user=name)
	followers = FollowersCount.objects.filter(follower=name)
	followings = FollowersCount.objects.filter(user=name)
	rooters = Root.objects.filter(group=name)
	roots = Root.objects.filter(rooter=name)
	root_class=[]
	user_followers1 = []
	for i in user_followers0:
		user_followers0 = i.follower
		user_followers1.append(user_followers0)
	if logged_in_user in user_followers1:
		follow_button_value = 'unfollow'
	else:
		follow_button_value = 'follow'
	for root in rooters:
		class_rooter_id = root.user
		root_class.append(class_rooter_id)
	if logged_in_user in root_class:
		root_button_value = 'unroot'
	else:
		root_button_value = 'root'
	template  = loader.get_template('class.html')
	context = {
		# 'notifications': notifications,
		# 'class': roots,x
		'rooms': rooms,
		'groups': groups,
		'comments': comments,
		'return_comments': return_comments,
		'community':name,
		'manages': manages, 
		'roots': roots,
		'rooters': rooters,
		'current_user': current_user,
		'followers': followers,
		'followings': followings,
		'logged_in_user': logged_in_user,
		'user_followers': user_followers,
		'user_comments': user_comments,
		'user_following ': user_following,
		'follow_button_value': follow_button_value,
		'root_button_value':root_button_value,
	}
	return HttpResponse(template.render(context, request))
def root_selecter(request):
	if request.method == "POST":
		value = request.POST["value"]
		user = request.POST["user"]
		group = request.POST["group"]	
		rooters= request.POST.getlist("rooter") 
		# rooters = request.POST["rooter"]
		# rooters = Group.objects.get(name=root)
		if value == 'root':
			for rooter in rooters:
				root_sel=Root.objects.create(group=group, rooter=rooter, user=user)
				root_sel.save()
		else: 
			for rooter in rooters:
				root_sel=Root.objects.filter(group=group, rooter=rooter, user=user)
				root_sel.delete()
		return redirect('/community/' + group)
def follow_counts(request):
	if request.method == "POST":
		value = request.POST["value"]
		user = request.POST['user']
		follower = request.POST['follower']
		if value == 'follow':
			followers_cnt = FollowCount.objects.create( user=user, follower=follower)
			followers_cnt.save()
		else:
			followers_cnt = FollowCount.objects.get(user=user, follower=follower)
			followers_cnt.delete()
		return redirect('/account/'+ user )
def root_count(request):
	if request.method == "POST":
		value = request.POST["value"]
		user = request.POST["user"]
		rooter= request.POST["rooter"]
		if value == "root":
			root_sel = AccountRoot.objects.create(user=user, rooter=rooter)
			root_sel.save()
		else:
			root_sel = AccountRoot.objects.get(user=user, rooter=rooter)
			root_sel.delete()
		return redirect('/account/'+ rooter)
def follow_count(request):
	if request.method == "POST":
		value = request.POST["value"]
		user = request.POST['user']
		follower = request.POST['follower']
		if value == 'follow':
			followers_cnt = FollowersCount.objects.create(user=user, follower=follower)
			followers_cnt.save()
		else:
			followers_cnt = FollowersCount.objects.get(user=user, follower=follower)
			followers_cnt.delete()
		return redirect('/community/'+ user )
def class_request(request):
	if request.method == "POST":
		form = ClassCreateForm(request.POST)
		if form.is_valid():
			users = form.save()
			if users is not None:
				login(request, users)
				messages.success(request, "Create class successful." )			
			return redirect("/")
		messages.error(request, "Unsuccessful create class. Invalid information.")
	form = ClassCreateForm()
	return render (request=request, template_name="create.html", context={"create_form":form})
class IndexView(ListView):
	model = Group
	template_name = "home.html"
	def get_queryset(self):
		queryset = Group.objects.order_by("-class_name")
		keyword = self.request.GET.get("keyword")
		if keyword:
			queryset = queryset.filter(
				Q(class_name__icontains=keyword) | Q(genre__icontains=keyword)
			)
		return queryset
def categorys(request, name):
	categorys = Category.objects.get(name=name)
	accouunts = Group.objects.filter(category=categorys)
	return render(request, 'home.html', {'category': categorys, 'accounts':accouunts})
def comment(request,pk):
    template = loader.get_template('class.html')
    comment = Comment.objects.get(pk=pk)
    context = {
        'comment': comment
    }
    return HttpResponse(template.render(context, request))

def return_comments(request):
	template = loader.get_template('class.html')
	return_comments = ReturnComment.objects.order_by('created_at')[:100000]
	context = {
		'return_comments': return_comments
	}
	return HttpResponse(template.render(context, request))
def return_comment(request, pk):
	template = loader.get_template('class.html')
	return_comment = ReturnComment.objects.get(pk=pk)
	context={
		'return_comment': return_comment
	}
	return HttpResponse(template.render(context, request))
class CreateAccountView(generic.CreateView):
	form_class=AccountForm
	template_name = "account.html"
	success_url="/"
	def get_form_kwargs(self,*args, **kwargs):
		xlink_obj = super().get_form_kwargs(*args, **kwargs)
		form = AccountForm(self.request.POST, instance=User)
		# form.instance.name = self.kwargs['name']
		xlink_obj['mainuser'] = self.request.user
		xlink_obj['name'] = self.request.user.username
		# xlink_obj['name'] = Account.objects.get(name=form.instance.name)
		return xlink_obj
form_create=CreateAccountView.as_view()
class CreateClassView(generic.CreateView):
	form_class = ClassCreateForm
	template_name="create.html"
	success_url = '/'
	def get_form_kwargs(self,*args, **kwargs):
		xlink_obj = super().get_form_kwargs(*args, **kwargs)
		form = ClassCreateForm(self.request.POST, instance=Account)
		form.instance.name = self.request.user.username
		xlink_obj['mainuser'] = self.request.user
		xlink_obj['managername'] = Account.objects.get(name=form.instance.name)
		return xlink_obj
form_class = CreateClassView.as_view()
class CreateCommentView(generic.CreateView):
	form_class = CommentForm
	template_name="comment.html"
	success_url = '/'
	def get_form_kwargs(self,*args, **kwargs):
		kwargs = super().get_form_kwargs(*args, **kwargs)
		form = CommentForm(self.request.POST, self.request.FILES,  instance=Group and Account)
		form.instance.name = self.kwargs['name']
		form.instance.user = self.request.user.username
		form.instance.text = Comment.text
		kwargs['user'] = Account.objects.get(name=form.instance.user)
		kwargs['destination'] = Group.objects.get(name=form.instance.name)
		return kwargs
form_comment=CreateCommentView.as_view()
class CreateReturnComment(generic.CreateView):
	form_class = ReturnCommentForm
	template_name="return.html"
	success_url = '/'
	def get_form_kwargs(self,*args, **kwargs):
		kwargs = super().get_form_kwargs(*args, **kwargs)
		form = ReturnCommentForm(self.request.POST, instance=Comment and Group and Account)
		form.instance.comment= self.kwargs['pk'] 
		form.instance.name = self.kwargs['name']
		form.instance.user = self.request.user.username
		kwargs['class_name'] = Group.objects.get(name=form.instance.name)
		kwargs['comment'] = Comment.objects.get(id=form.instance.comment)
		kwargs['user'] = Account.objects.get(name=form.instance.user)
		return kwargs 
re_comment_form=CreateReturnComment.as_view()