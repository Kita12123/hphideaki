"""Connect Database"""

import psycopg2
DSN = "postgres://pstpacxxjqbbjd:0601cbccc17a7d5c9ad8a6b64b8da716997c62db65a80f952b0933dd63ede6ab@ec2-44-194-117-205.compute-1.amazonaws.com:5432/d3mj922dqsq6qd"

CONN = psycopg2.connect(DSN)
CUR = CONN.cursor()
def open():
    return CONN.cursor()
def close():
    CONN.close()
    CUR.close()
def commit():
    CONN.commit()

close()
