PYTHON = python3
PIP = pip
TEST_DIR = tests
SRC_DIR = src

install:
	$(PIP) install -r requirements.txt

format:
	black $(SRC_DIR) $(TEST_DIR)

test:
	$(PYTHON) -m pytest $(TEST_DIR)

clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	rm -rf .pytest_cache

all: install format test

docker-build:
	docker build -t projeto-nlp .

docker-run:
	docker run -p 80:80 projeto-nlp

help:
	@echo "Comandos disponíveis:"
	@echo "  make install   - Instala as dependências do projeto"
	@echo "  make format    - Formata o código usando black"
	@echo "  make test      - Executa os testes com pytest"
	@echo "  make clean     - Limpa arquivos temporários e caches"
	@echo "  make all       - Executa todas as tarefas (install, format, test)"
	@echo "  make help      - Exibe esta mensagem de ajuda"