from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, DeleteView
from django.views import View
from django.urls import reverse_lazy
from .form import *
from .modelForm import *
from .models import *


# def list_tracks(req):
#     context = {'tracks': Track.objects.all()}
#     return render(req, 'track/tracks.html', context)


# class ListTracks(View):
#     def get(self, req):
#         context = {'tracks': Track.objects.all()}
#         return render(req, 'track/tracks.html', context)
#
#     def post(self, req):
#         context = {'tracks': Track.objects.filter(name__contains=req.POST['search']), 'value': req.POST['search']}
#         return render(req, 'track/tracks.html', context)


class ListTrack(ListView):
    model = Track
    def post(self, req):
        context = {'object_list': Track.objects.filter(name__contains=req.POST['search']), 'value': req.POST['search']}
        return render(req, 'track/track_list.html', context)



@login_required
def add(req):
    context = {'form': AddTrack()}
    if req.method == 'POST':
        form = AddTrack(req.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('list')
    return render(req, 'track/add_track.html', context)


# class AddTrack(View):
#     def get(self, req):
#         context = {'form': AddTrackForm()}
#         return render(req, 'track/add_track.html', context)
#
#     def post(self, req):
#         form = AddTrackForm(req.POST)
#         if form.is_valid():
#             Track.objects.create(name=req.POST['name'])
#             return HttpResponseRedirect('list')
#         else:
#             context = {'error': form.errors, 'form': form}
#             return render(req, 'track/add_track.html', context)


# def add_track(req):
#     context = {}
#     if req.method == 'POST':
#         if req.POST['name'] is not None:
#             Track.objects.create(name=req.POST['name'], id=req.POST['id'])
#             return HttpResponseRedirect('list')
#         else:
#             context['msg'] = 'You must enter Track Name'
#     return render(req, 'track/add_track.html')


@login_required
def update_track(req, id):
    context = {'old_data': Track.objects.get(id=id)}
    if req.method == 'POST':
        Track.objects.filter(id=id).update(id=req.POST['id'], name=req.POST['name'])
        return HttpResponseRedirect('../list')
    return render(req, 'track/update_track.html', context)


# def delete_track(req, id):
#     Track.objects.filter(id=id).delete()
#     return HttpResponseRedirect('/track/list')


class DeleteTrack(DeleteView):
    model = Track
    success_url = reverse_lazy("list.tracks")
