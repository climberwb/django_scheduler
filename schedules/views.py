from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import Http404

from django.shortcuts import render, get_object_or_404, redirect
from django.forms import formset_factory
from .models import Schedule, Activity
from .forms import ScheduleForm, ActivityForm
# Create your views here.

def schedule_list(request):
    if request.method=="POST":
        f = ScheduleForm(request.POST)
        if f.is_valid():
            stmt = f.save()
        else:
            raise Http404
    new_form = ScheduleForm()
    
    all_schedules = Schedule.objects.all()
    params = {'schedules':all_schedules,'schedule_form':new_form}
    return render(request,'schedule_list.html',params)
    
def schedule_show(request,schedule_id):
    schedule=get_object_or_404(Schedule,id=schedule_id)
    if request.method == "POST":
        schedule.delete()
        return redirect("schedules:list")
    activities = schedule.activity_set.order_by('start').all()
    params = {
        'schedule':schedule,
        'activities': activities
    }
    return render(request,'schedule_show.html',params)

def activity_delete(request,schedule_id,activity_id):
    # TODO check if given activity belongs to schedule
    activity = get_object_or_404(Activity,id=activity_id)
    activity.delete()
    return redirect(reverse("schedules:show", kwargs={'schedule_id':schedule_id}))
    

def activity_create(request,schedule_id):
    schedule=get_object_or_404(Schedule,id=schedule_id)
    if request.method=="POST":
        
        f = ActivityForm(request.POST)
        if f.is_valid():
            stmt = f.save(commit=False)
            stmt.schedule_id = schedule_id
            stmt.save()
            return redirect(reverse("schedules:show", kwargs={'schedule_id':schedule_id}))
        else:
            raise Http404
    activity_form = ActivityForm()
    
    params = {
        'schedule_id':schedule.id,
        'activity_form': activity_form
    }
    return render(request,'activity_create.html', params)
    