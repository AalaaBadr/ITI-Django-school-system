from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect
from django.views import View
from .form import *
from .models import *

from track.models import *



# def list_instructors(req):
#     context = {}
#     instructors = Instructor.objects.all()
#     context['instructors'] = instructors
#     return render(req, 'instructor/instructors.html', context)


class ListInstructors(View):
    def get(self, req):
        context = {'instructors': Instructor.objects.all()}
        return render(req, 'instructor/instructors.html', context)

    def post(self, req):
        context = {'instructors': Instructor.objects.filter(name__contains=req.POST['search']), 'value': req.POST['search']}
        return render(req, 'instructor/instructors.html', context)


class AddInstructor(View):
    def get(self, req):
        context = {'track': Track.objects.all(), 'form': AddInstructorForm()}
        return render(req, 'instructor/add_instructor.html', context)

    def post(self, req):
        form = AddInstructorForm(req.POST)
        if form.is_valid():
            Instructor.objects.create(name=req.POST['name'], salary=req.POST['salary'],
                                      birth_date=req.POST['birthdate'], track=Track.objects.get(id=req.POST['track']))
            return HttpResponseRedirect('list')
        else:
            context = {'error': form.errors, 'form': form}
            return render(req, 'instructor/add_instructor.html', context)


# def add_instructor(req):
#     context = {}
#     if req.method == 'POST':
#         if req.POST['id'] is not None:
#             Instructor.objects.create(name=req.POST['name'], id=req.POST['id'], salary=req.POST['salary'],
#                                       birth_date=req.POST['birth_date'], track_id=req.POST['track'])
#             return HttpResponseRedirect('list')
#         else:
#             context['msg'] = 'You must enter Instructor ID'
#     return render(req, 'instructor/add_instructor.html')


@login_required
def update_instructor(req, id):
    tracks = Track.objects.all()
    old_data = Instructor.objects.get(id=id)
    modified_date = str(old_data.birth_date)
    context = {'tracks': tracks, 'old_data': old_data, 'modified_date': modified_date}
    if req.method == 'POST':
        Instructor.objects.filter(id=id).update(name=req.POST['name'], id=req.POST['id'], salary=req.POST['salary'],
                                                birth_date=req.POST['birth_date'], track_id=req.POST['track'])
        return HttpResponseRedirect('../list')
    return render(req, 'instructor/update_instructor.html', context)


@login_required
def delete_instructor(req, id):
    Instructor.objects.filter(id=id).delete()
    return HttpResponseRedirect('/instructor/list')
