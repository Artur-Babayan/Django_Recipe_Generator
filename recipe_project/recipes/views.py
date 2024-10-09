from django.shortcuts import render
from .forms import RecipeForm
from .openai_integration import RecipeGenerator, NutritionCalculator

def generate_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe_generator = RecipeGenerator()
            nutrition_calculator = NutritionCalculator()

            amount_of_persons = form.cleaned_data['amount_of_persons']
            dish_type = form.cleaned_data['dish_type']
            max_cooking_time = form.cleaned_data['max_cooking_time']
            allergie_list = form.cleaned_data['allergie_list'].split(',')
            diet_requirements = form.cleaned_data['diet_requirements'].split(',')
            cuisine_list = form.cleaned_data['cuisine_list']

            prompt = recipe_generator.generate_recipe_prompt(
                amount_of_persons, dish_type, max_cooking_time, allergie_list, diet_requirements, cuisine_list,
                output_data_format="JSON with parameters: 'Name', 'CookingTime', 'RequiredTools', 'Ingredients', 'Step-by-step directions'"
            )
            recipe = recipe_generator.get_recipe_from_openai(prompt)

            if recipe is None:
                return render(request, 'recipes/error.html', {'message': 'Failed to generate recipe. Please try again later.'})

            nutritional_values = nutrition_calculator.calculate_nutritional_values(recipe)

            if nutritional_values:
                recipe['nutritional_values'] = nutritional_values

            return render(request, 'recipes/result.html', {'recipe': recipe})
    else:
        form = RecipeForm()

    return render(request, 'recipes/form.html', {'form': form})
