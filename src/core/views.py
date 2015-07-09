from django.core.urlresolvers import reverse_lazy

# Create your views here.
from django.views import generic
from simple_history.views import HistoryRecordListViewMixin, RevertFromHistoryRecordViewMixin
from .forms import (DocumentForm, DocumentRevertForm, PessoaSaveForm,
                    ReadOnlyPessoaFodona, ReadOnlyPessoaFodona2)
from .models import DocumentContent, Pessoa


class DocumentContentListView(generic.ListView):
    model = DocumentContent
    ordering = ['-modified_at', ]


class DocumentContentCreateView(generic.CreateView):
    template_name = 'core/documentcontent_form.html'
    model = DocumentContent
    form_class = DocumentForm
    success_url = reverse_lazy('document_list')


class DocumentContentUpdateView(HistoryRecordListViewMixin, generic.UpdateView):
    template_name = 'core/documentcontent_form.html'
    model = DocumentContent
    form_class = DocumentForm
    success_url = reverse_lazy('document_list')
    history_records_paginate_by = 2
    history_records_field_name = ''


class DocumentContentRevertView(RevertFromHistoryRecordViewMixin, generic.UpdateView):
    template_name = 'core/documentcontent_form2.html'
    model = DocumentContent
    form_class = DocumentRevertForm
    success_url = reverse_lazy('document_list')
    # history_records_paginate_by = 2
    # history_records_field_name = ''


class PessoaListView(generic.ListView):
    model = Pessoa


class PessoaCreateView(generic.CreateView):
    template_name = 'core/pessoa_form.html'
    model = Pessoa
    form_class = PessoaSaveForm
    success_url = reverse_lazy('pessoa_list')


class PessoaUpdateView(HistoryRecordListViewMixin, generic.UpdateView):
    template_name = 'core/pessoa_form.html'
    model = Pessoa
    form_class = PessoaSaveForm
    success_url = reverse_lazy('pessoa_list')


class PessoaHistoryView(HistoryRecordListViewMixin, generic.DetailView):
    model = Pessoa


class PessoaRevertView(RevertFromHistoryRecordViewMixin, generic.UpdateView):
    model = Pessoa
    history_records_field_name = 'historico_modificacoes'
    form_class = ReadOnlyPessoaFodona2  # PessoaRevertForm
    success_url = reverse_lazy('pessoa_list')


class PessoaIndexView(generic.TemplateView):
    template_name = 'core/pessoa_index.html'


