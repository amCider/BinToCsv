#format_***の詳細は→https://docs.python.org/ja/3/library/struct.html
import struct
import array
import csv

format_128B = "<BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB"
offset_128B = 128
format_64B  = "<BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB"
offset_64B  = 64
format_32B  = "<BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB"
offset_32B  = 32
format_24B  = "<BBBBBBBBBBBBBBBBBBBBBBBB"
offset_24B  = 24
format_B    = "<B"
offset_B    = 1

# U16対応
Awidth  = 176   #横
Aheight = 120   #縦
Bwidth  = 120   #横
Bheight = 80    #縦

str_fname   = "C:/work/python/binToCsv/" #必ず最後に/をつけてください.
str_outname = "imgB.csv"
str_inname  = "imgB.bin"

def file_convert(out_filename, in_filename, str_folder):    # 共通処理とif分岐まとめ
    with open(out_filename, mode='w', newline="") as outf:  # 出力ファイルのオープン試行
        with open(str_folder + in_filename, "rb") as inf:   # 入力ファイルのオープン試行
            print(in_filename + " to " + out_filename)
            out_raw_data = inf.read()
            writer = csv.writer(outf)
            map_xxbit_convert(1, offset_24B, out_raw_data, writer, format_24B, offset_24B)

# xxビット(幅)*[range_2]行のMapデータを[range_1]回分出力する(RGBの各面が同じBINに格納されている場合とか3回
# range_1:BINファイル何面分が1ファイルにあるか、基本は1
# range_2:行数または高さ
# read_data:読み込んだデータ
# write_file:書き込み先
# format_xxb:1行分データを切り出すフォーマット
# offset_xxb:1行分データのサイズ
def map_xxbit_convert(range_1, range_2, read_data, write_file, format_xxb, offset_xxb):
    for num1 in range (range_1):
        write_file.writerow("") # 面が多い場合に備え1行開ける処理
        for num2 in range (range_2):
            in_data1 = struct.unpack_from( format_xxb, read_data, offset_xxb * (num2 +( num1 * range_2)))   # 
            write_file.writerows ([in_data1]) # 1行書き出し

if __name__ == "__main__":
    file_convert(str_outname, str_inname, str_fname)


