from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect
from django.views import View
from .form import *
from .models import *
from track.models import *


# def list_trainees(req):
#     context = {}
#     trainees = Trainee.objects.all()
#     context['trainees'] = trainees
#     return render(req, 'trainee/trainees.html', context)


class ListTrainees(View):
    def get(self, req):
        context = {'trainees': Trainee.objects.all()}
        return render(req, 'trainee/trainees.html', context)

    def post(self, req):
        context = {'trainees': Trainee.objects.filter(name__contains=req.POST['search']), 'value': req.POST['search']}
        return render(req, 'trainee/trainees.html', context)


class AddTrainee(View):
    def get(self, req):
        context = {'track': Track.objects.all(), 'form': AddTraineeForm()}
        return render(req, 'trainee/add_trainee.html', context)

    def post(self, req):
        form = AddTraineeForm(req.POST)
        if form.is_valid():
            Trainee.objects.create(name=req.POST['name'], birth_date=req.POST['birthdate'],
                                   track=Track.objects.get(id=req.POST['track']))
            return HttpResponseRedirect('list')
        else:
            context = {'error': form.errors, 'form': form}
            return render(req, 'trainee/add_trainee.html', context)


@login_required
def update_trainee(req, id):
    tracks = Track.objects.all()
    old_data = Trainee.objects.get(id=id)
    modified_date = str(old_data.birth_date)
    context = {'tracks': tracks, 'old_data': old_data, 'modified_date': modified_date}
    if req.method == 'POST':
        Trainee.objects.filter(id=id).update(name=req.POST['name'], id=req.POST['id'],
                                             birth_date=req.POST['birth_date'], track_id=req.POST['track'])
        return HttpResponseRedirect('../list')
    return render(req, 'trainee/update_trainee.html', context)


@login_required
def delete_trainee(req, id):
    Trainee.objects.filter(id=id).delete()
    return HttpResponseRedirect('/trainee/list')
