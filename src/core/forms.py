# place form definition here
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from .models import Document


class SaveHelper(FormHelper):
    def __init__(self, form=None):
        super(SaveHelper, self).__init__(form)
        self.layout.append(Submit(name='save', value='Salvar'))
        self.form_show_errors = True
        self.render_required_fields = True


class SaveHelperFormMixin(object):
    def __init__(self, *args, **kwargs):
        super(SaveHelperFormMixin, self).__init__(*args, **kwargs)
        self.helper = SaveHelper(self)



class RevertHelper(FormHelper):
    def __init__(self, form=None):
        super(RevertHelper, self).__init__(form)
        self.layout.append(Submit(name='revert', value='Reverter'))
        self.form_show_errors = True
        self.render_required_fields = True

class DocumentForm(SaveHelperFormMixin, forms.ModelForm):
    class Meta:
        model = Document
        fields = '__all__'


class DocumentRevertForm(RevertHelper, forms.ModelForm):
    class Meta:
        model = Document
        fields = '__all__'

