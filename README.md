# melplot

Plot melodeon[^dba] layout diagrams

## Notes

### Inspiration

* standard 21-key D/G with acc. notes highlighted and piano-key octave numbers marked:
  <http://forum.melodeon.net/files/site/keyboards/2%20Row%20-%20D_G%20-%20with%20accidentals.jpg>
* standard 21-key D/G with notes on stave, from [Mel Forum](http://forum.melodeon.net):
  <http://forum.melodeon.net/files/site/DGwithStave.pdf>
* as above, with ABC notation labels added, from [Daddy Long Les](https://www.daddylongles.com/dg-melodeon-resources):
  <https://www.daddylongles.com/_files/ugd/2a4ead_6501161c36fa470fbb1f64d24261ad9d.pdf>
* Dipper blank 30-key Anglo concertina scheme, with push/pull "pills" and piano keyboard with octaves highlighted:
  <http://www.johndipper.co.uk/downloads/blank-scheme.pdf>

### TODO

*and ideas*

* [x] basic diagram using mpl
* [ ] different ways to indicate octaves (e.g. color; piano key notation or wrt. root)
* [ ] different options for pitch labels (ABC, piano key notation, scale degrees)
* [ ] plotting notes on stave
* [ ] CLI
* [ ] first PyPI release
* [ ] HTML/CSS output option
* [ ] fancier button style option (some 3-D-ness)
* [ ] draw connections in bellows direction for consecutive notes or chord
* [ ] docs build with layout library

### Input format

ASCII representation of the layout.

Ideas:

* notes in ABC notation, push/pull separated by `/` or `|`, push/pull pairs separated by whitespace
* for each row, specify horizontal offset in the layout (zero implicit; e.g. 0.5 for the second row in a typical 11/10 layout)
  - maybe like `x0.5` instead of just `0.5`, to emphasize just space
* bass chords also in ABC notation, but maybe also support the common `+`/`-`?

### Layout sources

* [Mel Forum 2-row](http://forum.melodeon.net/index.php/page,keyboard_2_row.html)
* [Mel Forum 2.5-row](http://forum.melodeon.net/index.php/page,keyboard_25_row.html)
* [Mel Forum 3-row](http://forum.melodeon.net/index.php/page,keyboard_3_row.html)
* [bass layouts from Squeezehead](http://squeezehead.com/keyboard-layouts/basses/LAYOUTS.html)
* [2.5ish-row layouts from Orest](http://www.geocities.ws/kozulich/2plusrowDG.html)


[^dba]: [Diatonic button accordion](https://en.wikipedia.org/wiki/Diatonic_button_accordion) (DBA) / melodeon / "box" / accordéon diatonique / diato / etc. Also may later extend to plotting the layouts of other button accordion family instruments like concertinas.
