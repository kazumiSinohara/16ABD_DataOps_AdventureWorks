# Importando as bibliotecas que vamos utilizar
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

# definição de argumentos básicos
default_args = {
    "owner": "16ABD",
    "depends_on_past": False,
    "start_date": datetime(2022, 1, 1),
    "max_active_runs":1,
    "concurrency":4,
    "schedule_interval":'*/2 * * * *', #..cada minuto
    "email": ["airflow@airflow.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
}
# Nomeando a DAG e definindo quando ela vai ser executada (você pode usar argumentos em Crontab também caso queira que a DAG execute por exemplo todos os dias as 8 da manhã)
dag = DAG(
   'report-region-online',
   schedule_interval=timedelta(minutes=2),
   catchup=False,
   default_args=default_args
   )
# Definindo as tarefas que a DAG vai executar, nesse caso a execução de dois programas Python, chamando sua execução por comandos bash
# O operador Bash, também pode ser utilizado para executar jobs Talend via Sh
t1 = BashOperator(
   dag=dag,
   task_id='generate-csv',
   bash_command="""
   cd $AIRFLOW_HOME/dags/talend_jobs/reportRegionOnline
   ./reportRegionOnline_run.sh
   """)
# Definindo o padrão de execução, nesse caso executamos t1 e depois t2
t1
