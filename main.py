import db_config
from auth import login
import client
import rider
import user
import admin


def main():
    role, userId = login.join()
    if role == "clients":
        client.inputFunction(userId)
    if role == "riders":
        rider.inputFunction(userId)
    if role == "admin":
        admin.inputFunction(userId)
    if role == "users":
        user.inputFunction(userId)

    db_config.cur.close()
    db_config.con.close()


if __name__ == '__main__':
    main()
