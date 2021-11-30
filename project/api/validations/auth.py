from django import forms
from ..models import User
import json
import crypt
import getpass
import pwd
from hmac import compare_digest as compare_hash
from ..helpers.jwt import generateToken

class AuthSignUpForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50)
    password_confirmation = forms.CharField(max_length=50)
    token = forms.CharField(required=False)

    def clean(self):
        data = self.cleaned_data

        print(data)

        if User.objects.filter(name=data['name']).exists():
            self.add_error('name', 'Already exists')

        if User.objects.filter(email=data['email']).exists():
            self.add_error('email', 'Already exists')
        
        return data

    def save(self):
        data = self.cleaned_data

        user = User.objects.create(
            name=data['name'],
            email=data['email'],
            password=crypt.crypt(data['password']),
        )

        self.cleaned_data['token'] = user.token

        return user

    def getErrors(self):
        errors = json.loads(self._errors.as_json())

        errors_list = {}

        for key in errors:
            errors_list[key] = []
            for error in errors[key]:
                errors_list[key].append(error['message'])

        return errors_list

class AuthSignInForm(forms.Form):
    email = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50)

    def clean(self):
        data = self.cleaned_data

        print(data)

        user = User.objects.filter(email=data['email'])

        if not user.exists():
            self.add_error('email', 'Does not exist')

        user = user.first()

        if not compare_hash(crypt.crypt(data['password'], user.password), user.password):
            self.add_error('password', 'Wrong password')

        return data

    def getErrors(self):
        errors = json.loads(self._errors.as_json())

        errors_list = {}

        for key in errors:
            errors_list[key] = []
            for error in errors[key]:
                errors_list[key].append(error['message'])

        return errors_list

class AuthSignOutForm(forms.Form):
    email = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50)

    def clean(self):
        data = self.cleaned_data

        print(data)

        if User.objects.filter(email=data['email']).exists():
            self.add_error('email', 'Already exists')
        
        return data

    def save(self):
        data = self.cleaned_data

        password = data['password']

        hashed = crypt.crypt(password)
        print('hashed: ',hashed)

        # compare = compare_hash(hashed, crypt.crypt('123456', hashed))
        # print('compare: ',compare)

        return User.objects.create(
            name=data['name'],
            email=data['email'],
            password=hashed,
        )

    def getErrors(self):
        errors = json.loads(self._errors.as_json())

        errors_list = {}

        for key in errors:
            errors_list[key] = []
            for error in errors[key]:
                errors_list[key].append(error['message'])

        return errors_list

        