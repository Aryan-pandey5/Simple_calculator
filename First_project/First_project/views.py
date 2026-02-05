from django.http import HttpResponse
from django.shortcuts import render


def calculator(request):

    try:
        if request.method =="POST":
            num1 = int(request.POST.get('num1'))
            num2 = int(request.POST.get('num2'))
            operation = request.POST.get('operation')

            result = None

            if operation == 'add':
                result = num1 + num2
            elif operation == 'subtract':
                result = num1 - num2
            elif operation == 'multiply':
                result = num1 * num2
            elif operation == 'divide':
                if num2 != 0:
                    result = num1 / num2
                else:
                    result = "Error: Division by zero"

            return render(request, "calculator.html", {'output': result})

    except Exception as e:
        print(e)    
    return render(request, "calculator.html")