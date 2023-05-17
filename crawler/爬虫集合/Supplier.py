import pymysql
import requests
from bs4 import BeautifulSoup


def get_conn():
    '''建立数据库连接'''
    conn = pymysql.connect(host='10.20.4.51',
                                user='root',
                                password='YY5VV5',
                                db='avatar_test',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)
    return conn


def insert(conn, info):
    '''数据写入数据库'''
    with conn.cursor() as cursor:
        sql = "INSERT INTO `tb_oid` (`oid`, `sup`) VALUES (%s, %s)"
        cursor.execute(sql, info)
    conn.commit()


def main():
    # i = 11850
        conn = get_conn()
    # while i < 48149:
    #     print(i)
        oid = "1.3.6.1.4.1." + str(11791)
        url = "http://oidref.com/"+oid
        print(url)
        html = requests.get(url).text
        soup = BeautifulSoup(html, "html.parser")
        a = soup.find(lambda tag:  "View at oid-info.com" in tag.text in tag).parent
        b = a.get_text('|', strip=True).split('|')[0]

        info = []
        info.append(oid)
        info.append(b)
        insert(conn, info)
        # print(info)

        table = soup.find_all('table')
        if (1 == len(table)):
            table = table[0]

        if(2 == len(table)):
            table = table[1]
        rows = table.find_all('tr')

        for m, row in enumerate(rows):
            columns = row.find_all('td')
            if(5 == len(columns)):
                info = []
                info.append(columns[0].text)
                info.append(columns[4].text)
                insert(conn, info)
                # print(info)

        # i = i + 100

if __name__ == '__main__':
    main()
