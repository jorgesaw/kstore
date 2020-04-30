"""Django forms widgets."""

# Django
from django import forms


class CustomDateInput(forms.DateInput):
    """Custom date input class."""

    input_type = 'date'
