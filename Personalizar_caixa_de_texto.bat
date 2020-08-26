@ECHO.
@ECHO ...............................................
@ECHO Este batch permite a instalacao automatica 
@ECHO da caixa de texto escolhida para o jogo.
@ECHO ...............................................
@ECHO.
@ECHO 1 - Caixa de Texto Padrao (fundo marrom). 
@ECHO 2 - Caixa de Texto com borboletas no fundo.
@ECHO 3 - Caixa de Texto transparente com logo.
@ECHO 4 - Caixa de Texto transparente sem logo.
@ECHO 5 - Sair
@ECHO.

@SET /P M=Escolha sua opcao e pressione ENTER:
IF %M%==1 unzip textbox1.zip
IF %M%==2 unzip textbox2.zip
IF %M%==3 unzip textbox3.zip
IF %M%==4 unzip textbox4.zip
IF %M%==5 exit
pause