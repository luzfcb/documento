from __future__ import absolute_import, unicode_literals, print_function
from django.db import models
from django.utils import timezone
from django.conf import settings
from model_utils import tracker
from simple_history.models import HistoricalRecords

USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')


# basically is this:
class Document(models.Model):
    title = models.CharField(blank=True, max_length=500)
    content = models.TextField(blank=True)

    created_at = models.DateTimeField(default=timezone.now, blank=True, editable=False)
    created_by = models.ForeignKey(to=USER_MODEL,
                                   related_name="%(app_label)s_%(class)s_created_by", null=True,
                                   blank=True, on_delete=models.SET_NULL)

    modified_at = models.DateField(auto_now=True, blank=True, editable=False)
    modified_by = models.ForeignKey(to=USER_MODEL,
                                    related_name="%(app_label)s_%(class)s_modified_by", null=True,
                                    blank=True, on_delete=models.SET_NULL)

    is_active = models.NullBooleanField(default=True, editable=False)

    content_tracker = tracker.FieldTracker()

    historico_modificacoes = HistoricalRecords()

    def __unicode__(self):
        return "{}".format(self.content)

    @property
    def _history_user(self):
        return self.modified_by

    @_history_user.setter
    def _history_user(self, value):
        self.modified_by = value
