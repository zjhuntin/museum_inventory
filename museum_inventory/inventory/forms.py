from django.forms import ModelForm
from inventory.models import CheckOutLog


class CheckOutForm(ModelForm):
    class Meta:
        model = CheckOutLog
        fields = ['tool_id', 'checkout_ID']
