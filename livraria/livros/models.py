from django.db import models
from django.urls import reverse
from livraria.models.produto import Produto


class Livro(Produto):
    quantidade_paginas = models.IntegerField()

    def get_absolute_url(self):
        return reverse('livro_editar', kwargs={'pk': self.pk})

    def get_quantidade_paginas(self):
        return self.quantidade_paginas

    def set_quantidade_paginas(self, quantidade):
        self.quantidade_paginas = quantidade

    def get_valor(self):
        if self.promocao:
            return '{:.2f}'.format(self.valor - (self.valor * 0.6))
        return self.valor
