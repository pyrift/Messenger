from django.urls import path
from .views import singe_up_view, login_view
urlpatterns = [
    path('signup/', singe_up_view, name='signup'),
    path('login/', login_view, name='login'),

]