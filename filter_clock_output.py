import json

def filter_clock_output(data):
    latest_results = {}
    for line in data.splitlines():
        parts = line.split(',')
        hostname = parts[0]
        clock_info = parts[1:]
        time_info = next((info for info in clock_info if 'KST' in info), None)
        source_info = next((info for info in clock_info if 'Time Source' in info), None)
        if time_info and source_info:
            latest_results[hostname] = f'{hostname}, {time_info.strip("[]\'")}\', {source_info.strip("[]\'")}\']'

    return '\n'.join(latest_results.values())

if __name__ == "__main__":
    import sys
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    with open(input_file, 'r') as infile:
        data = infile.read()

    filtered_data = filter_clock_output(data)

    with open(output_file, 'w') as outfile:
        outfile.write(filtered_data)