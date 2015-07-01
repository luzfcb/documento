from django.core.urlresolvers import reverse_lazy

# Create your views here.
from django.views import generic
from .forms import DocumentForm
from .models import Document


class DocumentListView(generic.ListView):
    model = Document


class DocumentCreateView(generic.CreateView):
    template_name = 'core/document_form.html'
    model = Document
    form_class = DocumentForm
    success_url = reverse_lazy('document_list')


class DocumentUpdateView(generic.UpdateView):

    template_name = 'core/document_form.html'
    model = Document
    form_class = DocumentForm
    success_url = reverse_lazy('document_list')

