import pendulum
import google.cloud.logging
import logging
from airflow import DAG
from airflow.operators.python import PythonOperator

# 实例化一个日志客户端
logging_client = google.cloud.logging.Client()
# 要写入的日志的名称
log_name = "mylog"
# 选择要写入的日志
logger = logging_client.logger(log_name)
logger.log_text('DAG 开始')
logging.warning('DAG 开始 python logging')
print('DAG 开始 python print')

with DAG(
    'with_dag_logging',
    description='使用TeskFlow测试Cloud logging 客户端.',
    schedule_interval='0 22 * * *',
    start_date=pendulum.datetime(2022, 1, 1, tz="Asia/Tokyo"),
    catchup=False,
    tags=['demo']
) as dag:
    def extract():
        logger.log_text('DAG 开始')
        print('调用 API')
        logger.log_text('DAG 结束')

    extract_task = PythonOperator(
        task_id='task001',
        python_callable=extract
    )

    extract_task
