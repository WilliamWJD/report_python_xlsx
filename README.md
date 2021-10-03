<h1 align="center">Report Python</h1>
<p align="center">Relatório de vendas por unidade</p>


## 💻 O Projeto
O objetivo do projeto é gerar um relatório a partir de um arquivo xlsx, esse relatório irá ler a planilha e calcular o faturamento por loja, a quantidade vendida por loja e o ticket médio por loja, após isso será enviado um e-mail com esse relatório no corpo.

## ☕ Funcionalidades
- Leitura de arquivo xlsx
- Calculo de faturamento por loja
- Calculo da quantidade vendida por loja
- Caculo do ticket médio por Loja
- Envio de e-mail com o relatório.

## :pushpin: Tecnologias
Projeto desenvolvido com as seguintes tecnologias:
- [Python](https://www.python.org/)

## 🚀 Execução do projeto
1. Crie um arquivo `.env` seguindo o modelo do .env.example, colocando a senha de e-mail do remetente
2. Utilize uma conta `gmail` ou modifique a variável `smtp` e sua porta.
3. Em `MeuArquivo.py` modifique a variável `email_to` colocando o e-mail do destinatário
4. Pronto, basta rodar o projeto. Devido ao tamanho da planilha o script pode demorar um pouco para ser executado.


## 🤔 Como contribuir

- Faça um fork desse repositório;
- Cria uma branch com a sua feature: `git checkout -b minha-feature`;
- Faça commit das suas alterações: `git commit -m 'feat: Minha nova feature'`;
- Faça push para a sua branch: `git push origin minha-feature`.


## :memo: Licença

Esse projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE.md) para mais detalhes.

---

Desenvolvido por [William José Dias!](https://github.com/WilliamWJD)
