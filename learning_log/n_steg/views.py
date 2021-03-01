from django.shortcuts import render
from django.views.decorators import csrf
import sys
sys.path.append("D:\\OneDrive - whu.edu.cn\\桌面\\NeuralSteganography-master1\\")
import run_single
# Create your views here.


def info(request):
    """文本隐写的主页"""
    return render(request, 'n_steg/info.html')


def encrypt(request):
    """用于进行隐写加密"""
    request.encoding = 'utf-8'
    context = {}
    answers = []
    if request.POST:
        message = request.POST.get('message_text')
        algorithm = request.POST.get('steg_method')
        parameter = request.POST.get('temp')
        answers = run_single.embed(mode=algorithm, name=message, temp=parameter)

        for j in range(0, len(answers)):
            answer_temp = list(answers[j])
            for i in range(0, len(answer_temp)):
                if answer_temp[i] is '\n':
                    answer_temp[i] = '-'
            # answers[j] = str(answer_temp)
            answers[j] = ''.join(answer_temp)

        context = {'answers': answers}
    # return render(request, "post.html", ctx)
    return render(request, 'n_steg/encrypt.html', context)


def decrypt(request):
    """用于进行解码解密"""
    request.encoding = 'utf-8'
    context = {}
    answers = []
    if request.POST:
        message = request.POST.get('cover_text')
        name_en = request.POST.get('name_en')
        algorithm = request.POST.get('steg_method')
        parameter = request.POST.get('temp')

        answer_temp = list(message)
        for i in range(0, len(answer_temp)):
            if answer_temp[i] is '-':
                answer_temp[i] = '\n'
        # answers[j] = str(answer_temp)
        message = ''.join(answer_temp)

        answers = run_single.extract(mode=algorithm, name=name_en, temp=parameter, covertext=message)
        context = {'answers': answers}
    # return render(request, 'n_steg/decrypt.html')
    return render(request, 'n_steg/decrypt.html', context)



def encrypting(request):
    """处理用户数据实现加密"""

    return render(request, 'n_steg/info.html')
