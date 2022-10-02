import pendulum
from google.cloud import logging
from airflow import DAG
from airflow.operators.python import PythonOperator

# 实例化一个日志客户端
logging_client = logging.Client()
# 要写入的日志的名称
log_name = "with_dag_cloud_logging"
# 选择要写入的日志
logger = logging_client.logger(log_name)

with DAG(
    'with_dag_cloud_logging',
    description='使用 with dag 的方式 测试 Cloud logging 客户端.',
    schedule_interval='0 22 * * *',
    start_date=pendulum.datetime(2022, 1, 1, tz="Asia/Tokyo"),
    catchup=False,
    tags=['demo']
) as dag:

    def task_start():
        logger.log_text('with_dag_cloud_logging' + ' DAG 开始')

    def task_001():
        logger.log_text('with_dag_cloud_logging' + ' TASK001 开始')
        print('调用 API')
        logger.log_text('with_dag_cloud_logging' + ' TASK001 结束')

    def task_end():
        logger.log_text('with_dag_cloud_logging' + ' DAG 结束')

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