from django.db import models

# Create your models here.

class Ocupacao(models.Model):
    nome_ocupacao = models.CharField(max_length=100)
    def __str__(self):
        return self.nome_ocupacao
    
class Cidade(models.Model):
    nome_cidade = models.CharField(max_length=100)
    uf = models.CharField(max_length=2)
    def __str__(self):
        return self.nome_cidade

class Pessoa(models.Model):
    nome_pessoa = models.CharField(max_length=100)
    pai_pessoa = models.CharField(max_length=100)
    mae_pessoa = models.CharField(max_length=100)
    cpf_pessoa = models.CharField(max_length=11, unique=True)
    cpf_pessoa= models.DateField()
    email_pessoa =  models.CharField(max_length=100)
    cidade_pessoa = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    ocupacao_pessoa = models.ForeignKey(Ocupacao, on_delete=models.CASCADE)
    def __str__(self):
        return self.nome_pessoa
    
class Instituicao(models.Model):
    nome_instituicao = models.CharField(max_length=100)
    site_instituicao = models.CharField(max_length=100)
    telefone_instituicao = models.CharField(max_length=100)
    def __str__(self):
        return self.nome_instituicao
    
class Area(models.Model):
    nome_area = models.CharField(max_length=100)
    def __str__(self):
        return self.nome_area
    
class Curso(models.Model):
    nome_curso = models.CharField(max_length=100)
    carga_curso = models.CharField(max_length=100)
    duracao_curso = models.CharField(max_length=100)
    area_curso = models.ForeignKey(Area, on_delete=models.CASCADE)
    instituicao_curso = models.ForeignKey(Instituicao, on_delete=models.CASCADE)
    def __str__(self):
        return self.nome_curso
    
class Semestre(models.Model):
    periodo_semestre = models.CharField(max_length=100)
    def __str__(self):
        return self.periodo_semestre
        
class Diciplina(models.Model):
    nome_diciplina = models.CharField(max_length=100)
    area_diciplina = models.ForeignKey(Area, on_delete=models.CASCADE)
    def __str__(self):
        return self.nome_diciplina
        
class Matriculas(models.Model):
    instituicao_matricula = models.ForeignKey(Instituicao, on_delete=models.CASCADE)
    ocupacao_pessoa = models.ForeignKey(Ocupacao, on_delete=models.CASCADE)
    ocupacao_pessoa = models.ForeignKey(Ocupacao, on_delete=models.CASCADE)
    data_inicio = models.DateField()
    data_term = models.DateField()
    def __str__(self):
        return self.instituicao_matricula
         
class TipoAvaliacao(models.Model):
    nome_tipoavaliacao = models.CharField(max_length=100)
    def __str__(self):
        return self.nome_tipoavaliacao
         
class Avaliacao(models.Model):
    descricao_avaliacao = models.CharField(max_length=100)
    curso_avaliacao = models.ForeignKey(Curso, on_delete=models.CASCADE) 
    diciplina_avaliacao = models.ForeignKey(Diciplina, on_delete=models.CASCADE)
    tipo_avaliacao = models.ForeignKey(TipoAvaliacao, on_delete=models.CASCADE) 
    def __str__(self):
        return self.descricao_avaliacao

class Frequencia(models.Model):
    curso_frequencia = models.ForeignKey(Curso, on_delete=models.CASCADE) 
    diciplina_frequencia = models.ForeignKey(Diciplina, on_delete=models.CASCADE)
    numero_faltas = models.CharField(max_length=100)
    def __str__(self):
        return self.curso_frequencia

class Turmas(models.Model):
    nome_turmas= models.CharField(max_length=100)
    periodo_semestre = models.ForeignKey(Semestre, on_delete=models.CASCADE)
    def __str__(self):
        return self.nome_turmas

class Ocorrencias(models.Model):
    descricao_ocorrencia = models.CharField(max_length=100)
    data_ocorrencia = models.DateField()
    curso_ocorrencia = models.ForeignKey(Curso, on_delete=models.CASCADE) 
    periodo_ocorrencia = models.ForeignKey(Semestre, on_delete=models.CASCADE)
    def __str__(self):
        return self.descricao_ocorrencia
         
class Diciplinascurso(models.Model):
    nome_diciplinacurso = models.CharField(max_length=100)
    carga_diciplinacurso = models.CharField(max_length=100)
    curso_diciplinacurso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    periodo_diciplinacurso = models.ForeignKey(Semestre, on_delete=models.CASCADE)
    def __str__(self):
        return self.nome_diciplinacurso

     


         

    
    