# !/usr/bin/env python
# -*- coding:utf-8 -*-

import leancloud

APPID = '0yyYeurRNrUCdrweSzok57AL-gzGzoHsz'
# 填写应用的 APPID

APPKEY = '2HCskXbdErEWO73y1srONuWC'
# 填写应用的 APPKEY

MASTERKEY = 'AGOwXJuF8BI6Bl0qanSQRKia'
# 填写应用的 MASTERKEY

HEROKUAPP = r''
# 应用的 heroku 版网址（可不填）

leancloud.init(APPID,APPKEY,master_key=MASTERKEY)
