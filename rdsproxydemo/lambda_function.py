import json
import logging
import sys
import rds_config
import pymysql

# rds settings
rds_host = rds_config.rds_host
db_username = rds_config.db_username
db_password = rds_config.db_password

logger = logging.getLogger()
logger.setLevel(logging.INFO)

try:
    conn = pymysql.connect(host=rds_host, user=db_username, passwd=db_password, db="rdsporxydb", connect_timeout=5)
except Exception as err:
    logger.error("ERROR: Unexpected error: Could not connect to MySQL instance.")
    logger.error(err)
    sys.exit()

logger.info("SUCCESS: Connection to RDS MySQL instance succeeded")


def lambda_handler(event, context):
    """
     This function fetches content from MySQL RDS instance
     """

    with conn.cursor() as cur:
        sql = "select * from user"
        cur.execute(sql)
        body = cur.fetchall()

    return {
        "statusCode": 200,
        "body": json.dumps(body)
    }
