# Socket Performance Monitoring

This repository contains a complete example of a **socket-based client–server application** with an accompanying **performance analysis** toolkit.

##  Features
- **Client–Server Architecture**:
  - Simple TCP socket implementation.
  - Client sends requests, and the server replies with data.
- **Detailed Performance Metrics**:
  - Latency measurement for both Client and Server (in milliseconds).
  - Throughput analysis (requests per minute).
- **Data Visualization**:
  - Client–side and Server–side latency distribution.
  - Throughput trends across timestamps.
- **Easy to Extend**:
  - Supports both plain text and JSON payloads.
  - Provides a foundation for more complex performance monitoring.

## Scripts Included
- `client.py` — Client script for making requests.
- `server.py` — Server script for accepting connections and responding.
- `performance_analysis.py` — Analyzes logged latency and throughput data using **Pandas** and **Matplotlib**.

##  Getting Started
1. Run the `server.py` script on your server.
2. Run the `client.py` script to send requests.
3. Collect performance data (latency and timestamps).
4. Save the data to `client_performance.csv` and `server_performance.csv`.
5. Run `performance_analysis.py` to analyze and visualize results.

##  Contributing
Contributions, improvements, and new ideas are welcome! Open an issue or create a pull request.

