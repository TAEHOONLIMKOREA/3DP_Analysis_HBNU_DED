from sources import data_loader

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    dir_path = 'data/20220612_DED.csv'
    data_loader.csv_data_load(dir_path)
    # data_loader.csv_data_load_pandas(dir_path)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
