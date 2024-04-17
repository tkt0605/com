# X.LiNK.com
### the Source Code of X.LiNK
## profile.html sample　code
{% extends "base.html" %}
{%load static%}
{% load crispy_forms_tags %}
{% block extra_head %}
  <link rel="stylesheet" href="{% static 'css/profile.css'%}">
{% endblock %}
{% block title%}X.LiNK|Profile{% endblock%}
{% block content %}
<main>
    <nav class="name_bord">
      <div>
        <span>
          <img src="/media/{{room.image}}" class="image_user"/>
          <br>
          <div class="user-main-data">
            <img src="/media/{{room.icon}}" class="user_image"/>
            <span><div class="lkooscao"><b>{{room.name}}</b></div></span>
            <hr class="hr_style">
            {% if room.mainuser == user %}
            <div class="dsch">
                <a class="side_name" href='/profile-edit/'>
                    <button class="edit_profile">
                        <div class="edit"><b>プロフィール編集</b></div>
                    </button>
                </a>
              </div>
            {% else %}
            <form id="follow_button" action="/follow_counts" method="post">
              {% csrf_token %}
              <input type="hidden" name="follow_id" value="{{room.id}}" readonly/>
              <input type="hidden" name="user_id" value="{{user.id}}" readonly/>
              <input type="hidden" name="user" value="{{room.name}}"readonly/>
              <input type="hidden" name="follower" value="{{user.username}}" readonly/>
              {% comment %} <input type="hidden" name="comment" value="{{comment_name}}" readonly/> {% endcomment %}
              {% if follow_button_value == 'follow' %}
              <input type="hidden" name="value" value="follow" readonly/>
              <button class="follow" type="submit"><b>フォロー</b><div style="display:none;">{{user.username}}</div></button>
              {% else %}
              <input type="hidden" name="value" value="unfollow" readonly/>
              <button class="following" type="submit"><b>フォロー中</b><div style="display:none;">{{user.username}}</div></button>
              {% endif %}
            </form>
            <form id="post_button" action="/root_count" method="post">
              {% csrf_token %}
              <input type="hidden" name="root_id" value="{{room.id}}" readonly/>
              <input type="hidden" name="user" value="{{user.username}}" readonly/>
              <input type="hidden" name="rooter" value="{{room.name}}"readonly/>
              {% if root_button_value == 'root' %}
              <input type="hidden" name="value" value="root" readonly/>
              <button class="root1" type="submit"><b>ルート</b><div style="display: none;">{{user.username}}</div></button> 
              {% elif room.name == user %}
              <div class="dcbsdhc"></div>
              {% else %}
              <input type="hidden" name="value" value="unroot" readonly/>
              <button class="rooting1" type="submit"><b>ルート中</b><div style="display: none;">{{user.username}}</div></button>
              {% endif %}
            </form>
            {% endif %}
            <b><div class="info">{{room.infomation }}</div></b>
            <br>
            <div class="hobbys"><span class="data_base">趣味:</span>{{room.hobby}}</div>
            <div class="details"><span class="data_base">詳細:</span>{{room.detail}}</div>
            <li class="class">
              <span>
                <div class="sdjvhsu">
                  <svg style="margin-top: 30px; margin-left: -20px;" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-calendar3" viewBox="0 0 16 16">
                    <path d="M14 0H2a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2zM1 3.857C1 3.384 1.448 3 2 3h12c.552 0 1 .384 1 .857v10.286c0 .473-.448.857-1 .857H2c-.552 0-1-.384-1-.857V3.857z"/>
                    <path d="M6.5 7a1 1 0 1 0 0-2 1 1 0 0 0 0 2zm3 0a1 1 0 1 0 0-2 1 1 0 0 0 0 2zm3 0a1 1 0 1 0 0-2 1 1 0 0 0 0 2zm-9 3a1 1 0 1 0 0-2 1 1 0 0 0 0 2zm3 0a1 1 0 1 0 0-2 1 1 0 0 0 0 2zm3 0a1 1 0 1 0 0-2 1 1 0 0 0 0 2zm3 0a1 1 0 1 0 0-2 1 1 0 0 0 0 2zm-9 3a1 1 0 1 0 0-2 1 1 0 0 0 0 2zm3 0a1 1 0 1 0 0-2 1 1 0 0 0 0 2zm3 0a1 1 0 1 0 0-2 1 1 0 0 0 0 2z"/>
                  </svg>
                  <span class="group">
                    <div style='margin-left: 0px; margin-top: -20px; color: rgb(155, 155, 155);'>{{room.created_at|date:'Y年n月j日'}}から利用しています。</div>
                  </span>
                </div>
              </span>
            </li>
            <li class="followerscount">
              <span><b>{{user_followers}}</b></span>
              <div class="followandfollower">followers</div>
            </li>
            <li class="followingcount">
              <span><b>{{user_following}}</b></span>
              <div class="followandfollower">following</div>
            </li>
            <br>
            <ul class="tab2-group">
              <li class="tab2 tab2-A is-active2">
                  <div class="menu"><b>メイン</b></div>
              </li>
              <li class="tab2 tab2-B">
                  <div class="menu4"><b>通知</b></div>
              </li>       
              <li class="tab2 tab2-C">
                <div class="menu4"><b>クラス</b></div>
            </li>       
              <li class="tab2 tab2-D">
                  <div class="menu4"><b>ルーター</b></div>
              </li>
              <li class="tab2 tab2-E">
                  <div class="menu4"><b>フォロワー</b></div>
              </li>           
            </ul>
          </div>
        </span>
      </div>
      <div class="panel2-group">
        <div class="panel2 tab2-A is-show2">
            <div class="class_post_field">
              <ul>
                <li style="color: rgb(241, 240, 240);">
                  {% for comment in comments%}
                  {% if room == comment.user %}
                  <span>
                    {% if room == comment.user and comment.image %}
                    <div class="jvsbdvjkds" id="nbgsfdgcsdcfs">
                      <ul  class="comments_bord2">
                        <a href="/account/{{comment.user}}/">
                          <img class="image2_bord" src="/media/{{comment.user.icon}}" alt="">
                          <b><li class="comment_commenter_name">{{comment.user}}</li></b>
                        </a>
                        <div class="from_comment_post"><small>/<b>@To the</b><a href="/community/{{comment.destination}}/"><u>{{comment.destination}}</u></a></small></div>
                        <div class="comment_time"><small>[{{comment.created_at}}]</small></div>
                        <div class="comment">{{comment.text}}</div>
                        <div>
                          <img class="zxxcvbnm" src="/media/{{comment.image}}" alt=""/>
                        </div>
                      </ul>
                    </div>
                    {% elif room == comment.user and comment.video %}
                    <div class="jvsbdvjkds" id="nbgsfdgcsdcfs">
                      <ul  class="comments_bord2">
                        <a href="/account/{{comment.user}}/">
                          <img class="image2_bord" src="/media/{{comment.user.icon}}" alt="">
                          <b><li class="comment_commenter_name">{{comment.user}}</li></b>
                        </a>
                        <div class="from_comment_post"><small>/<b>@To the</b><a href="/community/{{comment.destination}}/"><u>{{comment.destination}}</u></a></small></div>
                        <div class="comment_time"><small>[{{comment.created_at}}]</small></div>
                        <div class="comment">{{comment.text}}</div>
                        <video class="video_bord"  src="/media/{{comment.video}}/" id="image" controls></video>
                      </ul>
                    </div>
                    {% else %}
                    <div class="jvsbdvjkds2" id="nbgsfdgcsdcfs">
                      <ul  class="comments_bord2">
                        <a href="/account/{{comment.user}}/">
                          <img class="image2_bord" src="/media/{{comment.user.icon}}" alt="">
                          <b><li class="comment_commenter_name">{{comment.user}}</li></b>
                        </a>
                        <div class="from_comment_post"><small>/<b>@To the</b><a href="/community/{{comment.destination}}/"><u>{{comment.destination}}</u></a></small></div>
                        <div class="comment_time"><small>[{{comment.created_at}}]</small></div>
                        <div class="comment">{{comment.text}}</div>
                      </ul>
                    </div>
                    {%endif%}
                  </span>
                  <br>
                  {%endif%}
                  {% endfor %}
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>
      <div class="panel2 tab2-B">
        <div class="followerroom">
            <div class="post_talk_bord">
                <hr class="hr_follower">
                <div class="follower"><b><center>通知</center></b></div>
                <br>
                <li style="color: white">
                  <ul class="notifications_list">
                    {% comment %} {% for notification in notifications %}
                    {% if notification.user == room %}
                    <li class="notifications">
                      <b>
                        <a href="/account/{{notification.mainuser}}/"><div class="notification_name"><img src="/media/{{notification.mainuser.icon}}/" class="user_icon" alt="" />{{notification.mainuser}}</div></a>
                        <div class="notification_text">{{notification.message}}</div>
                      </b>
                    </li>
                    <br>
                    {% endif %}
                    {% endfor %} {% endcomment %}
                  </ul>
                </li>
              </div>
        </div>
      </div>
      <div class="panel2 tab2-C">
        <div class="post_talk_bord">
          <hr class="hr_follower">
          <div class="follower"><b><center>MyClass</center></b></div>
          <li style="color: white;">
            <ul class="followers_list">
              {% for group in groups%}
              <li class="followers">
                <b>
                    <div>
                        <a class="font" href="/community/{{group.name}}/">
                            <img src="/media/{{group.icon}}/" class="root_user_icon"/>{{group.name}}
                        </a>
                    </div>
                </b>
                <div class="class_index"><b>{{group.index}}</b></div>
              </li>
              <br>
              {%endfor%}
            </ul>
          </li>
        </div>
      </div>
      <div class="panel2 tab2-D">
        <div class="post_talk_bord">
          <hr class="hr_follower">
          <div class="follower"><b><center>Rooter</center></b></div>
          <li style="color: white;">
            {% for rooter in rooters %}
            <ul class="followers_list">
              {% for account in accounts%}
              {% if rooter.rooter == account.name %}
              <li class="followers">
                <b>
                    <div>
                        <a class="font" href="/account/{{account.name}}/"><img src="/media/{{account.icon}}/" class="root_user_icons"/>{{account.name}}</a>
                    </div>
                </b>
              </li>
              <br>
              {% endif %}
              {%endfor%}
            </ul>
            {%endfor%}
          </li>
        </div>
      </div>
      <div class="panel2 tab2-E">
          <div class="post_talk_bord">
            <hr class="hr_follower">
            <div class="follower"><b><center>Follower</center></b></div>
            <br>
            <li style="color: white;">
              {% for follower in followers %}
              <ul class="followers_list">
                {% for account in accounts%}
                {% if follower.follower == account.name %}
                <li class="followers">
                    <b>
                        <div>
                            <a class="font" href="/account/{{account.name}}/">
                                <img src="/media/{{account.icon}}/" class="root_user_icons"/>{{account.name}}
                            </a>
                        </div>
                    </b>
                </li>
                <br>
                {% endif %}
                {%endfor%}
              </ul>
              {%endfor%}
            </li>
          </div>
      </div>
      </div>
    </nav>
</main>
<script type="text/javascript">
    document.addEventListener('DOMContentLoaded', function(){
      // タブに対してクリックイベントを適用
      const tabs = document.getElementsByClassName('tab2');
      for(let i = 0; i < tabs.length; i++) {
        tabs[i].addEventListener('click', tabSwitch, false);
      }
    
      // タブをクリックすると実行する関数
      function tabSwitch(){
        // タブのclassの値を変更
        document.getElementsByClassName('is-active2')[0].classList.remove('is-active2');
        this.classList.add('is-active2');
        // コンテンツのclassの値を変更
        document.getElementsByClassName('is-show2')[0].classList.remove('is-show2');
        const arrayTabs = Array.prototype.slice.call(tabs);
        const index = arrayTabs.indexOf(this);
        document.getElementsByClassName('panel2')[index].classList.add('is-show2');
      };
    }, false);
    const aside = document.getElementById('aside_bar');
    aside.onmouseover = function(event) {
      let target = event.target;
      target.style.background = 'white';
      text.value += "mouseover " + target.tagName + "\n";
      text.scrollTop = text.scrollHeight;
    };
    aside.onmouseout = function(event) {
      let target = event.target;
      target.style.background = '';
      text.value += "mouseout " + target.tagName + "\n";
      text.scrollTop = text.scrollHeight;
    };
</script>
{% endblock %}