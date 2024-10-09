from django import forms

class RecipeForm(forms.Form):
    amount_of_persons = forms.IntegerField(
        label="Number of Persons",
        min_value=1,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter number of persons'})
    )
    dish_type = forms.CharField(
        label="Dish Type",
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter dish type'})
    )
    max_cooking_time = forms.IntegerField(
        label="Max Cooking Time (minutes)",
        min_value=1,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter max cooking time'})
    )
    allergie_list = forms.CharField(
        label="Allergies (comma separated)",
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter allergies, e.g., nuts, gluten'})
    )
    diet_requirements = forms.CharField(
        label="Diet Requirements (comma separated)",
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter diet requirements, e.g., vegan, vegetarian'})
    )
    cuisine_list = forms.CharField(
        label="Cuisine",
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter cuisine, e.g., Italian'})
    )