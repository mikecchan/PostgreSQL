#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import psycopg2

DBNAME = "news"


def query(q, end_str):
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(q)
    results = c.fetchall()
    n = 0
    for row in results:
        print str(results[n][0]) + ' - ' + str(results[n][1]) + end_str
        n = n + 1
    db.close()
    print "\n"


def most_pop_art():
    q = "select articles.title, views " \
        "from articles " \
        "join (select path, count(*) as views " \
        "from log " \
        "where status = '200 OK' " \
        "group by path) as log " \
        "on log.path = CONCAT('/article/', articles.slug) " \
        "order by views desc " \
        "limit 3; "

    print "What are the most popular three articles of all time?  Which " \
          "articles have been accessed the most?" + "\n"

    query(q, ' views')


def most_pop_auth():
    q = "Select Name, sum_views from " \
        "(Select author, cast(sum(views) as integer) as sum_views from " \
        "(select path, cast(count(id) as integer) as views " \
        "from log where status = '200 OK' group by path) as Table_log " \
        "right join Articles on Table_log.path like '%' || Articles.slug || " \
        "'%' group by author) as Article_Joined_with_Table_log " \
        "right join Authors on Authors.Id = " \
        "Article_Joined_with_Table_log.author "

    print "Who are the most popular article authors of all time?" + "\n"

    query(q, ' views')


def request_errors():
    q = "select to_char(new_timestamp, 'FMMonth DD, YYYY'), per_error from " \
        "(select cast(time as date) as new_timestamp, " \
        "round(100 * cast(sum(case when status = '404 NOT FOUND' " \
        "then 1 else 0 end) as numeric) /  " \
        "cast(count(*) as numeric),1) as per_error  " \
        "from log " \
        "group by new_timestamp " \
        ") as table2 " \
        "where per_error > 1"

    print "On which days (time) did more than 1% of requests " \
          "lead to errors?" + "\n"

    query(q, '% errors')

if __name__ == '__main__':
    most_pop_art()
    most_pop_auth()
    request_errors()
