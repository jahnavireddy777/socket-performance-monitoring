import pandas as pd
import matplotlib.pyplot as plt
# 1. Read Client and Server performance data
client_data = pd.read_csv("client_performance.csv", parse_dates=["timestamp"])
server_data = pd.read_csv("server_performance.csv", parse_dates=["timestamp"])


# 2. Convert latency from seconds to milliseconds

client_data["latency_ms"] = client_data["latency_sec"] * 1000
server_data["latency_ms"] = server_data["latency_sec"] * 1000


# 3. Client Side Latency per End-Point

client_latency_per_endpoint = client_data.groupby("endpoint")["latency_ms"].mean()
print("\nClient Side - Average Latency per Endpoint (ms):\n", client_latency_per_endpoint)


# 4. Client Side Latency Distribution

plt.figure(figsize=(10, 6))
client_data["latency_ms"].plot(kind="hist", bins=30, title="Client Side Latency Distribution")
plt.xlabel("Latency (ms)")
plt.show()


# 5. Server Side Latency per End-Point

server_latency_per_endpoint = server_data.groupby("endpoint")["latency_ms"].mean()
print("\nServer Side - Average Latency per Endpoint (ms):\n", server_latency_per_endpoint)


# 6. Server Side Latency Distribution

plt.figure(figsize=(10, 6))
server_data["latency_ms"].plot(kind="hist", bins=30, title="Server Side Latency Distribution")
plt.xlabel("Latency (ms)")
plt.show()


# 7. Throughput Analysis (Client Side)

client_data["count"] = 1
client_data.set_index("timestamp", inplace=True)
client_throughput = client_data.resample("1T")["count"].sum()
print("\nClient Side Throughput (requests per minute):\n", client_throughput)

plt.figure(figsize=(10, 6))
client_throughput.plot(title="Client Side Throughput (requests/minute)", marker='o')
plt.xlabel("Time")
plt.ylabel("Requests per Minute")
plt.show()


# 8. Throughput Analysis (Server Side)
server_data["count"] = 1
server_data.set_index("timestamp", inplace=True)
server_throughput = server_data.resample("1T")["count"].sum()
print("\nServer Side Throughput (requests per minute):\n", server_throughput)

plt.figure(figsize=(10, 6))
server_throughput.plot(title="Server Side Throughput (requests/minute)", marker='o', color='red')
plt.xlabel("Time")
plt.ylabel("Requests per Minute")
plt.show()
