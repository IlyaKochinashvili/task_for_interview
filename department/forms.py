from django.forms import CharField, IntegerField, forms, TextInput


class PhoneCheckForm(forms.Form):
    phone_number = CharField(max_length=13, widget=TextInput(attrs={"class": "form-control"}))


class FirstUserForm(forms.Form):
    first_name = CharField(max_length=100, widget=TextInput(attrs={"class": "form-control"}))
    last_name = CharField(max_length=100, widget=TextInput(attrs={"class": "form-control"}))
    password = CharField(max_length=100, widget=TextInput(attrs={"class": "form-control"}))
    password_confirm = CharField(max_length=100, widget=TextInput(attrs={"class": "form-control"}))
    otp_pass = IntegerField(widget=TextInput(attrs={"class": "form-control"}))

    def __init__(self, *args, **kwargs):
        kwargs.pop('phone_number')
        super(FirstUserForm, self).__init__(*args, **kwargs)


class UserForm(forms.Form):
    first_name = CharField(max_length=100, widget=TextInput(attrs={"class": "form-control"}))
    last_name = CharField(max_length=100, widget=TextInput(attrs={"class": "form-control"}))
    otp_pass = IntegerField(widget=TextInput(attrs={"class": "form-control"}))

    def __init__(self, *args, **kwargs):
        kwargs.pop('phone_number')
        super(UserForm, self).__init__(*args, **kwargs)


class IsStaffUserForm(forms.Form):
    password = CharField(max_length=100, widget=TextInput(attrs={"class": "form-control"}))
    otp_pass = IntegerField(widget=TextInput(attrs={"class": "form-control"}))

    def __init__(self, *args, **kwargs):
        kwargs.pop('phone_number')
        super(IsStaffUserForm, self).__init__(*args, **kwargs)


class NotStaffUserForm(forms.Form):
    otp_pass = IntegerField(widget=TextInput(attrs={"class": "form-control"}))

    def __init__(self, *args, **kwargs):
        kwargs.pop('phone_number')
        super(NotStaffUserForm, self).__init__(*args, **kwargs)
