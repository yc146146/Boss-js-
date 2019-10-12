import requests

import re

import time
import lxml
import lxml.etree

import datetime
import json
import os

#获取数据
def get_data(job_type):
	headers = {
	"cookie": "__zp_stoken__=83e1X5YpcRFMK1zJSxLlD%2Fq29HxRpoAvm5wYUBQ1y1yirE0gTv6UxKTwAB1XMKxwvGetlVjwo8c7ASjRS9CyEYyEcg%3D%3D	",
	"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"
	}

	#算出
	#d4941heL0wAtaBjUUGn%2BG0yjgNIPpBdrGbafLiOdL0vBnygY0jEG9Y%2BfOhDkUPxzTueFxegwoSzfkodfvQIZuqi4tIblCzgvuMabFR2liUJhDF0%3D
	#d4941heL0wAtaBjUUGn%2BG0yjgNVypkHTTdeNWtd6KrSBpT%2BwFzGCr8uwFdFNM8vSAgi6wDNGkwQcJWtxt%2FLKnr8XkA%3D%3D
	#d4941heL0wAtaBjUUGn%2BG0yjgHvbi1lB6QxS5HoL9Ga84MkA%2BpVQYBMt9I9IWWE9AFbmo8Dx7uqa6zArFfl9QCjfhA%3D%3D

	#找出
	#d4941heL0wAtaBjUUGn%2BG0yjgP6UdkZe8v0C9dyIzETj7vWzOICWJoUcJjDH0Ps0ibR8y%2BHJGW7eHFbmdJr2Trn1og%3D%3D
	#d4941heL0wAtaBjUUGn%2BG0yjgOkoNF5t52d9%2BsjykSqZkQ%2FAP5ET7PGaMLAuBcdh3VgoGRm747Z8ozsOeBclpooXpA%3D%3D		
	#d4941heL0wAtaBjUUGn%2BG0yjgOkoNF5t52d9%2BsjykSqZkQ%2FAP5ET7PGaMLAuBcdh3VgoGRm747Z8ozsOeBclpooXpA%3D%3D	

	#计算昨天
	date_old = datetime.datetime.now() - datetime.timedelta(days=1)
	date_old = str(date_old)[:10]
	#date_old_str = date_old
	date_old = datetime.datetime.strptime(date_old,"%Y-%m-%d")

	#停止标志
	stop_flag = 0

	#写入文件前的列表
	item_lists=[]

	i = 0

	url_https = "https://www.lagou.com/jobs/list_python?px=new&city=全国"
	url_json = 'https://www.lagou.com/jobs/positionAjax.json?px=new&city=全国'

	#无线循环去提取数据
	while i<1:
	#for i in range(1,20):
		
		i += 1

		if stop_flag == 1:
			print(i)
			print("外部结束")
			break
			
		print("第 %d 次"%i)

		#url = "https://www.liepin.com/zhaopin/?isAnalysis=&dqs=010&pubTime=&salary=&subIndustry=&industryType=&compscale=&key="+job_type+"&init=-1&searchType=1&headckid=3f6ecbd086bc43eb&compkind=&fromSearchBtn=2&sortFlag=15&ckid=5ad0d88e8843d1ff&degradeFlag=0&jobKind=&industries=&clean_condition=&siTag=L-w5IwSlwjrBONoihH-bfA~F5FSJAXvyHmQyODXqGxdVw&d_sfrom=search_sub_site&d_ckId=a5fa4c20a16d10fa83c0162f6decfd11&d_curPage=1&d_pageSize=40&d_headId=79d2e58aee5351493c98ea314807d3f7&curPage="+str(i)
		#url = "https://www.zhipin.com/c101010100/?query="+job_type+"&page="+str(i)
		#url = "https://www.zhipin.com/?ka=header-home"
		#url = "https://www.zhipin.com/job_detail/6f8d7ea774c360d31H153tm9FFU~.html?ka=search_list_1"
		#url = "https://www.zhipin.com/c101010100/?query=Php&page=1&ka=page-1"
		url = "https://www.zhipin.com/c101010100/?query=Php&page=1&ka=page-1"

		# try:
		# 	response = requests.get(url, headers = headers)
		# 	print(response.content.decode("gbk"))
		# 	out_tree = lxml.etree.HTML(response.content)
		# except:
		# 	time.sleep(10)
		# 	response = requests.get(url, headers = headers)
		# 	#print(response.content.decode("gbk"))
		# 	out_tree = lxml.etree.HTML(response.content)

		response = requests.get(url, headers = headers)
		print(response.content.decode("utf-8"))

		print("加密网址： "+response.url)

		#job_info_list = mytree.xpath('//div[@class="describtion__detail-content"]//text()')


		#爬取外部列表页数据
		tables = out_tree.xpath('//ul/li')

		

		for context in tables:

			job_title = context.xpath('./div/div[@class="info-primary"]/h3/a/div/text()')
			job_href = context.xpath('./div/div[@class="info-primary"]/h3/a/@href')
			company = context.xpath('./div/div[@class="info-company"]/div/h3/a/text()')
			job_info = context.xpath('./div/div[@class="info-primary"]/p/text()')

			salary = context.xpath('./div/div[@class="info-primary"]/h3/a/span[@class="red"]/text()')

			#company_type = context.xpath("./i/b/text()")
			# address= context.xpath('.//div[@class="job-info"]/p[@class="condition clearfix"]/a[@class="area"]//text()')
			# education= context.xpath('.//div[@class="job-info"]/p[@class="condition clearfix"]/span[@class="edu"]/text()')
			# experience= context.xpath('.//div[@class="job-info"]/p[@class="condition clearfix"]/span[-1]/text()')
			
			print(job_title)
			print(job_href)
			print(company)
			print(job_info)
			print(salary)

			# job_title = job_title[0] if job_title else ""
			# job_href = job_href[0] if job_href else ""
			# company = company[0] if company else ""
			# date = date[0] if date else ""
			# job_info = job_info[0] if job_info else ""

		
			#address, experience, education = job_info

	# 		job_title = re.sub(r"\s", "", job_title)

	# 		if education.find("大专") >= 0:
	# 			education = "大专"
	# 		elif education.find("本科") >= 0:
	# 			education = "本科"
	# 		elif education.find("硕士") >= 0:
	# 			education = "硕士"
	# 		elif education.find("博士") >= 0:
	# 			education = "博士"
	# 		elif education.find("学历不限") >= 0:
	# 			education = "学历不限"
	# 		elif education.find("中专") >= 0:
	# 			education = "中专"
	# 		elif education.find("高中") >= 0:
	# 			education = "高中"

	# 		if experience == "1年以上":
	# 			experience = "1年经验"
	# 		elif experience == "2年以上":
	# 			experience = "2年经验"
	# 		elif experience == "3年以上" or experience == "4年以上":
	# 			experience = "3-4年经验"
	# 		elif experience == "5年以上":
	# 			experience = "5-7年经验"

	# 		#date = date
	# 		#re.sub(r"\s","", date)
	# 		date = re.findall(r"([0-9]+)", date)
	# 		date = "-".join(date)
	# 		#print(date)

	# 		date_str = date
	# 		date = datetime.datetime.strptime(date,"%Y-%m-%d")

	# 		# print(date)
	# 		# print(date_old)
	# 		# time.sleep(1)
			

	# 		#如果日期小于昨天则 停止
	# 		if date < date_old:
	# 			stop_flag = 1
	# 			print("内部结束")
	# 			break

	# 		#如果标题中不存在python 或 Python 则跳过
	# 		#if job_title.find("python") == -1 and job_title.find("Python") == -1:
	# 		# if job_title.upper().find("python") == -1 and job_title.find("Python") == -1:
	# 		# 	continue

	# 		#如果日期大于昨天则 跳过
	# 		if date > date_old:
	# 			continue

	# 		try:
	# 			if salary != "":
	# 				if salary == "面议":
	# 					salary_min = 0
	# 					salary_max = 0
	# 				else:
	# 					#金额 与 时间 换算
	# 					money = salary
	# 					unit = None
	# 					salary_min = 0
	# 					salary_max = 0

	# 					money, unit = money[:-1], money[-1]
	# 					salary_min, salary_max = eval(money.split("-")[0]),eval(money.split("-")[1])

	# 					if unit == "万":
	# 						salary_min, salary_max = round(salary_min/12 * 10000,2), round(salary_max/12 * 10000,2)
	# 					else:
	# 						salary_min = 0
	# 						salary_max = 0

	# 			else:
	# 				salary_min = 0
	# 				salary_max = 0

	# 		except:
	# 			salary_min = -1
	# 			salary_max = salary

	# 		#标题去空格
	# 		#job_title = job_title.replace(" ","")
	# 		#job_title = re.sub(r"\s","", job_title)

	# 		item = {}
	# 		job_type_temp = ""
	# 		if job_type == "C%2B%2B":
	# 			job_type_temp = "C++"
	# 		elif job_type == "C%23":
	# 			job_type_temp = "C#"
	# 		elif job_type == "Go语言":
	# 			job_type_temp = "Golang"
	# 		else:
	# 			job_type_temp = job_type


	# 		if job_href.find("/a/") == 0:
	# 			job_href = "https://www.liepin.com"+job_href

	# 		item["job_type"] = job_type_temp
	# 		item["platform"] = "liepin"
	# 		item["profession_type"] = "后端开发语言"
	# 		item["job_title"] = job_title
	# 		item["job_href"] = job_href
	# 		item["address"] = address
	# 		item["company"] = company
	# 		item["salary_min"] = salary_min
	# 		item["salary_max"] = salary_max
	# 		item["date"] = date_str
	# 		item["education"] = education
	# 		item["experience"] = experience


	# 		#爬取内部详情页数据
	# 		#arg2 = ""
	# 		sess = requests.session()
	# 		#job_href = 'https://www.liepin.com/job/1914905602.shtml'
	# 		#job_href = 'https://www.liepin.com/a/15893903.shtml'
	# 		try:
	# 			response2 = sess.get(job_href, headers = headers)
	# 			in_tree = lxml.etree.HTML(response2.content)

	# 		except:
	# 			time.sleep(10)
	# 			response2 = sess.get(job_href, headers = headers)
	# 			in_tree = lxml.etree.HTML(response2.content)

	# 		#print(response2.text)

	# 		job_info_list = ""
	# 		company_ownership = ""
	# 		company_size = ""


			# job_info_list = in_tree.xpath('//div[@class="detail-content"]/div[@class="job-sec"]/div[@class="text"]/text()')

			# company_ownership = in_tree.xpath('//div[@class="job-sider"]/div[@class="sider-company"]/p[4]/a/text()')
			# company_size = in_tree.xpath('//div[@class="job-sider"]/div[@class="sider-company"]/p[3]/text()')




			
	# 		address_detail = in_tree.xpath('//p[@class="basic-infor"]/span/a/text()')
	# 		#print(len(address_detail))
			
	# 		if len(address_detail) <= 0:
	# 			address_detail = in_tree.xpath('//p[@class="basic-infor"]/span/text()')

	# 		# print(job_info_list)
	# 		# print(address_detail)
	# 		# print(company_ownership)
	# 		#print(company_size)


	# 		job_info_list = job_info_list if job_info_list else ""
	# 		address_detail = address_detail[0] if address_detail else ""
	# 		company_ownership = company_ownership[0] if company_ownership else ""


	# 		job_info = []
	# 		for job in job_info_list:
	# 			#替换不可见字符
	# 			job_temp = re.sub(r"\s", "",job)
	# 			#匹配字母数字
	# 			job_temp = re.findall(r"([\S]+)", job_temp)
	# 			if job_temp:
	# 				job_info.append(job_temp[0])

	# 		#item={}
	# 		item["job_info"] = job_info
	# 		item["address_detail"] = address_detail
	# 		item["company_ownership"] = company_ownership
	# 		item["company_size"] = company_size
	# 		item["company_type"] = "私企"


	# 		print(item)
	# 		item_lists.append(item)
	# #返回所有数据
	# return item_lists

#保存结果
def save_date(item_lists, job_type):
	json_list = json.dumps(item_lists, ensure_ascii=False)

	today = str(datetime.date.today())

	if job_type == "C%2B%2B":
		job_type = "C++"
	elif job_type == "C%23":
		job_type = "C#"
	elif job_type == "Go语言":
		job_type = "Go语言"

	d = "./content_file/liepin_all_lang_"+ today
	if not os.path.exists(d):
		os.makedirs(d)

	try:
		#保存爬取数据
		#with open('./content_file/51job_'+job_type+'_'+today+'.json', 'w', encoding="utf-8") as f:
		with open(d+"/"+job_type+'.json', 'w', encoding="utf-8") as f:
			f.write(json_list)

		#保存日志记录数据
		with open('./content_file/logs.txt', 'a+', encoding="utf-8") as f:
			f.write( today+" "+job_type+"_的总条数:"+str(len(item_lists))+"\n" )

		return 1
	except:
		return 0

#执行函数
if __name__ == '__main__':

	today = str(datetime.date.today())

	d = "./content_file/liepin_all_lang_"+ today
	if not os.path.exists(d):
		os.makedirs(d)

	#job_type = "ASP"
	job_type_list = ["ASP"]
	
	#job_type_list = ["Java","C++","PHP","C#",".NET","Hadoop","Python","Delphi","VB","Perl","Ruby","Node.js","Go","ASP"]
	#job_type_list = ["C%252B%252B","PHP","C%2523",".NET","HADOOP","PYTHON","DELPHI","VB","PERL","RUBY","NODE.JS","GO%25E8%25AF%25AD%25E8%25A8%2580","GOLANG","ASP","JAVA"]

	#job_type_list = ["C%2B%2B","PHP","C%23",".NET","Hadoop","Python","Delphi","VB","Perl","Ruby","Node.js","Go语言","Golang","ASP","Java"]


	for job_type in job_type_list:

		item_lists = get_data(job_type)
		res = save_date(item_lists, job_type)

		if res:
			print(job_type+":完成")