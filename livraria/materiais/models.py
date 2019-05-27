from django.urls import reverse
from django.db import models
from livraria.models.produto import Produto


class MaterialEscolar(Produto):
    categoria = models.CharField(max_length=200)

    def get_absolute_url(self):
        return reverse('material_editar', kwargs={'pk': self.pk})

    def get_categoria(self):
        return self.categoria

    def set_categoria(self, categoria):
        self.categoria = categoria

    def get_valor(self):
        if self.promocao:
            return '{:.2f}'.format(self.valor - (self.valor * 0.8))
        return self.valor
