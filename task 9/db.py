import psycopg2
import os


def get_stats():
    conn = psycopg2.connect(
        host="db",
        database=os.environ['POSTGRES_DB'],
        user=os.environ['POSTGRES_USER'],
        password=os.environ['POSTGRES_PASSWORD'])
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS visit_stats (
            id serial PRIMARY KEY,
            visit_time timestamp,
            client_info text
        );
        SELECT visit_time, client_info, cnt.count
        FROM (
            SELECT * FROM public.visit_stats ORDER BY visit_time DESC LIMIT 1
        ) AS subq
        CROSS JOIN (
            SELECT count(*) FROM public.visit_stats
        ) AS cnt
        GROUP BY visit_time, client_info, cnt.count;
    """)
    data = cur.fetchall()
    cur.close()
    conn.close()
    return f'total visits: {data[0][2]}, last one on {data[0][0]} by {data[0][1]}' if data and len(data) > 0 and len(data[0]) > 1 else 'Nothing'


def increment_and_get_stats(client_info: str):
    conn = psycopg2.connect(
        host="db",
        database=os.environ['POSTGRES_DB'],
        user=os.environ['POSTGRES_USER'],
        password=os.environ['POSTGRES_PASSWORD'])
    cur = conn.cursor()


    cur.execute("""
        CREATE TABLE IF NOT EXISTS visit_stats (
            id serial PRIMARY KEY,
            visit_time timestamp,
            client_info text
        );
        INSERT INTO visit_stats (visit_time, client_info) VALUES (now(), %s);
        SELECT visit_time, client_info, cnt.count
        FROM (
            SELECT * FROM public.visit_stats ORDER BY visit_time DESC LIMIT 1
        ) AS subq
        CROSS JOIN (
            SELECT count(*) FROM public.visit_stats
        ) AS cnt
        GROUP BY visit_time, client_info, cnt.count;
    """, (client_info,))
    conn.commit()
    data = cur.fetchall()
    cur.close()
    conn.close()
    return f'visits: {data[0][2]}\n last one on {data[0][0]} by {data[0][1]}'