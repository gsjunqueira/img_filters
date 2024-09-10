# Projeto de Filtros de Imagem com OpenCV

Este projeto realiza a captura de vídeo a partir de diferentes webcams vinculadas à conta Apple, aplicando diversos filtros de borda e suavização em tempo real utilizando a biblioteca OpenCV.

## Funcionalidades

- Captura de vídeo da webcam (iPhone 13, iPhone 14, MacBook Air).
- Aplicação de filtros de borda:
  - Sobel (X, Y, 2X, 2Y)
  - Laplaciano
  - Canny
- Aplicação de filtros de suavização:
  - Filtro de Média
  - Filtro Gaussiano
  - Filtro de Mediana
- Detecção de cores em tons de azul e vermelho utilizando máscaras HSV.
- Visualização simultânea dos frames com os diferentes filtros aplicados.

## Bibliotecas Utilizadas

- `time`: Para controle de tempo entre frames.
- `cv2` (OpenCV): Para manipulação de imagem e vídeo.
- `numpy`: Para operações numéricas e manipulação de arrays.

## Gerenciamento de Dependências com Poetry

Este projeto utiliza o [Poetry](https://python-poetry.org/) para gerenciar as dependências.

### Instalando o Poetry

Caso ainda não tenha o Poetry instalado, você pode instalá-lo executando o seguinte comando:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

### Instalando as dependências

Após instalar o Poetry, você pode clonar o repositório e instalar as dependências necessárias com:

```bash
git clone <url-do-repositorio>
cd <nome-do-repositorio>
poetry install
```

Isso instalará todas as dependências definidas no arquivo `pyproject.toml`.

### Rodando o projeto

Depois de instalar as dependências, você pode rodar o projeto no ambiente virtual gerenciado pelo Poetry:

```bash
poetry run python seu_script.py
```

Pressione Q para encerrar a execução.

### Como Executar o Projeto (Sem Poetry)

1. Instale as bibliotecas necessárias:

   - `OpenCV`: pip install opencv-python
   - `NumPy`: pip install numpy

2. Conecte as webcams nos dispositivos:
    Este projeto considera três webcams:
    - `Índice 0`: iPhone 13
    - `Índice 1`: iPhone 14
    - `Índice 2`: MacBook Air
Certifique-se de que seus dispositivos estejam conectados corretamente e reconhecidos pela sua máquina.

3. Executando o código:
Após conectar os dispositivos, execute o script:

```bash
python seu_script.py
```

Pressione Q para encerrar a execução.

### Personalização dos Filtros

No código, é possível alterar os parâmetros de alguns filtros, como o tamanho do kernel para suavização e os valores de detecção de borda para o filtro Canny.

#### Exemplo de Modificação

Para alterar o tamanho do kernel do Filtro de Média:

```bash
media = cv2.blur(frame, (7, 7))  # Alterado de (5, 5) para (7, 7)
```

### Estrutura do Projeto

- Captura de Vídeo: Utiliza cv2.VideoCapture() para acessar a webcam.
- Aplicação dos Filtros: Utilizam-se métodos do OpenCV como cv2.Sobel(), cv2.Canny(), cv2.GaussianBlur(), entre outros.
- Máscaras HSV: As máscaras de cores são aplicadas para detecção de objetos nas cores azul e vermelho, com os intervalos definidos em formato HSV.

### Exibição dos Filtros

O vídeo capturado é exibido em janelas separadas para cada filtro:

- Sobel (X, Y, 2X, 2Y)
- Laplaciano
- Canny
- Filtros de suavização (Média, Gaussiano, Mediana)
- Detecção de cores HSV (Azul, Vermelho)

## Saída de Exemplo

Após rodar o projeto, serão exibidas diversas janelas mostrando as imagens processadas com os filtros aplicados, como Sobel, Laplaciano, Canny e as máscaras de cores para azul e vermelho.

## Conclusão

Este projeto demonstra a aplicação de diferentes técnicas de processamento de imagem usando OpenCV. Ele pode ser estendido para incluir outros filtros, técnicas de reconhecimento de padrões, ou integração com outros dispositivos de captura.
