import sys
from typing import Optional
from simuleval import options


def cli_argument_list(config_dict: Optional[dict]):
    if config_dict is None:
        return sys.argv[1:]
    else:
        string = ""
        for key, value in config_dict.items():
            if f"--{key.replace('_', '-')}" in sys.argv:
                continue

            if type(value) is not bool:
                string += f" --{key.replace('_', '-')} {value}"
            else:
                string += f" --{key.replace('_', '-')}"
    if not in_notebook():
        return sys.argv[1:] + string.split()
    else:
        return string.split()

def in_notebook():
    try:
        from IPython import get_ipython
        if 'IPKernelApp' not in get_ipython().config:  # pragma: no cover
            return False
    except ImportError:
        return False
    except AttributeError:
        return False
    return True

def check_argument(name: str, config_dict: Optional[dict] = None):
    parser = options.general_parser()
    args, _ = parser.parse_known_args(cli_argument_list(config_dict))
    return getattr(args, name)
