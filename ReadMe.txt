Como salvar os registros de Tópicos em arquivos .bag e lê-los


    1. Escolher o tópico que você quer guardar:

        rostopic list -v 

        Será listado os tópicos, escolha os quais quer acompanhar, copie para algum
        outro lugar para não ter que o digitar um zilhão de vezes

    2. Gravar os dados dos tópicos que escolheu:

        rosbag record -O subset <topico01> <topico02> ... <topico1000> -O <NOME>.bag -l <*>

        * = numero maximo de dados a serem capturados antes de record fechar
        Obs: também é possível usar -d <tempo_max_em_seg>, mas não funcionou na minha maquina
        A gravação será feita no diretorio em que é executado o comando acima

    3. PlayBack dos dados gravados nos arquivos .bag com saída em multiplos terminais

        Para abrir novas abas no terminal (Ubuntu) use Ctrl+Shift+T 

        a. Inicie na aba 01 do Terminal:

            roscore

        b. Na aba 02 do Terminal execute:

            rostopic echo <Nome_Do_Tópico> | tee <Nome_Do_Arquivo_espelho>.yaml

            Faça isso novamente para cada tópico que estiver acompanhando.        
        
        c. Numa nova aba do Terminal, execute:

            rosbag play --immediate <NOME>.bag --topics <topico01> <topico02> ... <topico1000>
        
        d. Os arquivos .yaml podem ser abertos com o VScode facilmente.







