"""Executa os casos de teste deste programa."""
from pathlib import Path
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "apoio"))
from execucao import main

if __name__ == "__main__":
    sys.exit(main(mutante_local=7))