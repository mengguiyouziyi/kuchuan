# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

import base64
from random import choice

# 代理服务器
proxyServer = "http://proxy.abuyun.com:9020"

# 代理隧道验证信息
# proxyUser = "H4XGPM790E93518D"
# proxyPass = "2835A47D56143D62"

# 1
# proxyUser = "HJA1354AT829M77D"
# proxyPass = "F222C0D807890356"

# 2
# proxyUser = "H8J738EHR4H5GE5D"
# proxyPass = "3018672C5A167A3D"

# 3
# proxyUser = "HWAP93ES770B921D"
# proxyPass = "FD67384CCCADBF04"

# 4
# proxyUser = "H24CFQ64JP06V1WD"
# proxyPass = "FA1D98DF8F3E55FF"

# 5
# proxyUser = "HQ78N3Y82239165D"
# proxyPass = "AA99073C3271DBFA"

# 6
proxyUser = "HQ78N3Y82239165D"
proxyPass = "AA99073C3271DBFA"


# for Python3
proxyAuth = "Basic " + base64.urlsafe_b64encode(bytes((proxyUser + ":" + proxyPass), "ascii")).decode("utf8")


class ProxyMiddleware(object):
	def process_request(self, request, spider):
		request.meta["proxy"] = proxyServer
		request.headers["Proxy-Authorization"] = proxyAuth


class RetryMiddleware(object):
	def process_response(self, request, response, spider):
		if response.status == 429:
			print('wrong status: %s, retrying~~' % response.status, request.meta['item']['ap'])
			return request.replace(url=request.url)
		else:
			return response

	def process_exception(self, request, exception, spider):
		return request.replace(url=request.url)


class RotateUserAgentMiddleware(object):
	"""Middleware used for rotating user-agent for each request"""

	def __init__(self, agents):
		self.agents = agents

	@classmethod
	def from_crawler(cls, crawler):
		return cls(crawler.settings.get('USER_AGENT_CHOICES', []))

	def process_request(self, request, spider):
		request.headers.setdefault('User-Agent', choice(self.agents))
