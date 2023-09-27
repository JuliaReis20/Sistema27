from django.shortcuts import render
from . models  import*

def consulta(request):
    consultas = {
         'consultas':Curso.objects.all()
        }

    return render(request,'consulta/consulta.html',consultas)

def reserva(request):
    if request.POST:
        nova_reseva= Emprestimo()
        nova_reseva.data_emprestimo = request.POST.get('data')
        nova_reseva.data_devolução = request.POST.get('data2')
        try:
            leitor: Leitor.objects.get(pk=request.POST.get('leitor'))
            livro: Livro.objects.get(pk=request.POST.get('livro'))
            nova_reseva.leitor = leitor
            nova_reseva.livro = livro
            nova_reseva.save()

        except leitor.DoesNotExist:
            print("leitor não encotrado")

        except livro.DoesNotExist:
            print("Llivro não encotrado")  

        except Exception as e:
            print("Erro de Integridade:", e)    

        nova_reseva= Emprestimo()

    reservas = {
         'leitor':leitor.objects.all(),
         'livro':livro.objects.all(),
        }
    
    return render(request,'reserva/resercva.html',reservas)