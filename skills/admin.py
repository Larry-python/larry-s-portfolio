from django.contrib import admin
from .models import Skill,Project, Service, Testimonial
# Register your models here.
admin.site.register(Skill)
admin.site.register(Project)
admin.site.register(Service)
@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'role',
        'rating',
        'approved',
        'created_at',
    )
    
    list_filter = (
        'approved',
        'rating',
    )
    
    search_fields=(
        'name',
        'role',
        'message',
    )
    
    
actions = ['approve_testimonials']

@admin.action(description='Approve selected testimonials')
def approve_testimonials(self, request, queryset):

    updated = queryset.update(approved=True)

    self.message_user(
        request,
        f'{updated} testimonial(s) approved successfully.'
        )