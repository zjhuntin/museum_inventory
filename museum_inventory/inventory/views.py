from django.shortcuts import render
from .models import Tool, CheckOutLog, Borrower
 '''
 Simple view to check in tool, though I think I will try to have it
 be done through ajax requests
 '''

def check_out_tool(request, tool_id):
    if request.POST:

def check_in_tool(request, tool_id):

@login_required
def show_checked_out(request, user_id):
    user = User.objects.get(pk=user_id).select_related()
    checked_out_tools = request.user.tool_set.all()
    return render(request, 'inventory/display_checked_out' checked_out_tools)
