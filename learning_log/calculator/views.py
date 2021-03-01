from django.shortcuts import render

# Create your views here.
from django.http import HttpRequest
from django.template import RequestContext

import subprocess
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
'''
import sys
sys.path.append("D:\\OneDrive - whu.edu.cn\\桌面\\steg\\")
import mathtest
'''

def home(request):
    return render(request, 'info.html',)


def run_code(code):
    try:
        code = 'print(' + code + ')'
        output = subprocess.check_output(['python', '-c', code], universal_newlines=True, stderr=subprocess.STDOUT,
                                         timeout=30)
    except subprocess.CalledProcessError as e:
        output = '公式输入有误'
    return output


@csrf_exempt
@require_POST
def compute(request):
    code = request.POST.get('code')
    result = run_code(code)
    return JsonResponse(data={'result': result})