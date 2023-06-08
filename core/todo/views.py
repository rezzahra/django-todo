from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Tesk
from django.urls import reverse_lazy
from django.shortcuts import redirect, get_object_or_404


class TaskList(LoginRequiredMixin, generic.ListView):
    model = Tesk
    context_object_name = "tasks"

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)


class TaskCreate(LoginRequiredMixin, generic.CreateView):
    model = Tesk
    fields = ["title"]
    success_url = reverse_lazy("list_task")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)


class TaskUpdate(LoginRequiredMixin, generic.UpdateView):
    model = Tesk
    success_url = reverse_lazy("list_task")
    fields = ['title']


class TaskDone(LoginRequiredMixin, generic.View):
    model = Tesk
    success_url = reverse_lazy("list_task")

    def get(self, request, *args, **kwargs):
        object = get_object_or_404(Tesk, pk=kwargs.get("pk"))
        object.done = True
        object.save()
        return redirect(self.success_url)


class TaskDelete(LoginRequiredMixin, generic.DeleteView):
    model = Tesk
    success_url = reverse_lazy('list_task')

    def get(self, request, *args, **kwargs):
        object = get_object_or_404(Tesk, pk=kwargs.get("pk"))
        Tesk.delete(object)
        return redirect(self.success_url)


