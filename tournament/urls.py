from django.urls import path
from .views import RegisterView, LoginView, LogoutView, TournamentManageView, TeamManageView, FixtureManageView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('tournament/', TournamentManageView.as_view()),
    path('tournament/<int:pk>/', TournamentManageView.as_view()),
    path('teams/', TeamManageView.as_view()),
    path('teams/<int:pk>/', TeamManageView.as_view()),
    path('create-fixture/', FixtureManageView.as_view()),
]

