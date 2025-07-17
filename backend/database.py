# import mysql.connector

# def get_asl_video(word):
#     conn = mysql.connector.connect(host="localhost", user="root", password="bangtan@4545", database="asl_db")
#     cursor = conn.cursor()
#     cursor.execute("SELECT video_url FROM asl_mapping WHERE word = %s", (word,))
#     result = cursor.fetchone()
#     return result[0] if result else "No ASL Video Found"

# if __name__ == "__main__":
#     print(get_asl_video("hello"))
