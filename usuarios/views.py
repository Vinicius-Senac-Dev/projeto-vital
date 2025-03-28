from django.shortcuts import render, redirect

#Criamos as views, nossas funções que receberam dados do banco de dados e é responsável por intermedia esses dados, processar a requisição e, se necessário, buscando dados no banco por meio da Model.
#Criamos a view cadastro, que é responsável por lidar com as requisições feitas à rota de cadastro e passamos como parâmetro a requisição
#A view pode tanto buscar os dados do banco quanto processar os dados enviados pelo usuário antes de enviá-los ao template
def cadastro(request):
    #Se a requisição for do método get, retorne a renderização da página cadastro.html, ou seja, a view recebe a requisição e depois de verificar o tipo de requisição ou método, chama/encaminha para a página cadastro.html. # Isso significa que, quando o usuário acessar a rota de cadastro, o Django irá processar a requisição
    # e carregar o template 'cadastro.html' para exibição na tela. 
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == "GET":
        return render(request, 'cadastro.html')
    else:
        primeiro_nome = request.POST.get('primeiro_nome')
        ultimo_nome = request.POST.get('ultimo_nome')
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        if not senha == confirmar_senha:
            return redirect('cadastro')
        if len(senha) < 6:
            return redirect('cadastro')
        
        try:
            #username deve ser único!
            user = User.objects.create_user(
                first_name=primeiro_nome,
                last_name=ultimo_nome,
                username=username,
                email=email,
                password=senha,
            )
        except:
            return redirect('cadastro')
        
        return redirect(cadastro)
    

    # Esse fluxo segue o padrão MVT (Model-View-Template) do Django:
    # - Model: Gerencia os dados no banco de dados.
    # - View: Lida com a lógica da requisição e resposta.
    # - Template: Exibe a interface para o usuário.