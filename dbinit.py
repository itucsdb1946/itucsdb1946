import os
import sys

import psycopg2 as dbapi2


INIT_STATEMENTS = [
    """CREATE TABLE IF NOT EXISTS SITEUSER(
                        ID SERIAL PRIMARY KEY,
                        USERNAME VARCHAR(40),
                        PASSWORD VARCHAR(100),
                        USERTYPE VARCHAR(10));
    """,
    """
                    CREATE TABLE IF NOT EXISTS CUSTOMER(
                            ID INTEGER,
                            NAME VARCHAR(50),
                            SURNAME VARCHAR(50),
                            ADDRESS VARCHAR(300),
                            TOTAL_ORDERS INTEGER DEFAULT 0,
                            CONSTRAINT CONSTRAINT1
                            FOREIGN KEY (ID) REFERENCES SITEUSER(ID)
                            ON DELETE CASCADE);
    ""","""               CREATE TABLE IF NOT EXISTS COMPANY(
                        ID INTEGER,
                        NAME VARCHAR(40),
                        AVGDAY INTEGER,
                        YEAR_FOUNDED INTEGER,
                        TOTAL_ORDERS INTEGER DEFAULT 0,
                        CONSTRAINT CONSTRAINT1
                            FOREIGN KEY (ID) REFERENCES SITEUSER(ID)
                            ON DELETE CASCADE);
    ""","""             CREATE TABLE IF NOT EXISTS MYORDER(
                        ORDER_ID SERIAL PRIMARY KEY,
                        CUSTOMER_ID INTEGER,
                        COMPANY_ID INTEGER,
                        ORDER_DATE DATE NOT NULL DEFAULT CURRENT_DATE,
                        ITEM VARCHAR(100),
                        CONSTRAINT CONSTRAINT1
                            FOREIGN KEY (CUSTOMER_ID) REFERENCES SITEUSER(ID)
                            ON DELETE CASCADE,
                        CONSTRAINT CONSTRAINT2
                            FOREIGN KEY (COMPANY_ID) REFERENCES SITEUSER(ID)
                            ON DELETE CASCADE);
                        """
]


def initialize(url):
    with dbapi2.connect(url) as connection:
        print("DENEME1: " ,url)
        cursor = connection.cursor()
        for statement in INIT_STATEMENTS:
            cursor.execute(statement)
        cursor.close()


if __name__ == "__main__":
    url = os.getenv("DATABASE_URL")
    if url is None:
        print("DENEME2: " ,url)
        print("Usage: DATABASE_URL=url python dbinit.py", file=sys.stderr)
        sys.exit(1)
    initialize(url)
