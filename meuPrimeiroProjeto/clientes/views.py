from django.shortcuts import render, redirect, get_object_or_404
from .models import Person
from .form import PersonForm

# Create your views here.

#cRud = READ
#Listar do Banco de Dados
#Caso Esteja no Visual Studio e Person esteja dando erro instale pylint-django usando o pip seguinte forma
#pip install pylint-django
#Em seguida, no Visual Studio Code goto: Configurações do usuário ( Ctrl + ','(Tecla de Virgula) ou
#File > Preferences > Settings, se disponível) Coloque o seguinte no setting.JSON(observe as chaves que são necessárias 
#para configurações de usuário personalizadas no VSC):
''' {"python.linting.pylintArgs": [
    "--load-plugins=pylint_django"
],}'''
#Tutorial acima disponível em <https://stackoverflow.com/questions/45135263/class-has-no-objects-member>

def list_person(request): 
    persons = Person.objects.all() #"objects" é a função que busca do BD e "all"(tudo) informa que quer o BD completo
    return render(request, 'person.html', {'persons':persons})

#Crud = CREATE
#Cadastro no Banco de dados
def person_new(request):
    #request.POST é para caso o usuário ja tenha informado o dados
    #request.FILE para pegar imagens e salvar
    #None caso seja a primeira vez que esteja abrindo o form
    form = PersonForm(request.POST or None, request.FILES or None)
    if form.is_valid():#Validando o form (caso o Usuário ja tenha cadastrado)
        form.save()#Salvando o form
        return redirect('list_person') #Redirecionando para a página que lista os usuário cadastrados
    return render(request,'person_form.html',{'form':form})#Mandando o formulário para a página person_form.html(Caso seja a primeira vez do usuáio abrindo(Passando pela primeira vez aqui))  

#crUd = UPDATE
#Modifica campo ja cadastrado no Banco de dados
def person_update(request, id):
    person = get_object_or_404(Person, pk=id) #Tenta recuperar o objeto passado caso não consiga retorna um 404
    #request.POST é para caso o usuário ja tenha informado o dados
    #request.FILE para pegar imagens e salvar
    #None caso seja a primeira vez que esteja abrindo o form
    #instance=person é a pessa que foi recuperada anteriormente (person)
    form = PersonForm(request.POST or None, request.FILES or None, instance=person)
    if form.is_valid():#Validando o form (caso o Usuário ja tenha cadastrado)
        form.save()#Salvando o form
        return redirect('list_person') #Redirecionando para a página que lista os usuário cadastrados

    return render(request, 'person_form.html', {'form':form})#Mandando o formulário para a página person_form.html(Caso seja a primeira vez do usuáio abrindo(Passando pela primeira vez aqui))  

#cruD = DELETE
#Apagar registro do Banco de Dados
def person_delete(request, id):
    person = get_object_or_404(Person,pk=id)#Tenta recuperar o objeto passado caso não consiga retorna um 404
    #request.POST é para caso o usuário ja tenha informado o dados
    #request.FILE para pegar imagens e salvar
    #None caso seja a primeira vez que esteja abrindo o form
    form = PersonForm(request.POST or None, request.FILES or None, instance=person)
    if  request.method== 'POST': #Validando se request.method é um POST
        person.delete() #Deleta a person
        return redirect('list_person') #Redirecionando para a página que lista os usuário cadastrados
    return render(request,'person_confirm_delete.html',{'person':person}) #Mandando a person para a página person_confirm_delete.html(Caso seja a primeira vez do usuáio abrindo(Passando pela primeira vez aqui))  
    #return render(request,'person_confirm_delete.html',{'form':form}) #Mandando o formulário para a página person_confirm_delete.html(Caso seja a primeira vez do usuáio abrindo(Passando pela primeira vez aqui))

