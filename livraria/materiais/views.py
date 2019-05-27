from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from materiais.models import MaterialEscolar


class MaterialForm(ModelForm):
    class Meta:
        model = MaterialEscolar
        fields = ['nome',
                  'descricao', 'categoria', 'valor', 'quantidade_estoque', 'promocao']


def listar_materiais(request, template_name='material_list.html'):
    material = MaterialEscolar.objects.all()
    data = {}
    data['object_list'] = material
    return render(request, template_name, data)


def detalhes_material(request, pk, template_name='material_detail.html'):
    material = get_object_or_404(MaterialEscolar, pk=pk)
    return render(request, template_name, {'object': material})


def criar_material(request, template_name='material_form.html'):
    form = MaterialForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('material_list')
    return render(request, template_name, {'form': form})


def alterar_material(request, pk, template_name='material_form.html'):
    material = get_object_or_404(MaterialEscolar, pk=pk)
    form = MaterialForm(request.POST or None, instance=material)
    if form.is_valid():
        form.save()
        return redirect('material_list')
    return render(request, template_name, {'form': form})


def deletar_material(request, pk, template_name='material_confirm_delete.html'):
    material = get_object_or_404(MaterialEscolar, pk=pk)
    if request.method == 'POST':
        material.delete()
        return redirect('material_list')
    return render(request, template_name, {'object': material})
