import csv
import datetime
import pandas as pd
from influxdb import InfluxDBClient


def csv_data_load_pandas(file_path):
    # 판다스로 읽기
    df = pd.read_csv('data/20220612_DED.csv')

    # df['Time'] = pd.to_datetime(df['Time'], format='%d%b%Y:%H:%M:%S.%f')

    print(df)




def csv_data_load(file_path):
    # 그냥 파일로 읽기
    f = open('data/20220612_DED.csv', 'r')
    csvreader = csv.reader(f)

    columns = next(csvreader)
    fist_value = next(csvreader)


    host = 'keties.iptime.org'
    port = 55586
    client = InfluxDBClient(host=host, port=port)
    dbname = 'HBNU_DED'
    measurement = '20220612_1454'

    print("Create database: " + dbname)
    client.drop_database(dbname)
    client.create_database(dbname)

    # create data
    data = []
    for row in csvreader:
        time_str = '2022-06-' + row[0]
        format_ = '%Y-%m-%d_%H:%M:%S.%f'
        timestamp = datetime.datetime.strptime(time_str, format_)

        X = float(row[1])
        Y = float(row[2])
        Z = float(row[3])
        Height = float(row[4])
        Temper = float(row[5])
        LaserPower = float(row[6])
        PowderGas = float(row[7])
        CoaxialGas = float(row[8])
        ShieldGas = float(row[9])
        Feeder1 = int(row[10])
        Feeder2 = int(row[11])
        Feeder3 = int(row[12])

        point = [
            {
                'measurement': measurement,
                'tags': {
                    'Layer_Z': Z,
                },
                'fields': {
                    'X': X,
                    'Y': Y,
                    'Height': Height,
                    'Temper': Temper,
                    'LaserPower': LaserPower,
                    'PowderGas': PowderGas,
                    'CoaxialGas': CoaxialGas,
                    'ShieldGas': ShieldGas,
                    'Feeder1': Feeder1,
                    'Feeder2': Feeder2,
                    'Feeder3': Feeder3
                },
                'time': timestamp
            }
        ]
        print("Write points: {0}".format(point))
        client.write_points(point, database=dbname)