#2.0版
selenium 已完成爬取，js直接爬取还未完成，还需努力。

# Boss-js-
Boss 直聘js破解

重点是破解这个字段
__zp_stoken__

boss_all_lang.py 文件
爬虫执行文件

但会跳转到一个js加密网址

selenium_test.py
使用selenium 爬取也会跳转到这个js网址

cookies分析是目前的进度状态


js加密.html
这个文件是加密网址 可以从里面计算出 __zp_stoken__ 的字段值，但与boss直聘的不同，还需要进一步处理。
