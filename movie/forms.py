from django.forms import ModelForm, Textarea

from movie.models import Review


class ReviewForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        self.fields['text'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Add review'}
        )
        self.fields['watchAgain'].widget.attrs.update(
            {'class': 'form-check-input'}
        )

    class Meta:
        model = Review
        fields = ['text', 'watchAgain']
        labels = {
            'watchAgain': 'Watch Again',
            'text': 'Review'
        }
        widgets = {
            'text': Textarea(attrs={'rows': 4}),
        }
