# main/views.py
from django.shortcuts import render

def home(request):
    # Данные для передачи
    context = {
        'contacts': {
            'phone': '+123456789',
            'email': 'info@example.com',
            'address': '123 Main St, City'
        },
        'team': [
            {'name': 'Alice', 'role': 'Developer'},
            {'name': 'Bob', 'role': 'Designer'},
            {'name': 'Charlie', 'role': 'Project Manager'},
        ]
    }
    return render(request, 'main/home.html', context)
