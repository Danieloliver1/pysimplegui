
import PySimpleGUI as sg                        # Part 1 - The import

 #Definir o conteúdo da janela
# class Layout:
#     sg.theme('DarkAmber')   # Add a touch of color
    
        
#     def layout1(self):   
#         layout = [  [sg.Text("What's your name?")],     # Part 2 - The Layout
#                     [sg.Input()],
#                     [sg.Output()],
#                     [sg.Text('col Row 2'), sg.Input('col input 1')],
#                     [sg.Button('Ok')] ]
#         return layout

#     def criarjanela(self):
#     # Criar a janela
#         window = sg.Window('Window Title', layout = self.layout1())      # Part 3 - Window Defintion
#         # Exibir e interagir com a Janela
        
#         event, values = window.read()  
#         # Faça algo com as informações coletadas
#         print('Hello', values[0], "! Thanks for trying PySimpleGUI")
#         return window    
    
# # Exibir e interagir com a Janela
# window = Layout().criarjanela()
# event, values = window.read()                   # Part 4 - Event loop or Window.read call

# # Faça algo com as informações coletadas
# print('Hello', values[0], "! Thanks for trying PySimpleGUI")

# Termine removendo da tela
# window = Layout().criarjanela().close()
# window.close()                                  # Part 5 - Close the Window














class Janela:
    
    sg.theme('DarkAmber')
      
    # def __init__(self,layout_direita,layout_esquerda,layout,janela):
        
    #      self.layout_direita =layout_direita
    #      self.layout_esquerda = layout_esquerda
    #     self.layout =layout
    #     self.janela =janela
        
    def layout_esquerda(self):
        
        Layout_esquerda = [
            [sg.StatusBar('Informações pessoais', font = ['Arial', 12])],
            [sg.Text('Nome completo'),sg.InputText(key='Nome',p=(0,0))],
            [sg.Text('Naturalidade'), sg.InputText(key='Naturalidade',p=(20,0),s=(20))],
            [sg.Text('Data de Nascimento'),sg.InputText( key='Data_nasc',p=(5,0),s=(10))],
            [sg.StatusBar('Endereço', font = ['Arial', 12])],
            [sg.Text('CEP')],
            [sg.InputText(key='CEP',s=15),
             sg.Button('atualizar',key='CEP_Atualiza'),
             sg.Text('Cidade:'),sg.Text(key='Cidade',s=9),
             sg.Text('Estado:'),sg.Text(key='Uf')], 
            [sg.Text('Bairro:'),sg.Text(key='Bairro',),
             sg.Text('Rua:'),sg.Text(key='Rua',),
             sg.Text('Número da casa:'),
             sg.Combo(values=list(range(9000)),key='Numero_da_casa',)],
            [sg.Text('E-mail')],
            [sg.InputText(key='Email')],
            [sg.Text('Telefone')],
            [sg.InputText( key='Telefone' )],
            #Atribuindo Pefil do curriculo
            [sg.Text('Seu Perfil Profissional')],
            [sg.Multiline(key='Texto_Perfil',s=(45,3))],     
      #Atribuindo Formação       
            [sg.StatusBar('FORMAÇÃO', font = ['Arial', 12])],
            [sg.Text('Sua Formação Profissional')],
            [sg.Multiline(key='Texto_Formatacao',s=(45,3))],
         #Atribuindo Experiencia 
            [sg.StatusBar('EXPERIÊNCIA', font = ['Arial', 12])],
            [sg.Text('Sua Experiência Profissional')],
            [sg.Multiline(key='Texto_Experiencia',s=(45,3))],           
            [sg.Button('Ok'),sg.Button('Cancel'),sg.Button('Imprimir')],
]  
        return Layout_esquerda
        
        
    def layout_direita(self):
        
        Layout_direita = [
                [sg.Output(size=(50,30))]
        ] 
        return Layout_direita
        
        
    def windows_layout(self): 
           
        layout = [
            [sg.Column(self.layout_esquerda(),size=(400,750)),sg.VSeparator(),sg.Column(self.layout_direita(),size=(400,750))]   
          ]   
        return layout 
        
    def windows(self):           
        janela = sg.Window('Window Title', self.windows_layout()) 
        while True:      
            eventos, valores  = janela.read()
            if eventos == sg.WIN_CLOSED or eventos == 'Cancel': # if user closes window or clicks cancel
                break
        janela.close()
        
        return janela
    
    
    
    
wind = Janela().windows()

# eventos, valores = wind.read()

# wind.close()