import pyodbc
from azure.identity import DefaultAzureCredential
import struct

# Define constant manually (if missing)
SQL_COPT_SS_ACCESS_TOKEN = 1256  # This is the correct integer value

# Get access token
credential = DefaultAzureCredential()
access_token = credential.get_token("https://database.windows.net/").token

# Convert token to bytes format
access_token_bytes = bytes(access_token, "utf-8")
access_token_struct = struct.pack("=i", len(access_token_bytes)) + access_token_bytes

# Connection string with access token
conn_str = (
    "DRIVER={ODBC Driver 18 for SQL Server};"
    "SERVER=tcp:slaauc-sql-server1.database.windows.net,1433;"
    "DATABASE=SLA_Auction_DB;"
    "Encrypt=yes;"
    "TrustServerCertificate=no;"
    "Authentication=ActiveDirectoryAccessToken"
)

# Establish connection
try:
    conn = pyodbc.connect(conn_str, attrs_before={pyodbc.SQL_COPT_SS_ACCESS_TOKEN: access_token_struct})
    print("✅ Connected successfully!")
except Exception as e:
    print(f"❌ Connection failed: {e}")
