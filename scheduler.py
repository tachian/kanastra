#!/usr/bin/env python
import logging

from apscheduler.schedulers.blocking import BlockingScheduler

from src.app import create_app
from src.application_layer.use_cases.jobs import JobsUseCase

app = create_app()

scheduler = BlockingScheduler(timezone='America/Sao_Paulo')

logger = logging.getLogger("cdc-manager."+__name__)


@scheduler.scheduled_job(
    trigger='cron',
    **app.config['SEND_SLIPS_CRON_PARAMS'])
def send_slips():
    with app.app_context():
        logger.info('[Start] Send slips.')
        JobsUseCase.send_slips()
        logger.info('[End] Send slips.')

if __name__ == '__main__':
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
    except Exception as e:
        logger.exception(e.message)
