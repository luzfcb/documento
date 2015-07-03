# place form definition here
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from django.utils import six
from .models import Document, Pessoa


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


class RevertHelperFormMixin(object):
    def __init__(self, *args, **kwargs):
        super(RevertHelperFormMixin, self).__init__(*args, **kwargs)
        self.helper = RevertHelper(self)

from django.utils import six
class ReadOnlyFieldsMixin(object):
    readonly_fields = ()
    all_fields = False

    def __init__(self, *args, **kwargs):
        super(ReadOnlyFieldsMixin, self).__init__(*args, **kwargs)
        for field in (field for name, field in six.iteritems(self.fields)
                      if name in self.readonly_fields
                      or self.all_fields is True):
            field.widget.attrs['disabled'] = 'true'
            field.required = False

    def clean(self):
        cleaned_data = super(ReadOnlyFieldsMixin, self).clean()
        for field in self.readonly_fields:
            cleaned_data[field] = getattr(self.instance, field)
        return cleaned_data


class DocumentForm(SaveHelperFormMixin, forms.ModelForm):
    class Meta:
        model = Document
        fields = '__all__'


class DocumentRevertForm(RevertHelperFormMixin, forms.ModelForm):
    class Meta:
        model = Document
        fields = '__all__'


class PessoaRevertForm(RevertHelperFormMixin, forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = '__all__'


class PessoaSaveForm(SaveHelperFormMixin, forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = '__all__'
