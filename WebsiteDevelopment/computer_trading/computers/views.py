from django.shortcuts import render
from django.views.generic import ListView,DetailView,TemplateView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import ComputerSpecification
from .forms import ModuleForm
from django.urls import reverse_lazy,reverse
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.models import User
# Create your views here.
class ComputersListView(ListView):
    model = ComputerSpecification
    template_name = "computers.html" 
    context_object_name="all_computers"
class ComputerDetailView(DetailView):
    model = ComputerSpecification
    template_name="computer_detail.html"
    context_object_name="computer"
class ComputerUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name="computer_update.html"
    model = ComputerSpecification
    fields="__all__"
    def test_func(self):
        if self.request.user== self.get_object().author:
            return True
        else:
            reverse_lazy('computers')
class ComputerCreateView(LoginRequiredMixin,CreateView):
   
    template_name="computer_add.html"
    form_class = ModuleForm
    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)
   
class ComputerDeleteView( LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    template_name="computer_delete.html"
    model = ComputerSpecification
    success_url=reverse_lazy("computers")
    context_object_name="computer"
    def test_func(self):
        return self.request.user== self.get_object().author
class UsedView(ListView):
    template_name="used.html"
    model=ComputerSpecification
    context_object_name="computer"
    
    
