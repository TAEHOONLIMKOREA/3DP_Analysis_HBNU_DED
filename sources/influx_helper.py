from influxdb import InfluxDBClient, DataFrameClient

host = 'keties.iptime.org'
port = 55586
user = 'honeyb'
passwd = '12345'
protocol = 'line'
dbname = 'HBNU_DED'
measurement = '20220612_1454_6'


def data_insert_pandas(data):
    client_pandas = DataFrameClient(host, port, user, passwd, dbname)
    # Write data to measurement of 'HBNU_DED' database.
    client_pandas.write_points(data, measurement, tag_columns=['Z'], protocol=protocol)

def data_insert(data):
    client = InfluxDBClient(host=host, port=port)
    # check database list
    list_db = client.get_list_database()
    ret = next((item for item in list_db if item['name'] == dbname), None)
    if ret is None:
        client.create_database(dbname)
    # Write data to measurement of 'HBNU_DED' database.
    client.write_points(data, database=dbname)