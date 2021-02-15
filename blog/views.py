from django.shortcuts import render
from .models import Post

def home(request):
    
    lista = [
        'Welcome-To-The-Django',
        'Passaport-Dev-Sênior',
        'Raio-X-Regex',
        'Raio-X-POO',
        'Raio-x-TDD'
        ]
    lista_post = Post.objects.all()    
    data = {'Nome': 'Vlademir', 'Ano': 2021, 'Cursos': lista, 'Post': lista_post}
    return render(request, 'index.html', data)  
