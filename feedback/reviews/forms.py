from django import forms

from .models import Review

# * Basic Form (This is totally valid)
# class ReviewForm(forms.Form):
#     name = forms.CharField(
#         label="Your Name",
#         max_length=100,
#         error_messages={
#             "required": "Your name must not be empty!",
#             "max_length": "Please enter a shorter name!",
#         },
#     )
#     review_text = forms.CharField(
#         label="Your Feedback", widget=forms.Textarea, max_length=200
#     )
#     rating = forms.IntegerField(label="Your Rating", min_value=1, max_value=5)


# * ModelForm
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = "__all__"  # Alternatively you can give a list of fields from the model
        # exclude = []  # You can also do this instead
        labels = {
            "name": "Your Name",
            "review_text": "Your Feedback",
            "rating": "Your Rating",
        }
        error_messages = {
            "name": {
                "required": "Your name must not be empty!",
                "max_length": "Please enter a shorter name!",
            }
        }
