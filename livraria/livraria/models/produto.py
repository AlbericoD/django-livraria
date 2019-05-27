from django.db import models
from django.urls import reverse


class Produto(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.CharField(max_length=600, blank=True)
    quantidade_estoque = models.IntegerField(default=0, blank=True)
    valor = models.FloatField(
        null=True, blank=True, default=None)
    promocao = models.BooleanField(default=False)

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('produto_editar', kwargs={'pk': self.pk})

    def get_nome(self):
        return self.nome

    def get_descricao(self):
        return self.descricao

    def get_quantidade_estoque(self):
        return self.quantidade_estoque

    def get_valor(self):
        return self.valor

    def get_promocao(self):
        return self.promocao

    def set_nome(self, nome):
        self.nome = nome

    def set_descricao(self, descricao):
        self.descricao = descricao

    def set_quantidade_estoque(self, quantidade):
        self.quantidade_estoque = quantidade

    def set_valor(self, valor):
        self.valor = valor

    def set_promocao(self, emPromocao):
        self.promocao = emPromocao

    class Meta:
        abstract = True
