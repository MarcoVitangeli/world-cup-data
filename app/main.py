#!/bin/python3
import os
from dotenv import load_dotenv
from pathlib import Path
from executor import RequestExecutor

def main() -> None:

    load_dotenv(dotenv_path=Path(".env"))
    executor = RequestExecutor(
                os.environ['API_TOKEN'],
                os.environ['API_URL']
            )

    print(executor.get_arg_group())

if __name__ == "__main__":
    main()
