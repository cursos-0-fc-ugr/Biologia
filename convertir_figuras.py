#!/usr/bin/env python3

import re
import sys
from pathlib import Path

if len(sys.argv) != 2:
    sys.exit(f"Uso: {sys.argv[0]} archivo.qmd")

archivo = Path(sys.argv[1])

texto = archivo.read_text(encoding="utf-8")

patron = re.compile(
    r'!\[\]\(([^)]+)\)\{([^}]*)\}'
)

def reemplazo(m):
    ruta = m.group(1)
    attrs = m.group(2)

    attrs = re.sub(
        r'\s*height="[^"]*"',
        '',
        attrs
    ).strip()

    return (
        '::: {style="text-align:center;"}\n'
        f'![]({ruta}){{{attrs}}}\n'
        ':::'
    )

nuevo = patron.sub(reemplazo, texto)

archivo.with_suffix(archivo.suffix + ".bak").write_text(
    texto,
    encoding="utf-8"
)

archivo.write_text(
    nuevo,
    encoding="utf-8"
)

print(f"Procesado: {archivo}")