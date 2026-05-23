from django.shortcuts import render
# Create your views here.

def inicioV(request):  
    return render(request,"calculadoraApp/inicio.html")

def calculadoraV(request):  
    return render(request,"calculadoraApp/index.html")

def obtener_numeros(request): #recupero los numeros ingresados en pantalla
    n1 = request.POST.get('n1', 0)
    n2 = request.POST.get('n2', 0)
    return float(n1), float(n2), n1, n2
#Vista de la suma
def sumaV(request):
    num1, num2, n1, n2 = obtener_numeros(request)
    resultado = num1 + num2
    context = {'resultado': resultado, 'n1': n1, 'n2': n2}
    return render(request, "calculadoraApp/index.html", context)
   
# Vista de la Resta
def restaV(request):
    num1, num2, n1, n2 = obtener_numeros(request)
    resultado = num1 - num2
    context = {'resultado': resultado, 'n1': n1, 'n2': n2}
    return render(request, "calculadoraApp/index.html", context)
   
# Vista de la Multiplicación
def multiplicacionV(request):
    num1, num2, n1, n2 = obtener_numeros(request)
    resultado = num1 * num2
    context = {'resultado': resultado, 'n1': n1, 'n2': n2}
    return render(request, "calculadoraApp/index.html", context)
   
# Vista de la División
def divisionV(request):
    num1, num2, n1, n2 = obtener_numeros(request)
    if num2 == 0:
        resultado = "Error: División por 0"
    else:
        resultado = num1 / num2
    context = {'resultado': resultado, 'n1': n1, 'n2': n2}
    return render(request, "calculadoraApp/index.html", context)



   
