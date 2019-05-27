from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from livros.models import Livro

# Create your views here.


class LivroForm(ModelForm):
    class Meta:
        model = Livro
        fields = ['nome',
                  'descricao', 'quantidade_paginas', 'valor', 'quantidade_estoque', 'promocao']


def home_page(request, template_name='base-content.html'):
    return render(request, template_name)


def listar_livros(request, template_name='livro_list.html'):
    livro = Livro.objects.all()
    data = {}
    data['object_list'] = livro
    return render(request, template_name, data)


def detalhes_livros(request, pk, template_name='livro_detail.html'):
    livro = get_object_or_404(Livro, pk=pk)
    return render(request, template_name, {'object': livro})


def criar_livro(request, template_name='livro_form.html'):
    form = LivroForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('livro_list')
    return render(request, template_name, {'form': form})


def alterar_livro(request, pk, template_name='livro_form.html'):
    livro = get_object_or_404(Livro, pk=pk)
    form = LivroForm(request.POST or None, instance=livro)
    if form.is_valid():
        form.save()
        return redirect('livro_list')
    return render(request, template_name, {'form': form})


def deletar_livro(request, pk, template_name='livro_confirm_delete.html'):
    livro = get_object_or_404(Livro, pk=pk)
    if request.method == 'POST':
        livro.delete()
        return redirect('livro_list')
    return render(request, template_name, {'object': livro})
