from django.shortcuts import render
from .models import Calculation


def add(a, b):
    return a + b 

def sub(a, b ):
    return a - b 

def mul(a, b ):
    return a * b 

def div(a, b):
    try:
        return a / b 
    except ZeroDivisionError:
        return "Error"

def mod(a, b , c):
    try:
        return a % b 
    except ZeroDivisionError:
        return "Error"

def manual_calculate(expr):
    operators = ["+", "-", "*", "/", "%"]

    for op in operators:
        if op in expr:
            try:
                a, b   = expr.split(op)

                a = int(a)
                b = int(b)
           


                if op == "+":
                    return add(a, b )
                elif op == "-":
                    return sub(a, b)
                elif op == "*":
                    return mul(a, b )
                elif op == "/":
                    return div(a, b )
                elif op == "%":
                    return mod(a, b )

            except:
                return "Error"

def calculator_view(request):
    buttons = [
        "9", "8", "7", "6",
        "5", "4", "3", "2",
        "1", "*", "/", "-",
        "0", ".", "%", "+",
        "C", "="
    ]

    expression = ""
    result = ""

    if request.method == "POST":
        button = request.POST.get("button")
        expression = request.POST.get("expression", "")

        if button == "C":
            expression = ""
            result = ""

        elif button == "=":
            result = manual_calculate(expression)

         
            Calculation.objects.create(
                expression=expression,
                result=str(result)
            )

        else:
            expression += button

    return render(request, "calculator.html", {
        "expression": expression,
        "result": result,
        "buttons": buttons,
    })






