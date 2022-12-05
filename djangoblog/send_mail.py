import os
from django.core.mail import send_mail
from django.conf import settings

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

if __name__ == '__main__':   

    send_mail(
        '来自www.liujiangblog.com的测试邮件',
        '欢迎访问www.liujiangblog.com！',
        'wolfoxonly@163.com',
        ['wolfoxg@gmail.com'],
    )
