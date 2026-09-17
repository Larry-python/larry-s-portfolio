from .models import Service, Testimonial,Project
from django.shortcuts import render, redirect
from my_profile.models import Profile
from .form import TestimonialForm


def services(request):
    profile = Profile.objects.first()
    services = Service.objects.all()

    context = {
        'profile': profile,
        'services': services,
    }

    return render(request, 'service.html', context)


def testimonials(request):
    profile = Profile.objects.first()

    testimonials = Testimonial.objects.filter(
        approved=True
    )

    context = {
        'profile': profile,
        'testimonials': testimonials,
    }

    return render(request, 'testimonial.html', context)

def leave_testimonial(request):

    if request.method == 'POST':
        form = TestimonialForm(request.POST, request.FILES)

        if form.is_valid():
            testimonial = form.save(commit=False)

            testimonial.profile = Profile.objects.first()
            testimonial.approved = False

            testimonial.save()

            return redirect('testimonial_success')

    else:
        form = TestimonialForm()

    context = {
        'form': form,
    }

    return render(
        request,
        'leave_testimonial.html',
        context
    )
def testimonial_success(request):
    return render(
        request,
        'testimonial_success.html'
    )



def projects(request):
    profile = Profile.objects.first()
    projects = Project.objects.all()

    context = {
        'profile': profile,
        'projects': projects,
    }

    return render(request, 'project.html', context)