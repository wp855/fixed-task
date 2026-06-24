There is an Apache-style access log in the working directory at `/app/access.log`.

Analyze the traffic and summarize what you find in a JSON report. The report should contain the total number of requests, the number of unique client IP addresses, and the most frequently accessed path. Save your findings so they can be reviewed.

### Success Criteria
1. A file named `report.json` must be created in the `/app` directory.
2. The JSON file must be properly formatted and contain exactly three keys:
   - `"total_requests"`: an integer representing the total number of entries in the log.
   - `"unique_ips"`: an integer representing the count of unique client IP addresses.
   - `"top_path"`: a string representing the most requested path.
3. The values must exactly reflect the data derived from the provided log file.