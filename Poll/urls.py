"""
URL configuration for PollApp project.

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

from django.urls import path, include
from . import views


urlpatterns = [
    path('create-Poll/',views.createPoll, name="createPoll"),
    path('view-Poll/',views.vewPoll, name="viewPollURL"),           #for url tag to work
    path('view-Poll/<str:uuid>',views.vewPoll, name="viewPoll"),
    path('results/',views.results, name="pollResultsURL"),          #for url tag to work
    path('results/<str:uuid>',views.results, name="pollResults"),
    path('post/',views.pollPost, name="pollPost"),
    path('posted-polls/',views.postedPolls, name="postedPolls"),
    path('voted-polls/',views.votedPolls, name="votedPolls"),
    path('delete-poll/',views.delPoll, name="deletePoll"),
]
