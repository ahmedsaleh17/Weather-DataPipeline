# read sample weather data 
import json     
import psycopg2 



def connect_to_db():

    print("connecting to the PostgreSQL database...")
    try: 
        conn = psycopg2.connect(
            host='localhost', 
            port=5000,
            dbname='WeatherDB', 
            user='db_user', 
            password='db_password'
        )
        

        # retrun connection 
        return conn 
    
    except psycopg2.Error as e: 
        print(f"Database connection faild: {e}")

    






