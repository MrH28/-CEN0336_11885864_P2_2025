#!/usr/bin/env python3

# Importa recursos para localizar e executar o script principal.
from pathlib import Path
import runpy


# Executa o script principal a partir da pasta deste arquivo.
script_principal = Path(__file__).with_name("script_CDS.py")
runpy.run_path(str(script_principal), run_name="__main__")
