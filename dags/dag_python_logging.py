import pendulum
# Imports Python standard library logging
import logging
from airflow import DAG
from airflow.operators.python import PythonOperator

dag = DAG(
    'dag_python_logging',
    description='使用 dag变量的写法 测试 Cloud logging 客户端.',
    schedule_interval='0 22 * * *',
    start_date=pendulum.datetime(2022, 1, 1, tz="Asia/Tokyo"),
    catchup=False,
    tags=['demo']
)

def task_start():
    # 连接处理程序后，应用中生成的所有处于INFO 级别或更高级别的日志都将默认发送至 Logging。
    # 如果将来自 App Engine 或 Google Kubernetes Engine 的消息记录到 Logging 中，则处理程序会将此类消息发送到这些环境各自的资源类型；
    # 否则，日志将默认显示在 Global 资源类型的 python 日志下。
    logging.info('dag_python_logging' + ' DAG 开始')

def task_001():
    logging.info('dag_python_logging' + ' TASK001 开始')
    print('调用 API')
    logging.info('dag_python_logging' + ' TASK001 结束')

def task_end():
    logging.info('dag_python_logging' + ' DAG 结束')

task_start = PythonOperator(
    task_id='task_start',
    python_callable=task_start,
    dag=dag
)

task_001 = PythonOperator(
    task_id='task_001',
    python_callable=task_001,
    dag=dag
)

task_end = PythonOperator(
    task_id='task_end',
    python_callable=task_end,
    dag=dag
)

task_start >> task_001 >> task_end