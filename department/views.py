from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView, ListView

from department.forms import FirstUserForm, PhoneCheckForm, UserForm, IsStaffUserForm, NotStaffUserForm
from department.models import User
import random


def otp_pass_gen():
    otp_pass = random.randint(1000, 9999)
    return otp_pass


otp = []


class PhoneCheckView(FormView):
    template_name = 'phone.html'
    form_class = PhoneCheckForm

    def get_form(self, form_class=PhoneCheckForm):
        form = super(PhoneCheckView, self).get_form()
        return form

    def get_success_url(self):
        form = self.get_form()
        phone = [item.value() for item in form]
        users_phone_numbers = [user.phone_number for user in User.objects.all()]
        otp.append(otp_pass_gen())
        print(otp)
        if not User.objects.filter().exists() and phone[0] not in users_phone_numbers:
            User.objects.create(phone_number=phone[0])
            return reverse_lazy('auth', kwargs={"phone_number": phone[0]})
        elif User.objects.filter().exists() and phone[0] not in users_phone_numbers:
            User.objects.create(phone_number=phone[0])
            return reverse_lazy('auth2', kwargs={"phone_number": phone[0]})
        elif phone[0] in users_phone_numbers and User.objects.get(phone_number=phone[0]).is_stuff is True:
            return reverse_lazy('auth3', kwargs={"phone_number": phone[0]})
        else:
            return reverse_lazy('auth4', kwargs={"phone_number": phone[0]})


class FirstUserView(FormView):
    template_name = 'authorization.html'
    success_url = 'home'
    form_class = FirstUserForm

    def get_form(self, form_class=None):
        form = super(FirstUserView, self).get_form()
        users_phone_numbers = [user.phone_number for user in User.objects.all()]
        values = [item.value() for item in form]
        phone = self.get_form_kwargs()['phone_number']
        if phone in users_phone_numbers:
            user = User.objects.get(phone_number=phone)
            user.first_name = values[0]
            user.last_mane = values[1]
            user.is_stuff = True
            password = hash(values[2])
            user.save()
        return form

    def get_form_kwargs(self):
        kwargs = super(FirstUserView, self).get_form_kwargs()
        kwargs.update({'phone_number': self.kwargs['phone_number']})
        return kwargs


class UserView(FormView):
    template_name = 'authorization.html'
    success_url = 'home'
    form_class = UserForm

    def get_form(self, form_class=None):
        form = super(UserView, self).get_form()
        values = [item.value() for item in form]
        users_phone_numbers = [user.phone_number for user in User.objects.all()]
        phone = self.get_form_kwargs()['phone_number']
        if phone in users_phone_numbers:
            user = User.objects.get(phone_number=phone)
            user.first_name = values[0]
            user.last_mane = values[1]
            user.save()
        return form

    def get_form_kwargs(self):
        kwargs = super(UserView, self).get_form_kwargs()
        kwargs.update({'phone_number': self.kwargs['phone_number']})
        return kwargs


class IsStaffUserView(FormView):
    template_name = 'authorization.html'
    form_class = IsStaffUserForm

    def get_form(self, form_class=None):
        form = super(IsStaffUserView, self).get_form()
        return form

    def get_success_url(self):
        form = self.get_form()
        if form['otp_pass'].value() == str(otp[0]):
            otp.pop()
            return f'home/{self.get_form_kwargs()["phone_number"]}'
        else:
            otp.pop()
            return 'wrong-pass'

    def get_form_kwargs(self):
        kwargs = super(IsStaffUserView, self).get_form_kwargs()
        kwargs.update({'phone_number': self.kwargs['phone_number']})
        return kwargs


class NotStaffUserView(FormView):
    template_name = 'authorization.html'
    form_class = NotStaffUserForm

    def get_form(self, form_class=None):
        form = super(NotStaffUserView, self).get_form()
        return form

    def get_success_url(self):
        form = self.get_form()
        if form['otp_pass'].value() == str(otp[0]):
            otp.pop()
            return f'home/{self.get_form_kwargs()["phone_number"]}'
        else:
            otp.pop()
            return 'wrong-pass'

    def get_form_kwargs(self):
        kwargs = super(NotStaffUserView, self).get_form_kwargs()
        kwargs.update({'phone_number': self.kwargs['phone_number']})
        return kwargs


def home(request, phone_number):
    user = User.objects.get(phone_number=phone_number)
    context = {"user": user}

    return render(request, "home.html", context)


class WrongPassView(ListView):
    template_name = 'wrong_pass.html'
    queryset = None
