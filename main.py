from datetime import datetime
import calendar
import time

def csv_data_encoder(filename):
    with open(filename, 'r', encoding='utf8', newline='') as rf:
        lines = rf.read().split("\n")
        data = [line.split("\t") for line in lines]
    return data

def decrypt_csv_timestamp(dataEncoded):
    for i in range(len(dataEncoded)-1):
        ts = int(dataEncoded[i][0])
        time_converted = datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        dataEncoded[i][0] = time_converted
    return dataEncoded

def csv_time_range(data):
    ranges = []
    ranges.append(data[0][0])
    ranges.append(data[-2][0])
    return ranges

def main():
    csv_data = csv_data_encoder("primaryschool.csv")
    csv_data_time_converted = decrypt_csv_timestamp(csv_data)
    csv_max_min_time_range = csv_time_range(csv_data_time_converted)

main()

