import logging

from celery import shared_task

from .models import jobs


logger = logging.getLogger(__name__)


@shared_task
def data_forms_load():

    # logger.info('starting request google sheets')
    censo = jobs.get_censo_data()
    jobs.load_questions(censo[0])
    jobs.load_answers(censo)

    return {'status': 'CENSO Carregado'}


@shared_task
def score_load():

    logger.info('starting request google sheets')

    score = jobs.get_score_data()
    jobs.load_score(score)

    perfil = jobs.get_perfil_data()
    jobs.load_regra_perfil(perfil)

    return {'status': 'Score carregado'}


@shared_task
def dropdown_metabase_load():

    jobs.load_dropdowns_metabase()

    return {'status': 'Dropdowns carregados'}
