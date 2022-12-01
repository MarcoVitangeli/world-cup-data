#!/bin/python3
from dotenv import load_dotenv
from pathlib import Path
from executor import RequestExecutor
import argparse, os
from colorama import Fore, Back, Style

def print_cli(s: str) -> None:
    print(Fore.WHITE + Back.LIGHTBLUE_EX + Style.DIM + s)

def main() -> None:
    load_dotenv(dotenv_path=Path(".env"))
    executor = RequestExecutor(
                os.environ['EMAIL'],
                os.environ['PASSWORD'],
                os.environ['API_URL']
            )
    
    parser = argparse.ArgumentParser(
                    prog = 'Informacion del mundial 2022',
                    description = 'Informacion del mundial 2022 sobre los distintos equipos',
                    epilog = 'usar -h o --help para ver el uso')
    
    parser.add_argument('country')
    parser.add_argument('-g', '--group', action='store_true')
    parser.add_argument('-p', '--pts', action='store_true')

    args = parser.parse_args()
        
    if args.group:
        teamId = executor.get_id_by_name(args.country)
        g: str = executor.get_group_by_id(teamId)
        print_cli(f'El grupo de {args.country.title()} es el: {g}')

    if args.pts:
        teamId = executor.get_id_by_name(args.country)
        pts = executor.get_pts_by_id(teamId)
        print_cli(f'{args.country.title()} tiene {pts} puntos!')


if __name__ == "__main__":
    main()
