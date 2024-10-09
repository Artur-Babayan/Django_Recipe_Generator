from django import forms

class RecipeForm(forms.Form):
    amount_of_persons = forms.IntegerField(label="Number of Persons")
    dish_type = forms.CharField(label="Dish Type")
    max_cooking_time = forms.IntegerField(label="Max Cooking Time (minutes)")
    allergie_list = forms.CharField(label="Allergies (comma separated)")
    diet_requirements = forms.CharField(label="Diet Requirements (comma separated)")
    cuisine_list = forms.CharField(label="Cuisine")
