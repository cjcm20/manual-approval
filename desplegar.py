import os
import sys


def leer_variable(nombre: str) -> str:
    valor = os.environ.get(nombre, "")
    if not valor:
        print(f"Error: falta la variable de entorno {nombre}", file=sys.stderr)
        sys.exit(1)
    return valor


def main() -> None:
    url = leer_variable("APP_URL")
    token = leer_variable("DEPLOY_TOKEN")

    print(f"Desplegando en {url}")
    print(f"Token recibido: {len(token)} caracteres")


if __name__ == "__main__":
    main()