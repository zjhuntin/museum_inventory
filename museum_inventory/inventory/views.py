from django.shortcuts import render
from .models import Tool, CheckOutLog, Borrower
from .forms Import CheckOutForm
from django.http import HttpResponse
from django.utils import timezone

 '''
 Simple view to check in tool, though I think I will try to have it
 be done through ajax requests
 '''

@login_required
def check_out_tool(request, tool_id):

    response = HttpResponse()

    if request.POST:
        tool = Tool.objects.get(pk=tool_id)
        if tool.checked_out:
            response.write('Tool Already Checked Out')
            return response
        form = CheckOutForm(request.POST)
        form.save()
        tool.checked_out = True
        tool.save()
        response.write('Tool {0} has been checked out.'.format(tool.name))

    else:
        response.write('Not a post.')

    return response

@login_required
def check_in_tool(request, tool_id):
    if request.POST:
        tool = Tool.objects.get(pk=tool_id)
        log = tool.get_latest_log
        log.check_in_time = timezone.now()


@login_required
def show_checked_out(request, user_id):
    user = User.objects.get(pk=user_id).select_related()
    checked_out_tools = request.user.tool_set.all()
    return render(request, 'inventory/display_checked_out' checked_out_tools)
