from django.db import models


class TipoIncidente(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome


class Incidente(models.Model):
    titulo = models.CharField(max_length=50, null=False)
    descricao = models.TextField(null=False)
    status = models.BooleanField(default=False)
    localizacao = models.CharField(max_length=50, default="Não definida")
    tipo = models.ForeignKey(TipoIncidente, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo
