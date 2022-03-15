# forms.py
from django import forms
from .models import ComputerSpecification

class ModuleForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ModuleForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = ComputerSpecification
        fields = ['model','core','ram','hard_disk','processor_speed','status','battery_life','screen_size','photo','phone','phone2','description','price']