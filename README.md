# 
# Django Recipe Generator & Nutrition Calculator

This project is a Django-based application that interacts with OpenAI's GPT-4 API to generate meal recipes based on user input and calculate their nutritional values.

## Features

- **Recipe Generation**: Generate meal recipes based on user input such as number of persons, dish type, dietary restrictions, and cuisine preferences.
- **Nutritional Value Calculation**: Calculate the nutritional values (calories, protein, fat, carbohydrates, total weight) for the generated recipe.
- **User-Friendly Interface**: Simple web form to input recipe parameters and receive the generated recipe in a visually appealing format.

## Project Structure

```
.
├── recipe_project/
│   ├── recipe_project/
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── wsgi.py
│   ├── recipes/
│   │   ├── migrations/
│   │   ├── templates/
│   │   │   └── recipes/
│   │   │       ├── form.html
│   │   │       └── result.html
|   |   |       └── error.html
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── forms.py
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── openai_integration.py
│   ├── manage.py
├── .env                        # Stores the OpenAI API key
├── README.md                   # Documentation of the project
```

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Artur-Babayan/Django_Recipe_Generator.git
   cd django-recipe-generator
   ```

2. Create a virtual environment and activate it:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:

   ```bash
   pip3 install -r requirements.txt
   ```

4. Set up your OpenAI API key:

   Create a file named `.env` in the root of your project with the following content:

   ```bash
   OPENAI_API_KEY=your_openai_api_key
   ```

   Replace `your_openai_api_key` with your actual OpenAI API key.

5. Apply migrations:

   ```bash
   python3 manage.py migrate
   ```

6. Run the application:

   ```bash
   python3 manage.py runserver
   ```

7. Open your browser and go to `http://127.0.0.1:8000/recipes/generate/` to generate a recipe.

## Usage

- Use the form to input the recipe parameters like number of persons, dish type, allergies, etc.
- Submit the form to generate a recipe.
- View the generated recipe along with its nutritional values.

## Dependencies

- `Django`: Web framework for building the application.
- `openai`: Python client for OpenAI API.
- `python-dotenv`: For loading environment variables from `.env` file.

Install all dependencies with:

```bash
pip3 install django openai python-dotenv
```

