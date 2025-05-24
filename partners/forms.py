from django import forms
from .models import PartnerApplication

class PartnerApplicationForm(forms.ModelForm):
    class Meta:
        model = PartnerApplication
        fields = ['company_name', 'contact_person', 'email', 'phone', 'website', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Опишіть ваші послуги, зону покриття та інші важливі деталі'}),
            'company_name': forms.TextInput(attrs={'placeholder': 'Повна назва охоронної організації'}),
            'contact_person': forms.TextInput(attrs={'placeholder': 'ПІБ відповідальної особи'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email для зв\'язку'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Контактний телефон'}),
            'website': forms.URLInput(attrs={'placeholder': 'https://example.com'}),
        }