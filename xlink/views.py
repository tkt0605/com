from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from .forms import AccountForm, ClassCreateForm, CommentForm, ReturnCommentForm
from django.contrib import messages
from django.contrib.auth import login
from .models import Account, Group, Comment, Category, FollowCount, CommentCount, ReturnComment, Root, FollowersCount, AccountRoot
from django.views import generic
from django.views.generic import ListView
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
User = get_user_model()
def index(request):
    template = loader.get_template('index.html')
    context = {
        'csrf_token': '',
    }
    return HttpResponse(template.render(context, request))
def rooms(request):
    rooms = Account.objects.order_by("-name")[:100000]
    template=loader.get_template("header.html", "home.html")
    context = {
        "csrf_token": "",
        "rooms": rooms,
    }
    return HttpResponse(template.render(context, request))
def accounts(request):
    accounts = Account.objects.order_by("-created_at")[:100000]
    rooms = Account.objects.order_by("-name")[:100000]
    template = loader.get_template("home.html")
    context = {
        "csrf_token": "",
        "accounts": accounts,
        "rooms":rooms
    }
    return HttpResponse(template.render(context, request))
def account(request, name):
    account = Group.objects.get(name=name)
    template = loader.get_template("class.html")
    context = {
        "account": account,
    }
    return HttpResponse(template.render(context, request))
def profiles(request):
    template = loader.get_template("header.html", "profile.html")
    rooms = Account.objects.order_by("-name")[:100000]
    context = {
        "rooms": rooms
    }
    return HttpResponse(template.render(context, request))
def groups(request):
    template = loader.get_template("class.html")
    groups = Group.objects.order_by("-name")[:100000]
    context = {
        "csrf_token": "",
        "groups": groups,
    }
    return HttpResponse(template.render(context, request))
def comments(request):
    comments = Comment.objects.order_by("-created_at")[:10000]
    accounts = Account.objects.order_by("name")[:10000]
    tempalte = loader.get_template("room.html")
    context = {
        "accounts": accounts,
        "comments": comments,
    }
    return HttpResponse(tempalte.render(context,request))
def room(request, name):
    name = Account.objects.get(name=name)
    groups = Group.objects.filter(managername=name)
    accounts=Account.objects.order_by("-created_at")[:100000]
    comments=Comment.objects.order_by("-created_at")[:100000]
    rooms=Account.objects.order_by("-name")[:10000]
    current_user=request.GET.get("user")
    logged_in_user = request.user.username
    user_followers = len(FollowCount.objects.filter(user=name))
    user_following = len(FollowersCount.objects.filter(follower=name))
    user_followers0 = FollowersCount.objects.filter(user=name)
    followers = FollowersCount.objects.filter(user=name)
    followings = FollowersCount.objects.filter(follower=name)
    user_root0 = AccountRoot.objects.filter(rooter=name)
    roots = AccountRoot.objects.filter(rooter=name)
    rooters = AccountRoot.objects.filter(user=name)
    root_class = []
    user_followers1 =[]
    for i in user_followers0:
        user_followers0 = i.follower
        user_followers1.append(user_followers0)
    if logged_in_user in user_followers1:
        follow_button_value = "following"
    else:
        follow_button_value = "follow"
    for root in rooters:
        class_rooter_id = root.user
        root_class.append(class_rooter_id)
    if logged_in_user in root_class:
        root_button_value = "rooting"
    else:
        root_button_value = "root"
    template = loader.get_template("profile.html")
    context = {
        "rooms": rooms,
        "groups": groups,
        "comments": comments,
        "accounts":accounts,
        "room": name,
        "roots": roots,
        "followers": followers,
        "followings": followings,
        "rooters": rooters,
        "user_root0": user_root0 ,
        "user_followers0": user_followers0,
        "current_user": current_user,
        "logged_in_user": logged_in_user,
        "user_followers": user_followers,
        "user_following": user_following,
        "follow_button_value": follow_button_value,
        "root_button_value": root_button_value
        }
    return HttpResponse(template.render(context, request))
def communitys(request):
    rooms = Account.objects.order_by("-name")[:100000]
    template = loader.get_template("header.html" "class.html")
    context = {
        "csrf_token": "",
        rooms: rooms,
    }
    return HttpResponse(template.render(context, request))
def community(request, name):
    current_user = request.GET.user
    logged_in_user = request.user.username
    groups = Group.objects.order_by("-created_at")[:100000]
    rooms = Account.objects.order_by("-created_at")[:100000]
    comments = Comment.objects.order_by("-created_at")[:10000]
    return_comments = ReturnComment.objects.order_by("-created_at")[:10000]
    manages = Group.objects.filter(mainuser=request.user)
    name = Group.objects.get(name=name)
    user_followers = len(FollowersCount.objects.filter(user=name))
    user_following = len(FollowersCount.objects.filter(follower=current_user))
    user_comments = len(CommentCount.objects.filter(classname=name))
    user_followers0 = FollowersCount.objects.filter(user=name)
    followers = FollowersCount.objects.filter(follower=name)
    followings = FollowersCount.objects.filter(user=name)
    rooters = Root.objects.filter(group=name)
    roots = Root.objects.filter(rooter=name)
    root_class=[]
    user_followers1=[]
    for i in user_followers0:
        user_followers0 = i.follower
        user_followers1.append(user_followers0)
    if logged_in_user in user_followers1:
        follow_button_value = "unfollow"
    else:
        follow_button_value = "follow"
    for root in rooters:
        class_rooter_id = root.user
        root_class.append(class_rooter_id)
    if logged_in_user in root_class:
        root_button_value = "unroot"
    else:
        root_button_value = "root"
    template = loader.get_template("class.html")
    context = {
        "rooms":rooms,
        "groups": groups,
        "comments": comments,
        "return_comments": return_comments,
        "community": name,
        "manages": manages,
        "roots": roots,
        "rooters": rooters,
        "current_user": current_user,
        "followers": followers,
        "followings": followings,
        "logged_in_user": logged_in_user,
        "user_followers": user_followers,
        "user_comments": user_comments,
        "user_following": user_following,
        "follow_button_value": follow_button_value,
        "root_button_value": root_button_value,
    }        
    return HttpResponse(template.render(context, request))
def root_selecter(request):
    if request.method == "POST":
        value = request.POST["value"]
        user = request.POST["uaer"]
        group = request.POST["group"]
        rooters = request.POST["rooter"]
        if value == "root":
            for rooter in rooters:
                root_sel = Root.objects.create(user=user, group=group, rooter=rooter)
                root_sel.save()
        else:
            for rooter in rooters:
                root_sel = Root.objects.get(user=user, group=group, rooter=rooter)
                root_sel.delete()
        return redirect("/community/"+group)
def follow_count(request):
    if request.method == "POST":
        value = request.POST["value"]
        user = request.POST["user"]
        follower = request.POST["follower"]
        if value == "follow":
            followerscount = FollowCount.objects.create(user=user, follower=follower)
            followerscount.save()
        else:
            followerscount = FollowCount.objects.get(user=user, follower=follower)
            followerscount.delete()
        return redirect("/community/"+user)
def root_count(request):
    if request.method == "POST":
        value = request.POST["value"]
        user = request.POST["user"]
        rooter = request.POST["rooter"]
        if value == "root":
            root_sel = AccountRoot.objects.create(user=user, rooter=rooter)
            root_sel.save()
        else:
            root_sel = AccountRoot.objects.get(user=user, rooter=rooter)
            root_sel.delete()
        return redirect("/account/" + rooter)
def follow_count(request):
    if request.methond == "POST":
        value = request.POST["value"]
        user = request.POST["user"]
        follower = request.POST["follower"]
        if value == "follow":
            followers_cut = FollowersCount.objects.create(user = user, follower = follower)
            followers_cut.save()
        else:
            followers_cut = FollowersCount.objects.get(user = user, follower=follower)
            followers_cut.delete()
        return redirect("/community/" + user)
def categorys(request, name):
    template = loader.get_template("home.html")
    categorys = Category.objects.get(name=name)
    accounts = Group.objects.filter(category=categorys)
    return render(request, "home.html",{"category": categorys, "accounts": accounts})
def comment(request, pk):
    template = loader.get_template("class.html")
    comment = Comment.objects.get(pk=pk)
    context = {
        "comment": comment
    }
    return HttpResponse(template.render(context, request))
def return_comments(request):
    template = loader.get_template("class.html")
    return_comments = ReturnComment.objects.order_by("-created_at")
    context = {
        "return_comments": return_comments,
    }
    return HttpResponse(template.render(context, request))
def return_comment(request, pk):
    template = loader.get_template("class.html")
    return_comment = ReturnComment.objects.get(pk=pk)
    context = {
        "return_comment": return_comment,
    }
    return HttpResponse(template.render(context, request))
class CreateAccountView(generic.CreateView):
    form_class = AccountForm
    template_name = "account.html"
    def get_form_kwargs(self, *args, **kwargs):
        xlink_obj = super().get_form_kwargs(*args, **kwargs)
        form = AccountForm(self.request.POST, isinstance=User)
        xlink_obj["mainuser"] = self.request.user
        xlink_obj["name"] = self.request.user.username
        return xlink_obj
form_create=CreateAccountView.as_view()
class ClassCreateView(generic.CreateView):
    form_class = ClassCreateForm
    template_name = "create.html"
    def get_form_kwargs(self, *args, **kwargs):
        xlink_obj = super().get_form_kwargs(*args, **kwargs)
        form = ClassCreateForm(self.request.POST, isinstance=Account)
        form.instance.name = self.request.user.username
        xlink_obj["mainuser"] = self.request.user
        xlink_obj["managername"]= Account.objects.get(name=form.instance.name)
        return xlink_obj
form_class = ClassCreateView.as_view()
class CreateCommentView(generic.CreateView):
    form_class = CommentForm
    template_name = "comment.html"
    success_url = "/"
    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super().get_form_kwargs(*args, **kwargs)
        form = CommentForm(self.request.POST,self.request.FILES , instance=Account and Group)
        form.instance.name = self.kwargs["name"]
        form.instance.user = self.request.user.username
        form.instance.text = Comment.text
        kwargs["user"] = Account.objects.get(name=form.instance.user)
        kwargs["destination"] = Group.objects.get(name = form.instance.name)
        return kwargs
form_comment=CreateCommentView.as_view()
class CreateReturnCommentView(generic.CreateView):
    form_class = ReturnCommentForm
    template_name = "return.html"
    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super().get_form_kwargs(*args, **kwargs)
        form = ReturnCommentForm(self.request.POST, isinstance=Comment and Account and Group)
        form.instance.comment = self.kwargs["pk"]
        form.instance.name = self.kwargs["name"]
        form.instance.user = self.request.user.username
        kwargs["class_name"] = Group.objects.get(name=form.instance.name)
        kwargs["comment"] = Comment.objects.get(id = form.instance.comment)
        kwargs["user"] = Account.objects.get(name = form.instance.user)
        return kwargs
form_return = CreateReturnCommentView.as_view()