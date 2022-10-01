
import json
import pendulum

from airflow.decorators import dag, task
from google.cloud import logging

# 实例化一个日志客户端
logging_client = logging.Client()
# 要写入的日志的名称
log_name = "taskflow-logging"
# 选择要写入的日志
logger = logging_client.logger(log_name)
logger.log_text('DAG 开始')
@dag(
    description='使用TeskFlow测试Cloud logging 客户端.',
    schedule_interval='0 22 * * *',
    start_date=pendulum.datetime(2022, 1, 1, tz="Asia/Tokyo"),
    catchup=False,
    tags=['demo'],
)
def taskflow_logging():
    @task()
    def task001():
        data_string = '{"1001": 301.27, "1002": 433.21, "1003": 502.22}'

        order_data_dict = json.loads(data_string)
        return order_data_dict

    logger.log_text('task 开始')
    task001()
    logger.log_text('task 结束')

logger.log_text('DAG 开始')
# Airflow 只会加载出现在 DAG 文件顶层的 DAG。 这意味着您不能只使用 @dag 声明一个函数 - 您还必须在 DAG 文件中至少调用一次并将其分配给顶级对象，如下所示：
dag = taskflow_logging()
logger.log_text('DAG 结束')
