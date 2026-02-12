from connection import get_connection

def test():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT version();")
    version = cursor.fetchone()

    print("Versão do PostgreSQL:")
    print(version)

    cursor.close()
    conn.close()


if __name__ == "__main__":
    test()
