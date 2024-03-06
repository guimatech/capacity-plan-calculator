# Capacity Plan Calculator
Calculator from the capacity plan from your solution architecture,

### The inputs are:
 - Daily Active User (DAU): **integer**
 - Requests per User: **integer**
 - Size per Request: **integer**
 - Reads vs Writes: **e.g: 9:1**

### And the outputs are:
 - Requests Per Second (RPS)
 - Bandwidth
 - Storage

Just run `app.py` and enter the requested values:

```shellscript
$  python app.py
DAU (Daily Active Users): 1000000
Requests per user: 5
Size for request (kb): 20
Reads vs Writes (e.g.: 9:1): 9:1
Replication factor: 2

Capacity plan

Requests:
1000000 * 5 = 5000000 requests per day
1000000 * 5 = 50.0rps

Writes:
50.0rps / 10 * 1 = 5.0rps

Reads:
50.0rps / 10 * 9 = 45.0rps

Bandwidth:
50.0rps * 20kb = 1000.0kb/s
or
1.0mb/s

Storage:
Storage for second: 0.2mb
Storage for day: 20.0gb
Storage for year: 7.3tb
Storage in 5 years: 36.5tb

Thank you for use the capacity-plan-calculator.py
```