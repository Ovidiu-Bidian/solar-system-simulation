three.js for the solar system simulation
=========================================

three-0.187.0.js      three.js 0.187.0, the version the simulation was tested with (shipped with it; MIT license
                      inside). Keep it: the simulation falls back to it.
default-version.js    the version used by default; 0.187.0 unless you change it (see below).
make-three-file.py    makes a three-<version>.js file for another version.

Why a special file: the simulation also runs opened from the disk (double-click on solar-system-simulation.html).
There the browser does not load JavaScript modules or plain files from the folder, so the files of a three.js
release (or of its archive) cannot simply be put here: three.js is kept in one classic script, three-<version>.js,
that holds the text of the modules the simulation needs (three.module.js and the line add-ons).

Using another three.js version (AT YOUR OWN RISK: the simulation was tested with 0.187.0)
1. Make its file with Python 3 (no other packages needed), in this folder, for example for a version 0.188.0:
     python3 make-three-file.py 0.188.0
   (downloads three.js 0.188.0 from https://cdn.jsdelivr.net/npm/three@0.188.0/), or, from a release archive you
   downloaded and extracted (for example three.js-r188 from https://github.com/mrdoob/three.js/releases or a mirror):
     python3 make-three-file.py 0.188.0 --from path/to/three.js-r188
   Release r188 is version 0.188.0. This writes three-0.188.0.js here.
2. In default-version.js write the version: window.THREE_DEFAULT = '0.188.0';
3. Open the simulation. About (Help) shows "three.js in use: 0.188.0 (the default version, chosen in
   data/three/default-version.js)". If the file is missing or this version does not start, the simulation uses
   0.187.0 and says so in a note at the top.
The version tested before, until views_fix v_3.17, was 0.160.0: to use it again, make its file the same way
(python3 make-three-file.py 0.160.0; it gives exactly the file shipped until then) and write '0.160.0'.
Back to the tested version: write '0.187.0' in default-version.js again.

The simulation also offers newer three.js versions by itself (a note, and Help > About): those are kept in the
browser, not in this folder.
