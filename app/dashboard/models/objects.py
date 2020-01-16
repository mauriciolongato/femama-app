from django.db import models


# ONGS
class Ong(models.Model):
    nome = models.CharField(max_length=500)
    cidade = models.CharField(max_length=50, null=True)
    estado = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=50, null=True)
    whatsapp = models.CharField(max_length=50, null=True)
    cnpj = models.CharField(max_length=15,  null=True)
    cnes = models.CharField(max_length=15,  null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Informações Cadastrais Ong'

    def __str__(self):
        return u'%s' % self.nome


class SegmentoOng(models.Model):
    ong = models.ForeignKey(Ong, on_delete=models.CASCADE)
    segmento = models.CharField(max_length=50, null=True)
    score = models.IntegerField(null=True)

    class Meta:
        verbose_name_plural = 'Segmento da Ong'

    def __str__(self):
        return u'%s' % self.ong.nome


class QuestionarioCenso(models.Model):
    numero_pergunta = models.IntegerField(null=True)
    secao = models.IntegerField(null=True)
    pergunta = models.CharField(max_length=500, null=True)

    class Meta:
        verbose_name_plural = 'Questões do Censo'

    def __str__(self):
        return u'%s' % self.numero_pergunta


class CensoRespostas(models.Model):
    ong = models.ForeignKey(Ong, on_delete=models.CASCADE)
    pergunta = models.ForeignKey(QuestionarioCenso, on_delete=models.CASCADE)
    id_censo = models.IntegerField(null=True)
    resposta = models.TextField(null=True)

    class Meta:
        verbose_name_plural = 'Respostas do Censo'

    def __str__(self):
        return u'%s' % self.ong.nome


class ScoreRespostas(models.Model):
    pergunta = models.ForeignKey(QuestionarioCenso, on_delete=models.CASCADE)
    secao = models.IntegerField(null=True)
    alternativa = models.CharField(max_length=200, null=True)
    peso = models.IntegerField(null=True)
    advocacy = models.IntegerField(null=True)
    proximidade_femama = models.IntegerField(null=True)
    maturidade_data = models.IntegerField(null=True)

    class Meta:
        verbose_name_plural = 'Peso das Perguntas'

    def __str__(self):
        return u'%s' % self.pergunta


class RegraPerfil(models.Model):
    nome_perfil = models.CharField(max_length=200, null=True)
    atuacao_advocacy = models.CharField(max_length=200, null=True)
    relacao_femama = models.CharField(max_length=200, null=True)
    potencial_advocacy_dados = models.CharField(max_length=200, null=True)

    class Meta:
        verbose_name_plural = 'Regras dos perfis'

    def __str__(self):
        return u'%s' % self.pergunta


# DASH COMUNICAÇÃO
# num_pergunta 137 ('Como a instituição divulga ações realizadas?')
class Divulgacao(models.Model):
    tipo_divulgacao = models.CharField(max_length=500, null=True)

    class Meta:
        verbose_name_plural = 'Divulgações'


# num_pergunta 138 ('Em quais canais sua ONG está presente?')
class CanalDigital(models.Model):
    canal = models.CharField(max_length=500, null=True)

    class Meta:
        verbose_name_plural = 'Canais digitais'


# num_pergunta 140 ('Existem fornecedores de comunicação contratados ou parceiros que prestam serviço contínuo?')
class Fornecedor(models.Model):
    tipo_fornecedor = models.CharField(max_length=500, null=True)

    class Meta:
        verbose_name_plural = 'Fornecedores'


# num_pergunta entre 98 a 108 ('Quem são os parceiros principais da ONG? De quem busca apoio e para quê?')
class Parceria(models.Model):
    tipo_parceiro = models.CharField(max_length=500, null=True)

    class Meta:
        verbose_name_plural = 'Parcerias'


# num_pergunta entre 98 a 108 ('Quem são os parceiros principais da ONG? De quem busca apoio e para quê?')
class TipoParceria(models.Model):
    tipo_parceria = models.CharField(max_length=500, null=True)

    class Meta:
        verbose_name_plural = 'Tipos de parceria'


# num_pergunta 84 ('Quantos voluntários estão ligados à ONG de maneira geral? Considere tanto os voluntários que ocupam
# cargos quanto os que participam de ações pontuais.')
class QuantidadeVoluntarios(models.Model):
    quantidade = models.CharField(max_length=500, null=True)

    class Meta:
        verbose_name_plural = 'Quantidade de voluntários'


# DASH PACIENTE
class TipoCancer(models.Model):
    # tabela questionario_censo - num_pergunta entre 60 a 61 ('Qual o tipo de câncer dos pacientes atendidos pela ONG?')
    tipo_cancer = models.CharField(max_length=500, null=True)

    class Meta:
        verbose_name_plural = 'Tipos de cancer'


# num_pergunta 62 a 63 ('Das pacientes com câncer de mama atendidas, em qual estágio se encontram atualmente?')
class EstagioCancer(models.Model):
    estagio_cancer = models.CharField(max_length=500, null=True)

    class Meta:
        verbose_name_plural = 'Estagios de cancer'


# num_pergunta 64 a 65('Considerando pacientes com câncer de mama atendidas, de qual o sistema de saúde usufruem?')
class SistemaSaude(models.Model):
    tipo_sistema = models.CharField(max_length=500, null=True)

    class Meta:
        verbose_name_plural = 'Sistemas de saúde'


# num_pergunta 66 a 67 ('Considerando pacientes com câncer de mama atendidas, qual sua faixa etária?')
class FaixaEtaria(models.Model):
    classe_faixa = models.CharField(max_length=500, null=True)

    class Meta:
        verbose_name_plural = 'Faixas etarias'


# num_pergunta 156 	('Quais informações A ONG mapeia no cadastro de paciente?')
class MapeamentoPaciente(models.Model):
    informacao = models.CharField(max_length=500, null=True)

    class Meta:
        verbose_name_plural = 'Mapeamentos de pacientes'


# num_pergunta 156 ('Quais informações A ONG mapeia no cadastro de paciente?')
class ContatoPaciente(models.Model):
    informacao = models.CharField(max_length=500, null=True)

    class Meta:
        verbose_name_plural = 'Contatos de pacientes'


# Pergunta rods
# num_pergunta 156 ('Quais informações A ONG mapeia no cadastro de paciente?')
class Coalizao(models.Model):
    coalizao = models.CharField(max_length=500, null=True)

    class Meta:
        verbose_name_plural = 'Coalizões'


# Upload imagens
class ImagensDash(models.Model):
    img = models.ImageField(upload_to='img/')
