import logging

from celery import shared_task

from .models import jobs


logger = logging.getLogger(__name__)


@shared_task
def data_forms_load():

    logger.info('starting request google sheets')
    censo = jobs.get_censo_data()
    jobs.load_questions(censo[0])
    jobs.load_answers(censo)
    logger.info('done')

    return {'status': 'CENSO Carregado'}


@shared_task
def score_load():

    score = jobs.get_score_data()
    jobs.load_score(score)

    return {'status': 'Score carregado'}
