from django.shortcuts import render

# Create your views here.
#vistas de la pagina principal

def index(request):
    #render tomar el request y el template que se va a renderizar
    return render(request, 'home/index.html')

# vista de la pagina de contacto
def contacto(request):
    return render(request, 'home/contacto.html')
