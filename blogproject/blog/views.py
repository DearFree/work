from django.shortcuts import render

# Create your views here.
from django.db import models

from django.shortcuts import render
import MySQLdb
def get_data(sql):#获取数据库的数据
    conn = MySQLdb.connect(host="localhost",user="root",passwd="123456",db="test",charset="utf8")
    cur = conn.cursor()
    cur.execute(sql)
    results = cur.fetchall() # 搜取所有结果
    cur.close()
    conn.close()
    return results
def order(request):# 向页面输出订单
    sql = "SELECT name,url " \
          "FROM tb_douban "
    m_data = get_data(sql)
    return render(request,'order_list.html',{'order':m_data})
