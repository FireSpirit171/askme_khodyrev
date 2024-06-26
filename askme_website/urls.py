"""
URL configuration for askme_website project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name = 'index'),
    path('hot/', views.hot, name = 'hot'),
    path( 'tag/<str:tag_name>', views.tag, name = 'tag'),
    path( 'questions/<int:question_id>', views.question, name = "question" ),
    path( 'login/', views.login_view, name = 'login'),
    path( 'signup/', views.signup, name = 'signup' ),
    path( 'logout/', views.logout_view, name = 'logout' ),
    path( 'member/<str:member_name>', views.member, name = 'member' ),
    path( 'profile/edit/', views.settings, name = 'settings' ),
    path( 'ask/', views.ask, name = 'ask' ),
    path( 'likequestion/<int:question_id>', views.like_question, name='like_question' ),
    path( 'likeanswer/<int:answer_id>', views.like_answer, name='like_answer' ),
    path( 'correctanswer/<int:answer_id>', views.correct_answer, name='correct_answer' )
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
