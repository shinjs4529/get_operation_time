import csv
import re

def korean_time_to_seconds(time_str):
    match = re.match(r'(\d+)시간 (\d+)분 (\d+)초', time_str)
    if match:
        hours, minutes, seconds = map(int, match.groups())
        return hours * 3600 + minutes * 60 + seconds
    return None

def convert_txt_to_csv(input_txt, output_csv):
    with open(input_txt, 'r', encoding='utf-8') as infile, open(output_csv, 'w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(["Original Time", "Total Seconds"])
        
        for line in infile:
            line = line.strip()
            total_seconds = korean_time_to_seconds(line)
            if total_seconds is not None:
                writer.writerow([line, total_seconds])

if __name__ == "__main__":
    input_txt = "korean_time.txt"
    output_csv = "parsed_time.csv"
    convert_txt_to_csv(input_txt, output_csv)
    print(f"Conversion completed. Output saved in {output_csv}")
