import os

import pymysql
import yaml


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
        sql = "INSERT INTO `tb_os_type` (`os`, `text`, `type`) VALUES (%s, %s, %s)"
        cursor.execute(sql, info)
    conn.commit()


def main():
    conn = get_conn()
    file_path = "D:\definitions"

    for file in os.listdir(file_path):
        with open(os.path.join(file_path, file), "r", encoding="UTF-8") as f:
            yamlConf = yaml.load(f.read(), Loader=yaml.FullLoader)
            info = []
            info.append(yamlConf.get("os"))
            info.append(yamlConf.get("text"))
            info.append(yamlConf.get("type"))
            insert(conn, info)


if __name__ == '__main__':
    main()
