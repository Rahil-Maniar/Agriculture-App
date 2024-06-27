from django import forms
from django.forms import TextInput, EmailInput, PasswordInput
from .models import Signup
from django.contrib.auth.forms import AuthenticationForm


class MyForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, field in self.fields.items():
            field.label = ""
            # Add margin to the bottom of each field
            field.widget.attrs["class"] = field.widget.attrs.get("class", "") + " mb-4"

    class Meta:
        model = Signup
        fields = "__all__"
        widgets = {
            "email": EmailInput(
                attrs={
                    "class": "text-slate-500 bg-white border-2 border-slate-900 rounded-xl block w-full max-w-md h-11 p-2.5 hover:border-green-500",
                    "placeholder": "Email",
                }
            ),
            "username": TextInput(
                attrs={
                    "class": "text-slate-500 bg-white border-2 border-slate-900 rounded-xl block w-full max-w-md h-11 p-2.5 hover:border-green-500",
                    "placeholder": "Username",
                }
            ),
            "first_name": TextInput(
                attrs={
                    "class": "text-slate-500 bg-white border-2 border-slate-900 rounded-xl block w-full max-w-md h-11 p-2.5 hover:border-green-500",
                    "placeholder": "First Name",
                }
            ),
            "last_name": TextInput(
                attrs={
                    "class": "text-slate-500 bg-white border-2 border-slate-900 rounded-xl block w-full max-w-md h-11 p-2.5 hover:border-green-500",
                    "placeholder": "Last Name",
                }
            ),
            "password": PasswordInput(
                attrs={
                    "class": "text-slate-500 bg-white border-2 border-slate-900 rounded-xl block w-full max-w-md h-11 p-2.5 hover:border-green-500",
                    "placeholder": "Password",
                }
            ),
        }


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "w-full px-4 py-2 rounded-lg bg-gray-100 border border-gray-300 focus:outline-none focus:ring-2 focus:ring-teal-500",
                "placeholder": "Username",
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "w-full px-4 py-2 rounded-lg bg-gray-100 border border-gray-300 focus:outline-none focus:ring-2 focus:ring-teal-500",
                "placeholder": "Password",
            }
        )
    )


class FertilizerRecommenderForm(forms.Form):
    CROP_CHOICES = [
        ("", "Select the type of crop you'd like to grow"),
        ("crop1", "Crop 1"),
        ("crop2", "Crop 2"),
        ("crop3", "Crop 3"),
        ("crop4", "Crop 4"),
    ]

    SOIL_CHOICES = [
        ("", "Select the type of soil you want to grow on"),
        ("soil1", "Soil 1"),
        ("soil2", "Soil 2"),
        ("soil3", "Soil 3"),
        ("soil4", "Soil 4"),
    ]

    crop = forms.ChoiceField(
        choices=CROP_CHOICES,
        widget=forms.Select(
            attrs={"class": "w-full p-2 border border-gray-300 rounded"}
        ),
    )
    soil = forms.ChoiceField(
        choices=SOIL_CHOICES,
        widget=forms.Select(
            attrs={"class": "w-full p-2 border border-gray-300 rounded"}
        ),
    )
    nitrogen = forms.FloatField(
        widget=forms.NumberInput(
            attrs={
                "class": "w-full p-2 border border-gray-300 rounded",
                "placeholder": "Nitrogen Content in (kg/ha)",
            }
        )
    )
    phosphorus = forms.FloatField(
        widget=forms.NumberInput(
            attrs={
                "class": "w-full p-2 border border-gray-300 rounded",
                "placeholder": "Phosphorus Content in (kg/ha)",
            }
        )
    )
    potassium = forms.FloatField(
        widget=forms.NumberInput(
            attrs={
                "class": "w-full p-2 border border-gray-300 rounded",
                "placeholder": "Potassium Content in (kg/ha)",
            }
        )
    )
    ph = forms.FloatField(
        widget=forms.NumberInput(
            attrs={
                "class": "w-full p-2 border border-gray-300 rounded",
                "placeholder": "pH Value",
            }
        )
    )
    rainfall = forms.FloatField(
        widget=forms.NumberInput(
            attrs={
                "class": "w-full p-2 border border-gray-300 rounded",
                "placeholder": "Annual Rainfall in (mm)",
            }
        )
    )
    temperature = forms.FloatField(
        widget=forms.NumberInput(
            attrs={
                "class": "w-full p-2 border border-gray-300 rounded",
                "placeholder": "Temperature in (°C)",
            }
        )
    )


class CropRecommenderForm(forms.Form):
    nitrogen = forms.FloatField(
        widget=forms.NumberInput(
            attrs={
                "class": "w-full p-2 border border-gray-300 rounded",
                "placeholder": "Nitrogen Content in (kg/ha)",
            }
        )
    )
    phosphorus = forms.FloatField(
        widget=forms.NumberInput(
            attrs={
                "class": "w-full p-2 border border-gray-300 rounded",
                "placeholder": "Phosphorus Content in (kg/ha)",
            }
        )
    )
    potassium = forms.FloatField(
        widget=forms.NumberInput(
            attrs={
                "class": "w-full p-2 border border-gray-300 rounded",
                "placeholder": "Potassium Content in (kg/ha)",
            }
        )
    )
    temperature = forms.FloatField(
        widget=forms.NumberInput(
            attrs={
                "class": "w-full p-2 border border-gray-300 rounded",
                "placeholder": "Average Temperature in (°C)",
            }
        )
    )
    humidity = forms.FloatField(
        widget=forms.NumberInput(
            attrs={
                "class": "w-full p-2 border border-gray-300 rounded",
                "placeholder": "Average Humidity in (%)",
            }
        )
    )
    ph = forms.FloatField(
        widget=forms.NumberInput(
            attrs={
                "class": "w-full p-2 border border-gray-300 rounded",
                "placeholder": "pH Value",
            }
        )
    )
    rainfall = forms.FloatField(
        widget=forms.NumberInput(
            attrs={
                "class": "w-full p-2 border border-gray-300 rounded",
                "placeholder": "Annual Rainfall in (mm)",
            }
        )
    )

class CropYieldPredictionForm(forms.Form):
    CROP_CHOICES = [
        ("", "Select the type of crop you'd like to grow"),
        ("crop1", "Crop 1"),
        ("crop2", "Crop 2"),
        ("crop3", "Crop 3"),
        ("crop4", "Crop 4"),
    ]

    STATE_CHOICES = [
        ('', 'Select the state you want to predict yield'),
        ('1', 'State 1'),
        ('2', 'State 2'),
        ('3', 'State 3'),
        ('4', 'State 4'),
    ]

    SEASON_CHOICES = [
        ('', 'Select the season you want to grow crop'),
        ('1', 'Spring'),
        ('2', 'Summer'),
        ('3', 'Autumn'),
        ('4', 'Winter'),
    ]

    crop = forms.ChoiceField(
        choices=CROP_CHOICES,
        widget=forms.Select(
            attrs={"class": "w-full p-2 border border-gray-300 rounded"}
        ),
    )
    state = forms.ChoiceField(
        choices=STATE_CHOICES,
        widget=forms.Select(
            attrs={"class": "w-full p-2 border border-gray-300 rounded"}
        ),
    )

    season = forms.ChoiceField(
        choices=SEASON_CHOICES,
        widget=forms.Select(
            attrs={"class": "w-full p-2 border border-gray-300 rounded"}
        ),
    )

    area = forms.FloatField(
        widget=forms.NumberInput(
            attrs={
                "class": "w-full p-2 border border-gray-300 rounded",
                "placeholder": "Area in (ha)",
            }
        )
    )

    annual_rainfall = forms.FloatField(
        widget=forms.NumberInput(
            attrs={
                "class": "w-full p-2 border border-gray-300 rounded",
                "placeholder": "Annual Rainfall in (mm)",
            }
        )
    )

    fertilizer_usage = forms.FloatField(
        widget=forms.NumberInput(
            attrs={
                "class": "w-full p-2 border border-gray-300 rounded",
                "placeholder": "Fertilizer Usage in (kg/ha)",
            }
        )
    )

    pesticide_usage = forms.FloatField(
        widget=forms.NumberInput(
            attrs={
                "class": "w-full p-2 border border-gray-300 rounded",
                "placeholder": "Pesticide Usage in (kg/ha)",
            }
        )
    )