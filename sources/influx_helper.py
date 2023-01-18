from influxdb import InfluxDBClient, DataFrameClient

class info:
    host = 'keties.iptime.org'
    port = 55586
    user = 'honeyb'
    passwd = '12345'
    dbname = 'HBNU_DED'
    protocol = 'line'
    measurement = '20220612_1454_3'
    client_pandas = DataFrameClient(host,port, user, passwd, dbname)
    client = InfluxDBClient(host=host, port=port)
def create_db_pandas():
    # check database list
    list_db = info.client_pandas.get_list_database()
    ret = next((item for item in list_db if item['name'] == info.dbname), None)
    if ret is None:
        info.client_pandas.create_database(info.dbname)

def create_db():
    # check database list
    list_db = info.client.get_list_database()
    ret = next((item for item in list_db if item['name'] == info.dbname), None)
    if ret is None:
        info.client.create_database(info.dbname)

def data_insert_pandas(data):
    # Write data to measurement of 'HBNU_DED' database.
    info.client_pandas.write_points(data, info.measurement, tag_columns=['Z'], protocol=info.protocol)

def data_insert(point):
    # Write data to measurement of 'HBNU_DED' database.
    info.client.write_points(point, database=info.dbname)