import syntax_analyzer as ps
import lexical_analyzer as lexic
import Executor as exec
import sys
import os

# Testar o interpretador MiniPar
        
def read_program_from_file(file_path):
    with open(file_path, 'r') as file:
        program = file.read()
    return program

5.95
def main():
    if len(sys.argv) < 2:
        print("Uso: python main.py <nome_do_program.mp>")
        sys.exit(1)

    program_file = sys.argv[1]
    if not os.path.exists(program_file):
        print(f"Erro: O arquivo '{program_file}' não foi encontrado.")
        sys.exit(1)

    entrada = read_program_from_file(program_file)
    lexer = lexic.lexer
    result = ps.parser.parse(entrada, lexer=lexer)
    if result:
        if not exec.has_error:
            exec.execute_stmt(result)
        else:
            pass

if __name__ == "__main__":
    main()