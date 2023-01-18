import csv
import datetime
import pandas as pd
from sources import influx_helper

def csv_data_load_pandas(file_path):
    # 판다스로 파일 읽기
    df = pd.read_csv('data/20220612_DED.csv', sep=',')
    df['Time'] = '2022-06-' + df['Time']
    df['Time'] = pd.to_datetime(df['Time'], format='%Y-%m-%d_%H:%M:%S.%f')

    # 'Time'을 데이터프레임 인덱스로 지정
    df.set_index('Time', inplace=True)

    return df


def csv_data_load(file_path):
    # 그냥 파일로 읽기
    f = open('data/20220612_DED.csv', 'r')
    csvreader = csv.reader(f)

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
                'measurement': influx_helper.info.measurement,
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

        print(point)
        print("Write points: {0}".format(point))

        influx_helper.data_insert(point)
