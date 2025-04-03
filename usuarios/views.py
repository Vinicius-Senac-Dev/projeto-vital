from django.shortcuts import render, redirect
from django.contrib.messages import constants
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

#Criamos as views, nossas funções que receberam dados do banco de dados e é responsável por intermedia esses dados, processar a requisição e, se necessário, buscando dados no banco por meio da Model.
#Criamos a view cadastro, que é responsável por lidar com as requisições feitas à rota de cadastro e passamos como parâmetro a requisição
#A view pode tanto buscar os dados do banco quanto processar os dados enviados pelo usuário antes de enviá-los ao template
def cadastro(request):
    #Se a requisição for do método get, retorne a renderização da página cadastro.html, ou seja, a view recebe a requisição e depois de verificar o tipo de requisição ou método, chama/encaminha para a página cadastro.html. # Isso significa que, quando o usuário acessar a rota de cadastro, o Django irá processar a requisição
    # e carregar o template 'cadastro.html' para exibição na tela. 
    # Recebe uma requisição que verifica se o usuário não está autenticado e direciona para a página home
    if request.user.is_authenticated:
        return redirect('home')
    
    #Verifica se o tipo da requisição é get, se for direciona para cadastro.html
    if request.method == "GET":
        return render(request, 'cadastro.html')
    # Se não for do tipo get, é porque ele quer realizar o cadastro e enviar dados para o servidor,
    # Para isso, capturamos os dados digitados no input do formulário.
    else:
        primeiro_nome = request.POST.get('primeiro_nome')
        ultimo_nome = request.POST.get('ultimo_nome')
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')


        # Verifica se a senha é diferente da confirmação de senha, se for ele redireciona para realizar o 
        # cadastro novamente
        
        if not senha == confirmar_senha:
            # Caso a senha não seja a mesma, apresenta mensagem de erro
            messages.add_message(request, constants.ERROR, 'As senhas não coincidem')
            return redirect('cadastro')
            
        
        # Verifica se a quantidade de caracteres digitas no input senha é menor que 6, se for ele
        # redireciona para a tela de cadastro novamente 
        if len(senha) < 6:
            messages.add_message(request, constants.ERROR, 'A senha tem que conter pelo menos 6 caracteres')
            return redirect('cadastro')
        
        try:
            #username deve ser único!
            # Criando um usuario para tabela do banco de dados, utilizamos o dicionári para isso, definimos
            # A variável user que recebe um objeto para criação da tabela e dentro definimos a chave
            # e valor, firstname=primeiro_nome recebe o nome que o usuário digitou no input do formulário e com isso, iremos cadastrar no banco de dados.
            user = User.objects.create_user(
                first_name=primeiro_nome,
                last_name=ultimo_nome,
                username=username,
                email=email,
                password=senha,
            )

            messages.add_message(request, constants.SUCCESS, 'Usuário cadastrado com sucesso!')
        except:
            return redirect('cadastro')
        
        return redirect(cadastro)
    
# Criando a view/logica de login
def logar(request):
        # Verifica se o usuário está autenticado
        #request.user: representa o usuário que fez a requisição
        # .is_authenticated: retorna true se o usuário estiver autenticado(logado) e false se não estiver.
        # redirect('home'): redireciona o usuário para a rota 'home', que está definida na url.py
        if request.user.is_authenticated:
            return redirect('home')
        if request.method == 'GET':
            return render(request, 'login.html')
        else:
            username = request.POST.get('username')
            senha = request.POST.get('senha')
        # authenticate: faz parte do django authentication e precisamos importar do framework, é um método
        # Ele irá verificar se o username e o password correspondem a um usuário registrado no banco de dados
        #Se forem válidas, ele retorna um objeto do usuário autenticado, se forem inválidas, ele retorna none
        user = authenticate(username=username, password=senha)
        
        # Se forem válidas, user retornará um objeto como true e irá realizar o login, se não irá para o else
        if user:
            # Precisamos importar também o login do django.contribs.auth
            # O login(request, user) que autentica o usuário na sessão.
            login(request, user)
            return redirect('home/')
        # Se user retornar none, irá se executado o else
        else:
            messages.add_message(request, constants.ERROR, 'Usuário ou senha inválidos')
            return redirect('login')
def home(request):
    # Se o usuário estiver autenticado, passamos o nome dele para o template
    if request.user.is_authenticated:
        nome = request.user.first_name
        return render(request, 'home.html', {'nome': nome})
    return render(request, 'home.html')

def sair(request):
    logout(request)
    return redirect('/')


    # Esse fluxo segue o padrão MVT (Model-View-Template) do Django:
    # - Model: Gerencia os dados no banco de dados.
    # - View: Lida com a lógica da requisição e resposta.
    # - Template: Exibe a interface para o usuário.