from django.shortcuts import render
from .models import Tool, CheckOutLog, Borrower


@login_required
def show_checked_out(request, user_id):
    user = User.objects.get(pk=user_id).select_related()
    checked_out_tools = request.user.tool_set.all()
    return render(request, 'inventory/display_checked_out' checked_out_tools)
