from __future__ import print_function
import logging
import pickle
import os.path
from datetime import datetime
# from dashboard.models import objects
from . import objects
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


logger = logging.getLogger(__name__)


# Google forms interface
def auth_get_credentials(scopes):
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('dashboard/models/config/token.pickle'):
        with open('dashboard/models/config/token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'dashboard/models/config/credentials.json', scopes)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('dashboard/models/config/token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    return creds


def get_sheets_data(sample_spreadsheet_id, sample_range_name, scopes):
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    creds = auth_get_credentials(scopes)
    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=sample_spreadsheet_id,
                                range=sample_range_name).execute()
    values = result.get('values', [])

    if not values:
        return None
    else:
        return values


# Get censo answer
def get_censo_data():
    # If modifying these scopes, delete the file token.pickle.
    # https://docs.google.com/spreadsheets/d/1sMCY3ossyTUGfu792G_S3Bc2Hql-9IaAU9TfTcJ1GQ8/edit#gid=755250185
    scopes = ['https://www.googleapis.com/auth/spreadsheets.readonly']

    # The ID and range of a sample spreadsheet.
    sample_spreadsheet_id = '1sMCY3ossyTUGfu792G_S3Bc2Hql-9IaAU9TfTcJ1GQ8'
    sample_range_name = 'Form Responses 1!A:GG'

    data = get_sheets_data(sample_spreadsheet_id, sample_range_name, scopes)
    return data


def get_score_data():
    # If modifying these scopes, delete the file token.pickle.
    # https://docs.google.com/spreadsheets/d/1BGjuMFYUAFqUlgkQcyhFnyzlBi62G-ckeSHj0JfaypQ/edit#gid=0
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

    # The ID and range of a sample spreadsheet.
    SAMPLE_SPREADSHEET_ID = '1BGjuMFYUAFqUlgkQcyhFnyzlBi62G-ckeSHj0JfaypQ'
    SAMPLE_RANGE_NAME = 'pesos!A:H'

    data = get_sheets_data(SAMPLE_SPREADSHEET_ID, SAMPLE_RANGE_NAME, SCOPES)
    return data


def get_perfil_data():
    # If modifying these scopes, delete the file token.pickle.
    # https://docs.google.com/spreadsheets/d/1BGjuMFYUAFqUlgkQcyhFnyzlBi62G-ckeSHj0JfaypQ/edit#gid=0
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

    # The ID and range of a sample spreadsheet.
    SAMPLE_SPREADSHEET_ID = '1BGjuMFYUAFqUlgkQcyhFnyzlBi62G-ckeSHj0JfaypQ'
    SAMPLE_RANGE_NAME = 'perfil!A:D'

    data = get_sheets_data(SAMPLE_SPREADSHEET_ID, SAMPLE_RANGE_NAME, SCOPES)
    return data


# DB functions
def clean_db_data():
    objects.Ong.objects.all().delete()
    objects.QuestionarioCenso.objects.all().delete()
    objects.CensoRespostas.objects.all().delete()
    objects.ScoreRespostas.objects.all().delete()
    objects.SegmentoOng.objects.all().delete()


def load_questions(questions):
    for num_pergunta in range(len(questions)):
        p, created = objects.QuestionarioCenso.objects.update_or_create(
            numero_pergunta=num_pergunta + 1,
            defaults={'pergunta': questions[num_pergunta]},
        )


def load_answers(answers):
    questions = answers[0]
    answers = answers[1:]

    id_censo = 0
    for respostas in answers:
        nome_ong = respostas[1]
        cidade = respostas[2].title()
        estado = respostas[3]
        email = respostas[4].lower()
        whatsapp = respostas[5]
        cnpj = respostas[8]
        cnes = respostas[9]

        logger.info('{}'.format(nome_ong))

        ong, created = objects.Ong.objects.update_or_create(
            nome=nome_ong,
            defaults={'cidade': cidade,
                      'estado': estado,
                      'email': email,
                      'whatsapp': whatsapp,
                      'cnpj': cnpj,
                      'cnes': cnes},
        )
        print(datetime.now(), ' - ', nome_ong)
        # Perguntas e respostas
        for num_pergunta, resposta in zip(range(len(questions)), respostas):
            p = objects.QuestionarioCenso.objects.get(numero_pergunta=num_pergunta + 1)

            objects.CensoRespostas.objects.update_or_create(
                ong=ong,
                pergunta=p,
                defaults={'id_censo': id_censo,
                          'resposta': resposta}
            )
        id_censo = id_censo + 1


def load_score(score):
    objects.ScoreRespostas.objects.all().delete()

    for pergunta in score[1:]:
        p = objects.QuestionarioCenso.objects.get(numero_pergunta=int(pergunta[0]))
        print(datetime.now())
        print(int(pergunta[0]), pergunta, p)
        print('\n')

        objects.ScoreRespostas.objects.create(
            pergunta=p,
            secao=pergunta[1],
            alternativa=pergunta[3],
            peso=pergunta[4],
            advocacy=pergunta[5],
            proximidade_femama=pergunta[6],
            maturidade_data=pergunta[7],
        )


def load_regra_perfil(l_perfil):
    objects.RegraPerfil.objects.all().delete()

    for grupo in l_perfil[1:]:

        objects.RegraPerfil.objects.create(
            nome_perfil=grupo[0],
            atuacao_advocacy=grupo[1],
            relacao_femama=grupo[2],
            potencial_advocacy_dados=grupo[3],
        )


def load_dropdowns_metabase():
    objects.TipoCancer.objects.all().delete()
    l1 = objects.TipoCancer.objects.create(tipo_cancer="Outros")
    l2 = objects.TipoCancer.objects.create(tipo_cancer="Mama")
    l1.save()
    l2.save()

    objects.EstagioCancer.objects.all().delete()
    l1 = objects.EstagioCancer.objects.create(estagio_cancer="Local / inicial")
    l2 = objects.EstagioCancer.objects.create(estagio_cancer="Metastático")
    l1.save()
    l2.save()

    objects.SistemaSaude.objects.all().delete()
    l1 = objects.SistemaSaude.objects.create(tipo_sistema="Sistema Público (SUS)")
    l2 = objects.SistemaSaude.objects.create(tipo_sistema="Sistema Privado (Planos e Convênios)")
    l1.save()
    l2.save()

    objects.FaixaEtaria.objects.all().delete()
    l1 = objects.FaixaEtaria.objects.create(classe_faixa="Menos de 50 anos")
    l2 = objects.FaixaEtaria.objects.create(classe_faixa="Mais de 50 anos")
    l1.save()
    l2.save()

    objects.MapeamentoPaciente.objects.all().delete()
    l1 = ["Não realizamos cadastro",
          "Nome do paciente",
          "Endereço do paciente",
          "Email do paciente",
          "Telefone do paciente",
          "Sistema de saúde que utiliza (sus/particular)",
          "Tipo de câncer (mama ou outras neoplastias)",
          "Subtipo do câncer de mama (her2 +, triplo negativo, etc.)",
          "Câncer hereditário (presença de mutação em genes como BRCA ou outros)",
          "Estágio no momento do diagnóstico",
          "Estágio no momento que chegou à ONG",
          "Tempo de espera de diagnóstico",
          "Tempo de espera para início de tratamento",
          "Dificuldades de acesso relatadas pelo paciente (reconstrução mamária negada, falta de medicamento, etc)"
          ]
    objects.MapeamentoPaciente.objects.bulk_create([objects.MapeamentoPaciente(informacao=x) for x in l1])

    objects.ContatoPaciente.objects.all().delete()
    l1 = ["Não guardamos informações",
          "Fazemos cadastro de papel",
          "Fazemos cadastro digital (word, formulário, excel)",
          "Possuímos um sistema digital (plataforma, aplicativo ou ferramenta) próprio para isso",
          "Incluímos o paciente num mailling/grupo de e-mail",
          "Incluímos o paciente em um grupo do whatsapp"
          ]

    objects.ContatoPaciente.objects.bulk_create([objects.ContatoPaciente(informacao=x) for x in l1])

    objects.Divulgacao.objects.all().delete()
    l1 = ["Divulga nas redes sociais",
          "Publica notícia no site ou blog da instituição",
          "Contata a imprensa local",
          "Envia e-mail para listas de contatos",
          "Envia fotos e informações pelo WhatsApp para seus contatos",
          "Relata para funcionários / voluntários em reunião presencial",
          "Coloca avisos em murais"
          ]
    objects.Divulgacao.objects.bulk_create([objects.Divulgacao(tipo_divulgacao=x) for x in l1])

    objects.CanalDigital.objects.all().delete()
    l1 = ["Facebook",
          "Instagram",
          "Site",
          "Youtube",
          "Linkedin",
          "Twitter"
          ]
    objects.CanalDigital.objects.bulk_create([objects.CanalDigital(canal=x) for x in l1])

    objects.Fornecedor.objects.all().delete()
    l1 = ["Assessoria/assessor de imprensa",
          "Agência/profissional de propaganda",
          "Agência/profissional de comunicação/marketing digital",
          "Agência/profissional de design",
          "Não temos fornecedores contratados"
          ]
    objects.Fornecedor.objects.bulk_create([objects.Fornecedor(tipo_fornecedor=x) for x in l1])

    objects.Parceria.objects.all().delete()
    l1 = ["Farmacêuticas",
          "Universidades",
          "Clínicas e hospitais públicos",
          "Clínicas e hospitais privados",
          "Comércio local",
          "Marcas / empresas de produtos e serviços",
          "Prefeitura, secretaria de saúde ou outros órgãos públicos",
          "Legislativo",
          "Imprensa local",
          "Influenciadores digitais",
          "FEMAMA",
          "Outras ONGs (sem contar a FEMAMA)"
          ]
    objects.Parceria.objects.bulk_create([objects.Parceria(tipo_parceiro=x) for x in l1])

    objects.TipoParceria.objects.all().delete()
    l1 = ["Apoio financeiro",
          "Apoio de capacitação",
          "Apoio de prestação de serviço",
          "Apoio de divulgação",
          "Apoio em advocacy",
          "Não tenho"
          ]
    objects.TipoParceria.objects.bulk_create([objects.TipoParceria(tipo_parceria=x) for x in l1])

    objects.QuantidadeVoluntarios.objects.all().delete()
    l1 = ["0",
          "de 1 - 10",
          "de 11 a 20",
          "de 21 a 30",
          "51 a 100",
          "100+"
          ]
    objects.QuantidadeVoluntarios.objects.bulk_create([objects.QuantidadeVoluntarios(quantidade=x) for x in l1])

    objects.Coalizao.objects.all().delete()
    l1 = ["Abc Alliance",
          "Alianza Latina",
          "Brazil Foundation",
          "Coniacc",
          "Conselho Estadual Da Condição Feminina De São Paulo (Cecf)",
          "Fórum De Patologias Crônicas Da Bahia",
          "Frente Estadual De Combate Ao Câncer De Mama Do Rj",
          "Movimento Todos Juntos Contra O Câncer",
          "Não",
          "Projeto City Cancer Challenge",
          "Recan",
          "Recomeçar",
          "Rede Feminina De Combate Ao Câncer",
          "Rede Mama Ceará",
          "Uicc",
          "Ulaccam"
          ]
    objects.Coalizao.objects.bulk_create([objects.Coalizao(coalizao=x) for x in l1])


# Calculation
def calculate_score(ong_id):
    # ong = objects.Ong.objects.get(ong_id=ong_id)
    p = objects.ScoreRespostas.objects.all()
    answers = objects.CensoRespostas.objects.select_related('ong', 'pergunta')
    # answers = objects.QuestionarioCenso.objects.filter(ong_id=ong_id, pergunta=p).select_related()
    # score = objects.ScoreRespostas.objects.select_related('pergunta')
    return answers
