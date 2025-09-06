from django.shortcuts import render
from .models import User, Product

# Create your views here.
def integrated_view(request):
    users = User.objects.all()
    context = {
        'users': [
            {'name': u.name, 'products': [p.name for p in u.product_set.all()]} for u in users
        ]
    }
    return render(request, 'core/integrated.html', context)
