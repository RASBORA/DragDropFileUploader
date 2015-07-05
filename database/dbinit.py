#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3


database = sqlite3.connect('./illust.sqlite3')

database.execute('''
create table illustindex(
	pixivid integer primary key,
	revision integer,
	user text
	);	''')

database.execute("""
create table illustdata(
	pixivid integer,
	revision integer,
	date text,
	title text,
	caption text,
	bookmarkcount integer,
	viewcount integer,
	point integer,
	pointclick integer,
	primary key(pixivid,revision)
	);	""")

database.execute("""
create table illust(
	pixivid integer,
	revision integer,
	page integer,
	savename text,
	md5,
	primary key(pixivid,revision)
	);	""")

database.execute("""
create table tagmap(
	pixivid integer,
	revision integer,
	tagid integer,
	primary key(pixivid,revision)
	);	""")

database.execute("""
create table tag(
	tagid integer primary key,
	tagname text
	);	""")

database.commit()
database.close()

