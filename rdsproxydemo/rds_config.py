import secretkey

secret = secretkey.get_secret()
print("Secret key Details :: {}", secret)

rds_host = "<RDS_PROXY_ENDPOINT_URL>"
db_username = secret['username']
db_password = secret['password']
