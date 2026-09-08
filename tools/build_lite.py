#!/usr/bin/env python3
"""Build a local ZIP of the four public Lite files (Python 3.10+, stdlib only).

From the repository root: python tools/build_lite.py
Checks only: python tools/build_lite.py --check-only
No upload, AI call, payment, package installation, or scheduled execution.
Passing these checks is not a functional test, security audit, or release approval.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import os
import re
import sys
import tempfile
import zipfile
from pathlib import Path

FILES = ('LICENSE.md', 'README.md', 'skills/idea-to-spec/SKILL.md',
         'skills/launch-checklist/SKILL.md')
SECRET = re.compile(r'sk-(?:proj-|ant-)[A-Za-z0-9_-]{25,}|AKIA[0-9A-Z]{16}|'
                    r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----')


def collect(root: Path) -> dict[str, bytes]:
    root = root.resolve()
    result = {}
    for name in FILES:
        current = root
        for part in Path(name).parts:
            current = current / part
            if current.is_symlink():
                raise ValueError(f'Symlinks are not allowed: {name}')
        if not current.is_file() or current.stat().st_size > 2_000_000:
            raise ValueError(f'Missing or oversized file: {name}')
        data = current.read_bytes()
        text = data.decode('utf-8')
        if SECRET.search(text):
            raise ValueError(f'Potential secret in {name}; value not displayed')
        if current.name == 'SKILL.md':
            lines = text.splitlines()
            if not lines or lines[0] != '---' or '---' not in lines[1:]:
                raise ValueError(f'Missing or unclosed frontmatter: {name}')
            front = '\n'.join(lines[1:lines.index('---', 1)])
            expected = re.escape(current.parent.name)
            if not re.search(r'^name:\s*' + expected + r'\s*$', front, re.M):
                raise ValueError(f'Skill name/folder mismatch: {name}')
            if not re.search(r'^description:\s*\S.+$', front, re.M):
                raise ValueError(f'Missing description: {name}')
        result[name] = data
    return result


def build(root: Path, output: Path) -> Path:
    entries = collect(root)
    manifest = {'edition': 'Lite', 'files': {n: hashlib.sha256(b).hexdigest() for n, b in entries.items()},
                'notice': 'Packaging checks only; no AI functional test or release approval.'}
    entries['BUILD_MANIFEST.json'] = (json.dumps(manifest, ensure_ascii=False, indent=2) + '\n').encode()
    output.mkdir(parents=True, exist_ok=True)
    target = output / 'claude-code-indie-skills-lite.zip'
    if target.is_symlink():
        raise ValueError('Refusing to replace a symlink')
    with tempfile.NamedTemporaryFile(dir=output, prefix='.lite-', delete=False) as file:
        temporary = Path(file.name)
    try:
        with zipfile.ZipFile(temporary, 'w', compression=zipfile.ZIP_DEFLATED) as archive:
            for name, data in sorted(entries.items()):
                info = zipfile.ZipInfo(name, date_time=(2020, 1, 1, 0, 0, 0))
                info.compress_type = zipfile.ZIP_DEFLATED
                info.external_attr = 0o100644 << 16
                archive.writestr(info, data)
        os.replace(temporary, target)
    finally:
        temporary.unlink(missing_ok=True)
    return target


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--output', type=Path, default=Path('dist'))
    parser.add_argument('--check-only', action='store_true')
    args = parser.parse_args()
    try:
        if args.check_only:
            print(f'Packaging checks passed for {len(collect(args.root))} public Lite files.')
        else:
            print(f'Created local ZIP: {build(args.root, args.root / args.output)}')
        print('No upload, payment, or publication performed.')
        return 0
    except (OSError, ValueError) as error:
        print(f'STOP: {error}', file=sys.stderr)
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
