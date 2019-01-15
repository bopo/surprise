from django.forms import ModelForm
from suit.widgets import SuitSplitDateTimeWidget

from ..models.affairs import Affairs, Notice


class AffairsForm(ModelForm):
    class Meta:
        model = Affairs
        fields = "__all__"
        widgets = {
            'created': SuitSplitDateTimeWidget,
            'modified': SuitSplitDateTimeWidget,
            'status_changed': SuitSplitDateTimeWidget,
        }


class NoticeForm(ModelForm):
    class Meta:
        model = Notice
        fields = "__all__"
        widgets = {
            'created': SuitSplitDateTimeWidget,
            'modified': SuitSplitDateTimeWidget,
            'status_changed': SuitSplitDateTimeWidget,
        }
