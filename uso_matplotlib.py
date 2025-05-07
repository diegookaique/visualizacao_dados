import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('C:/Users/kaiqu/OneDrive/Área de Trabalho/Ciência de Dados/clientes-v3-preparado.csv')
print(df.head(20).to_string())

# Gráfico de Barras
plt.figure(figsize=(10, 6))
df['nivel_educacao'].value_counts().plot(kind='bar', color='#90ee70')  # Link na descrição
plt.title('Divisão de Escolariedade -1')
plt.xlabel('Nível de Educação')
plt.ylabel('Quantidade')
plt.xticks(rotation=0)
plt.show()  # Exibe o Gráfico

x = df['nivel_educacao'].value_counts().index
y = df['nivel_educacao'].value_counts().values

plt.figure(figsize=(10, 6))
plt.bar(x, y, color='#60aa65')
plt.title('Divisão de Escolariedade - 2')
plt.xlabel('Nível de Educação')
plt.ylabel('Quantidade')

# Gráfico de pizza
plt.figure(figsize=(10, 6))
plt.pie(y, labels=x, autopct='%.1f%%', startangle=90)
plt.title('Distribuição de Nível de Educação')
plt.show()  # Exibe o Gráfico

# Gráfico de dispersão
plt.hexbin(df['idade'], df['salario'], gridsize=40, cmap='Blues')  # Link na descrição
plt.colorbar(label='Contagem dentro do bin')
plt.xlabel('Idade')
plt.ylabel('Salário')
plt.title('Dispersão de Idade e Salário')
plt.show()  # Exibe o Gráfico
