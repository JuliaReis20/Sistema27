# Generated by Django 4.2.5 on 2023-09-20 12:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_area', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_cidade', models.CharField(max_length=100)),
                ('uf', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_curso', models.CharField(max_length=100)),
                ('carga_curso', models.CharField(max_length=100)),
                ('duracao_curso', models.CharField(max_length=100)),
                ('area_curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.area')),
            ],
        ),
        migrations.CreateModel(
            name='Diciplina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_diciplina', models.CharField(max_length=100)),
                ('area_diciplina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.area')),
            ],
        ),
        migrations.CreateModel(
            name='Instituicao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_instituicao', models.CharField(max_length=100)),
                ('site_instituicao', models.CharField(max_length=100)),
                ('telefone_instituicao', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Ocupacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_ocupacao', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Semestre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('periodo_semestre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TipoAvaliacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_tipoavaliacao', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Turmas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_turmas', models.CharField(max_length=100)),
                ('periodo_semestre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.semestre')),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_pessoa', models.CharField(max_length=100)),
                ('pai_pessoa', models.CharField(max_length=100)),
                ('mae_pessoa', models.CharField(max_length=100)),
                ('cpf_pessoa', models.CharField(max_length=11, unique=True)),
                ('data_pessoa', models.DateField()),
                ('email_pessoa', models.CharField(max_length=100)),
                ('cidade_pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cidade')),
                ('ocupacao_pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.ocupacao')),
            ],
        ),
        migrations.CreateModel(
            name='Ocorrencias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao_ocorrencia', models.CharField(max_length=100)),
                ('data_ocorrencia', models.DateField()),
                ('curso_ocorrencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.curso')),
                ('periodo_ocorrencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.semestre')),
            ],
        ),
        migrations.CreateModel(
            name='Matriculas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_inicio', models.DateField()),
                ('data_term', models.DateField()),
                ('instituicao_matricula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.instituicao')),
                ('ocupacao_pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.ocupacao')),
            ],
        ),
        migrations.CreateModel(
            name='Frequencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_faltas', models.CharField(max_length=100)),
                ('curso_frequencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.curso')),
                ('diciplina_frequencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.diciplina')),
            ],
        ),
        migrations.CreateModel(
            name='Diciplinascurso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_diciplinacurso', models.CharField(max_length=100)),
                ('carga_diciplinacurso', models.CharField(max_length=100)),
                ('curso_diciplinacurso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.curso')),
                ('periodo_diciplinacurso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.semestre')),
            ],
        ),
        migrations.AddField(
            model_name='curso',
            name='instituicao_curso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.instituicao'),
        ),
        migrations.CreateModel(
            name='Avaliacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao_avaliacao', models.CharField(max_length=100)),
                ('curso_avaliacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.curso')),
                ('diciplina_avaliacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.diciplina')),
                ('tipo_avaliacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.tipoavaliacao')),
            ],
        ),
    ]