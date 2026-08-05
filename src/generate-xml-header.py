#!/usr/bin/env python3

import sys
import re
from pathlib import Path


def make_variable_name(xml_file):
    name = Path(xml_file).name

    # Equivalent to:
    # sed -e 's/[-\.]/_/g' -e 's/.xml/_xml/g'
    name = re.sub(r'[-.]', '_', name)
    name = name.replace('_xml', '_xml')

    return name


def escape_c_string(text):
    lines = []

    for line in text.splitlines():
        line = line.replace('\\', '\\\\')
        line = line.replace('"', '\\"')
        lines.append(f'"{line}\\n"')

    return '\n'.join(lines)


def generate(xml_path, output_path):
    xml_text = Path(xml_path).read_text()

    variable = make_variable_name(xml_path)

    escaped = escape_c_string(xml_text)

    output = f"""/* Generated file. Do not edit. */

static const gchar {variable}[] =
{escaped}
;
"""

    Path(output_path).write_text(output)


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print(
            f"Usage: {sys.argv[0]} input.xml output.h",
            file=sys.stderr
        )
        sys.exit(1)

    generate(sys.argv[1], sys.argv[2])