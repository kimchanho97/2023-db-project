import psycopg2

# 전역 설정
con = psycopg2.connect(
    database='gdms2023',
    user='db2023',
    password='db!2023',
    host='::1',
    port='5432'
)
cur = con.cursor()


def dbInit():
    # admin 테이블 생성
    cur.execute("""
        CREATE TABLE IF NOT EXISTS admin(
            admin_id INT PRIMARY KEY,
            user_name VARCHAR,
            email VARCHAR,
            password VARCHAR
        );
    """)

    # menu 테이블 생성
    cur.execute("""
        CREATE TABLE IF NOT EXISTS menu(
            menu_id INT PRIMARY KEY,
            restaurant_id INT,
            menu_name VARCHAR,
            price INT
        );
    """)

    # cart 테이블 생성
    cur.execute("""
        CREATE TABLE IF NOT EXISTS cart(
            cart_id INT PRIMARY KEY,
            user_id INT,
            menu_id INT,
            restaurant_id INT,
            quantity INT
        );
    """)

    # 익명 블록
    # PostgreSQL에서는 CREATE TYPE이나 EXCEPTION 구문을 단독으로 사용할 수 없다.
    # 익명 블록 내에서 사용해야 한다.
    cur.execute("""
        DO $$ BEGIN
            CREATE TYPE user_type AS ENUM ('normal', 'vip');
        EXCEPTION
            WHEN duplicate_object THEN null;
        END $$;
    """)
    # user 테이블 생성
    cur.execute("""
        CREATE TABLE IF NOT EXISTS "user"(
            user_id INT PRIMARY KEY,
            user_name VARCHAR,
            email VARCHAR,
            password VARCHAR,
            user_type user_type
        );
    """)

    cur.execute("""
        DO $$ BEGIN
            CREATE TYPE approval_status AS ENUM ('pending', 'accepted');
        EXCEPTION
            WHEN duplicate_object THEN null;
        END $$;
    """)
    # restaurant 테이블 생성
    cur.execute("""
        CREATE TABLE IF NOT EXISTS restaurant(
            restaurant_id INT PRIMARY KEY,
            client_id INT,
            region VARCHAR,
            category VARCHAR,
            approval_status approval_status,
            restaurant_name VARCHAR,
            restaurant_address VARCHAR
        );
    """)

    # client 테이블 생성
    cur.execute("""
        CREATE TABLE IF NOT EXISTS client(
            client_id INT PRIMARY KEY,
            restaurant_id INT,
            user_name VARCHAR,
            email VARCHAR,
            password VARCHAR
        );
    """)

    # order 테이블 생성
    cur.execute("""
        CREATE TABLE IF NOT EXISTS "order"(
            order_id INT PRIMARY KEY,
            user_id INT,
            restaurant_id INT,
            destination_address VARCHAR,
            order_date DATE
        );
    """)

    cur.execute("""
        DO $$ BEGIN
            CREATE TYPE delivery_status AS ENUM ('pending', 'accepted', 'completed');
        EXCEPTION
            WHEN duplicate_object THEN null;
        END $$;
    """)
    # delivery_request 테이블 생성
    cur.execute("""
        CREATE TABLE IF NOT EXISTS delivery_request(
            request_id INT PRIMARY KEY,
            order_id INT,
            delivery_person_id INT,
            request_date DATE,
            delivery_status delivery_status
        );
    """)

    # delivery_person 테이블 생성
    cur.execute("""
        CREATE TABLE IF NOT EXISTS delivery_person(
            delivery_person_id INT PRIMARY KEY,
            user_name VARCHAR,
            region VARCHAR,
            current_delivery_count INT,
            email VARCHAR,
            password VARCHAR
        );
    """)

    # order_detail 테이블 생성
    cur.execute("""
        CREATE TABLE IF NOT EXISTS order_detail(
            order_id INT,
            cart_id INT
        );
    """)

    # # 참조 관계 설정
    cur.execute(
        "ALTER TABLE menu ADD FOREIGN KEY (restaurant_id) REFERENCES restaurant(restaurant_id);")
    cur.execute(
        "ALTER TABLE cart ADD FOREIGN KEY (user_id) REFERENCES \"user\"(user_id);")
    cur.execute(
        "ALTER TABLE cart ADD FOREIGN KEY (restaurant_id) REFERENCES restaurant(restaurant_id);")
    cur.execute(
        "ALTER TABLE cart ADD FOREIGN KEY (menu_id) REFERENCES menu(menu_id);")
    cur.execute(
        "ALTER TABLE restaurant ADD FOREIGN KEY (client_id) REFERENCES client(client_id);")
    cur.execute(
        "ALTER TABLE client ADD FOREIGN KEY (restaurant_id) REFERENCES restaurant(restaurant_id);")
    cur.execute(
        "ALTER TABLE \"order\" ADD FOREIGN KEY (user_id) REFERENCES \"user\"(user_id);")
    cur.execute(
        "ALTER TABLE \"order\" ADD FOREIGN KEY (restaurant_id) REFERENCES restaurant(restaurant_id);")
    cur.execute(
        "ALTER TABLE delivery_request ADD FOREIGN KEY (order_id) REFERENCES \"order\"(order_id);")
    cur.execute(
        "ALTER TABLE delivery_request ADD FOREIGN KEY (delivery_person_id) REFERENCES delivery_person(delivery_person_id);")
    cur.execute(
        "ALTER TABLE order_detail ADD FOREIGN KEY (order_id) REFERENCES \"order\"(order_id);")
    cur.execute(
        "ALTER TABLE order_detail ADD FOREIGN KEY (cart_id) REFERENCES cart(cart_id);")
    con.commit()

    cur.execute("""
        SELECT table_name 
        FROM information_schema.tables 
        WHERE table_schema = 'public';
    """)
    result = cur.fetchall()
    print(f"Tables in the database: {len(result)}")
    result.sort()
    for i in range(len(result)):
        print(f"{i+1}. {result[i][0]}")

    cur.close()
    con.close()


def main():
    dbInit()


if __name__ == '__main__':
    main()
