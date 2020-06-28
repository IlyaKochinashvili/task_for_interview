from django.conf.urls import url
from django.urls import path

from department.views import PhoneCheckView, FirstUserView, home, UserView, NotStaffUserView, IsStaffUserView

urlpatterns = [
    path("", PhoneCheckView.as_view(), name="phone_check"),
    url(r'^auth/(?P<phone_number>[+38]\w{12})$', FirstUserView.as_view(), name="auth"),
    url(r'^auth2/(?P<phone_number>[+38]\w{12})$', UserView.as_view(), name="auth2"),
    url(r'^auth3/(?P<phone_number>[+38]\w{12})$', IsStaffUserView.as_view(), name="auth3"),
    url(r'^auth4/(?P<phone_number>[+38]\w{12})$', NotStaffUserView.as_view(), name="auth4"),
    url('auth*(\w.)home/(?P<phone_number>[+38]\w{12})$', home, name="home"),
]
