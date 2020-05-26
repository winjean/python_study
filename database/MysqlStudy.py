import pymysql


class MysqlUtils():

    def __init__(self, host, user, pwd, db, port=3306, charset='utf8'):
        self.host = host
        self.user = user
        self.password = pwd
        self.port = port
        self.dbname = db
        self.charset = charset
        self.conn = None  # 连接
        self.cur = None  # 游标

    def open(self):
        # 创建连接
        self.conn = pymysql.connect(host=self.host,
                                    user=self.user,
                                    password=self.password,
                                    port=self.port,
                                    db=self.dbname,
                                    charset=self.charset)
        # 创建游标
        self.cur = self.conn.cursor()

    def select(self, sql):
        # 查询数据
        self.cur.execute(sql)
        # 获取结果
        return self.cur.fetchall()

    def execute(self, sql):
        # 执行sql
        try:
            # 执行SQL语句
            self.cur.execute(sql)
            # 提交事务到数据库执行
            self.conn.commit()  # 事务是访问和更新数据库的一个程序执行单元

        except BaseException as f:
            print(f)
            self.conn.rollback()

        # 返回受影响行数
        return self.cur.rowcount

    def execute_many(self, sql, params):
        '''
        批量插入数据
        :param sql:    插入数据模版, 需要指定列和可替换字符串个数
        :param params:  插入所需数据，列表嵌套元组[(1, '张三', '男'),(2, '李四', '女'),]
        :return:    影响行数
        '''
        try:
            self.cur.executemany(sql, params)
            self.conn.commit()
        except BaseException as f:
            print(f)
            self.conn.rollback()

        return self.cur.rowcount

    def __enter__(self):
        # 当with语句在开始运行时，会在上下文管理器对象上调用 __enter__ 方法
        self.open()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # with语句运行结束后，会在上下文管理器对象上调用 __exit__ 方法
        # 退出时关闭游标关闭连接
        self.cur.close()
        self.conn.close()


def main():
    mysql = MysqlUtils("localhost", "root", "root", "winjean")
    with mysql as mysql:

        table_name = "test_table"
        try:
            sql = f"""
                CREATE TABLE {table_name} (
                    `a` int(11) NOT NULL AUTO_INCREMENT,
                    `b` varchar(255) DEFAULT NULL,
                    PRIMARY KEY (`a`)
                ) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;
            """
            mysql.execute(sql)

            print("创建表成功")
        except Exception as e:
            print(f"Error: 创建表异常: {e}")

        try:
            sql = f"""
                insert into {table_name}(a, b) values(6, 'winjean');
            """
            results = mysql.execute(sql)

            print(f"插入数据成功,共插入{results}条记录")
        except Exception as e:
            print(f"Error: 插入数据异常: {e}")

        try:
            sql = f"""
                insert into {table_name}(a, b) values(%s, %s);
            """
            params = [('7', '7'), ('8', '8'), ('9', '9')]

            results = mysql.execute_many(sql, params)

            print(f"批量插入数据成功,共插入{results}条记录")
        except Exception as e:
            print(f"Error: 插入数据异常: {e}")

        try:
            sql = f"""
                update {table_name} set b= %s;
            """
            params = ['19']

            results = mysql.execute_many(sql, params)

            print(f"批量更新数据成功,共修改{results}条记录")
        except Exception as e:
            print(f"Error: 插入数据异常: {e}")

        try:
            sql = f"select * from {table_name}"
            results = mysql.select(sql)
            for row in results:
                # 输出结果
                print(f"first_name={row[0]}, last_name={row[1]}")
        except Exception as e:
            print(f"Error: unable to fetch data. Error info: {e}")

        try:
            sql = f"""
                DELETE FROM {table_name}
            """
            results = mysql.execute(sql)

            print(f"删除表记录成功,共删除{results}条记录")
        except Exception as e:
            print(f"Error: 删除表记录异常: {e}")

        try:
            sql = f"""
                DROP TABLE {table_name}
            """
            mysql.execute(sql)

            print(f"删除表成功")
        except Exception as e:
            print(f"Error: 删除表异常: {e}")


if __name__ == "__main__":
    main()
