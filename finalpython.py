from tkinter import *
from tkinter.ttk import * 
from mysql.connector import * 
from mysql.connector import Error
from tkinter.messagebox import *

app = Tk()
app.geometry('800x500')
app.config(bg='#00222d')
colunas = ('idcliente','nomecli','dataclient','sexclient','ciddclient')
lisb= Treeview(app, columns=colunas, show='headings')
lisb.place(relx=0.05,rely=0.15,relheight=0.7,relwidth=0.8)

lisb.column('idcliente', width=50)
lisb.column('nomecli', width=150)
lisb.column('dataclient', width=120)
lisb.column('sexclient', width=75)
lisb.column('ciddclient', width=75)

lisb.heading('idcliente', text='Id')
lisb.heading('nomecli', text='Nome')
lisb.heading('dataclient', text='Data de Nascimento')
lisb.heading('sexclient', text='Sexo')
lisb.heading('ciddclient', text='Cidade')



con = connect(
    host= 'localhost',
    database = 'colegio',
    user = 'root',
    password=''
)
consulta_sql = 'SELECT * FROM cliente'
cursor = con.cursor()
cursor.execute(consulta_sql)
linhas = cursor.fetchall() #lista em ordem das rows
print('numero de registros retornados:', cursor.rowcount)
print()
for linha in linhas:
    listainsert = [linha[0],linha[1],linha[2],linha[3],linha[4]]
    lisb.insert('',END, values=listainsert)


entnom = Entry(app)
entnom.place(relx=0.05,rely=0.06)
lbnom = Label(app,text='Nome', font=('Stencil', 12),background='#00222d',foreground='white')
lbnom.place(relx=0.1,rely=0.01)

entdata = Entry(app)
entdata.place(relx=0.25,rely=0.06)
lbnom = Label(app,text='Idade', font=('Stencil', 12),background='#00222d',foreground='white')
lbnom.place(relx=0.3,rely=0.01)

entsex = Combobox(app)
entsex['values'] = ['Feminino','Masculino']
entsex.place(relx=0.45,rely=0.06)
lbnom = Label(app,text='Sexo', font=('Stencil', 12),background='#00222d',foreground='white')
lbnom.place(relx=0.5,rely=0.01)

entcidd = Combobox(app)
entcidd['values'] = ['Venancio Aires','Chapecó','São Paulo','Dallas']
entcidd.place(relx=0.65,rely=0.06)
lbnom = Label(app,text='Cidade', font=('Stencil', 12),background='#00222d',foreground='white')
lbnom.place(relx=0.7,rely=0.01)

def inserir():
    try:
        nome = str(entnom.get())
        data = str(entdata.get())
        if entsex.get() == 'Masculino':
            sexo = 1
        else:
            sexo= 2
        if entcidd.get() == 'Venancio Aires':
            cidade = 1
        elif entcidd.get() == 'Chapecó':
            cidade = 2
        elif entcidd.get() == 'São Paulo':
            cidade = 3
        elif entcidd.get() == 'Dallas':
            cidade = 4
        
        cursor.execute(f'INSERT INTO cliente (nomeCliente, dataNascimentoCliente, idSexo, idCidade) VALUES ("{nome}", "{data}", {sexo}, {cidade}) ')
        idclient= cursor.lastrowid
        lisb.insert("", END, values=(idclient,nome,data,sexo,cidade))
        showinfo(message='Dados inseridos com sucesso')
    except:
        showerror(message='Verifique se todos os campos estão preenchidos corretamente')
    finally:
        entnom.delete(0,END)
        entdata.delete(0,END)
        entsex.delete(0,END)
        entcidd.delete(0,END)
        con.commit()

def deletar():
    try:
        selecionado = lisb.selection()[0]
        idsel = lisb.item(selecionado)["values"][0]
        cursor.execute(f"DELETE FROM cliente WHERE idCliente = {idsel}")
        showinfo(message='Dados deletados com sucesso')
    except:
        showerror(message='Verifique se todos os campos estão preenchidos corretamente')
    finally:

        con.commit()
    
    lisb.delete(selecionado)


def update():
    nome = str(entnom.get())
    data = str(entdata.get())
    if entsex.get() == 'Masculino':
        sexo = 1
    else:
        sexo= 2
    if entcidd.get() == 'Venancio Aires':
        cidade = 1
    elif entcidd.get() == 'Chapecó':
        cidade = 2
    elif entcidd.get() == 'São Paulo':
        cidade = 3
    elif entcidd.get() == 'Dallas':
        cidade = 4
    try:
        selecionado = lisb.selection()[0]
        idsel = lisb.item(selecionado)["values"][0]
        lisb.item(selecionado,values=(idsel,nome,data,sexo,cidade))

        cursor.execute(f'UPDATE cliente SET nomeCliente = "{nome}" WHERE idCliente = {idsel}')
        cursor.execute(f'UPDATE cliente SET dataNascimentoCliente = "{data}" WHERE idCliente = {idsel}')
        cursor.execute(f'UPDATE cliente SET idSexo = "{sexo}" WHERE idCliente = {idsel}')
        cursor.execute(f'UPDATE cliente SET idCidade = "{cidade}" WHERE idCliente = {idsel}')
        showinfo(message='Dados atualizados com sucesso')
    except:
        showerror(message='Verifique se todos os campos estão preenchidos corretamente')
    finally:
        
        entnom.delete(0,END)
        entdata.delete(0,END)
        entsex.delete(0,END)
        entcidd.delete(0,END)
        con.commit()

btdel = Button(app, text="Deletar", command=deletar)
btdel.place(relx=0.87,rely=0.35,relheight=0.1)

btins = Button(app, text="Inserir", command=inserir)
btins.place(relx=0.87,rely=0.15,relheight=0.1)

btdel = Button(app, text="Update", command=update)
btdel.place(relx=0.87,rely=0.55,relheight=0.1)































mainloop()