from django.core.urlresolvers import reverse_lazy

# Create your views here.
from django.views import generic
from simple_history.views import HistoryRecordListViewMixin, RevertFromHistoryRecordViewMixin
from .forms import (DocumentForm, DocumentRevertForm, PessoaSaveForm,
                    ReadOnlyPessoaFodona, ReadOnlyPessoaFodona2)
from .models import Document, Pessoa


class DocumentListView(generic.ListView):
    model = Document
    ordering = ['-modified_at', ]


class DocumentCreateView(generic.CreateView):
    template_name = 'core/document_form.html'
    model = Document
    form_class = DocumentForm
    success_url = reverse_lazy('document_list')


class DocumentUpdateView(HistoryRecordListViewMixin, generic.UpdateView):
    template_name = 'core/document_form.html'
    model = Document
    form_class = DocumentForm
    success_url = reverse_lazy('document_list')
    history_records_paginate_by = 2
    history_records_field_name = ''


class DocumentRevertView(RevertFromHistoryRecordViewMixin, generic.UpdateView):
    template_name = 'core/document_form2.html'
    model = Document
    form_class = DocumentRevertForm
    success_url = reverse_lazy('document_list')
    # history_records_paginate_by = 2
    # history_records_field_name = ''


class PessoaListView(generic.ListView):
    model = Pessoa


class PessoaCreateView(generic.CreateView):
    model = Pessoa
    form_class = PessoaSaveForm
    success_url = reverse_lazy('pessoa_list')


class PessoaUpdateView(HistoryRecordListViewMixin, generic.UpdateView):
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
