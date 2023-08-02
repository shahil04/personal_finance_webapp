# import pandas  as pd 
# data = pd.read_excel("Finance Database.xlsx")
# data.head()
# # step 2
# data = data.set_axis(list(data.iloc[0]), axis=1)
# data = data[1:]
# data.head()

# #step 3
# # piviot the table using melt 
# melted_df = pd.melt(data, id_vars=['Type', 'Component'], var_name='Date', value_name='Value')
# melted_df["Date"] = pd.to_datetime(melted_df["Date"],format='%b-%y')
# print(melted_df)


# ## single row and single value collect
# for i in range(0,len(melted_df)):
#   single =melted_df.iloc[i]
#   type_choose = single[0]
#   component = single[1]
#   date = single[2]
#   amount = single[3]
#   print(single[0],single[1],single[2],single[3])
  
# # type_choose
# # component  
# # amount     
# # date       

# dlist =[]
# for i in range(0,2):
#   single =melted_df.iloc[i]
#   type_choose = single[0]
#   component = single[1]
#   date = single[2]
#   amount = single[3]
#   dlist.append((type_choose,component, amount, date))
#   # dlist.append((single[0],single[1],single[2],single[3]))
#   print(dlist[0][1])
  

# import mysql.connector
# host="localhost"
# user = "root"
# password = "Azsxdcf123@"
# database = "duplicate_table"
# # connect to my sql
# conn = mysql.connector.connect(host=host,user=user, password = password,
#                                database =database)
# cursor = conn.cursor()
# data_to_insert =dlist

# #sql query to insert data into table 
# insert_query = "INSERT INTO home_daily_add_model_demo (type_choose,component, amount, date) VALUES (%s,%s,%s,%s)"

# cursor.executemany(insert_query,data_to_insert)

# conn.commit()
# cursor.close()
# conn.close()

import pandas as pd
import mysql.connector

# Assuming you already have a MySQL table named 'your_table_name' with columns (Name, Age, Email)

# Replace these with your MySQL database credentials
host="localhost"
user = "root"
password = "Azsxdcf123@"
database = "personalfinancedb"

# Connect to MySQL
conn = mysql.connector.connect(host=host, user=user, password=password, database=database)
cursor = conn.cursor()

# Read the Excel file into a pandas DataFrame
excel_file = 'Finance.xlsx'
df = pd.read_excel(excel_file)

# Replace 'your_table_name' with the name of your MySQL table
table_name = 'Daily_add_model_demo'

# SQL query to insert data into the table
insert_query = f"INSERT INTO {table_name} (Tpye Choose, Age, Email) VALUES (%s, %s, %s)"

# Iterate over the rows of the DataFrame and insert data into the MySQL table
for index, row in df.iterrows():
    values = (row['Name'], row['Age'], row['Email'])
    print(f"Inserting row {index + 1}: {values}")
    cursor.execute(insert_query, values)

# Commit the changes to the database
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()
