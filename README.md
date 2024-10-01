<h1 align="center">AlphaTech Educacional <img src="https://github.com/user-attachments/assets/47d54f58-3607-488c-9df2-8646c6bfe1fe" alt="Descrição da imagem" width="30"/></h1> 

O AlphaTech Educacional será um portal acadêmico inovador, projetado para oferecer uma plataforma completa para instituições de ensino e alunos. O objetivo é facilitar o acesso a conteúdos educacionais, matrículas, notas e acompanhamento de desempenho acadêmico. Através de uma interface amigável e intuitiva, alunos poderão acessar recursos de aprendizado, realizar avaliações e monitorar seu progresso. Instituições poderão gerenciar turmas, cursos e materiais de forma centralizada, oferecendo uma experiência de ensino mais eficiente e personalizada para todos os envolvidos.

## Como usar?

## ⚙️ Requisitos
Python 3.6 ou superior.

## Links 
-  [Projeto - Jira](https://cesar-team-c925b8yd.atlassian.net/jira/software/projects/AW/boards/5?atlOrigin=eyJpIjoiOGQyNjQxNmVlNzYxNDUzNmEwMDA5Y2Y4YTZiMmVkMmEiLCJwIjoiaiJ9)
-  [Protótipo Lo-Fi & Sketchboard - Figma](https://www.figma.com/design/7uEuFDZ5T9I2HeTYMGfnR9/FDS-Entrega-1?node-id=0-1&t=nimLCI6xdHeemn50-1)
## Configuração do ambiente

## Entregas

* Entrega 1
    -  [Print do Backlog das histórias](Backlog.md)
    -  [Screencast do Protótipo Lo-Fi](https://youtu.be/NCyXO3E3Ow8)
    -  [Protótipo Lo-Fi & Sketchboard - Figma](https://www.figma.com/design/7uEuFDZ5T9I2HeTYMGfnR9/FDS-Entrega-1?node-id=0-1&t=nimLCI6xdHeemn50-1)
    -  [ Quadro da Sprint 1 inicializada](Quadro.md)

 * Entrega 2
  <p>Links:</p>
   <ul>
  <li>
    <a  href="https://cesar-team-c925b8yd.atlassian.net/jira/software/projects/AW/boards/5?atlOrigin=eyJpIjoiOGQyNjQxNmVlNzYxNDUzNmEwMDA5Y2Y4YTZiMmVkMmEiLCJwIjoiaiJ9"
      >Projeto - Jira</a>
  </li>
    <li>
    <a  href="https://www.figma.com/design/7uEuFDZ5T9I2HeTYMGfnR9/FDS-Entrega-1?node-id=0-1&t=nimLCI6xdHeemn50-1"
      >Protótipo Lo-Fi & SketchBoard Figma</a>
  </li>
   <li>
    <a  href=""
      >Screencast - Entrega 02</a>
  </li>
</ul>
<br/>

Deployment das histórias produzidas:
<ul>
  <li>
    <a  href=""
      >Projeto na Azure</a>
  </li>
</ul>
<br/>

**Instruções de Acesso:**

Essa sessão descreve as funcionalidades disponíveis atualmente no menu de navegação do portal acadêmico da AlphaTech na Azure Websites, até o momento foram implementadas apenas histórias para alunos, portanto não será disponível visualizar as histórias para outros tipo de usuários (professores) .  A página inicial do site é o Login, onde é necessário por o nome de usuário e senha, se ainda não estiver cadastrado é possível clicar em "cadastre-se" para enviar suas informações de cadastro e criar seu perfil, serão necessárias informações como:
- Matrícula
- Nome 
- Idade
- Tipo de usuário (aluno/ professor)
- Curso
- Endereço
- Período de Ingresso
- Senha

Ao cadastrar suas informações no banco de dados poderá prosseguir para a Home Page que contém uma tela de boas vindas que possui um menu de navegação lateral, que é por onde é possível ver todas as funcionalidades implementadas, atualmente são:

- Calendário
- Serviços
- Dados pessoais


Ao pressionar "Calendário", aparecerá o calendário anual, apartir de setembro de 2024, com eventos que o usuário poderá registrar e deixar salvo em seu calendário pessoal, como uma espécie de agenda, selecionando uma data, dando um título do evento e por fim clicando em "Registre um Novo Evento", para salvar essas informações no banco de dados e exibi-lo em seu Calendário. Também é possível navegar entres os meses.

Ao pressionar "serviços", o usuário será direcionado para uma pagina com 4 campos: 
- Matrícula: O campo deve ser preenchido com a matrícula do usuário;
- Tipo de Serviço: O usuário deverá selecionar uma das opções de serviço: trocar de turma, declarar matrícula, declarar imposto de renda; 
- Motivo: O campo deve ser preenchido com o motivo da solicitação;
- Descrição: O campo deve ser preenchido com os detalhes da solicitação;

Abaixo dos campos estão 2 botões:
- Enviar Solicitação: O botão, que envia a solicitação de serviço, será pressionável somente após o preenchimento de todos os campos;
- Página Principal: Direciona o usuário de volta ao home.

Ao pressionar "Dados Pessoais", o usuário será direcionado para uma página com apenas um campo pedindo a matrícula do aluno. Após digitar a matrícula, as seguintes informações serão exibidas:
- Matrícula;
- Idade;
- Tipo de usuário;
- Curso;
- Endereço;
- Período de ingresso;

**Diagrama de Atividade do Sistema:**

![Diagrama](imgdump2/diagrama-entrega-2-(3).png)

**Print do Backlog do Projeto:**
![Backlog](imgdump2/backlog-entrega-2-(3).png)

**Print do Quadro da Sprint:**
![Quadro da Sprint](imgdump2/sprint-entrega-2-(2).png)

**Relato da Programação em Par Experimentada:**
<br><br>
Este relatório tem como objetivo discutir a prática de Pair Programming aplicada ao desenvolvimento do projeto Alphatech Educational, uma plataforma baseada em Django voltada para a gestão educacional. O Alphatech Educational é projetado para atender às necessidades de instituições de ensino, oferecendo funcionalidades como cadastro de professores e estudantes, gestão de boletins e um calendário acadêmico integrado. Através do Pair Programming, buscamos melhorar a eficiência, a qualidade do código e a colaboração no desenvolvimento dessas funcionalidades, maximizando a produtividade e a inovação no projeto. Os pares foram divididos como:
<br><br>
 - Matheus Lustosa e Pedro Gusmão:
No início do desenvolvimento da funcionalidade de visualização do calendário escolar na AlphaTech Educacional, Mathues e Pedro foram encarregados de criar uma interface onde os usuários pudessem visualizar datas importantes, como início de aulas, feriados e eventos escolares. Essa tarefa envolveu o uso de tecnologias como Django para o backend e HTML/CSS para a interface. Embora os integrantes do par já tivessem alguma familiaridade com Python e HTML, eram novos em Django e Azure. Para superar essas dificuldades, buscaram apoio em aulas específicas e consultaram o professor, além de contarem com a ajuda de colegas mais experientes. Esse suporte foi essencial para esclarecer dúvidas e garantir o progresso do projeto. Durante o desenvolvimento, o par utilizou tanto o trabalho presencial quanto remoto, empregando o compartilhamento de tela do Google Meet para facilitar a colaboração. Essa dinâmica permitiu uma alternância eficaz entre codificação e revisão do código, promovendo uma abordagem mais ágil e prevenindo possíveis erros na implementação da funcionalidade de calendário.<br>
- Augusto Barbosa e Felipe Andrade:
Após a divisão de tarefas, Augusto e Felipe foram encarregados de desenvolver a funcionalidade de solicitação de serviços acadêmicos, permitindo que os alunos pudessem requisitar serviços como tutoria, orientações e emissão de documentos. Para isso, os integrantes se reuniram em uma sala remota e dividiram as atividades. Um membro ficou responsável pela criação do HTML e CSS da interface, enquanto o outro se concentrou na codificação em Django e na integração com o banco de dados na Microsoft Azure.
Com as tarefas iniciais concluídas, surgiram novas demandas, como a correção de erros e a implementação de recursos adicionais. Um dos integrantes decidiu adicionar uma funcionalidade que permitisse aos alunos visualizar o status de suas solicitações. Essa colaboração e a clara divisão de responsabilidades foram fundamentais para garantir que a funcionalidade de solicitação de serviços acadêmicos fosse desenvolvida de forma eficiente e atendessem às necessidades dos usuários.<br>
 - Arthur Xavier e Rodrigo Guimarães:
Após a divisão de tarefas, o Arthur e Rodrigo receberam a missão de desenvolver a funcionalidade que permite aos alunos visualizar seus dados pessoais, como nome, matrícula, etc. Para isso, os integrantes se organizaram em uma sala remota, dividindo as responsabilidades. Um membro focou na criação da interface usando HTML e CSS, enquanto o outro trabalhou na programação em Django e na integração com o banco de dados na Microsoft Azure.
À medida que as atividades progrediram, novas necessidades surgiram, incluindo correções e melhorias. Um dos integrantes decidiu implementar um recurso que garantisse que os alunos pudessem acessar apenas suas próprias informações, garantindo a privacidade. Essa colaboração e a definição clara de papéis foram cruciais para que a funcionalidade fosse desenvolvida de maneira eficaz e atendessem às expectativas dos usuários.



## 💻Tecnologias Utilizadas
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![Jira](https://img.shields.io/badge/jira-%230A0FFF.svg?style=for-the-badge&logo=jira&logoColor=white)
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)
## 🙋‍♂️ Criado por:
[Matheus Lustosa](https://github.com/MatheusLustosa)
[Pedro Gusmão](https://github.com/pedroguswander)
[Arthur Xavier](https://github.com/arthurxavi)
[Felipe Andrade](https://github.com/felipeandrader)
[Rodrigo Guimarães](https://github.com/Rodrigo-Guimaraes-P)
[Augusto Barbosa](https://github.com/AugustoBarbosa87)


