#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import locale

#テーブルデータと差があるかどうかは他関数で判定
#savename,md5はリスト filesはsha256付き二重配列[[filename,md5]]
def insert(pixivid,userid,date=None,title=None,caption=None,bookmarkcount=None,viewcount=None,point=None,pointclick=None,files=[],tags=[],isdelete=False):
	revision = 1;
	database = sqlite3.connect('./illust.sqlite3')

	#最終的にDBに書き込むデータは頭にw付ける
	getdate=None;
	#データチェック
	
	locale.setlocale(locale.LC_ALL, 'ja')
	d = datetime.datetime.today()
	getdate = d.strftime("%Y-%m-%d %H:%M:%S")

	databese.execute("select * from index where pixivid = %s "%str(pixivid)
						+"inner join illustdata on index.pixivid=illustdata.pixivid and index.revision=illustdata.revision")
	indexrow = database.fetchone();
	if rev_row["revision"]!=None :
		#UPDATE

		#まえのデータから引き継ぎ
		if not title:
			title=indexrow["title"]
		if not date:
			date=indexrow["date"]
		if not caption:
			caption=indexrow["caption"]
		if not bookmark:
			bookmarkcount=indexrow["bookmarkcount"]
		if not viewcount:
			viewcount=indexrow["viewcount"]
		if not point:
			point=indexrow["point"]
		if not pointclick:
			pointclick=indexrow["pointclick"]
		if userid != indexrow["userid"]:
			print "ERROR userid disagree"
			database.close()
			return;

		revision=rev_row["revision"]+1
		databese.execute("update index set revision=?,getdate=?,isdelete=?",revision,getdate,isdelete)


	else:
		#INSERT
		databese.execute("insert into index values(?,?,?,?)",(pixivid,revision,userid,getdate,0));
		databese.execute("insert into illustdata values(?,?,?,?,?,?,?,?,?)",\
		(pixivid,revision,date,title,caption,bookmarkcount,viewcount,point,pointclick));

		count = 1;
		for f in files:
			databese.execute("insert into illust values(?,?,?,?,?)",(pixivid,revision,f[0],count,f[1]))
			count++
		for t in tags:
			databese.execute("select * from tag where tagname=? ",t);
			indexrow = database.fetchone()
			if indexrow!=None:
				databese.execute("insert into tag(tagname) values(?)",(t,))
				indexrow = databese.execute("select * from tag where tagname "%str(t));
			tagid = indexrow["tagid"]
			databese.execute("insert into tagmap values(?,?)",(pixivid,tagid))

	database.commit()
	database.close()

#作業分割のための関数　汎用的ではない
def insert_sub():




