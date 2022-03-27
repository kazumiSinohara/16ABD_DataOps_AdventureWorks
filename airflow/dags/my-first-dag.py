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
    "schedule_interval":'*/1 * * * *', #..cada minuto
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
   'my-first-dag',
   schedule_interval=timedelta(minutes=1),
   catchup=False,
   default_args=default_args
   )
# Definindo as tarefas que a DAG vai executar, nesse caso a execução de dois programas Python, chamando sua execução por comandos bash
# O operador Bash, também pode ser utilizado para executar jobs Talend via Sh
t1 = BashOperator(
   dag=dag,
   task_id='primeiro_etl',
   bash_command="""
   cd $AIRFLOW_HOME/dags/etl_scripts/
   python3 primeiro_etl.py
   """)
t2 = BashOperator(
   dag=dag,
   task_id='segundo_etl',
   bash_command="""
   cd $AIRFLOW_HOME/dags/etl_scripts/
   python3 segundo_etl.py
   """)
# Definindo o padrão de execução, nesse caso executamos t1 e depois t2
t1 >> t2
