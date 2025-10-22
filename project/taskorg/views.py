from django.shortcuts import render
from django.views.generic.list import ListView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView
from taskorg.models import Program
from taskorg.forms import OrganizationForm 
from django.urls import reverse_lazy
from django.db.models import Q
from django.utils import timezone

class ProgramList(ListView):
   model = Program
   context_object_name = 'program'
   template_name = 'program_list.html'
   paginate_by = 5

   def get_ordering(self):
      allowed = ["prog_name", "college__college_name"]
      sort_by = self.request.GET.get("sort_by")
      if sort_by in allowed:
         return sort_by
      return "prog_name"

class OrganizationList(ListView):
 model = Program
 context_object_name = 'organization'
 template_name = 'org_list.html'
 paginate_by = 5
 ordering = ["college__college_name","name"]

 def get_queryset(self):
    qs = super().get_queryset()
    query = self.request.GET.get('q')
    
    if query:
       qs = qs.filter(
          Q(name__icontains=query) |
          Q(description__icontains=query)
          )
       return qs


class OrganizationCreateView(CreateView):
    model = Program
    form_class = OrganizationForm
    template_name = 'org_form.html'
    success_url = reverse_lazy('organization-list')

class OrganizationUpdateView(UpdateView):
    model = Program
    form_class = OrganizationForm
    template_name = 'org_form.html'
    success_url = reverse_lazy('organization-list')

class OrganizationDeleteView(DeleteView):
    model = Program
    template_name = 'org_del.html'
    success_url = reverse_lazy('organization-list')
# Create your views here.

class HomePageView(TemplateView):
   template_name = 'home.html'
