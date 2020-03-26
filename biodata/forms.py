from django import forms
from .models import Biodata, JenjangPendidikan, Pendidikan

class BioForm(forms.ModelForm):
    class Meta:
        model = Biodata
        fields = "__all__"

class PendidikanForm(forms.ModelForm):
    class Meta:
        model = Pendidikan
        fields = "__all__"

