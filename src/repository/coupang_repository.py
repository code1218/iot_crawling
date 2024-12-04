import pymysql

def saveCoupangData(coupangData: list):
    try:
        connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='coupang_db')
        try:
            cursor = connection.cursor()
            for data in coupangData:
                sql = "insert into category_tb values(default, %s)"
                cursor.execute(sql, data["category"])
                category_id = cursor.lastrowid

                values = ",\n".join(list(map(lambda product: f"(default, \'{product['productName']}\', {product['price'].replace(',', '')}, \'{product['productImgUrl']}\', {category_id})", data['products'])))
                sql = "insert into product_tb values" + values
                cursor.execute(sql)
            connection.commit()
        except Exception as e:
            print(e) #SQL 오류
        finally:
            connection.close()

    except Exception as e:
        print("데이터베이스 연결 실패")