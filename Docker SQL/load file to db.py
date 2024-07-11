'''
Configure connection to db
Read files from folder
Load files into new table in db using filename as table name
'''

import pandas as pd
import sqlalchemy
import psycopg2
import glob

##define connection variables
db = 'test_db'
dbhost = 'localhost'
dbport = '5432'
dbuser = 'admin'
dbpass = 'admin'
options=""

##define folder with source csv files
folder = "<Define folder name here, code will load all csvs contaned in that folder into the local SQL db>"
csv_files = [file.split('/')[-1].split('.')[0] for file in glob.glob(folder + "/*.csv")]

##loop through each filename and create a 
for name in csv_files:
    tbl = name
    ###import source file to df
    data = pd.read_csv(f"<file path>{tbl}.csv")
    df = pd.DataFrame(data)
    ###create ddl for source file
    ddl = pd.io.sql.get_schema(df, tbl)

    ##create connection
    con = psycopg2.connect(dbname= db, host= dbhost, port= dbport, user= dbuser, password= dbpass,options=options)

    #create table in database
    cur = con.cursor()
    cur.execute(ddl)
    con.commit()

    #load data into database
    query_string = (f'COPY {tbl} FROM stdin WITH (FORMAT CSV, HEADER TRUE, DELIMITER \',\')')
    with open(f"/Users/michaelmallen/Documents/Data/Contoso/{tbl}.csv", 'r') as f:
        cur.copy_expert(query_string, f)
    con.commit()
