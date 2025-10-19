from django.shortcuts import render
from django.views.generic.list import ListView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from taskorg.models import Organization
from taskorg.forms import OrganizationForm 
from django.urls import reverse_lazy
from django.db.models import Q
from django.utils import timezone

class HomePageView(ListView):
    model = Organization
    context_object_name = 'home'
    template_name = "home.html"
    
    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context["total_students"] = Student.objects.count()
       
       today = timezone.now().date()
       count = (
          OrgMember.objects.filter(
             date_joined__year=today.year
             )
             .values("student")
             .distinct()
             .count()
        )
       
       context["students_joined_this_year"] = count
       return context

class OrganizationList(ListView):
 model = Organization
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
    model = Organization
    form_class = OrganizationForm
    template_name = 'org_form.html'
    success_url = reverse_lazy('organization-list')

 class OrganizationUpdateView(UpdateView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'org_form.html'
    success_url = reverse_lazy('organization-list')

 class OrganizationDeleteView(DeleteView):
    model = Organization
    template_name = 'org_del.html'
    success_url = reverse_lazy('organization-list')
# Create your views here.
