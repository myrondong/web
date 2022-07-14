"""
用户账户功能都是在这
"""
from django.shortcuts import render
from django.http import HttpResponse
from web.forms.account import RegisterModelForm,SendForm
def register(request):
    form = RegisterModelForm()
    return render(request,'register.html',{"form":form},status=200)

def send_sms(request):
    """发送短信注册"""
    print(request.GET)
    mobile_phone = request.GET['mobilePhone']
    tpl = request.GET['tpl']
    form = SendForm(data=request.GET)
    # 校验手机号
    if form.is_valid():
        pass
    return HttpResponse('成功')
