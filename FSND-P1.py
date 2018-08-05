import psycopg2
from datetime import datetime

DBNAME = "news"

def topThreeArticles():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select path, count(*) as views from log group by path order by views DESC limit 3 offset 1;")
    newTable = c.fetchall()
    print("MOST POPULAR 3 ARTICLES OF ALL TIME")
    for item in newTable:
        fixedTitle = item[0][9:].replace("-", " ").title()
        print(". {} - {} views".format(fixedTitle, item[1]))
    db.close()

topThreeArticles()

def bestAuthors():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select name, count(*) as views from (authors join articles on authors.id = articles.author) join log on articles.slug = substring(log.path, 10) group by name order by views DESC;")
    authors = c.fetchall()
    print("\nTOP AUTHORS OF ALL TIME")
    for item in authors:
        print(". {} - {} views".format(item[0], item[1]))
    db.close()

bestAuthors()

def findErrorDates():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select dates, percentage from (select finderror.dates, round(1.00*errors/clicks, 3) as percentage from (select substring(cast(time as varchar),1,10) as dates, count(*) as errors from log where status = '404 NOT FOUND' group by dates order by errors DESC) as finderror join (select substring(cast(time as varchar),1,10) as dates, count(*) as clicks from log group by dates order by clicks DESC) as findtotal on finderror.dates = findtotal.dates order by errors desc limit 3) as sortedtable where percentage > .01;")
    days = c.fetchall()
    print("\nDAYS WITH OVER 1" + "%" + " ERRORS")
    for item in days:
        date = item[0]
        print(". {} - {}".format(date, item[1] * 100) + "%" + " error rate")

findErrorDates()
