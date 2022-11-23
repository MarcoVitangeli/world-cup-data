#!/bin/python3
import os, sys
from dotenv import load_dotenv
from pathlib import Path

import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)


from ..lib import RequestExecutor

def main() -> None:

    load_dotenv(dotenv_path=Path(".env"))
    executor = RequestExecutor(
                os.environ['API_TOKEN'],
                os.environ['API_URL']
            )

    print(executor.get_arg_group())

if __name__ == "__main__":
    main()
