count = 0

with open("sample.log") as log_file:
    for number, line in enumerate(log_file, start=1):
        if "error" in line.lower():
            print(number, line.strip())
            count = count + 1

print("Error lines:", count)
