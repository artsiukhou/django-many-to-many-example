# django-many-to-many-example

Simple example of many-to-many objects relationships with additional metadata using Django & DjangoRestFramework.

I've also used 2 different serializers as I need to display this relationship items differently on GetRecipe and on CreateRecipe.


# Run
1. Clone the repo
2. Install and active virtual environment
3. Install all the dependencies from `requirements.txt`
4. Run & apply migrations
5. Start django server
```bash
python manage.py runserver
```
6. Go to http://127.0.0.1:8000/api/ingredient to create some ingredients
7. Go to http://127.0.0.1:8000/api/recipe/ to create some recipies