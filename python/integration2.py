import logging
import google.cloud.logging
from google.cloud.logging.handlers import CloudLoggingHandler, setup_logging

# 实例化一个日志客户端
client = google.cloud.logging.Client()
# 获得 Cloud Logging API 调用的handler, 并提供名称。
handler = CloudLoggingHandler(client, name="mycustomlog")
# 返回具有指定名称的logging。
cloud_logger = logging.getLogger()
# Set the logging level of this logger.
cloud_logger.setLevel(logging.INFO)

# Add the specified handler to this logger.
setup_logging(handler)
logging.error('bad news00B')
cloud_logger.error('bad news00C')