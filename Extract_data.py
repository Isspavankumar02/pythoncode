import pyodbc
import pandas as pd
#Function to extract data from file to table
def extract_file():
	data = pd.read_csv (r'C:\Users\Desktop\Test\customer.csv')   #read the csv file
	df = pd.DataFrame(data, columns= ['Customer_Name','Customer_Id','Open_Date','Last_Consulted_Date','Vaccination_Id','Dr_Name''State','Country','DOB','Is_Active'])   
	#create a data frame
	# Connect to SQL Server
	conn = pyodbc.connect('Driver={ODBC Driver 13 for SQL Server};'
                      'Server=Servername;'
                      'Database=DBName;'
                      'Trusted_Connection=yes;')
	cursor = conn.cursor()
	# Create Table
	cursor.execute('create table staging_table(
	Name varchar(255) not null,
	Cust_I varchar(18) not null,
	Open_Dt date not null,
	Consul_Dt date,
	VAC_ID char(5),
	DR_Name char(255), 
	State char(5),
	Country char(5),
	DOB date,
	FLAG char
	primary key(Name)'))
	# Insert DataFrame to Table
	for row in df.itertuples():
		cursor.execute('''insert into staging_table (Customer_Name,Customer_Id,Open_Date,Last_Consulted_Date,Vaccination_Id,Dr_Name,State,Country,DOB,FlAG)
		VALUES (?,?,?,?,?,?,?,?,?,?)''',row.Customer_Name,row.Customer_Id,row.Open_Date,row.Last_Consulted_Date,row.Vaccination_Id,row.Dr_Name,row.State,row.Country,row.DOB,row.Is_Active)
	conn.commit()

'''
def findcountry():
	return -1 #tdd to test
'''
def findcountry(): #select distinct countries from the tables;
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 13 for SQL Server};SERVER='Servername';DATABASE='DBName';UID='Username';PWD='Password')

    cursor = conn.cursor()
    sqlSt=""" select distinct country from staging_table"""
	cursor.execute(sqlStmt)
	for row in cursor.fetchall()::
		load_data(row)
		

def load_data(row): #load data to corresponding tables based on the countryname 
	conn = pyodbc.connect(
        'DRIVER={ODBC Driver 13 for SQL Server};SERVER='Servername';DATABASE='DBName';UID='Username';PWD='Password')
    cursor = conn.cursor()
	if row=='india':
		sqlSt="""INSERT INTO table_india SELECT * FROM staging_table WHERE country='ind';"""
	elif row=='USA
		sqlSt="""INSERT INTO table_USA SELECT * FROM staging_table WHERE country='USA';"""
	elif row=='PHIL'
		sqlSt="""INSERT INTO table_PHIL SELECT * FROM staging_table WHERE country='PHIL';"""
	elif row=='NYC'
		sqlSt="""INSERT INTO table_NYC SELECT * FROM staging_table WHERE country='NYC';"""
	elif row=='AU'
		sqlSt="""INSERT INTO table_AU SELECT * FROM staging_table WHERE country='AU';"""
	cursor.execute(sqlStmt)
if __name__ == '__main__':
	extract_file()
	load_data()
