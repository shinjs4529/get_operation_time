import os
import re
import csv
from datetime import datetime
from collections import defaultdict

def extract_log_data(log_dir, output_csv, summary_csv):
    log_pattern = re.compile(r'^(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}Z) .*? (boot... ok)')
    timestamp_pattern = re.compile(r'^(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}Z)')
    
    log_files = [f for f in os.listdir(log_dir) if f.endswith('.log')]
    result_data = []
    total_time_by_robot = defaultdict(float)
    
    for log_file in log_files:
        robot_id = log_file.split('_')[0]
        log_path = os.path.join(log_dir, log_file)
        
        with open(log_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        boot_times = []
        for idx, line in enumerate(lines):
            if "boot" in line and "ok" in line:
                match = timestamp_pattern.search(line)
                if match:
                    boot_times.append((idx, match.group(1)))
        
        if not boot_times:
            continue
        
        # Find the last valid timestamp in the file
        last_valid_time = None
        for line in reversed(lines):
            match = timestamp_pattern.search(line)
            if match:
                last_valid_time = match.group(1)
                break
        
        for i in range(len(boot_times)):
            boot_index, boot_time = boot_times[i]
            
            if i + 1 < len(boot_times):
                next_boot_index, _ = boot_times[i + 1]
                end_index = max(next_boot_index - 10, 0)
                end_match = timestamp_pattern.search(lines[end_index])
                end_time = end_match.group(1) if end_match else boot_times[i + 1][1]
            else:
                end_time = last_valid_time if last_valid_time else boot_time
            
            start_dt = datetime.strptime(boot_time, "%Y-%m-%dT%H:%M:%S.%fZ")
            end_dt = datetime.strptime(end_time, "%Y-%m-%dT%H:%M:%S.%fZ")
            length = (end_dt - start_dt).total_seconds()
            
            result_data.append([robot_id, boot_time, end_time, length])
            total_time_by_robot[robot_id] += length
    
    # Write the first CSV file
    with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["robotId", "startTime", "endTime", "length"])
        writer.writerows(result_data)
    
    # Write the summary CSV file
    with open(summary_csv, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["robotId", "totalTime"])
        for robot_id, total_time in total_time_by_robot.items():
            writer.writerow([robot_id, f"{total_time:.3f}"])
    
    print(f"CSV file saved: {output_csv}")
    print(f"Summary CSV file saved: {summary_csv}")

# Usage
log_directory = "logs"  # Place log files
output_csv_file = "output.csv"
summary_csv_file = "summary_output.csv"
extract_log_data(log_directory, output_csv_file, summary_csv_file)
