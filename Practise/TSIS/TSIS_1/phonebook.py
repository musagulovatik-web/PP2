import psycopg2
import json
from connect import connect

def export_json(cursor):
    cursor.execute("""
        SELECT c.name, c.email, c.birthday, g.name as group_name 
        FROM contacts c 
        LEFT JOIN groups g ON c.group_id = g.id
    """)
    data = cursor.fetchall()
    res = []
    for row in data:
        res.append({"name": row[0], "email": row[1], "birthday": str(row[2]), "group": row[3]})
    with open("contacts.json", "w") as f:
        json.dump(res, f)

def import_json(cursor, conn):
    with open("contacts.json", "r") as f:
        data = json.load(f)
    for item in data:
        cursor.execute("SELECT id FROM contacts WHERE name = %s", (item['name'],))
        exists = cursor.fetchone()
        if exists:
            choice = input(f"Duplicate {item['name']}. Overwrite? (y/n): ")
            if choice == 'y':
                cursor.execute("UPDATE contacts SET email=%s, birthday=%s WHERE name=%s", 
                (item['email'], item['birthday'], item['name']))
        else:
            cursor.execute("INSERT INTO contacts (name, email, birthday) VALUES (%s, %s, %s)", 
            (item['name'], item['email'], item['birthday']))
    conn.commit()

def main():
    conn = connect()
    cursor = conn.cursor()
    page = 1
    limit = 5

    while True:
        print("\n1. Search/Filter")
        print("2. List (Paginated)")
        print("3. Next Page")
        print("4. Prev Page")
        print("5. Add phone")
        print("6. Move to group")
        print("7. Export JSON")
        print("8. Import JSON")
        print("9. Exit")

        choice = input("Select: ")

        if choice == '1':
            query = input("Query: ")
            cursor.execute("SELECT * FROM search_contacts(%s)", (query,))
            for row in cursor.fetchall():
                print(row)

        elif choice == '2':
            cursor.execute("SELECT * FROM contacts ORDER BY name LIMIT %s OFFSET %s", 
                           (limit, (page - 1) * limit))
            for row in cursor.fetchall():
                print(row)

        elif choice == '3':
            page += 1
            print(f"Page: {page}")

        elif choice == '4':
            if page > 1:
                page -= 1
            print(f"Page: {page}")

        elif choice == '5':
            name = input("Name: ")
            phone = input("Phone: ")
            p_type = input("Type: ")
            cursor.execute("CALL add_phone(%s, %s, %s)", (name, phone, p_type))
            conn.commit()

        elif choice == '6':
            name = input("Name: ")
            group = input("Group: ")
            cursor.execute("CALL move_to_group(%s, %s)", (name, group))
            conn.commit()

        elif choice == '7':
            export_json(cursor)
            print("Exported")

        elif choice == '8':
            import_json(cursor, conn)
            print("Imported")

        elif choice == '9':
            break

    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()