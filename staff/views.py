from django.shortcuts import render
from django.views.generic import DetailView
from .models import *
# Create your views here.


def about_us(request):

    groups = Group.objects.all()
    tutors = Tutor.objects.filter(tutor_position='tutor')

    return render(request, 'about-us.html', {'groups': groups, 'tutors' :tutors})


class GroupDetail(DetailView):
    """
    class for rendering group detail
    """
    model = Group
    template_name = 'class-details.html'
    context_object_name = 'group'

    def get_context_data(self, **kwargs):
        context = super(GroupDetail, self).get_context_data(**kwargs)
        group = context['group']
        tutors = group.tutor.filter(tutor_position='tutor')
        assistans = group.tutor.filter(tutor_position='assistant')
        section = group.section.all()
        context['tutors'] = tutors
        context['assistants'] = assistans
        print('section', section)
        return context



