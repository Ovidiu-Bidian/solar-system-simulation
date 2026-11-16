#!/usr/bin/env python3
"""Make data/three/three-<version>.js for the solar system simulation from a three.js release.

The simulation (solar-system-simulation.html) also runs opened from the disk (file://), where browsers do not load
JavaScript modules from files. So three.js is kept in one classic script, three-<version>.js, that holds the text of the
modules the simulation needs:

    window.THREE_LIB = { version: '<version>', modules: { 'three': '<text>', 'three/addons/lines/...js': '<text>', ... } };

The page turns each text into a module (a Blob URL) and maps it with an importmap. The modules are taken unchanged from
the release, except their relative imports ('./x.js', '../lines/x.js'), which become the names above (a Blob URL has no
folder): build/three.module.js is 'three', examples/jsm/<path> is 'three/addons/<path>', any other file 'three/<path>'.
Files imported by these (as build/three.core.js since 0.170) are added the same way. three.js's MIT license is put at the
top. This is how data/three/three-0.187.0.js was made (and three-0.160.0.js, shipped until views_fix v_3.17).

Use (Python 3, no other packages):
    python3 make-three-file.py 0.188.0                  download the version from https://cdn.jsdelivr.net/npm/three@0.188.0/
    python3 make-three-file.py 0.188.0 --from DIR       from DIR, an extracted three.js release archive (the folder holding
                                                        build/ and examples/, e.g. three.js-r188 from GitHub or a mirror)
The file is written next to this script, unless --out DIR is given. Then write the version in default-version.js.
"""
import json, os, re, sys, urllib.request

ENTRY = ['build/three.module.js', 'examples/jsm/lines/LineSegments2.js', 'examples/jsm/lines/LineSegmentsGeometry.js',
         'examples/jsm/lines/LineMaterial.js']
IMPORT = re.compile(r"""(\bfrom\s*|\bimport\s*\(?\s*)(['"])(\.\.?/[^'"]+)\2""")


def key_of(p):
    if p == 'build/three.module.js':
        return 'three'
    if p.startswith('examples/jsm/'):
        return 'three/addons/' + p[len('examples/jsm/'):]
    return 'three/' + p


def make(version, src=None, out=None):
    if src:
        def get(p):
            with open(os.path.join(src, *p.split('/')), encoding='utf-8') as f:
                return f.read()
        where = 'the release archive ' + os.path.basename(os.path.abspath(src))
    else:
        base = 'https://cdn.jsdelivr.net/npm/three@' + version + '/'
        def get(p):
            with urllib.request.urlopen(base + p) as r:
                return r.read().decode('utf-8')
        where = base
    modules, todo, seen = {}, list(ENTRY), set(ENTRY)
    while todo:
        p = todo.pop(0)
        d = p[:p.rfind('/') + 1]

        def fix(m):
            parts = []
            for s in (d + m.group(3)).split('/'):
                if s == '..':
                    parts.pop()
                elif s != '.':
                    parts.append(s)
            path = '/'.join(parts)
            if path not in seen:
                seen.add(path)
                todo.append(path)
            return m.group(1) + m.group(2) + key_of(path) + m.group(2)
        modules[key_of(p)] = IMPORT.sub(fix, get(p))
    lic = get('LICENSE').strip()
    name = os.path.join(out or os.path.dirname(os.path.abspath(__file__)), 'three-' + version + '.js')
    with open(name, 'w', encoding='utf-8', newline='\n') as f:
        f.write('/* three.js ' + version + ' for solar-system-simulation.html, made by make-three-file.py from ' + where + ':\n'
                '   ' + ', '.join(sorted(seen)) + ',\n'
                '   unchanged except their relative imports (made into the names of the modules); kept as text, turned into\n'
                '   modules by the page.\n\n'
                + '\n'.join('   ' + l for l in lic.split('\n')) + '\n*/\n')
        f.write("window.THREE_LIB = { version: '" + version + "', modules: " + json.dumps(modules, ensure_ascii=False) + ' };\n')
    return name, len(modules)


if __name__ == '__main__':
    a = sys.argv[1:]
    if not a or not re.fullmatch(r'\d+(\.\d+)+', a[0]):
        sys.exit(__doc__)
    opt = lambda k: a[a.index(k) + 1] if k in a and a.index(k) + 1 < len(a) else None
    name, n = make(a[0], opt('--from'), opt('--out'))
    print('written', name, '(' + str(n) + ' modules)')
