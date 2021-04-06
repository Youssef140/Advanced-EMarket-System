from .models import Category

categories = Category.objects.all()

def get_categories(request):
    return {
        'categories': categories
    }