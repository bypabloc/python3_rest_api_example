from django import forms
from ..models import Company
import json

class CompanyValidation(forms.Form):
    name = forms.CharField(max_length=50, )
    description = forms.CharField( required=False, )
    url = forms.CharField(max_length=100)
    city = forms.CharField(max_length=255)
    address = forms.CharField(max_length=255)

    def clean(self):
        data = self.cleaned_data

        print(data)

        if Company.objects.filter(name=data['name']).exists():
            self.add_error('name', 'Company already exists')

        # if data.get('password') != data.get('password_confirm'):
        #     self._errors['password'] = self.error_class([
        #         'Minimum 5 characters required'])
        
        return data

    def save(self):
        data = self.cleaned_data
        return Company.objects.create(
            name=data['name'],
            description=data['description'],
            url=data['url'],
            city=data['city'],
            address=data['address'],
        )

    def getErrors(self):
        errors = json.loads(self._errors.as_json())

        errors_list = {}

        for key in errors:
            errors_list[key] = []
            for error in errors[key]:
                errors_list[key].append(error['message'])

        return errors_list