from django import forms
from django.forms import ModelForm
from polls.models import proveedor, licitaciones
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field

class add_proveedoresform(ModelForm):
    class Meta:
    	model = proveedor
    	fields = '__all__'


class add_licitacionesform(ModelForm):
	# inicio = widget{}
    class Meta:
    	model = licitaciones
    	exclude = ('fecha_chekeo', 'fecha_ubicacion')
    	fields = '__all__'
    	widgets = {
            'inicio': forms.DateInput(attrs={'type': 'date'}),
        }

helper = FormHelper()
helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))
helper.form_method = 'POST'