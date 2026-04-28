import customtkinter as ctk
from PIL import Image
from banco import get_dados_residuos
import tkinter as tk


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.dados = get_dados_residuos()

        self.title("RECICLAGEM CONSCIENTE")
        self.wm_resizable(False,False)
        ctk.set_appearance_mode("light")
        self.geometry('720x950')
        self.configure(fg_color='#f0f7f0')

        imagem_original = Image.open("image.jpg") 
        self.bg_image = ctk.CTkImage(light_image=imagem_original,dark_image=imagem_original, size=(720, 950))

        self.bg_label = ctk.CTkLabel(self, image=self.bg_image, text='')
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)



        frame = ctk.CTkFrame(self,corner_radius=10, fg_color='#ffffff')
        frame.pack(fill="both", expand=True, padx=90, pady=90)

        img = ctk.CTkImage(Image.open('reciclagem.png'), size=(60,60))
        self.emoji = ctk.CTkLabel(frame, image=img, text='')
        self.emoji.pack(pady=(40,40))

        

        self.label1 = ctk.CTkLabel(frame, text="RECICLAGEM", text_color="#075C0E",font=('Georgia Bold', 20))
        self.label1.pack(padx=5)

        self.label2 = ctk.CTkLabel(frame, text="CONSCIENTE", text_color="#86BE8A")
        self.label2.pack(pady=(10,50))

        self.label3 = ctk.CTkLabel(frame, text="O que você quer descartar?", text_color="#1D1D1D")
        self.label3.pack(pady=(40,10))

        self.entrada = ctk.CTkEntry(frame, placeholder_text="", width = 355, height= 60,)
        self.entrada.pack(pady=(10, 20))

        self.botao = ctk.CTkButton(frame, text="VERIFICAR", command=self.tratar_entrada, width= 355, height= 70, fg_color="#0A8F15", hover_color="#17401B")
        self.botao.pack(pady=(10,40))

        self.resultado_label = ctk.CTkLabel(frame,text="",font=("Arial", 14), wraplength=500)
        self.resultado_label.pack(pady=20)

    
         

    def tratar_entrada(self):
         item_digitado = self.entrada.get().lower().strip()

         if item_digitado in self.dados:
             categoria = self.dados[item_digitado]
             mensagem = f"{item_digitado.upper()}: {categoria}"
             self.resultado_label.configure(text=mensagem, text_color="green")
             print(f"Item encontrado: {item_digitado} - {categoria}")
         else:
            mensagem = f" {item_digitado} não encontrado no sistema de reciclagem!"
            self.resultado_label.configure(text=mensagem, text_color="red")
            print(f"Item não encontrado: {item_digitado}")

app = App()
app.mainloop()