# annot-5.htm

**Source:** https://physionet.org/physiotools/wag/annot-5.htm

---

Name annot - WFDB annotation file formats Synopsis #include <wfdb/ecgcodes.h> Description Programs compiled with the WFDB library ( -lwfdb ) can read annotation
files in two formats.  The preferred format (MIT format) is compact (averaging
slightly over two bytes per annotation) and extensible, and is normally
used for on-line annotation files.  The alternative format (AHA DB distribution
format) uses 16 bytes per annotation, and is normally used only for exchange
of files between institutions on 9-track tape. Both formats are binary, but
readable on any machine without reformatting. WFDB library applications
can distinguish between the formats automatically when opening a file for
input. MIT format: Each annotation occupies an even number of bytes.  The
first byte in each pair is the least significant byte. The six most significant
bits ( A ) of each byte pair are the annotation type code, and the ten remaining
bits ( I ) specify the time of the annotation, measured in sample intervals
from the previous annotation (or from the beginning of the record for the
first annotation). If 0 < A <= ACMAX , then A is defined in <wfdb/ecgcodes.h> .
 Several other possibilities exist: A = SKIP [59.] I = 0; the next four
bytes are the interval in PDP-11 long integer format (the high 16 bits first,
then the low 16 bits, with the low byte first in each pair). A = NUM [60.] I = annotation num field for current and subsequent annotations;  otherwise,
assume previous annotation num (initially 0). A = SUB [61.] I = annotation subtyp field for current annotation only; otherwise, assume subtyp = 0. A = CHN [62.] I = annotation chan field for current and subsequent annotations;
otherwise, assume previous chan (initially 0). A = AUX [63.] I = number of
bytes of auxiliary information (which is contained in the next I bytes);
 an extra null, not included in the byte count, is appended if I is odd. A = I = 0:  End of file. AHA format: All annotations occupy exactly 16 bytes.
 Within each block, the first byte is unused, the second byte contains
the AHA annotation code (an ASCII character; see <wfdb/ecgmap.h> ), the third
through sixth bytes contain the time (see below) in PDP-11 long integer
format as above, and the seventh and eighth bytes contain an annotation
serial number. In annotation files taken directly from the AHA database
distribution tapes, the last eight bytes in each annotation are unused,
and the time is given in milliseconds measured from the beginning of the
annotated segment of the record.  In AHA-format annotation files generated
by WFDB library applications, annotation times are given in sample intervals
from the beginning of the record, and the last eight bytes of each annotation
contain the MIT annotation subtype (in the ninth byte), the MIT annotation
code (in the tenth byte), and up to six ASCII characters (in the remaining
bytes) used to describe RHYTHM and NOTE annotations. See Also header (5) , signal (5) , wfdbcal (5) WFDB Programmer’s Guide Author George B. Moody (george@mit.edu).  The original
MIT annotation format was designed by Paul Schluter, and the AHA annotation
format was designed by Russ Hermes. Table of Contents Name Synopsis Description MIT format: AHA format: See Also Author Up: WFDB Applications Guide Please e-mail your comments and suggestions to webmaster@physionet.org , or post them to: PhysioNet MIT Room E25-505A 77 Massachusetts Avenue Cambridge, MA 02139 USA Updated 10 June 2022

Each annotation occupies an even number of bytes.  The
first byte in each pair is the least significant byte. The six most significant
bits ( A ) of each byte pair are the annotation type code, and the ten remaining
bits ( I ) specify the time of the annotation, measured in sample intervals
from the previous annotation (or from the beginning of the record for the
first annotation). If 0 < A <= ACMAX , then A is defined in <wfdb/ecgcodes.h> .
 Several other possibilities exist: A = SKIP [59.] I = 0; the next four
bytes are the interval in PDP-11 long integer format (the high 16 bits first,
then the low 16 bits, with the low byte first in each pair). A = NUM [60.] I = annotation num field for current and subsequent annotations;  otherwise,
assume previous annotation num (initially 0). A = SUB [61.] I = annotation subtyp field for current annotation only; otherwise, assume subtyp = 0. A = CHN [62.] I = annotation chan field for current and subsequent annotations;
otherwise, assume previous chan (initially 0). A = AUX [63.] I = number of
bytes of auxiliary information (which is contained in the next I bytes);
 an extra null, not included in the byte count, is appended if I is odd. A = I = 0:  End of file. AHA format: All annotations occupy exactly 16 bytes.
 Within each block, the first byte is unused, the second byte contains
the AHA annotation code (an ASCII character; see <wfdb/ecgmap.h> ), the third
through sixth bytes contain the time (see below) in PDP-11 long integer
format as above, and the seventh and eighth bytes contain an annotation
serial number. In annotation files taken directly from the AHA database
distribution tapes, the last eight bytes in each annotation are unused,
and the time is given in milliseconds measured from the beginning of the
annotated segment of the record.  In AHA-format annotation files generated
by WFDB library applications, annotation times are given in sample intervals
from the beginning of the record, and the last eight bytes of each annotation
contain the MIT annotation subtype (in the ninth byte), the MIT annotation
code (in the tenth byte), and up to six ASCII characters (in the remaining
bytes) used to describe RHYTHM and NOTE annotations. See Also header (5) , signal (5) , wfdbcal (5) WFDB Programmer’s Guide Author George B. Moody (george@mit.edu).  The original
MIT annotation format was designed by Paul Schluter, and the AHA annotation
format was designed by Russ Hermes. Table of Contents Name Synopsis Description MIT format: AHA format: See Also Author Up: WFDB Applications Guide Please e-mail your comments and suggestions to webmaster@physionet.org , or post them to: PhysioNet MIT Room E25-505A 77 Massachusetts Avenue Cambridge, MA 02139 USA Updated 10 June 2022

All annotations occupy exactly 16 bytes.
 Within each block, the first byte is unused, the second byte contains
the AHA annotation code (an ASCII character; see <wfdb/ecgmap.h> ), the third
through sixth bytes contain the time (see below) in PDP-11 long integer
format as above, and the seventh and eighth bytes contain an annotation
serial number. In annotation files taken directly from the AHA database
distribution tapes, the last eight bytes in each annotation are unused,
and the time is given in milliseconds measured from the beginning of the
annotated segment of the record.  In AHA-format annotation files generated
by WFDB library applications, annotation times are given in sample intervals
from the beginning of the record, and the last eight bytes of each annotation
contain the MIT annotation subtype (in the ninth byte), the MIT annotation
code (in the tenth byte), and up to six ASCII characters (in the remaining
bytes) used to describe RHYTHM and NOTE annotations. See Also header (5) , signal (5) , wfdbcal (5) WFDB Programmer’s Guide Author George B. Moody (george@mit.edu).  The original
MIT annotation format was designed by Paul Schluter, and the AHA annotation
format was designed by Russ Hermes. Table of Contents Name Synopsis Description MIT format: AHA format: See Also Author Up: WFDB Applications Guide Please e-mail your comments and suggestions to webmaster@physionet.org , or post them to: PhysioNet MIT Room E25-505A 77 Massachusetts Avenue Cambridge, MA 02139 USA Updated 10 June 2022

In annotation files taken directly from the AHA database
distribution tapes, the last eight bytes in each annotation are unused,
and the time is given in milliseconds measured from the beginning of the
annotated segment of the record.  In AHA-format annotation files generated
by WFDB library applications, annotation times are given in sample intervals
from the beginning of the record, and the last eight bytes of each annotation
contain the MIT annotation subtype (in the ninth byte), the MIT annotation
code (in the tenth byte), and up to six ASCII characters (in the remaining
bytes) used to describe RHYTHM and NOTE annotations. See Also header (5) , signal (5) , wfdbcal (5) WFDB Programmer’s Guide Author George B. Moody (george@mit.edu).  The original
MIT annotation format was designed by Paul Schluter, and the AHA annotation
format was designed by Russ Hermes. Table of Contents Name Synopsis Description MIT format: AHA format: See Also Author Up: WFDB Applications Guide Please e-mail your comments and suggestions to webmaster@physionet.org , or post them to: PhysioNet MIT Room E25-505A 77 Massachusetts Avenue Cambridge, MA 02139 USA Updated 10 June 2022

Table of Contents Name Synopsis Description MIT format: AHA format: See Also Author Up: WFDB Applications Guide Please e-mail your comments and suggestions to webmaster@physionet.org , or post them to: PhysioNet MIT Room E25-505A 77 Massachusetts Avenue Cambridge, MA 02139 USA Updated 10 June 2022

Table of Contents Name Synopsis Description MIT format: AHA format: See Also Author Up: WFDB Applications Guide Please e-mail your comments and suggestions to webmaster@physionet.org , or post them to: PhysioNet MIT Room E25-505A 77 Massachusetts Avenue Cambridge, MA 02139 USA Updated 10 June 2022

Name Synopsis Description MIT format: AHA format: See Also Author Up: WFDB Applications Guide Please e-mail your comments and suggestions to webmaster@physionet.org , or post them to: PhysioNet MIT Room E25-505A 77 Massachusetts Avenue Cambridge, MA 02139 USA Updated 10 June 2022

Up: WFDB Applications Guide Please e-mail your comments and suggestions to webmaster@physionet.org , or post them to: PhysioNet MIT Room E25-505A 77 Massachusetts Avenue Cambridge, MA 02139 USA Updated 10 June 2022

Please e-mail your comments and suggestions to webmaster@physionet.org , or post them to: PhysioNet MIT Room E25-505A 77 Massachusetts Avenue Cambridge, MA 02139 USA Updated 10 June 2022

PhysioNet MIT Room E25-505A 77 Massachusetts Avenue Cambridge, MA 02139 USA Updated 10 June 2022
