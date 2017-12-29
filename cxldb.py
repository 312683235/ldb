#陈翔六点半优酷视频抓取
from urllib.parse import urlencode
from lxml import etree
import pandas as pd
import requests,json


def get_index():
	url = 'http://i.youku.com/i/UMTA3OTczNTEy/videos?page=1'
	html = requests.get(url)
	if html.status_code == 200:
		return html.text
	return None

def main():
	result = get_index()
	write_csv(result)
	
def write_csv(pro):
	projson = etree.HTML(pro)
	v_title = projson.xpath('//div[@class="v-meta-title"]/a/text()')
	v_num = projson.xpath('//span[@class="v-num"]/text()')
	v_time = projson.xpath('//span[@class="v-time"]/text()')
	v_publishtime = projson.xpath('//span[@class="v-publishtime"]/text()')
	csv_writer = pd.DataFrame({'标题':v_title,'播放量':v_num,'视频时长':v_time,'发布时间':v_publishtime})
	csv_writer.to_csv("data.csv",index=False,sep=',')
	
	
	
if __name__ == '__main__':
	main()