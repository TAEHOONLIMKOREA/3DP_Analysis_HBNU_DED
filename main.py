from sources import data_loader
from sources import influx_helper

if __name__ == '__main__':
    dir_path = 'data/20220612_DED.csv'
    # data_loader.csv_data_load(dir_path)
    data = data_loader.csv_data_load_pandas(dir_path)

    influx_helper.create_db_pandas()

    influx_helper.data_insert_pandas(data)

