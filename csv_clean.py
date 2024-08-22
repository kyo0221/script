import csv

def round_csv_values(file_path, output_file):
    rounded_data = []

    # CSVファイルを読み込む
    with open(file_path, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        
        # 各行を読み込み
        for row in csvreader:
            rounded_row = []
            for value in row:
                try:
                    # 各値を小数点第6位で四捨五入
                    rounded_value = round(float(value), 6)
                    rounded_row.append(rounded_value)
                except ValueError:
                    # 数値以外のデータがあればそのまま追加
                    rounded_row.append(value)
            rounded_data.append(rounded_row)

    # 結果を新しいCSVファイルに書き込む
    with open(output_file, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(rounded_data)

    print(f"Rounded data has been saved to {output_file}")

# 入力ファイルと出力ファイルのパスを指定
input_file = '/home/kyo/formula_ws/src/main_executor/config/course_data/gazebo_shihou_cource.csv'
output_file = '/home/kyo/formula_ws/src/main_executor/config/cource_data/output.csv'

round_csv_values(input_file, output_file)

