from django.shortcuts import render
from .models import *

def consulta(request):
    consultas = {
        'consultas' : Livro.objects.all()
    }

    return render(request, 'consulta/consulta.html', consultas)

def reserva(request):
    if request.POST:
        nova_reserva= Emprestimo()
        nova_reserva.data.emprestimo = request.POST.get('data')
        nova_reserva.ata_devolucao = request.POST.get('data2')
        try:
            leitor = Leitores.objects.get(pk=request.POST.get('leitor'))
            livro = Livro.objects.get(pk=request.POSt.get('livro'))
            nova_reserva.leitor = leitor
            nova_reserva.livro = livro
            nova_reserva.save()
        except Leitores.DoesNoExit:
                print("Leitor não encontrado.")
        except Livro.DoesNoExit:
                print("Livro não encontrado.")
        except Exception as e:
                print("Erro de integridade:", e)
    reservas = {
          'leitor':Leitores.objects.all(),
          'livro':Livro.objects.all(),
    }

    return render(request,'reserva/reserva.html', reservas)

def autor(request):
    autores = {
        'autor' : Autor.objects.all()
    }

    return render(request, 'autores/autores.html', autores)  

def categoria(request):
    categorias = {
        'categorias' : Categoria.objects.all()
    }

    return render(request, 'categorias/categorias.html', categorias)  

def editoras(request):
    editoras = {
        'editoras' : Editora.objects.all()
    }

    return render(request, 'editoras/editoras.html', editoras)  

