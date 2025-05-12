# Faça um programa que peça o nome e a data de nascimento. Classifique a
# pessoa conforme sua idade exibindo a mensagem: “Nome +
# Criança para 0 até 11 anos; Adolescente para 12 até 18 anos; Jovem para
# 19 até 24 anos; Adulto para 25 até 40 anos; Meia Idade para 41 até 60 anos;
# Idoso acima de 60 anos.
from prompt_toolkit import prompt
from prompt_toolkit.validation import Validator, ValidationError
from prompt_toolkit.document import Document
from datetime import datetime

def aplicar_mascara(data_raw):
    # Remove tudo que não for número
    digits = ''.join(filter(str.isdigit, data_raw))
    # Aplica a máscara dd/mm/aaaa
    if len(digits) > 4:
        return f"{digits[:2]}/{digits[2:4]}/{digits[4:8]}"
    elif len(digits) > 2:
        return f"{digits[:2]}/{digits[2:4]}"
    else:
        return digits

# Validador que só permite 8 dígitos numéricos
class DataValidator(Validator):
    def validate(self, document: Document):
        digits = ''.join(filter(str.isdigit, document.text))
        if len(digits) != 8:
            raise ValidationError(message="Digite exatamente 8 números (ddmmaaaa)")

def main():
    nome = input("Digite seu nome: ")

    # Prompt com validação
    data_raw = prompt(
        "Digite sua data de nascimento (ddmmaaaa): ",
        validator=DataValidator(),
        validate_while_typing=True
    )

    # Aplica a máscara
    data_formatada = aplicar_mascara(data_raw)

    try:
        data_nasc = datetime.strptime(data_formatada, "%d/%m/%Y")
        hoje = datetime.today()
        idade = hoje.year - data_nasc.year - ((hoje.month, hoje.day) < (data_nasc.month, data_nasc.day))

        if idade <= 11:
            classificacao = "Criança"
        elif idade <= 18:
            classificacao = "Adolescente"
        elif idade <= 24:
            classificacao = "Jovem"
        elif idade <= 40:
            classificacao = "Adulto"
        elif idade <= 60:
            classificacao = "Meia Idade"
        else:
            classificacao = "Idoso"

        print(f"{nome} - {classificacao} ({idade} anos)")
    except Exception as e:
        print("Erro ao interpretar a data:", e)

if __name__ == "__main__":
    main()
