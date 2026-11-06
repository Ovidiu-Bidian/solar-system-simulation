# Solar system simulation

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23988621.svg)](https://doi.org/10.5281/zenodo.23988621)

A 3D simulation of the solar system moving through absolute space, in a single HTML file that runs in the browser.

**Live demo:** https://ovidiu-bidian.github.io/solar-system-simulation/solar-system-simulation.html

## What it shows

The Sun is not still. It moves around the center of our galaxy at about 230 km/s, towards the constellation Cygnus,
at about 60 degrees to the plane of the planets' orbits. The planets do not move on closed ellipses through space:
they follow the Sun, so their real paths are long spirals. The simulation draws these paths as trails, in an absolute
space around the Sun's path, over one revolution of Neptune (about 165 years).

What is real in the simulation (as known today):

- the motion of the Sun through absolute space: speed and direction;
- the orbits of Mercury, Venus, the Earth, Mars, Jupiter, Saturn, Uranus, Neptune and Pluto: real orbital elements
  (JPL, J2000), real periods, Kepler's laws, real sizes of the celestial bodies;
- the orbit of the Moon around the Earth, with its main disturbances by the Sun (Meeus, from ELP-2000/82);
- the rotation axes of the celestial bodies, their surface maps, the light of the Sun, the eclipses of the Sun and of
  the Moon;
- the constellations: the real directions, brightness and colors of their stars (Hipparcos catalogue), among them
  the constellations from which the motion of the Sun was determined (Hercules, Lyra, Columba, Cygnus, Sagittarius,
  Vela and those of Herschel's seven stars of 1783).
- the Milky Way: NASA's map of the glow of our galaxy, in its real place on the sky (brightest towards Sagittarius,
  the center of the galaxy, with its dark dust lanes).

What is not real (visual aids) is listed in the program, in Help → About: for example the minimum apparent size of
the celestial bodies, so that they can be seen from far away, the spin of the bodies (one turn every 10 seconds) and
the background stars, placed at random.

## The ideas behind the simulation

The simulation is built on a few principles, defined by Ovidiu Bidian in 2026 and written down in the requirements:

- **Real paths through absolute space.** Every motion is computed in one fixed space, the absolute space, through which
  the Sun travels at its real speed and direction. The paths of the planets and of the Moon are not drawn; they come
  out of the real orbits combined with the Sun's motion, as the spirals of their trails. The camera can stay at rest
  in this space, travelling with the Sun ("absolute space" mode), or follow a celestial body ("celestial body" mode).
- **Two reference systems for every view.**\
  The view's own system is where the camera moves: for a celestial body,
  the body's frame (its center, its rotation axis, and its equator from the node where the ecliptic crosses it going
  north, on the Earth the vernal equinox).\
  The camera's head system works like a camera on a pan/tilt head: +x is the
  direction the head faces (forward), +y the tilt axis (left), +z the pan axis (up). Both are drawn on the screen: the
  ecliptic and the equatorial axes of the body, with the equatorial plane, and, in the test version, the head of the
  recorded camera in its replay.
- **A camera path.** Each view moves the camera on a defined path in its own system; for example, the pole view moves
  it on a circle C around the body, tilted to the equator by the C angle.
- **Automatic and manual control.**\
  The keys and the mouse wheel are the automatic control: they move the camera
  along its path and set an automatic view, which keeps the body at its place on the screen.\
  The mouse is the manual control: it always grabs the image, as on a touch screen, and adds a look relative to the automatic view, kept
  through every movement.\
  The final view is the automatic view plus the manual look: you can look at the sky while
  the camera walks around the body, and the sky then turns on the screen as the automatic view turns. What is seen
  never turns faster than 30 degrees per second.
- **The pole view** is the first view built completely on these principles.\
  In the leveled pan the rotation axis stays vertical on the screen, with the north pole at the top, or the south pole at the top when the camera is below
  the equator (the picture turns by 180 degrees only when the camera clearly passes to the other side: a band of
  ±10 degrees).\
  In the rotating pan the picture turns evenly as the camera walks around the body, one turn per lap.\
  In the polar pan the rotation axis swings between the poles: the pole near the camera is at the top while the camera
  goes round it, and the moves are the same at both poles.

The other views will be rebuilt on the same principles.

## Walk in the sky

In absolute space mode the camera is not tied to any celestial body: it stays at rest relative to the Sun, so it
travels with the Sun through absolute space at about 230 km/s ("Cam speed" in the information panel), and moves
in other directions only when the user moves it. Here it looks around and moves among the trails of the planets, with the real
constellations behind them: Cygnus, the direction in which the Sun moves around the center of the galaxy;
Hercules (lambda Herculis) and Lyra (Vega), near the solar apex found by Herschel in 1783; Columba, the antapex;
Sagittarius, towards the center of the galaxy; Ursa Major and Ursa Minor, Centaurus and Crux, Carina, Octans.
All the trails run towards Vela, opposite Cygnus: the direction from which the Sun comes.

https://github.com/user-attachments/assets/38069d98-4ba8-4d3d-9f91-202c3ee40b27

## Sun rotation around planets

Seen from a planet, the Sun seems to turn around it: once a year around the Earth (yes, the Sun rotates around the Earth),
once in about 29.5 years around Saturn (yes, the Sun rotates also around Saturn, everything depending on the chosen reference system).
This is the motion people saw for thousands of years, and it is only relative (to the chosen reference system): in absolute space
the planet does not stand still at the center, it follows the Sun along its path through the galaxy.

In these two videos the camera travels with the planet (the reference celestial body).
Around the Earth, the camera looks towards Vela, the direction from which the Sun comes: the Sun turns around the Earth, while all
the trails run away towards the same point in Vela.
Around Saturn, the camera looks towards Centaurus and Crux: the Sun, with the inner planets around it, makes a full turn around Saturn
while their trails, twisted around the Sun's path, always run towards Vela.

https://github.com/user-attachments/assets/fe950ab0-0b5a-400a-bdfb-dbfdb159049a

https://github.com/user-attachments/assets/cd1e935e-f72b-4811-be28-34aad8edef6b

## Example: the planets seen from Saturn

The camera travels with Saturn through absolute space (Saturn is the reference celestial body). Far away, at the
top of the picture, the Sun moves along its path towards Cygnus, and the inner planets follow it: their yellow
trails twist around the Sun's path, the spirals they draw in absolute space. The zoom screen (the "T" key) shows
the Sun and the planets near it, with their names in its corner.

https://github.com/user-attachments/assets/e03716b3-45bc-4b04-a848-d7cda1d23848

## Example: the retrograde motion of Mars

Seen from the Earth, Mars usually moves in one direction against the stars, but for about two and a half months, while the Earth
overtakes it on its inner orbit, it stops, moves backwards and then turns again: a loop on the sky. The simulation
shows it without any special code: it follows only from the real orbits of the Earth and of Mars. The picture under
the video was traced from it (the Earth as the reference celestial body, one dot every 2 seconds).

https://github.com/user-attachments/assets/8ba0c998-d300-4b44-9d25-85f9814e0080

<img width="1764" height="800" alt="Mars_retrograde_path" src="https://github.com/user-attachments/assets/b9d2a074-0685-43c6-bd57-42c6907c9050" />

## Eclipses of the Sun and of the Moon

The eclipses are not drawn on purpose: they follow from the real orbits of the Earth and of the Moon and from the
real sizes of the Sun, the Earth and the Moon. For every point of a surface the simulation computes how much of the
disk of the Sun is covered by the other body, so the shadows have a dark center (umbra) and a soft edge (penumbra).\
In the first video (the Moon as the reference celestial body, Earth locked view) the shadow of the Moon crosses the
Earth: an eclipse of the Sun, total only in the small spot of the umbra.\
In the second video (the Earth as the reference celestial body, Moon locked view) the Moon enters the shadow of the Earth and turns copper red: it is lit
only by the sunlight that the atmosphere of the Earth bends into its shadow, mostly red. In these two views the other
body is drawn larger (or smaller) than real, so that it can be seen, but its place and its shadow stay real.

https://github.com/user-attachments/assets/a889ed82-bb39-40ba-ba99-891f224d293e

https://github.com/user-attachments/assets/79f34e43-c585-4be8-be82-ed102b1a7f6d

## How to use it

Open the live demo, or download `solar-system-simulation.html` and open it in a browser (Edge, Chrome or Firefox;
an internet connection is needed for the three.js library).

- the menu (upper left) chooses the reference system: absolute space, or a celestial body that the camera follows;
  each celestial body has several views (tilted meridian, meridian, pole view, Sun locked, turntable);
- the information panel (upper right) shows the data of the celestial body; "Run/Stop" and "-" / "+" set the motion
  and the speed of the simulation; the reference axes button (or the "J" key) chooses which axes of the celestial
  body are drawn: both, none, the equatorial ones or the ecliptic ones;
- Help → Controls lists the keys and the mouse controls of the current camera mode.

## Requirements

The simulation was built from written requirements, kept in this repository and updated with every version:
- `Requirements/requirements_EN.req.txt`: English
- `Requirements/specificatii_simulare_RO.req.txt`: Romanian, mirrored line by line

The versions are the git tags: `v_X` for the simulation and `specs_v_X` for the requirements at the same level. Each
tag carries the list of its changes.

## Background

This simulation is for scientific and educational purposes. It is also a support software for the book
"Marea greșeală a „marelui” Einstein" by Ovidiu Bidian (Artpress, ISBN 978-973-108-587-6).

To cite it: Ovidiu Bidian, *Solar system simulation*, Zenodo, 2026, https://doi.org/10.5281/zenodo.23988621
(this DOI always leads to the latest version; each version has its own DOI on Zenodo).

The software was written by Claude Code (Anthropic) under the direct and close requirements and supervision of
Ovidiu Bidian: the requirements, the review of every version and the tests are his.

## Credits

- [three.js](https://threejs.org/) (MIT license), loaded from a CDN
- Surface maps of Mercury, Venus, the Earth, the Moon, Mars, Jupiter, Saturn and its rings, Uranus and Neptune:
  [Solar System Scope](https://www.solarsystemscope.com/textures/), CC BY 4.0
- Map of Pluto: NASA / JHUAPL / SwRI (New Horizons, PIA11707), public domain
- Stars and constellation lines: [d3-celestial](https://github.com/ofrohn/d3-celestial) by Olaf Frohn (BSD 3-clause),
  from the Hipparcos catalogue
- Milky Way: NASA Goddard Space Flight Center, Scientific Visualization Studio,
  [Deep Star Maps 2020](https://svs.gsfc.nasa.gov/4851) (from the Hipparcos, Tycho and Gaia catalogues)
- Orbital elements: JPL; orbit of the Moon: J. Meeus, Astronomical Algorithms

## License

MIT (see `LICENSE`), for the code and the requirements. The surface maps and the star data keep their own
licenses (see Credits above).
