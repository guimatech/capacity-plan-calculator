# 86400 exactly, but to round 10^5
seconts_per_day = 1e5

days_of_the_year = 365


def kb_to_mb(x):
    return x / 1e3


def mb_to_gb(x):
    return x / 1e3


def gb_to_tb(x):
    return x / 1e3


def mb_to_tb(x):
    return x / 1e6


daily_active_users = int(input("DAU (Daily Active Users): "))
request_per_user = int(input("Requests per user: "))
size_for_request = int(input("Size for request (kb): "))
reads, writes = [int(x) for x in input("Reads vs Writes (e.g.: 9:1): ").split(":")]
replication_factor = int(input("Replication factor: "))

print("\nCapacity plan")

print("\nRequests:")
request_per_day = daily_active_users * request_per_user
request_per_second = request_per_day / seconts_per_day
print(f'{daily_active_users} * {request_per_user} = {request_per_day} requests per day')
print(f'{daily_active_users} * {request_per_user} = {request_per_second}rps')

print("\nWrites:")
writes_per_second = (request_per_second / (reads + writes)) * writes 
print(f'{request_per_second}rps / {reads + writes} * {writes} = {writes_per_second}rps')

print("\nReads:")
reads_per_second = (request_per_second / (reads + writes)) * reads 
print(f'{request_per_second}rps / {reads + writes} * {reads} = {reads_per_second}rps')

print("\nBandwidth:")
bandwidth_kb = request_per_second * size_for_request
bandwidth_mb = kb_to_mb(bandwidth_kb)
print(f'{request_per_second}rps * {size_for_request}kb = {bandwidth_kb}kb/s')
print("or")
print(f'{bandwidth_mb}mb/s')

print("\nStorage:")

storage_per_second_mb = kb_to_mb(writes_per_second * size_for_request * replication_factor)
print(f'Storage for second: {storage_per_second_mb}mb')

storage_per_day = mb_to_gb(storage_per_second_mb * seconts_per_day)
storage_per_year = gb_to_tb(storage_per_day * days_of_the_year)
storage_in_5_years = storage_per_year * 5
print(f'Storage for day: {storage_per_day}gb')
print(f'Storage for year: {storage_per_year}tb')
print(f'Storage in 5 years: {storage_in_5_years}tb')


print("\nThank you for use the capacity-plan-calculator.py")
