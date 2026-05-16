from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Appointment, AppointmentData, obesityDisorder, mentalDisorder, pcosDisorder, DoctorUser


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['appointment_date']


class AppointmentDataForm(forms.ModelForm):
    class Meta:
        model = AppointmentData
        fields = '__all__'
        exclude = ['user', 'doctor', 'status']
        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-control col-md-12'}),
            'phone': forms.TextInput(attrs={'class': 'form-control col-md-12'}),
            'appointmentDate': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control'}),
        }

class MentalDisorderForm(forms.ModelForm):
    class Meta:
        model = mentalDisorder
        fields = '__all__'
        exclude = ['user']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control col-md-12'})
            if isinstance(field.widget, forms.Select):
                field.empty_label = "Choose one"

class pcosDisorderForm(forms.ModelForm):
    class Meta:
        model = pcosDisorder
        fields = '__all__'
        exclude = ['user']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control col-md-12'})
            if isinstance(field.widget, forms.Select):
                field.empty_label = "Choose one"
                
class obesityDisorderForm(forms.ModelForm):
    class Meta:
        model = obesityDisorder
        fields = '__all__'
        exclude = ['user']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control col-md-12'})
            if isinstance(field.widget, forms.Select):
                field.empty_label = "Choose one"


class UserRegistrationForm(UserCreationForm):
    """Registration form for regular users with styled fields."""
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # for CSS Properties
        self.fields['username'].widget.attrs.update({'class': 'col-md-10 form-control'})
        self.fields['email'].widget.attrs.update({'class': 'col-md-10 form-control'})
        self.fields['first_name'].widget.attrs.update({'class': 'col-md-10 form-control'})
        self.fields['last_name'].widget.attrs.update({'class': 'col-md-10 form-control'})
        self.fields['password1'].widget.attrs.update({'class': 'col-md-10 form-control'})
        self.fields['password2'].widget.attrs.update({'class': 'col-md-10 form-control'})

        self.fields['username'].help_text = '<span class="text-muted">Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</span>'
        self.fields['email'].help_text = '<span class="text-muted">Required. Inform a valid email address.</span>'
        self.fields['password2'].help_text = '<span class="text-muted">Enter the same password as before, for verification.</span>'
        self.fields['password1'].help_text = '<span class="text-muted"><ul class="small"><li class="text-muted">Your password can not be too similar to your other personal information.</li><li class="text-muted">Your password must contain at least 8 characters.</li><li class="text-muted">Your password can not be a commonly used password.</li><li class="text-muted">Your password can not be entirely numeric.</li></ul></span>' 

class DoctorRegistrationForm(UserRegistrationForm):
    """Registration form for doctors with additional professional fields."""
    phone = forms.CharField(max_length=20)
    specialization = forms.CharField(max_length=100)
    hospital = forms.CharField(max_length=255)
    city = forms.CharField(max_length = 100)
    state = forms.CharField(max_length = 100)
    country = forms.CharField(max_length = 100)
    about = forms.CharField(max_length = 1000)
    education = forms.CharField(max_length = 1000)
    experience = forms.CharField(max_length = 1000)
    languages = forms.CharField(max_length = 1000)
    expertise = forms.CharField(max_length = 1000)

    class Meta:
        model = DoctorUser
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2', 
                'phone', 'specialization', 'hospital', 'city', 'state', 'country',
                'about', 'education', 'experience', 'languages', 'expertise']
        db_table = 'doctor_user'

    DoctorUser.groups.field.related_name = 'doctor_groups'
    DoctorUser.user_permissions.field.related_name = 'doctor_user_permissions'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # for CSS Properties
        self.fields['username'].widget.attrs.update({'class': 'col-md-10 form-control'})
        self.fields['email'].widget.attrs.update({'class': 'col-md-10 form-control'})
        self.fields['first_name'].widget.attrs.update({'class': 'col-md-10 form-control'})
        self.fields['last_name'].widget.attrs.update({'class': 'col-md-10 form-control'})
        self.fields['password1'].widget.attrs.update({'class': 'col-md-10 form-control'})
        self.fields['password2'].widget.attrs.update({'class': 'col-md-10 form-control'})
        self.fields['phone'].widget.attrs.update({'class': 'col-md-10 form-control'})
        self.fields['specialization'].widget.attrs.update({'class': 'col-md-10 form-control'})
        self.fields['hospital'].widget.attrs.update({'class': 'col-md-10 form-control'})
        self.fields['city'].widget.attrs.update({'class': 'col-md-10 form-control'})
        self.fields['state'].widget.attrs.update({'class': 'col-md-10 form-control'})
        self.fields['country'].widget.attrs.update({'class': 'col-md-10 form-control'})
        self.fields['about'].widget.attrs.update({'class': 'col-md-10 form-control'})
        self.fields['education'].widget.attrs.update({'class': 'col-md-10 form-control'})
        self.fields['experience'].widget.attrs.update({'class': 'col-md-10 form-control'})
        self.fields['languages'].widget.attrs.update({'class': 'col-md-10 form-control'})
        self.fields['expertise'].widget.attrs.update({'class': 'col-md-10 form-control'})

        self.fields['username'].help_text = '<span class="text-muted">Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</span>'
        self.fields['email'].help_text = '<span class="text-muted">Required. Inform a valid email address.</span>'
        self.fields['password2'].help_text = '<span class="text-muted">Enter the same password as before, for verification.</span>'
        self.fields['password1'].help_text = '<span class="text-muted"><ul class="small"><li class="text-muted">Your password can not be too similar to your other personal information.</li><li class="text-muted">Your password must contain at least 8 characters.</li><li class="text-muted">Your password can not be a commonly used password.</li><li class="text-muted">Your password can not be entirely numeric.</li></ul></span>' 