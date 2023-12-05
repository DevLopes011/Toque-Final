from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Usuario
from .forms import UsuarioForm

def home(request):
    return render(request,'usuarios/home.html')

def cadastro_usuarios(request):
    return render(request,'usuarios/cadastro_usuarios.html')

def usuarios(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        telefone = request.POST.get('telefone')
        email = request.POST.get('email')
        cpf = request.POST.get('cpf')
        endereco = request.POST.get('endereco')
        senha = request.POST.get('senha')

        if Usuario.objects.filter(email=email).exists():
            messages.error(request, 'E-mail já cadastrado. Por favor, escolha outro e-mail.')
        else:
            novo_usuario = Usuario(nome=nome, telefone=telefone, email=email, cpf=cpf, endereco=endereco, senha=senha)
            novo_usuario.save()
            messages.success(request, 'Cadastro realizado com sucesso!')

    usuarios = {'usuarios': Usuario.objects.all()}
    return render(request, 'usuarios/usuarios.html', usuarios)

def delete_item(request, id_usuario):
    item = Usuario.objects.get (id_usuario=id_usuario)
    item.delete()
    return redirect('listagem_usuarios')

def edit_item(request, id_usuario):
    usuario = get_object_or_404(Usuario, pk=id_usuario)

    if request.method == "POST":
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário atualizado com sucesso!')
            return redirect('listagem_usuarios')
        else:
            messages.error(request, 'Erro ao atualizar o usuário. Verifique os campos.')

    else:
        form = UsuarioForm(instance=usuario)

    return render(request, 'usuarios/editar_usuario.html', {'form': form, 'usuario': usuario})

def get_user(request, id_usuario):
    usuario = get_object_or_404(Usuario, id_usuario=id_usuario)
    print(request.method)
    print('ENTROU AQUI NO GET_USER!!! ')

    form = UsuarioForm(instance=usuario)

    context = {'usuario': usuario, 'form': form}
    return render(request, 'usuarios/editar_usuario.html', context)