from django.shortcuts import render

def calculator(request):
    result = None
    num1 = num2 = operation = None
    if request.method == 'POST':
        try:
            num1 = float(request.POST.get('num1', 0))
            num2 = float(request.POST.get('num2', 0))
            operation = request.POST.get('operation')
            if operation == 'add':
                result = num1 + num2
            elif operation == 'subtract':
                result = num1 - num2
            elif operation == 'mulitiply':
                result = num1 * num2
            elif operation == 'devide':
                if num2 != 0:
                    result = num1 / num2
                else:
                    result = 'Cannot divide by zero'
        except:
            result = 'Invalid input'
    return render(request, 'calculator.html', {
        'result': result,
        'num1': num1,
        'num2': num2,
        'operation': operation
    })