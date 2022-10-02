import pendulum

from airflow.decorators import dag, task
from google.cloud import logging

# 实例化一个日志客户端
logging_client = logging.Client()
# 要写入的日志的名称
log_name = "taskflow_cloud_logging"
# 选择要写入的日志
logger = logging_client.logger(log_name)

@dag(
    description='使用 TeskFlow 测试Cloud logging 客户端.',
    schedule_interval='0 22 * * *',
    start_date=pendulum.datetime(2022, 1, 1, tz="Asia/Tokyo"),
    catchup=False,
    tags=['demo'],
)
def taskflow_cloud_logging():

    @task
    def task_start():
        logger.log_text('taskflow_cloud_logging' + 'DAG 开始')

    @task()
    def task_001():
        logger.log_text('taskflow_cloud_logging' + ' TASK001 开始')
        print('API调用开始')
        logger.log_text('taskflow_cloud_logging' + ' TASK001 结束')

    @task
    def task_end():
        logger.log_text('taskflow_cloud_logging' + ' DAG 结束')

    task_start() >> task_001() >> task_end()

# Airflow 只会加载出现在 DAG 文件顶层的 DAG。 这意味着您不能只使用 @dag 声明一个函数 - 您还必须在 DAG 文件中至少调用一次并将其分配给顶级对象，如下所示：
dag = taskflow_cloud_logging()
