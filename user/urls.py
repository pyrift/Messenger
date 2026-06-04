from django.urls import path
from .views import singe_up_view, login_view
urlpatterns = [
    path('', singe_up_view, name='singe_up_view'),
    path('signup/', login_view, name='signup'),
    path('login/', login_view, name='login'),

]