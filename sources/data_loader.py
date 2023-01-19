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

    # This line skips the first row of the CSV file.
    next(csvreader)

    # create data
    data = []
    for row in csvreader:
        time_str = '2022-06-' + row[0]

        timestamp = datetime.datetime.strptime(time_str, '%Y-%m-%d_%H:%M:%S.%f' )

        point = {
                'measurement': influx_helper.measurement,
                'tags': {
                    'Layer_Z': float(row[3]),
                },
                'fields': {
                    'X': float(row[1]),
                    'Y': float(row[2]),
                    'Height': float(row[4]),
                    'Temper': float(row[5]),
                    'LaserPower': float(row[6]),
                    'PowderGas': float(row[7]),
                    'CoaxialGas': float(row[8]),
                    'ShieldGas': float(row[9]),
                    'Feeder1': int(row[10]),
                    'Feeder2': int(row[11]),
                    'Feeder3': int(row[12])
                },
                'time': timestamp
            }

        data.append(point)
        # print("Write points: {0}".format(point))
    print(data)
    return data