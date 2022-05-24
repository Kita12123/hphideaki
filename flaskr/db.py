"""Connect Database"""

import psycopg2
DSN = "postgres://pstpacxxjqbbjd:0601cbccc17a7d5c9ad8a6b64b8da716997c62db65a80f952b0933dd63ede6ab@ec2-44-194-117-205.compute-1.amazonaws.com:5432/d3mj922dqsq6qd"

def select(sql:str):
    with psycopg2.connect(DSN) as conn:
        with conn.cursor() as cur:
            return cur.execute(sql).fetchall()

def insert(sql:str,param:list):
    with psycopg2.connect(DSN) as conn:
        conn.autocommit = True
        with conn.cursor() as cur:
            cur.execute(sql, param)

def delete(sql:str):
    with psycopg2.connect(DSN) as conn:
        conn.autocommit = True
        with conn.cursor() as cur:
            cur.execute(sql)
