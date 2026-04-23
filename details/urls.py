from django.urls import path
from .views import PlayerRankingView, MatchListView, NewsListView, SeasonListView, MonthListView



urlpatterns = [
    path('player-rankings/', PlayerRankingView.as_view(), name='player-rankings'),
    path('seasons/', SeasonListView.as_view(), name='season-list'),
    path('months/', MonthListView.as_view(), name='month-list'),
    path('matches/', MatchListView.as_view(), name='match-list'),
    path('news/', NewsListView.as_view(), name='news-list'),
]