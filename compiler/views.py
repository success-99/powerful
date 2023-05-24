from django.shortcuts import render
import subprocess

def home(request):
    return render(request, 'compiler/home.html')

def run_code(request):
    if request.method == 'POST':
        code = request.POST.get('code')
        try:
            result = subprocess.check_output(['python', '-c', code], stderr=subprocess.STDOUT, timeout=5)
            return render(request, 'compiler/home.html', {'result': result.decode('utf-8')})
        except subprocess.CalledProcessError as e:
            return render(request, 'compiler/home.html', {'error': e.output.decode('utf-8')})
        except subprocess.TimeoutExpired:
            return render(request, 'compiler/home.html', {'error': 'Execution timed out.'})
    return render(request, 'compiler/home.html')
