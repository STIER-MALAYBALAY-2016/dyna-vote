from django.shortcuts import render, HttpResponse,HttpResponseRedirect,get_object_or_404
from django.urls import reverse,reverse_lazy
from home.models import *
from django.contrib.auth.decorators import login_required
from django.core.signing import Signer
signer = Signer()
from home.forms import SignUpForm
from django.views.generic import TemplateView, CreateView
from django.db.models import Q
from django.contrib.auth import login, logout
from django.views import View
from django.utils.decorators import method_decorator

class SignUpView(CreateView):
    model = User
    form_class = SignUpForm
    template_name = 'registration/signup_form.html'


    def get_context_data(self, **kwargs):
        # do with data here
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        
        user = form.save(commit=False)
        user.save()

        login(self.request, user)

        return HttpResponseRedirect(reverse('home:home'))





@login_required
def home(request):
    poll_events = PollEvent.objects.all()
    context = {
        'poll_events':poll_events
    }
    return render(request,"home/home.html",context)

@method_decorator(login_required, name='dispatch')
class poll(View):
    template_name = 'home/poll.html'

    def get(self, request, *args, **kwargs):
        poll = get_object_or_404(PollEvent, pk=signer.unsign(kwargs['poll_id']))
        is_vote_casted = Tally.objects.filter(Q(candidate__position__event=poll) & Q(voted_by=request.user)).count()
        context = {
            'poll':poll,
            'is_vote_casted': True if is_vote_casted > 0 else False
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        selected_candidates = request.POST.getlist('selected_candidates[]')
        for sel_can in selected_candidates:
            candidate = Candidate.objects.get(pk=signer.unsign(sel_can))
            Tally.objects.create(
                candidate=candidate,
                voted_by=request.user
            )
            
        return HttpResponseRedirect(reverse('home:poll',kwargs={'poll_id':kwargs['poll_id']}))