import psycopg2,psycopg2.extras
from dotenv import load_dotenv
import os

load_dotenv()

DB_URL="postgresql://midd_owner:npg_lAmbJFE9GTh1@ep-rough-bread-a1hcwdyh-pooler.ap-southeast-1.aws.neon.tech/midd?sslmode=require"

def db_connection():
    try:
        conn=psycopg2.connect(DB_URL)
        cur=conn.cursor()
        return conn,cur
    except Exception as e:
        print(f"Error: {e}")
        return None,None
