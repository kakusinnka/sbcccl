import pendulum
# Imports Python standard library logging
import logging

from airflow.decorators import dag, task

@dag(
    description='使用 TeskFlow 测试Cloud logging 客户端.',
    schedule_interval='0 22 * * *',
    start_date=pendulum.datetime(2022, 1, 1, tz="Asia/Tokyo"),
    catchup=False,
    tags=['demo'],
)
def taskflow_python_logging():

    @task
    def task_start():
        # 连接处理程序后，应用中生成的所有处于INFO 级别或更高级别的日志都将默认发送至 Logging。
        # 如果将来自 App Engine 或 Google Kubernetes Engine 的消息记录到 Logging 中，则处理程序会将此类消息发送到这些环境各自的资源类型；
        # 否则，日志将默认显示在 Global 资源类型的 python 日志下。
        logging.info('taskflow_python_logging' + ' DAG 开始')

    @task()
    def task_001():
        logging.info('taskflow_python_logging' + ' TASK001 开始')
        print('API调用开始')
        logging.info('taskflow_python_logging' + ' TASK001 结束')

    @task
    def task_end():
        logging.info('taskflow_python_logging' + ' DAG 结束')

    task_start() >> task_001() >> task_end()

# Airflow 只会加载出现在 DAG 文件顶层的 DAG。 这意味着您不能只使用 @dag 声明一个函数 - 您还必须在 DAG 文件中至少调用一次并将其分配给顶级对象，如下所示：
dag = taskflow_python_logging()
