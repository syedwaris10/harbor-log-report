Parse /app/access.log and write a JSON report to /app/report.json.

The report must contain these fields:

1. total_requests — integer, total number of log lines
2. unique_ips — integer, count of distinct client IP addresses
3. top_path — string, the most frequently requested URL path
