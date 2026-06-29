
connection={"host":"127.0.0.1","port":3306,"user":"root"}
conn_str=f"connecting to {connection['user']}@{connection['host']}:{connection['port']}"
print(conn_str)

for key,value in connection.items():
     print(key,value)