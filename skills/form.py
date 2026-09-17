from django import forms
from .models import Testimonial


class TestimonialForm(forms.ModelForm):

    class Meta:
        model = Testimonial

        fields = [
            'name',
            'role',
            'message',
            'image',
            'rating',
        ]

        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Your name',
                'class': 'form-input',
            }),

            'role': forms.TextInput(attrs={
                'placeholder': 'Your role or profession',
                'class': 'form-input',
            }),

            'message': forms.Textarea(attrs={
                'placeholder': 'Tell me about your experience...',
                'class': 'form-input',
                'rows': 6,
            }),

            'rating': forms.Select(
                choices=[
                    (5, '★★★★★ - Excellent'),
                    (4, '★★★★☆ - Very Good'),
                    (3, '★★★☆☆ - Good'),
                    (2, '★★☆☆☆ - Fair'),
                    (1, '★☆☆☆☆ - Poor'),
                ],
                attrs={
                    'class': 'form-input',
                }
            ),
        }