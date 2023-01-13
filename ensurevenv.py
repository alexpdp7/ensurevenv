import appdirs
import hashlib
from packaging import requirements
import pathlib
import subprocess
import sys
import typing
import venv


def get(packages):
    if are_all_installed(packages):
        return
    venv_path = get_venv_path()
    if not venv_path.exists():
        venv.create(venv_path, with_pip=True)
    # TODO: vendor appdirs and packaging
    subprocess.run([venv_path / "bin" / "pip", "install", "appdirs", "packaging"] + packages, check=True)
    sys.exit(subprocess.run([venv_path / "bin" / "python"] + sys.argv).returncode)


def are_all_installed(packages: typing.List[str]):
    all_installed = pip_freeze()
    for package in packages:
        if not is_installed(package, all_installed):
            return False
    return True
    

def is_installed(package, all_installed: typing.List[requirements.Requirement]):
    for installed_package in all_installed:
        if installed_package.name == package:
            return True
    return False


def pip_freeze():
    return list(map(requirements.Requirement, subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'], encoding="utf8").split()))


def get_venv_path():
    return pathlib.Path(appdirs.user_cache_dir("ensurevenv")) / hash_exe()

def hash_exe():
    exe = sys.argv[0]
    with open(exe, "rb") as exe_f:
        return hashlib.sha256(exe_f.read()).hexdigest() + "-" + pathlib.Path(exe).name
