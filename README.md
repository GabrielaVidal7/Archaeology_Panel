# Processamento de Nuvens de Pontos na Identificação de Artefatos Humanos Pictóricos em Abrigos Pré-Históricos

## Sobre o projeto

O presente repositório consiste dos códigos desenvolvidos para o Trabalho de Conclusão de Curso da aluna Gabriela Barion Vidal.

O projeto visa desenvolver um algoritmo que analisará nuvens de ponto de sítios arqueológicos que possuem petróglifos e gerar uma imagem em duas dimensões para servir como painel para artigos científicos futuros e documentação da região. Assim, o presente trabalho irá auxiliar na precisão e automação da documentação de arte rupestre gravada, gerando um modelo bidimensional mais preciso e rápido do que as técnicas manuais utilizadas na arqueologia. O projeto tem como objetivo principal a digitalização do sítio arqueológico presente na cidade de Dourado-SP, que consiste de um paredão com diversas artes rupestres gravadas.

## Executando o projeto
Para conseguir utilizar o projeto em outros trabalhos, é preciso possuir Python 10 e seguir as seguintes etapas:

1. Baixar o repositório
2. Baixar as seguintes bibliotecas em Python:
    * Open3D versão 0.15.1
    * OpenCV
    * NumPy
3. O formato da nuvem de pontos que o código reconhece é ".ply"
4. Rodar o seguinte comando: `python main.py -i {path_to_ply_file} -o {name_output_file} -z {zoom_out_value}`


## Etapas do processamento
O código desenvolvido passa por algumas etapas de pré-processamento e cálculos para encontrar a normal principal presente na nuvem de ponto e então utilizá-la para mover a câmera para a posição ideal. Abaixo está o passo a passo resumido de como funciona o código, assim como alguns exemplos do resultado de cada etapa. Para mais detalhes, visite o artigo.

1. Downsampling para diminuir a quantidade de outliers que a nuvem de ponto original pode ter;
2. Cálculo das normais presentes em cada ponto da nuvem de ponto reduzida;

<p align="center">
  <img src="https://github.com/GabrielaVidal7/Archaeology_Panel/blob/main/animacoes/normais_painel_1.gif" alt="animated" width="576" height="324"/>
</p>

3. Normalização das normais calculadas, para evitar que haja um peso entre as normais no cálculo da normal principal;
4. Cálculo da normal principal (na animação abaixo, o ponto roxo representa a extremidade do vetor normal calculado);

<p align="center">
  <img src="https://github.com/GabrielaVidal7/Archaeology_Panel/blob/main/animacoes/main_normal_painel_1.gif" alt="animated" width="576" height="324"/>
</p>

5. Movimentação da câmera para a posição desejada. Para isso, utiliza-se o parâmetro "zoom_out_value" passado pelo usuário ao rodar o código;
6. Exportação do painel em formato ".png" com o nome sendo o parâmetro "name_output_file" passado pelo usuário.



## Desenvolvedora

Gabriela Barion Vidal
