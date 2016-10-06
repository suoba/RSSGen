# !/usr/bin/env python
# -*- coding:utf-8 -*-

import leancloud

APPID = 'BzqA6gkANee9Suvk6CCc9ogW-gzGzoHsz'
# 填写应用的 APPID

APPKEY = 'UsXTxVIQKiNQYCfhyUDnhTCk'
# 填写应用的 APPKEY

MASTERKEY = '7Ax9jbK08uXXAf5sVAFx03Fx'
# 填写应用的 MASTERKEY

HEROKUAPP = r''
# 应用的 heroku 版网址（可不填）

leancloud.init(APPID,APPKEY,master_key=MASTERKEY)
