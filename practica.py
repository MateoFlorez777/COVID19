import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv("COVID19-JULIO2020.csv",low_memory=False)
print(data.shape)
data.info()
cols_cat=['PAIS','CIUDAD','SEXO','TIPO','ESTADO','ATENCION' ,'DEPARTAMENTO']
for col in cols_cat:
    print(f'Columna {col}: {data[col].nunique()} subniveles')
print(data['PAIS'].unique())

# GENERAR DIMENSION ESTADO

DM_ESTADO=pd.DataFrame(data['ESTADO'])
DM_ESTADO.drop_duplicates(inplace=True)
data=data.replace(["leve"], "Leve")
DM_ESTADO=pd.DataFrame(data['ESTADO'])
DM_ESTADO.drop_duplicates(inplace=True)
data['ESTADO'].fillna('NA',inplace=True)
DM_ESTADO=pd.DataFrame(data['ESTADO'])
DM_ESTADO.drop_duplicates(inplace=True)
DM_ESTADO.columns=DM_ESTADO.columns.str.replace('ESTADO','NOMBRE')
DM_ESTADO["IDESTADO"]=range(1,len(DM_ESTADO)+1)
data = pd.merge(DM_ESTADO,data,left_on="NOMBRE",right_on="ESTADO",how="right")

DM_ESTADO=DM_ESTADO[['IDESTADO','NOMBRE']]

#eliminar del dataset la columna ESTADO y NOMBRE

del data['ESTADO']
del data['NOMBRE']

# GENERAR DIMENSION ATENCION


DM_ATENCION=pd.DataFrame(data['ATENCION'])
DM_ATENCION.drop_duplicates(inplace=True)
data['ATENCION'].fillna('VACIO', inplace=True)
DM_ATENCION=pd.DataFrame(data['ATENCION'])
DM_ATENCION.drop_duplicates(inplace=True)

DM_ATENCION["IDATENCION"]=range(1,len(DM_ATENCION)+1)
DM_ATENCION.columns=DM_ATENCION.columns.str.replace('ATENCION','NOMBRE')
DM_ATENCION.columns=DM_ATENCION.columns.str.replace('IDNOMBRE','IDATENCION')
data = pd.merge(DM_ATENCION,data,left_on="NOMBRE",right_on="ATENCION",how="right")

DM_ATENCION=DM_ATENCION[['IDATENCION','NOMBRE']]

#eliminar del dataset la columna ATENCION y NOMBRE

del data['ATENCION']
del data['NOMBRE']

print(DM_ATENCION)

# GENERAR DIMENSION PAIS

# data['PAIS']=data.replace(["leve","Leve"])
data['PAIS'].fillna('COLOMBIA', inplace=True)
DM_PAIS=pd.DataFrame(data['PAIS'])
DM_PAIS.drop_duplicates(inplace=True)
data['PAIS']=data['PAIS'].replace(["ESTADOS UNIDOS DE AMÉRICA"], "ESTADOS UNIDOS")
data['PAIS']=data['PAIS'].replace(["ESTADOS UNIDOS DE AMERICA"], "ESTADOS UNIDOS")
data['PAIS']=data['PAIS'].replace(["PANAMÁ"], "PANAMA")
data['PAIS']=data['PAIS'].replace(["PERÚ"], "PERU")
data['PAIS']=data['PAIS'].replace(["MÉXICO"], "MEXICO")
data['PAIS']=data['PAIS'].replace(["CANADÁ"], "CANADA")

DM_PAIS=pd.DataFrame(data['PAIS'])
DM_PAIS.drop_duplicates(inplace=True)


DM_PAIS["IDPAIS"]=range(1,len(DM_PAIS)+1)
DM_PAIS.columns=DM_PAIS.columns.str.replace('PAIS','NOMBRE')
DM_PAIS.columns=DM_PAIS.columns.str.replace('IDNOMBRE','IDPAIS')

data = pd.merge(DM_PAIS,data,left_on="NOMBRE",right_on="PAIS",how="right")

DM_PAIS=DM_PAIS[['IDPAIS', 'NOMBRE']]

#eliminar del dataset la columna NOMBRE Y PAIS

del data['NOMBRE']
del data['PAIS']

# GENERAR DIMENSION CIUDAD

DM_CIUDAD=pd.DataFrame(data[['DIVIPOLA', 'CIUDAD']])
DM_CIUDAD.drop_duplicates(inplace=True)

#DM_CIUDAD["IDCIUDAD"]=range(1,len(DM_CIUDAD)+1)
del data['CIUDAD']
DM_CIUDAD.columns=DM_CIUDAD.columns.str.replace('CIUDAD','NOMBRE')
DM_CIUDAD.columns=DM_CIUDAD.columns.str.replace('DIVIPOLA','IDCIUDAD')
data.columns=data.columns.str.replace('DIVIPOLA','IDCIUDAD')

# GENERAR DIMENSION DEPARTAMENTO


DM_DEPARTAMENTO=pd.DataFrame(data[['IDCIUDAD','DEPARTAMENTO']])
DM_DEPARTAMENTO['IDDPTO']=DM_DEPARTAMENTO['IDCIUDAD']//1000
DM_DEPARTAMENTO.drop_duplicates(inplace=True)
del DM_DEPARTAMENTO['IDCIUDAD']
data['IDDPTO']=data['IDCIUDAD']//1000

#eliminar del dataset la columna DEPARTAMENTO

del data['DEPARTAMENTO']
DM_DEPARTAMENTO.columns=DM_DEPARTAMENTO.columns.str.replace('DEPARTAMENTO','NOMBRE')
DM_DEPARTAMENTO=DM_DEPARTAMENTO[['IDDPTO','NOMBRE']]

# GENERAR DIMENSION TIPO
DM_TIPO=pd.DataFrame(data[['TIPO']])
DM_TIPO.drop_duplicates(inplace=True)
data['TIPO']=data['TIPO'].replace(["RELACIONADO"], "Relacionado")
data['TIPO']=data['TIPO'].replace(["relacionado"], "Relacionado")
data['TIPO']=data['TIPO'].replace(["En Estudio"], "En estudio")

DM_TIPO=pd.DataFrame(data[['TIPO']])
DM_TIPO.drop_duplicates(inplace=True)
DM_TIPO.columns=DM_TIPO.columns.str.replace('TIPO','NOMBRE')

DM_TIPO['IDTIPO']=range(1,len(DM_TIPO)+1)
data=pd.merge(DM_TIPO,data,left_on='NOMBRE',right_on='TIPO', how="right")

DM_TIPO=DM_TIPO[['IDTIPO','NOMBRE']]

#eliminar del dataset la columna NOMBRE Y TIPO

del data['NOMBRE']
del data['TIPO']


#GENERAR DIMENSION FECHA 

data['FECHA']=pd.to_datetime(data['FECHA'])
DM_FECHA=pd.DataFrame(data['FECHA'].dt.strftime("%Y-%m-%d"))
DM_FECHA['MES']=data['FECHA'].dt.strftime("%m")
DM_FECHA['ANUAL']=data['FECHA'].dt.strftime("%Y")
DM_FECHA['DIA']=data['FECHA'].dt.strftime("%d")
DM_FECHA.drop_duplicates(inplace=True)
DM_FECHA.columns=DM_FECHA.columns.str.replace('FECHA','NOMBRE')

DM_FECHA['IDFECHA']=range(1,len(DM_FECHA)+1)
DM_FECHA=DM_FECHA[['IDFECHA','NOMBRE', 'ANUAL', 'MES', 'DIA']]

# CATEGORIZAR UNA COLUMNA

rangos= [0,5,10,17,59,100,110]
nombre=['BEBE','NIÑO','ADOLESCENTE','ADULTO','ADULTO MAYOR','ADULTO MUY MAYOR']
data['GEDAD']=pd.cut(data['EDAD'],rangos,labels=nombre)
del data['FECHA']
data1=data[['ID','IDPAIS','IDESTADO','IDTIPO','IDATENCION','IDDPTO','IDCIUDAD','EDAD','SEXO']]


#GENERAR ARCHIVOS .CSV

DM_PAIS.to_csv("DM_PAIS.csv",index=False)
DM_ESTADO.to_csv("DM_ESTADO.csv",index=False)
DM_ATENCION.to_csv("DM_ATENCION.csv",index=False)
DM_CIUDAD.to_csv("DM_CIUDAD.csv",index=False)
DM_DEPARTAMENTO.to_csv("DM_DEPARTAMENTO.csv",index=False)
DM_TIPO.to_csv("DM_TIPO.csv",index=False)
DM_FECHA.to_csv("DM_FECHA.csv",index=False)
data.to_csv("THCOVID.csv",index=False)


print(DM_ESTADO)