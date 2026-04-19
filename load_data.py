# read sample weather data
import json
import psycopg2


# connect to the data base
def connect_to_postgreDB():
    """
    This function will establish connection to WeatherDB
    """

    print("Connecting to the PostgtreSQL Database ...")
    try:
        # establish connection
        conn = psycopg2.connect(
            host="localhost",
            port=5000,
            dbname="WeatherDB",
            user="db_user",
            password="db_password",
        )

        # return connection object to use it in creating tables and insert data
        return conn

    except psycopg2.Error as e:
        print(f"Database connection failed: {e}")


def Create_table(conn):
    """
    This function will create table
    """
    print("Creating table if not exists...")
    try:

        cursor = conn.cursor()
        # creat table
        cursor.execute("""
            CREATE SCHEMA IF NOT EXISTS dev; 
            
            CREATE TABLE IF NOT EXISTS dev.raw_weather_data(
                id SERIAL PRIMARY KEY, 
                city TEXT, 
                temperature FLOAT, 
                weather_description TEXT, 
                wind_speed FLOAT, 
                time TIMESTAMP, 
                inserted_at TIMESTAMP DEFAULT NOW(),
                utc_offset TEXT   
            );
        """)
        conn.commit()
        print("Table was created")

    except psycopg2.Error as e:
        print(f"Failed to create table {e}")


def load_data(conn, data):
    """
    This function to insert weather records to postgreSQL DB
    Args: 
        conn: Database Connection Object 
        data (tuple): a tuple of weather records  
    """
   
    print("Loading Weather data into database...")

    try:
        # open a cursor to perform database operation
        cursor = conn.cursor()
        # Execute the insert statement
        insert_query = """INSERT INTO dev.raw_weather_data(
                            city,
                            temperature,
                            weather_description, 
                            wind_speed, 
                            time, 
                            inserted_at, 
                            utc_offset) VALUES(%s, %s, %s, %s, %s, NOW(), %s)"""

        # insert data 
        cursor.execute(insert_query, data)
        # save changes 
        conn.commit() 

    except psycopg2.Error as e:
        print(f"Failed to insert data: {e}")


if __name__ == "__main__":

    connection = connect_to_postgreDB()
    Create_table(conn=connection)

    # mock data for testing function
    with open("weather_data_sample.json", encoding="utf-8") as file:

        data = json.load(file)

    records = (
        data["location"]["name"],  # city
        data["current"]["temperature"],  # temperature
        data["current"]["weather_descriptions"][0],  # weathe_description
        data["current"]["wind_speed"],  # wind speed
        data["location"]["localtime"],  # time
        data["location"]["utc_offset"]  # utc_offset
    )

    load_data(connection, records)

