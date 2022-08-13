import pandas as pd
import numpy as np 
import os
student_df = pd.DataFrame(pd.read_csv("/mnt/sda1/patika_python/student_database/data_1.csv"))
student_df.index+=1


def search_student():
    os.system("clear")
    s_name = input("Enter First Name: ")
    s_lastname = input("Enter Last Name:")
    mask = (student_df['first_name'] == s_name) & (student_df['last_name'] == s_lastname)
    print(student_df[mask])
#main
c = 0
while c!=7:
    print(
        "\nChoose an option:"
        "\n1. Search a student."
        "\n2. Delete student."
        "\n3. Add Studnet."
        "\n4. Updtae student."
        "\n5. Sort students by..."
        "\n6. Studnet statistics"
        "\n7. Exit")
    c = int(input())
    if c == 1:
        search_student()