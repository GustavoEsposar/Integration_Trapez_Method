import tkinter as tk
from PIL import ImageTk, Image
import calculo as calc

class janelaApp:
    def janelaIniciar(self):
        root = tk.Tk()
        root.geometry("500x150")
        root.title("Interação Númerica")
        
        
        frameIntegral = tk.Frame(root, width=50, height=60, bg="white")
        frameIntegral.grid(row=0, column=0, sticky="nsew", padx=20, pady=0)
        
        
        labelValorA = tk.Label(frameIntegral, text="Valor de A:")
        labelValorA.grid(row=4, column=0, sticky="nsew")
        
        entryValorA = tk.Entry(frameIntegral)
        entryValorA.grid(row=5, column=0, sticky="nsew")
        
        labelValorB = tk.Label(frameIntegral, text="Valor de B:")
        labelValorB.grid(row=0, column=0, sticky="nsew")
        
        entryValorB = tk.Entry(frameIntegral)
        entryValorB.grid(row=1, column=0, sticky="nsew")
        
        img = Image.open("kisspng-integral-symbol-mathematics-calculus-5b37d73b4b71e3.046853161530386235309.png")
        resized = img.resize((60, 50), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(resized)
        
        canvasIntegral = tk.Label(frameIntegral, image=photo)
        canvasIntegral.grid(row=2, column=0, sticky="nsew")
        
        frameFuncao = tk.Frame(root, width=300, height=60)
        frameFuncao.grid(row=0, column=1, sticky="nsew", padx=0, pady=0)
        
        labelFuncao = tk.Label(frameFuncao, text="Função:")
        labelFuncao.grid(row=0, column=0, sticky="nsew", pady=(20,0))
        
        entryFuncao = tk.Entry(frameFuncao, width=38)
        entryFuncao.grid(row=0, column=1, padx=0, pady=(20,0))
        
        labelNCasas = tk.Label(frameFuncao, text="Nº de Casas:")
        labelNCasas.grid(row=1, column=0, sticky="nsew", pady=(10,0))
        
        entryNCasas = tk.Entry(frameFuncao, width=5)
        entryNCasas.grid(row=1, column=1, padx=0, pady=0, sticky='we')
        
        labelNTrapezios = tk.Label(frameFuncao, text="Nº de Trapézios:")
        labelNTrapezios.grid(row=3, column=0, sticky="nsew", pady=(10,0))
        
        entryNTrapezios = tk.Entry(frameFuncao, width=5)
        entryNTrapezios.grid(row=3, column=1, padx=0, pady=0, sticky='we')
        
        botaoCalcular = tk.Button(frameFuncao, text="Calcular", command=lambda: [self.janelaRespota(entryValorA.get(), entryValorB.get(), entryNTrapezios.get(), entryNCasas.get(), entryFuncao.get())])
        botaoCalcular.grid(row=4, column=0, columnspan=2, sticky="nsew", pady=(10,0))
        
        root.mainloop()
        
    def janelaRespota(self, a, b, t, c, input):
        
        janelaResposta = tk.Toplevel()
        
        resposta = calc.calculos.calcular(a, b, t, c, input)
        
        labelResposta = tk.Label(janelaResposta, text=resposta)
        labelResposta.grid(row=0, column=0, sticky="nsew")
        pass

        
pipipupu = janelaApp()
pipipupu.janelaIniciar()
    
    
    
