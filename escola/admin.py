from django.contrib import admin
from escola.models import Aluno, Curso, Matricula

class Alunos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'rg', 'cpf', 'data_nascimento',) # Campos que serão exibidos
    list_display_links = ('id', 'nome',) # Campos que serão links para edição
    search_fields = ('nome',) # Campos que serão pesquisados
    list_per_page = 20 # Quantidade de registros por página

admin.site.register(Aluno, Alunos)

class Cursos(admin.ModelAdmin):
    list_display = ('id', 'codigo_curso', 'descricao',) # Campos que serão exibidos
    list_display_links = ('id', 'codigo_curso',) # Campos que serão links para edição
    search_fields = ('codigo_curso',) # Campos que serão pesquisados

admin.site.register(Curso, Cursos)

class Matriculas(admin.ModelAdmin):
    list_display = ('id', 'aluno', 'curso', 'periodo',) # Campos que serão exibidos
    list_display_links = ('id', 'aluno',) # Campos que serão links para edição
    search_fields = ('aluno',) # Campos que serão pesquisados

admin.site.register(Matricula, Matriculas)
