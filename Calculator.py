import tkinter as tk

expresion = ""
resultadoMostrar = False

def button_pressed(valor):
    global expresion, resultadoMostrar
    if resultadoMostrar:
        if valor in "+-*/.":
            resultadoMostrar = False
        else:
            expresion = ""
            texto_variable.set(expresion)
            resultadoMostrar = False

    if valor == "C":
        expresion = ""
        texto_variable.set(expresion)
        resultadoMostrar = False
    else:
        expresion += str(valor)
        if str(expresion[0]) in "+-./*":
            expresion = ""
            texto_variable.set(expresion)
        texto_variable.set(expresion)

def calcular(expresion):
    resultado = eval(expresion)
    if resultado == int(resultado):
        resultado = int(resultado)
    return resultado

def equal_presed():
    global expresion, resultadoMostrar
    if expresion == "":
        return
    try:  
        resultado = calcular(str(expresion))
        expresion = str(resultado)
        resultadoMostrar = True
        texto_variable.set(resultado)

    except Exception:
        expresion = ""
        texto_variable.set("Error")


NewWindow = tk.Tk()

NewWindow.title("Calculator")
NewWindow.geometry("400x600")
NewWindow.minsize(400,300)
NewWindow.maxsize(1200,800)
NewWindow.configure(background='white')

for i in range(4):
    NewWindow.grid_columnconfigure(i, weight=1)

for i in range(6):
    NewWindow.grid_rowconfigure(i, weight=1)

texto_variable = tk.StringVar()
entry = tk.Entry(NewWindow, textvariable=texto_variable, font=('Helvetica', 24), bd=10, insertwidth=4, width=14, borderwidth=4, justify='right', 
    highlightthickness=2, highlightbackground="#1E3A8A", highlightcolor="#9B59B6",)
entry.grid(row=0, column=0, columnspan=4, sticky="nsew", pady=6, padx=6)

botones = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("C", 4, 2), ("+", 4, 3)
]

for i in range(len(botones)):
    
    valor = botones[i][0]

    if valor in "*+-/":
        color = "#9B59B6"
        fg = 'white'
    elif valor in "C.":
        color = "#1E3A8A"
        fg = 'white'
    else:
        color = "lightblue"
        fg = "black"

    boton = tk.Button(NewWindow, text=botones[i][0], font=('Helvetica', 20, 'bold'), command= lambda valor = botones[i][0]  : button_pressed(valor), 
        background=color, fg=fg, highlightthickness=3, highlightbackground="#cccccc")
    boton.grid(row=botones[i][1], column=botones[i][2], sticky="nsew", padx=3, pady=3) #sticky=nsew se expande en todas las direcciones, padx y pady espacio entre botones
    #sticky → cuánto del espacio ocupa el botón: n = arriba, s = abajo, e = derecha, w = izquierda. El grid reparte el espacio según weight

botonEqual = tk.Button(NewWindow, text="=", font=('Helvetica', 20, "bold"), command=equal_presed, background="#BDECB6", fg='black', highlightthickness=3, highlightbackground="#cccccc")
botonEqual.grid(row=5, column=0, columnspan=4, sticky="nsew", padx=3, pady=3, )



NewWindow.mainloop()