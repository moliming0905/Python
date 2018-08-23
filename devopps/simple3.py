#encoding=utf-8

import dns.resolver

domain = raw_input('Please input an domain: ')
#指定查询类型为NS记录
ns = dns.resolver.query(domain,'NS')

for i in ns.response.answer:
	for j in i.items:
		print(j.to_text())