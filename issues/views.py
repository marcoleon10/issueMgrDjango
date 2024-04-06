from typing import Any
from django.views.generic import(
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Issue
from django.urls import reverse_lazy
from django.contrib.auth.mixins import(
    LoginRequiredMixin,
    UserPassesTestMixin
)


class IssueListView(ListView):
    template_name = "issues/list.html"
    model = Issue
    
    
class IssueDetailView(DetailView):
    template_name = "issues/detail.html"
    model = Issue

class IssueCreateView(LoginRequiredMixin, CreateView):
    template_name = "issues/new.html"
    model = Issue
    fields = ["summary", "status","priority", "reporter", "assignee"]
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    
class IssueUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = "issues/edit.html"
    model = Issue
    fields = ["summary", "status","priority", "reporter", "assignee"]
    
    def test_func(self):
        issue = self.get_object()
        return issue.reporter == self.request.user  # Comparamos con el reporter en lugar del author

    
class IssueDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = "issues/delete.html"
    model = Issue
    success_url = reverse_lazy("list")
    
    def test_func(self):
        issue = self.get_object()
        return issue.reporter == self.request.user
    