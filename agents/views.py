import random

from django.core.mail import send_mail
from django.views import generic
from django.urls import reverse
from leads.models import Agent
from .forms import AgentModelForm
from .mixins import OrganisorAndLoginRequiredMixin

class AgentListView(OrganisorAndLoginRequiredMixin, generic.ListView):
    template_name = 'agents/agent_list.html'
    
    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation=organisation)
    # context_object_name = 'agents'

class AgentCreateView(OrganisorAndLoginRequiredMixin, generic.CreateView):
    template_name = "agents/agent_create.html"
    form_class = AgentModelForm

    def get_success_url(self):
        return reverse("agents:agent-list")
    
    # def form_valid(self, form):
    #     user = form.save(commit=False)
    #     user.is_agent = True
    #     user.is_organisor = False
    #     user.set_password(f"{random.randint(1,100000)}")
    #     user.save()
    #     Agent.objects.create(
    #         user=user,
    #         organisation=self.request.user.userprofile
    #     )

    def form_valid(self, form):
        agent = form.save(commit=False)
        agent.is_agent = True
        agent.organisation=self.request.user.userprofile
        # agent.set_password(f"{random.randint(1,100000)}")
        agent.save()
        # Agent.objects.create(
        #     user=user,
        #     organisation=self.request.user.userprofile
        # )

        # send_mail(
        #     subject="You're invited to be an Agent.",
        #     message="You were added as an Agent on DJCRM. Please come login to start working.",
        #     from_email="admin@test.com",
        #     recipient_list=[user.email]
        # )

        return super(AgentCreateView, self).form_valid(form)

class AgentDetailView(OrganisorAndLoginRequiredMixin, generic.DetailView):
    template_name = 'agents/agent_detail.html'
    
    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation=organisation)

class AgentUpdateView(OrganisorAndLoginRequiredMixin, generic.UpdateView):
    template_name = 'agents/agent_update.html'
    queryset = Agent.objects.all()
    form_class = AgentModelForm
    context_object_name: str = "agent"

    def get_success_url(self):
        return reverse("agents:agent-list")

class AgentDeleteView(OrganisorAndLoginRequiredMixin, generic.DeleteView):
    template_name = 'agents/agent_delete.html'    
    context_object_name = "agent"

    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation=organisation)
    
    def get_success_url(self):
        return reverse("agents:agent-list")
