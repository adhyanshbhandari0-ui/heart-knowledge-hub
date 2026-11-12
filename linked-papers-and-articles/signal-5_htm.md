# signal-5.htm

**Source:** https://physionet.org/physiotools/wag/signal-5.htm

---

Name signal - WFDB signal file formats Description WFDB signal files exist
in several formats.  Any of these formats can be used for multiplexed signal
files, in which samples from two or more signals are stored alternately.
 See header (5) for information on how to identify which of the formats
below is used for a particular signal file. Format 8 Each sample is represented
as an 8-bit first difference;  i.e., to get the value of sample n , sum the
first n bytes of the sample data file together with the initial value from
the header file. When format 8 files are created, first differences which
cannot be represented in 8 bits are represented instead by the largest
difference of the appropriate sign (-128 or +127), and subsequent differences
are adjusted such that the correct amplitude is obtained as quickly as
possible.  Thus there may be loss of information if signals in another of
the formats listed below are converted to format 8. Note that the first
differences stored in multiplexed format 8 files are always determined
by subtraction of successive samples from the same signal (otherwise signals
with baselines which differ by 128 units or more could not be represented
this way). Format 16 Each sample is represented by a 16-bit two’s complement
amplitude stored least significant byte first. Any unused high-order bits
are sign-extended from the most significant bit. Historically, the format
used for MIT-BIH and AHA database distribution 9-track tapes was format 16,
with the addition of a logical EOF (octal 0100000) and null-padding after
the logical EOF. Format 24 Each sample is represented by a 24-bit two’s complement
amplitude stored least significant byte first. Format 32 Each sample is represented
by a 32-bit two’s complement amplitude stored least significant byte first. Format 61 Each sample is represented by a 16-bit two’s complement amplitude
stored most significant byte first. Format 80 Each sample is represented
by an 8-bit amplitude in offset binary form (i.e., 128 must be subtracted
from each unsigned byte to obtain a signed 8-bit amplitude). Format 160 Each
sample is represented by a 16-bit amplitude in offset binary form (i.e., 32,768
must be subtracted from each unsigned byte pair to obtain a signed 16-bit
amplitude).  As for format 16, the least significant byte of each pair is
first. Format 212 Each sample is represented by a 12-bit two’s complement amplitude.
 The first sample is obtained from the 12 least significant bits of the
first byte pair (stored least significant byte first).  The second sample
is formed from the 4 remaining bits of the first byte pair (which are the
4 high bits of the 12-bit sample) and the next byte (which contains the
remaining 8 bits of the second sample).  The process is repeated for each
successive pair of samples. Most of the signal files in PhysioBank are written
in format 212. Format 310 Each sample is represented by a 10-bit two’s-complement
amplitude.  The first sample is obtained from the 11 least significant bits
of the first byte pair (stored least significant byte first), with the
low bit discarded.  The second sample comes from the 11 least significant
bits of the second byte pair, in the same way as the first.  The third sample
is formed from the 5 most significant bits of each of the first two byte
pairs (those from the first byte pair are the least significant bits of
the third sample).  Note that the unused bit in each byte pair is set to
zero when using the WFDB library to write a format 310 signal file.  The
entire process is then repeated for each successive set of three samples. Format 311 Each sample is represented by a 10-bit two’s-complement amplitude.
 Three samples are bit-packed into a 32-bit integer as for format 310, but
the layout is different.  Each set of four bytes is stored in little-endian
order (least significant byte first, most significant byte last).  The first
sample is obtained from the 10 least significant bits of the 32-bit integer,
the second is obtained from the next 10 bits, the third from the next 10
bits, and the two most significant bits are unused (note that these bits
are set to zero when using the WFDB library to write a format 311 signal
file).  This process is repeated for each successive set of three samples. Formats 508, 516, and 524 Signals are compressed using the FLAC (Free Lossless
Audio Codec) format, either using 8 bits per sample (in format 508), 16
bits per sample (in format 516), or 24 bits per sample (in format 524).
 See https://xiph.org/flac/format.html for the full specification of these
formats. Note that these formats impose some restrictions on the signal
data that can be stored: The number of signals must equal the number of
channels in the FLAC stream, which implies there can be at most eight signals
stored in a single file. Every signal in the file must have the same sampling
frequency, and therefore the same number of samples per frame. Conversely,
some limitations apply when generating a FLAC stream to be used as a WFDB
signal file: The FLAC ‘bits per sample’ field must be 8, 16, or 24. Every
sample in the stream must be within the range of values indicated by the
‘bits per sample’ field. Note that the number of samples per frame is unrelated
to the size of the blocks used in FLAC compression; a single FLAC block
may contain multiple WFDB frames, and a single WFDB frame may be split
across multiple FLAC blocks. Also note that the FLAC ‘sample rate’ field should
be set to 96000, regardless of the actual sampling frequency of the signals.
 For compatibility with older FLAC implementations, this field should not
be set to 88200, 176400, or 192000. See Also annot (5) , header (5) , wfdbcal (5) WFDB Programmer’s Guide Author George B. Moody (george@mit.edu) Table of Contents Name Description Format 8 Format 16 Format 24 Format 32 Format 61 Format 80 Format 160 Format 212 Format 310 Format 311 Formats 508, 516, and 524 See Also Author Up: WFDB Applications Guide Please e-mail your comments and suggestions to webmaster@physionet.org , or post them to: PhysioNet MIT Room E25-505A 77 Massachusetts Avenue Cambridge, MA 02139 USA Updated 10 June 2022

Each sample is represented
as an 8-bit first difference;  i.e., to get the value of sample n , sum the
first n bytes of the sample data file together with the initial value from
the header file. When format 8 files are created, first differences which
cannot be represented in 8 bits are represented instead by the largest
difference of the appropriate sign (-128 or +127), and subsequent differences
are adjusted such that the correct amplitude is obtained as quickly as
possible.  Thus there may be loss of information if signals in another of
the formats listed below are converted to format 8. Note that the first
differences stored in multiplexed format 8 files are always determined
by subtraction of successive samples from the same signal (otherwise signals
with baselines which differ by 128 units or more could not be represented
this way). Format 16 Each sample is represented by a 16-bit two’s complement
amplitude stored least significant byte first. Any unused high-order bits
are sign-extended from the most significant bit. Historically, the format
used for MIT-BIH and AHA database distribution 9-track tapes was format 16,
with the addition of a logical EOF (octal 0100000) and null-padding after
the logical EOF. Format 24 Each sample is represented by a 24-bit two’s complement
amplitude stored least significant byte first. Format 32 Each sample is represented
by a 32-bit two’s complement amplitude stored least significant byte first. Format 61 Each sample is represented by a 16-bit two’s complement amplitude
stored most significant byte first. Format 80 Each sample is represented
by an 8-bit amplitude in offset binary form (i.e., 128 must be subtracted
from each unsigned byte to obtain a signed 8-bit amplitude). Format 160 Each
sample is represented by a 16-bit amplitude in offset binary form (i.e., 32,768
must be subtracted from each unsigned byte pair to obtain a signed 16-bit
amplitude).  As for format 16, the least significant byte of each pair is
first. Format 212 Each sample is represented by a 12-bit two’s complement amplitude.
 The first sample is obtained from the 12 least significant bits of the
first byte pair (stored least significant byte first).  The second sample
is formed from the 4 remaining bits of the first byte pair (which are the
4 high bits of the 12-bit sample) and the next byte (which contains the
remaining 8 bits of the second sample).  The process is repeated for each
successive pair of samples. Most of the signal files in PhysioBank are written
in format 212. Format 310 Each sample is represented by a 10-bit two’s-complement
amplitude.  The first sample is obtained from the 11 least significant bits
of the first byte pair (stored least significant byte first), with the
low bit discarded.  The second sample comes from the 11 least significant
bits of the second byte pair, in the same way as the first.  The third sample
is formed from the 5 most significant bits of each of the first two byte
pairs (those from the first byte pair are the least significant bits of
the third sample).  Note that the unused bit in each byte pair is set to
zero when using the WFDB library to write a format 310 signal file.  The
entire process is then repeated for each successive set of three samples. Format 311 Each sample is represented by a 10-bit two’s-complement amplitude.
 Three samples are bit-packed into a 32-bit integer as for format 310, but
the layout is different.  Each set of four bytes is stored in little-endian
order (least significant byte first, most significant byte last).  The first
sample is obtained from the 10 least significant bits of the 32-bit integer,
the second is obtained from the next 10 bits, the third from the next 10
bits, and the two most significant bits are unused (note that these bits
are set to zero when using the WFDB library to write a format 311 signal
file).  This process is repeated for each successive set of three samples. Formats 508, 516, and 524 Signals are compressed using the FLAC (Free Lossless
Audio Codec) format, either using 8 bits per sample (in format 508), 16
bits per sample (in format 516), or 24 bits per sample (in format 524).
 See https://xiph.org/flac/format.html for the full specification of these
formats. Note that these formats impose some restrictions on the signal
data that can be stored: The number of signals must equal the number of
channels in the FLAC stream, which implies there can be at most eight signals
stored in a single file. Every signal in the file must have the same sampling
frequency, and therefore the same number of samples per frame. Conversely,
some limitations apply when generating a FLAC stream to be used as a WFDB
signal file: The FLAC ‘bits per sample’ field must be 8, 16, or 24. Every
sample in the stream must be within the range of values indicated by the
‘bits per sample’ field. Note that the number of samples per frame is unrelated
to the size of the blocks used in FLAC compression; a single FLAC block
may contain multiple WFDB frames, and a single WFDB frame may be split
across multiple FLAC blocks. Also note that the FLAC ‘sample rate’ field should
be set to 96000, regardless of the actual sampling frequency of the signals.
 For compatibility with older FLAC implementations, this field should not
be set to 88200, 176400, or 192000. See Also annot (5) , header (5) , wfdbcal (5) WFDB Programmer’s Guide Author George B. Moody (george@mit.edu) Table of Contents Name Description Format 8 Format 16 Format 24 Format 32 Format 61 Format 80 Format 160 Format 212 Format 310 Format 311 Formats 508, 516, and 524 See Also Author Up: WFDB Applications Guide Please e-mail your comments and suggestions to webmaster@physionet.org , or post them to: PhysioNet MIT Room E25-505A 77 Massachusetts Avenue Cambridge, MA 02139 USA Updated 10 June 2022

Each sample is represented by a 16-bit two’s complement
amplitude stored least significant byte first. Any unused high-order bits
are sign-extended from the most significant bit. Historically, the format
used for MIT-BIH and AHA database distribution 9-track tapes was format 16,
with the addition of a logical EOF (octal 0100000) and null-padding after
the logical EOF. Format 24 Each sample is represented by a 24-bit two’s complement
amplitude stored least significant byte first. Format 32 Each sample is represented
by a 32-bit two’s complement amplitude stored least significant byte first. Format 61 Each sample is represented by a 16-bit two’s complement amplitude
stored most significant byte first. Format 80 Each sample is represented
by an 8-bit amplitude in offset binary form (i.e., 128 must be subtracted
from each unsigned byte to obtain a signed 8-bit amplitude). Format 160 Each
sample is represented by a 16-bit amplitude in offset binary form (i.e., 32,768
must be subtracted from each unsigned byte pair to obtain a signed 16-bit
amplitude).  As for format 16, the least significant byte of each pair is
first. Format 212 Each sample is represented by a 12-bit two’s complement amplitude.
 The first sample is obtained from the 12 least significant bits of the
first byte pair (stored least significant byte first).  The second sample
is formed from the 4 remaining bits of the first byte pair (which are the
4 high bits of the 12-bit sample) and the next byte (which contains the
remaining 8 bits of the second sample).  The process is repeated for each
successive pair of samples. Most of the signal files in PhysioBank are written
in format 212. Format 310 Each sample is represented by a 10-bit two’s-complement
amplitude.  The first sample is obtained from the 11 least significant bits
of the first byte pair (stored least significant byte first), with the
low bit discarded.  The second sample comes from the 11 least significant
bits of the second byte pair, in the same way as the first.  The third sample
is formed from the 5 most significant bits of each of the first two byte
pairs (those from the first byte pair are the least significant bits of
the third sample).  Note that the unused bit in each byte pair is set to
zero when using the WFDB library to write a format 310 signal file.  The
entire process is then repeated for each successive set of three samples. Format 311 Each sample is represented by a 10-bit two’s-complement amplitude.
 Three samples are bit-packed into a 32-bit integer as for format 310, but
the layout is different.  Each set of four bytes is stored in little-endian
order (least significant byte first, most significant byte last).  The first
sample is obtained from the 10 least significant bits of the 32-bit integer,
the second is obtained from the next 10 bits, the third from the next 10
bits, and the two most significant bits are unused (note that these bits
are set to zero when using the WFDB library to write a format 311 signal
file).  This process is repeated for each successive set of three samples. Formats 508, 516, and 524 Signals are compressed using the FLAC (Free Lossless
Audio Codec) format, either using 8 bits per sample (in format 508), 16
bits per sample (in format 516), or 24 bits per sample (in format 524).
 See https://xiph.org/flac/format.html for the full specification of these
formats. Note that these formats impose some restrictions on the signal
data that can be stored: The number of signals must equal the number of
channels in the FLAC stream, which implies there can be at most eight signals
stored in a single file. Every signal in the file must have the same sampling
frequency, and therefore the same number of samples per frame. Conversely,
some limitations apply when generating a FLAC stream to be used as a WFDB
signal file: The FLAC ‘bits per sample’ field must be 8, 16, or 24. Every
sample in the stream must be within the range of values indicated by the
‘bits per sample’ field. Note that the number of samples per frame is unrelated
to the size of the blocks used in FLAC compression; a single FLAC block
may contain multiple WFDB frames, and a single WFDB frame may be split
across multiple FLAC blocks. Also note that the FLAC ‘sample rate’ field should
be set to 96000, regardless of the actual sampling frequency of the signals.
 For compatibility with older FLAC implementations, this field should not
be set to 88200, 176400, or 192000. See Also annot (5) , header (5) , wfdbcal (5) WFDB Programmer’s Guide Author George B. Moody (george@mit.edu) Table of Contents Name Description Format 8 Format 16 Format 24 Format 32 Format 61 Format 80 Format 160 Format 212 Format 310 Format 311 Formats 508, 516, and 524 See Also Author Up: WFDB Applications Guide Please e-mail your comments and suggestions to webmaster@physionet.org , or post them to: PhysioNet MIT Room E25-505A 77 Massachusetts Avenue Cambridge, MA 02139 USA Updated 10 June 2022

Each sample is represented by a 24-bit two’s complement
amplitude stored least significant byte first. Format 32 Each sample is represented
by a 32-bit two’s complement amplitude stored least significant byte first. Format 61 Each sample is represented by a 16-bit two’s complement amplitude
stored most significant byte first. Format 80 Each sample is represented
by an 8-bit amplitude in offset binary form (i.e., 128 must be subtracted
from each unsigned byte to obtain a signed 8-bit amplitude). Format 160 Each
sample is represented by a 16-bit amplitude in offset binary form (i.e., 32,768
must be subtracted from each unsigned byte pair to obtain a signed 16-bit
amplitude).  As for format 16, the least significant byte of each pair is
first. Format 212 Each sample is represented by a 12-bit two’s complement amplitude.
 The first sample is obtained from the 12 least significant bits of the
first byte pair (stored least significant byte first).  The second sample
is formed from the 4 remaining bits of the first byte pair (which are the
4 high bits of the 12-bit sample) and the next byte (which contains the
remaining 8 bits of the second sample).  The process is repeated for each
successive pair of samples. Most of the signal files in PhysioBank are written
in format 212. Format 310 Each sample is represented by a 10-bit two’s-complement
amplitude.  The first sample is obtained from the 11 least significant bits
of the first byte pair (stored least significant byte first), with the
low bit discarded.  The second sample comes from the 11 least significant
bits of the second byte pair, in the same way as the first.  The third sample
is formed from the 5 most significant bits of each of the first two byte
pairs (those from the first byte pair are the least significant bits of
the third sample).  Note that the unused bit in each byte pair is set to
zero when using the WFDB library to write a format 310 signal file.  The
entire process is then repeated for each successive set of three samples. Format 311 Each sample is represented by a 10-bit two’s-complement amplitude.
 Three samples are bit-packed into a 32-bit integer as for format 310, but
the layout is different.  Each set of four bytes is stored in little-endian
order (least significant byte first, most significant byte last).  The first
sample is obtained from the 10 least significant bits of the 32-bit integer,
the second is obtained from the next 10 bits, the third from the next 10
bits, and the two most significant bits are unused (note that these bits
are set to zero when using the WFDB library to write a format 311 signal
file).  This process is repeated for each successive set of three samples. Formats 508, 516, and 524 Signals are compressed using the FLAC (Free Lossless
Audio Codec) format, either using 8 bits per sample (in format 508), 16
bits per sample (in format 516), or 24 bits per sample (in format 524).
 See https://xiph.org/flac/format.html for the full specification of these
formats. Note that these formats impose some restrictions on the signal
data that can be stored: The number of signals must equal the number of
channels in the FLAC stream, which implies there can be at most eight signals
stored in a single file. Every signal in the file must have the same sampling
frequency, and therefore the same number of samples per frame. Conversely,
some limitations apply when generating a FLAC stream to be used as a WFDB
signal file: The FLAC ‘bits per sample’ field must be 8, 16, or 24. Every
sample in the stream must be within the range of values indicated by the
‘bits per sample’ field. Note that the number of samples per frame is unrelated
to the size of the blocks used in FLAC compression; a single FLAC block
may contain multiple WFDB frames, and a single WFDB frame may be split
across multiple FLAC blocks. Also note that the FLAC ‘sample rate’ field should
be set to 96000, regardless of the actual sampling frequency of the signals.
 For compatibility with older FLAC implementations, this field should not
be set to 88200, 176400, or 192000. See Also annot (5) , header (5) , wfdbcal (5) WFDB Programmer’s Guide Author George B. Moody (george@mit.edu) Table of Contents Name Description Format 8 Format 16 Format 24 Format 32 Format 61 Format 80 Format 160 Format 212 Format 310 Format 311 Formats 508, 516, and 524 See Also Author Up: WFDB Applications Guide Please e-mail your comments and suggestions to webmaster@physionet.org , or post them to: PhysioNet MIT Room E25-505A 77 Massachusetts Avenue Cambridge, MA 02139 USA Updated 10 June 2022

Each sample is represented
by a 32-bit two’s complement amplitude stored least significant byte first. Format 61 Each sample is represented by a 16-bit two’s complement amplitude
stored most significant byte first. Format 80 Each sample is represented
by an 8-bit amplitude in offset binary form (i.e., 128 must be subtracted
from each unsigned byte to obtain a signed 8-bit amplitude). Format 160 Each
sample is represented by a 16-bit amplitude in offset binary form (i.e., 32,768
must be subtracted from each unsigned byte pair to obtain a signed 16-bit
amplitude).  As for format 16, the least significant byte of each pair is
first. Format 212 Each sample is represented by a 12-bit two’s complement amplitude.
 The first sample is obtained from the 12 least significant bits of the
first byte pair (stored least significant byte first).  The second sample
is formed from the 4 remaining bits of the first byte pair (which are the
4 high bits of the 12-bit sample) and the next byte (which contains the
remaining 8 bits of the second sample).  The process is repeated for each
successive pair of samples. Most of the signal files in PhysioBank are written
in format 212. Format 310 Each sample is represented by a 10-bit two’s-complement
amplitude.  The first sample is obtained from the 11 least significant bits
of the first byte pair (stored least significant byte first), with the
low bit discarded.  The second sample comes from the 11 least significant
bits of the second byte pair, in the same way as the first.  The third sample
is formed from the 5 most significant bits of each of the first two byte
pairs (those from the first byte pair are the least significant bits of
the third sample).  Note that the unused bit in each byte pair is set to
zero when using the WFDB library to write a format 310 signal file.  The
entire process is then repeated for each successive set of three samples. Format 311 Each sample is represented by a 10-bit two’s-complement amplitude.
 Three samples are bit-packed into a 32-bit integer as for format 310, but
the layout is different.  Each set of four bytes is stored in little-endian
order (least significant byte first, most significant byte last).  The first
sample is obtained from the 10 least significant bits of the 32-bit integer,
the second is obtained from the next 10 bits, the third from the next 10
bits, and the two most significant bits are unused (note that these bits
are set to zero when using the WFDB library to write a format 311 signal
file).  This process is repeated for each successive set of three samples. Formats 508, 516, and 524 Signals are compressed using the FLAC (Free Lossless
Audio Codec) format, either using 8 bits per sample (in format 508), 16
bits per sample (in format 516), or 24 bits per sample (in format 524).
 See https://xiph.org/flac/format.html for the full specification of these
formats. Note that these formats impose some restrictions on the signal
data that can be stored: The number of signals must equal the number of
channels in the FLAC stream, which implies there can be at most eight signals
stored in a single file. Every signal in the file must have the same sampling
frequency, and therefore the same number of samples per frame. Conversely,
some limitations apply when generating a FLAC stream to be used as a WFDB
signal file: The FLAC ‘bits per sample’ field must be 8, 16, or 24. Every
sample in the stream must be within the range of values indicated by the
‘bits per sample’ field. Note that the number of samples per frame is unrelated
to the size of the blocks used in FLAC compression; a single FLAC block
may contain multiple WFDB frames, and a single WFDB frame may be split
across multiple FLAC blocks. Also note that the FLAC ‘sample rate’ field should
be set to 96000, regardless of the actual sampling frequency of the signals.
 For compatibility with older FLAC implementations, this field should not
be set to 88200, 176400, or 192000. See Also annot (5) , header (5) , wfdbcal (5) WFDB Programmer’s Guide Author George B. Moody (george@mit.edu) Table of Contents Name Description Format 8 Format 16 Format 24 Format 32 Format 61 Format 80 Format 160 Format 212 Format 310 Format 311 Formats 508, 516, and 524 See Also Author Up: WFDB Applications Guide Please e-mail your comments and suggestions to webmaster@physionet.org , or post them to: PhysioNet MIT Room E25-505A 77 Massachusetts Avenue Cambridge, MA 02139 USA Updated 10 June 2022

Each sample is represented by a 16-bit two’s complement amplitude
stored most significant byte first. Format 80 Each sample is represented
by an 8-bit amplitude in offset binary form (i.e., 128 must be subtracted
from each unsigned byte to obtain a signed 8-bit amplitude). Format 160 Each
sample is represented by a 16-bit amplitude in offset binary form (i.e., 32,768
must be subtracted from each unsigned byte pair to obtain a signed 16-bit
amplitude).  As for format 16, the least significant byte of each pair is
first. Format 212 Each sample is represented by a 12-bit two’s complement amplitude.
 The first sample is obtained from the 12 least significant bits of the
first byte pair (stored least significant byte first).  The second sample
is formed from the 4 remaining bits of the first byte pair (which are the
4 high bits of the 12-bit sample) and the next byte (which contains the
remaining 8 bits of the second sample).  The process is repeated for each
successive pair of samples. Most of the signal files in PhysioBank are written
in format 212. Format 310 Each sample is represented by a 10-bit two’s-complement
amplitude.  The first sample is obtained from the 11 least significant bits
of the first byte pair (stored least significant byte first), with the
low bit discarded.  The second sample comes from the 11 least significant
bits of the second byte pair, in the same way as the first.  The third sample
is formed from the 5 most significant bits of each of the first two byte
pairs (those from the first byte pair are the least significant bits of
the third sample).  Note that the unused bit in each byte pair is set to
zero when using the WFDB library to write a format 310 signal file.  The
entire process is then repeated for each successive set of three samples. Format 311 Each sample is represented by a 10-bit two’s-complement amplitude.
 Three samples are bit-packed into a 32-bit integer as for format 310, but
the layout is different.  Each set of four bytes is stored in little-endian
order (least significant byte first, most significant byte last).  The first
sample is obtained from the 10 least significant bits of the 32-bit integer,
the second is obtained from the next 10 bits, the third from the next 10
bits, and the two most significant bits are unused (note that these bits
are set to zero when using the WFDB library to write a format 311 signal
file).  This process is repeated for each successive set of three samples. Formats 508, 516, and 524 Signals are compressed using the FLAC (Free Lossless
Audio Codec) format, either using 8 bits per sample (in format 508), 16
bits per sample (in format 516), or 24 bits per sample (in format 524).
 See https://xiph.org/flac/format.html for the full specification of these
formats. Note that these formats impose some restrictions on the signal
data that can be stored: The number of signals must equal the number of
channels in the FLAC stream, which implies there can be at most eight signals
stored in a single file. Every signal in the file must have the same sampling
frequency, and therefore the same number of samples per frame. Conversely,
some limitations apply when generating a FLAC stream to be used as a WFDB
signal file: The FLAC ‘bits per sample’ field must be 8, 16, or 24. Every
sample in the stream must be within the range of values indicated by the
‘bits per sample’ field. Note that the number of samples per frame is unrelated
to the size of the blocks used in FLAC compression; a single FLAC block
may contain multiple WFDB frames, and a single WFDB frame may be split
across multiple FLAC blocks. Also note that the FLAC ‘sample rate’ field should
be set to 96000, regardless of the actual sampling frequency of the signals.
 For compatibility with older FLAC implementations, this field should not
be set to 88200, 176400, or 192000. See Also annot (5) , header (5) , wfdbcal (5) WFDB Programmer’s Guide Author George B. Moody (george@mit.edu) Table of Contents Name Description Format 8 Format 16 Format 24 Format 32 Format 61 Format 80 Format 160 Format 212 Format 310 Format 311 Formats 508, 516, and 524 See Also Author Up: WFDB Applications Guide Please e-mail your comments and suggestions to webmaster@physionet.org , or post them to: PhysioNet MIT Room E25-505A 77 Massachusetts Avenue Cambridge, MA 02139 USA Updated 10 June 2022

Each sample is represented
by an 8-bit amplitude in offset binary form (i.e., 128 must be subtracted
from each unsigned byte to obtain a signed 8-bit amplitude). Format 160 Each
sample is represented by a 16-bit amplitude in offset binary form (i.e., 32,768
must be subtracted from each unsigned byte pair to obtain a signed 16-bit
amplitude).  As for format 16, the least significant byte of each pair is
first. Format 212 Each sample is represented by a 12-bit two’s complement amplitude.
 The first sample is obtained from the 12 least significant bits of the
first byte pair (stored least significant byte first).  The second sample
is formed from the 4 remaining bits of the first byte pair (which are the
4 high bits of the 12-bit sample) and the next byte (which contains the
remaining 8 bits of the second sample).  The process is repeated for each
successive pair of samples. Most of the signal files in PhysioBank are written
in format 212. Format 310 Each sample is represented by a 10-bit two’s-complement
amplitude.  The first sample is obtained from the 11 least significant bits
of the first byte pair (stored least significant byte first), with the
low bit discarded.  The second sample comes from the 11 least significant
bits of the second byte pair, in the same way as the first.  The third sample
is formed from the 5 most significant bits of each of the first two byte
pairs (those from the first byte pair are the least significant bits of
the third sample).  Note that the unused bit in each byte pair is set to
zero when using the WFDB library to write a format 310 signal file.  The
entire process is then repeated for each successive set of three samples. Format 311 Each sample is represented by a 10-bit two’s-complement amplitude.
 Three samples are bit-packed into a 32-bit integer as for format 310, but
the layout is different.  Each set of four bytes is stored in little-endian
order (least significant byte first, most significant byte last).  The first
sample is obtained from the 10 least significant bits of the 32-bit integer,
the second is obtained from the next 10 bits, the third from the next 10
bits, and the two most significant bits are unused (note that these bits
are set to zero when using the WFDB library to write a format 311 signal
file).  This process is repeated for each successive set of three samples. Formats 508, 516, and 524 Signals are compressed using the FLAC (Free Lossless
Audio Codec) format, either using 8 bits per sample (in format 508), 16
bits per sample (in format 516), or 24 bits per sample (in format 524).
 See https://xiph.org/flac/format.html for the full specification of these
formats. Note that these formats impose some restrictions on the signal
data that can be stored: The number of signals must equal the number of
channels in the FLAC stream, which implies there can be at most eight signals
stored in a single file. Every signal in the file must have the same sampling
frequency, and therefore the same number of samples per frame. Conversely,
some limitations apply when generating a FLAC stream to be used as a WFDB
signal file: The FLAC ‘bits per sample’ field must be 8, 16, or 24. Every
sample in the stream must be within the range of values indicated by the
‘bits per sample’ field. Note that the number of samples per frame is unrelated
to the size of the blocks used in FLAC compression; a single FLAC block
may contain multiple WFDB frames, and a single WFDB frame may be split
across multiple FLAC blocks. Also note that the FLAC ‘sample rate’ field should
be set to 96000, regardless of the actual sampling frequency of the signals.
 For compatibility with older FLAC implementations, this field should not
be set to 88200, 176400, or 192000. See Also annot (5) , header (5) , wfdbcal (5) WFDB Programmer’s Guide Author George B. Moody (george@mit.edu) Table of Contents Name Description Format 8 Format 16 Format 24 Format 32 Format 61 Format 80 Format 160 Format 212 Format 310 Format 311 Formats 508, 516, and 524 See Also Author Up: WFDB Applications Guide Please e-mail your comments and suggestions to webmaster@physionet.org , or post them to: PhysioNet MIT Room E25-505A 77 Massachusetts Avenue Cambridge, MA 02139 USA Updated 10 June 2022

Each
sample is represented by a 16-bit amplitude in offset binary form (i.e., 32,768
must be subtracted from each unsigned byte pair to obtain a signed 16-bit
amplitude).  As for format 16, the least significant byte of each pair is
first. Format 212 Each sample is represented by a 12-bit two’s complement amplitude.
 The first sample is obtained from the 12 least significant bits of the
first byte pair (stored least significant byte first).  The second sample
is formed from the 4 remaining bits of the first byte pair (which are the
4 high bits of the 12-bit sample) and the next byte (which contains the
remaining 8 bits of the second sample).  The process is repeated for each
successive pair of samples. Most of the signal files in PhysioBank are written
in format 212. Format 310 Each sample is represented by a 10-bit two’s-complement
amplitude.  The first sample is obtained from the 11 least significant bits
of the first byte pair (stored least significant byte first), with the
low bit discarded.  The second sample comes from the 11 least significant
bits of the second byte pair, in the same way as the first.  The third sample
is formed from the 5 most significant bits of each of the first two byte
pairs (those from the first byte pair are the least significant bits of
the third sample).  Note that the unused bit in each byte pair is set to
zero when using the WFDB library to write a format 310 signal file.  The
entire process is then repeated for each successive set of three samples. Format 311 Each sample is represented by a 10-bit two’s-complement amplitude.
 Three samples are bit-packed into a 32-bit integer as for format 310, but
the layout is different.  Each set of four bytes is stored in little-endian
order (least significant byte first, most significant byte last).  The first
sample is obtained from the 10 least significant bits of the 32-bit integer,
the second is obtained from the next 10 bits, the third from the next 10
bits, and the two most significant bits are unused (note that these bits
are set to zero when using the WFDB library to write a format 311 signal
file).  This process is repeated for each successive set of three samples. Formats 508, 516, and 524 Signals are compressed using the FLAC (Free Lossless
Audio Codec) format, either using 8 bits per sample (in format 508), 16
bits per sample (in format 516), or 24 bits per sample (in format 524).
 See https://xiph.org/flac/format.html for the full specification of these
formats. Note that these formats impose some restrictions on the signal
data that can be stored: The number of signals must equal the number of
channels in the FLAC stream, which implies there can be at most eight signals
stored in a single file. Every signal in the file must have the same sampling
frequency, and therefore the same number of samples per frame. Conversely,
some limitations apply when generating a FLAC stream to be used as a WFDB
signal file: The FLAC ‘bits per sample’ field must be 8, 16, or 24. Every
sample in the stream must be within the range of values indicated by the
‘bits per sample’ field. Note that the number of samples per frame is unrelated
to the size of the blocks used in FLAC compression; a single FLAC block
may contain multiple WFDB frames, and a single WFDB frame may be split
across multiple FLAC blocks. Also note that the FLAC ‘sample rate’ field should
be set to 96000, regardless of the actual sampling frequency of the signals.
 For compatibility with older FLAC implementations, this field should not
be set to 88200, 176400, or 192000. See Also annot (5) , header (5) , wfdbcal (5) WFDB Programmer’s Guide Author George B. Moody (george@mit.edu) Table of Contents Name Description Format 8 Format 16 Format 24 Format 32 Format 61 Format 80 Format 160 Format 212 Format 310 Format 311 Formats 508, 516, and 524 See Also Author Up: WFDB Applications Guide Please e-mail your comments and suggestions to webmaster@physionet.org , or post them to: PhysioNet MIT Room E25-505A 77 Massachusetts Avenue Cambridge, MA 02139 USA Updated 10 June 2022

Each sample is represented by a 12-bit two’s complement amplitude.
 The first sample is obtained from the 12 least significant bits of the
first byte pair (stored least significant byte first).  The second sample
is formed from the 4 remaining bits of the first byte pair (which are the
4 high bits of the 12-bit sample) and the next byte (which contains the
remaining 8 bits of the second sample).  The process is repeated for each
successive pair of samples. Most of the signal files in PhysioBank are written
in format 212. Format 310 Each sample is represented by a 10-bit two’s-complement
amplitude.  The first sample is obtained from the 11 least significant bits
of the first byte pair (stored least significant byte first), with the
low bit discarded.  The second sample comes from the 11 least significant
bits of the second byte pair, in the same way as the first.  The third sample
is formed from the 5 most significant bits of each of the first two byte
pairs (those from the first byte pair are the least significant bits of
the third sample).  Note that the unused bit in each byte pair is set to
zero when using the WFDB library to write a format 310 signal file.  The
entire process is then repeated for each successive set of three samples. Format 311 Each sample is represented by a 10-bit two’s-complement amplitude.
 Three samples are bit-packed into a 32-bit integer as for format 310, but
the layout is different.  Each set of four bytes is stored in little-endian
order (least significant byte first, most significant byte last).  The first
sample is obtained from the 10 least significant bits of the 32-bit integer,
the second is obtained from the next 10 bits, the third from the next 10
bits, and the two most significant bits are unused (note that these bits
are set to zero when using the WFDB library to write a format 311 signal
file).  This process is repeated for each successive set of three samples. Formats 508, 516, and 524 Signals are compressed using the FLAC (Free Lossless
Audio Codec) format, either using 8 bits per sample (in format 508), 16
bits per sample (in format 516), or 24 bits per sample (in format 524).
 See https://xiph.org/flac/format.html for the full specification of these
formats. Note that these formats impose some restrictions on the signal
data that can be stored: The number of signals must equal the number of
channels in the FLAC stream, which implies there can be at most eight signals
stored in a single file. Every signal in the file must have the same sampling
frequency, and therefore the same number of samples per frame. Conversely,
some limitations apply when generating a FLAC stream to be used as a WFDB
signal file: The FLAC ‘bits per sample’ field must be 8, 16, or 24. Every
sample in the stream must be within the range of values indicated by the
‘bits per sample’ field. Note that the number of samples per frame is unrelated
to the size of the blocks used in FLAC compression; a single FLAC block
may contain multiple WFDB frames, and a single WFDB frame may be split
across multiple FLAC blocks. Also note that the FLAC ‘sample rate’ field should
be set to 96000, regardless of the actual sampling frequency of the signals.
 For compatibility with older FLAC implementations, this field should not
be set to 88200, 176400, or 192000. See Also annot (5) , header (5) , wfdbcal (5) WFDB Programmer’s Guide Author George B. Moody (george@mit.edu) Table of Contents Name Description Format 8 Format 16 Format 24 Format 32 Format 61 Format 80 Format 160 Format 212 Format 310 Format 311 Formats 508, 516, and 524 See Also Author Up: WFDB Applications Guide Please e-mail your comments and suggestions to webmaster@physionet.org , or post them to: PhysioNet MIT Room E25-505A 77 Massachusetts Avenue Cambridge, MA 02139 USA Updated 10 June 2022

Each sample is represented by a 10-bit two’s-complement
amplitude.  The first sample is obtained from the 11 least significant bits
of the first byte pair (stored least significant byte first), with the
low bit discarded.  The second sample comes from the 11 least significant
bits of the second byte pair, in the same way as the first.  The third sample
is formed from the 5 most significant bits of each of the first two byte
pairs (those from the first byte pair are the least significant bits of
the third sample).  Note that the unused bit in each byte pair is set to
zero when using the WFDB library to write a format 310 signal file.  The
entire process is then repeated for each successive set of three samples. Format 311 Each sample is represented by a 10-bit two’s-complement amplitude.
 Three samples are bit-packed into a 32-bit integer as for format 310, but
the layout is different.  Each set of four bytes is stored in little-endian
order (least significant byte first, most significant byte last).  The first
sample is obtained from the 10 least significant bits of the 32-bit integer,
the second is obtained from the next 10 bits, the third from the next 10
bits, and the two most significant bits are unused (note that these bits
are set to zero when using the WFDB library to write a format 311 signal
file).  This process is repeated for each successive set of three samples. Formats 508, 516, and 524 Signals are compressed using the FLAC (Free Lossless
Audio Codec) format, either using 8 bits per sample (in format 508), 16
bits per sample (in format 516), or 24 bits per sample (in format 524).
 See https://xiph.org/flac/format.html for the full specification of these
formats. Note that these formats impose some restrictions on the signal
data that can be stored: The number of signals must equal the number of
channels in the FLAC stream, which implies there can be at most eight signals
stored in a single file. Every signal in the file must have the same sampling
frequency, and therefore the same number of samples per frame. Conversely,
some limitations apply when generating a FLAC stream to be used as a WFDB
signal file: The FLAC ‘bits per sample’ field must be 8, 16, or 24. Every
sample in the stream must be within the range of values indicated by the
‘bits per sample’ field. Note that the number of samples per frame is unrelated
to the size of the blocks used in FLAC compression; a single FLAC block
may contain multiple WFDB frames, and a single WFDB frame may be split
across multiple FLAC blocks. Also note that the FLAC ‘sample rate’ field should
be set to 96000, regardless of the actual sampling frequency of the signals.
 For compatibility with older FLAC implementations, this field should not
be set to 88200, 176400, or 192000. See Also annot (5) , header (5) , wfdbcal (5) WFDB Programmer’s Guide Author George B. Moody (george@mit.edu) Table of Contents Name Description Format 8 Format 16 Format 24 Format 32 Format 61 Format 80 Format 160 Format 212 Format 310 Format 311 Formats 508, 516, and 524 See Also Author Up: WFDB Applications Guide Please e-mail your comments and suggestions to webmaster@physionet.org , or post them to: PhysioNet MIT Room E25-505A 77 Massachusetts Avenue Cambridge, MA 02139 USA Updated 10 June 2022

Each sample is represented by a 10-bit two’s-complement amplitude.
 Three samples are bit-packed into a 32-bit integer as for format 310, but
the layout is different.  Each set of four bytes is stored in little-endian
order (least significant byte first, most significant byte last).  The first
sample is obtained from the 10 least significant bits of the 32-bit integer,
the second is obtained from the next 10 bits, the third from the next 10
bits, and the two most significant bits are unused (note that these bits
are set to zero when using the WFDB library to write a format 311 signal
file).  This process is repeated for each successive set of three samples. Formats 508, 516, and 524 Signals are compressed using the FLAC (Free Lossless
Audio Codec) format, either using 8 bits per sample (in format 508), 16
bits per sample (in format 516), or 24 bits per sample (in format 524).
 See https://xiph.org/flac/format.html for the full specification of these
formats. Note that these formats impose some restrictions on the signal
data that can be stored: The number of signals must equal the number of
channels in the FLAC stream, which implies there can be at most eight signals
stored in a single file. Every signal in the file must have the same sampling
frequency, and therefore the same number of samples per frame. Conversely,
some limitations apply when generating a FLAC stream to be used as a WFDB
signal file: The FLAC ‘bits per sample’ field must be 8, 16, or 24. Every
sample in the stream must be within the range of values indicated by the
‘bits per sample’ field. Note that the number of samples per frame is unrelated
to the size of the blocks used in FLAC compression; a single FLAC block
may contain multiple WFDB frames, and a single WFDB frame may be split
across multiple FLAC blocks. Also note that the FLAC ‘sample rate’ field should
be set to 96000, regardless of the actual sampling frequency of the signals.
 For compatibility with older FLAC implementations, this field should not
be set to 88200, 176400, or 192000. See Also annot (5) , header (5) , wfdbcal (5) WFDB Programmer’s Guide Author George B. Moody (george@mit.edu) Table of Contents Name Description Format 8 Format 16 Format 24 Format 32 Format 61 Format 80 Format 160 Format 212 Format 310 Format 311 Formats 508, 516, and 524 See Also Author Up: WFDB Applications Guide Please e-mail your comments and suggestions to webmaster@physionet.org , or post them to: PhysioNet MIT Room E25-505A 77 Massachusetts Avenue Cambridge, MA 02139 USA Updated 10 June 2022

Signals are compressed using the FLAC (Free Lossless
Audio Codec) format, either using 8 bits per sample (in format 508), 16
bits per sample (in format 516), or 24 bits per sample (in format 524).
 See https://xiph.org/flac/format.html for the full specification of these
formats. Note that these formats impose some restrictions on the signal
data that can be stored: The number of signals must equal the number of
channels in the FLAC stream, which implies there can be at most eight signals
stored in a single file. Every signal in the file must have the same sampling
frequency, and therefore the same number of samples per frame. Conversely,
some limitations apply when generating a FLAC stream to be used as a WFDB
signal file: The FLAC ‘bits per sample’ field must be 8, 16, or 24. Every
sample in the stream must be within the range of values indicated by the
‘bits per sample’ field. Note that the number of samples per frame is unrelated
to the size of the blocks used in FLAC compression; a single FLAC block
may contain multiple WFDB frames, and a single WFDB frame may be split
across multiple FLAC blocks. Also note that the FLAC ‘sample rate’ field should
be set to 96000, regardless of the actual sampling frequency of the signals.
 For compatibility with older FLAC implementations, this field should not
be set to 88200, 176400, or 192000. See Also annot (5) , header (5) , wfdbcal (5) WFDB Programmer’s Guide Author George B. Moody (george@mit.edu) Table of Contents Name Description Format 8 Format 16 Format 24 Format 32 Format 61 Format 80 Format 160 Format 212 Format 310 Format 311 Formats 508, 516, and 524 See Also Author Up: WFDB Applications Guide Please e-mail your comments and suggestions to webmaster@physionet.org , or post them to: PhysioNet MIT Room E25-505A 77 Massachusetts Avenue Cambridge, MA 02139 USA Updated 10 June 2022

The number of signals must equal the number of
channels in the FLAC stream, which implies there can be at most eight signals
stored in a single file.

Every signal in the file must have the same sampling
frequency, and therefore the same number of samples per frame.

Conversely,
some limitations apply when generating a FLAC stream to be used as a WFDB
signal file: The FLAC ‘bits per sample’ field must be 8, 16, or 24. Every
sample in the stream must be within the range of values indicated by the
‘bits per sample’ field. Note that the number of samples per frame is unrelated
to the size of the blocks used in FLAC compression; a single FLAC block
may contain multiple WFDB frames, and a single WFDB frame may be split
across multiple FLAC blocks. Also note that the FLAC ‘sample rate’ field should
be set to 96000, regardless of the actual sampling frequency of the signals.
 For compatibility with older FLAC implementations, this field should not
be set to 88200, 176400, or 192000. See Also annot (5) , header (5) , wfdbcal (5) WFDB Programmer’s Guide Author George B. Moody (george@mit.edu) Table of Contents Name Description Format 8 Format 16 Format 24 Format 32 Format 61 Format 80 Format 160 Format 212 Format 310 Format 311 Formats 508, 516, and 524 See Also Author Up: WFDB Applications Guide Please e-mail your comments and suggestions to webmaster@physionet.org , or post them to: PhysioNet MIT Room E25-505A 77 Massachusetts Avenue Cambridge, MA 02139 USA Updated 10 June 2022

The FLAC ‘bits per sample’ field must be 8, 16, or 24.

Every
sample in the stream must be within the range of values indicated by the
‘bits per sample’ field.

Note that the number of samples per frame is unrelated
to the size of the blocks used in FLAC compression; a single FLAC block
may contain multiple WFDB frames, and a single WFDB frame may be split
across multiple FLAC blocks. Also note that the FLAC ‘sample rate’ field should
be set to 96000, regardless of the actual sampling frequency of the signals.
 For compatibility with older FLAC implementations, this field should not
be set to 88200, 176400, or 192000. See Also annot (5) , header (5) , wfdbcal (5) WFDB Programmer’s Guide Author George B. Moody (george@mit.edu) Table of Contents Name Description Format 8 Format 16 Format 24 Format 32 Format 61 Format 80 Format 160 Format 212 Format 310 Format 311 Formats 508, 516, and 524 See Also Author Up: WFDB Applications Guide Please e-mail your comments and suggestions to webmaster@physionet.org , or post them to: PhysioNet MIT Room E25-505A 77 Massachusetts Avenue Cambridge, MA 02139 USA Updated 10 June 2022

Also note that the FLAC ‘sample rate’ field should
be set to 96000, regardless of the actual sampling frequency of the signals.
 For compatibility with older FLAC implementations, this field should not
be set to 88200, 176400, or 192000. See Also annot (5) , header (5) , wfdbcal (5) WFDB Programmer’s Guide Author George B. Moody (george@mit.edu) Table of Contents Name Description Format 8 Format 16 Format 24 Format 32 Format 61 Format 80 Format 160 Format 212 Format 310 Format 311 Formats 508, 516, and 524 See Also Author Up: WFDB Applications Guide Please e-mail your comments and suggestions to webmaster@physionet.org , or post them to: PhysioNet MIT Room E25-505A 77 Massachusetts Avenue Cambridge, MA 02139 USA Updated 10 June 2022

See Also annot (5) , header (5) , wfdbcal (5) WFDB Programmer’s Guide Author George B. Moody (george@mit.edu) Table of Contents Name Description Format 8 Format 16 Format 24 Format 32 Format 61 Format 80 Format 160 Format 212 Format 310 Format 311 Formats 508, 516, and 524 See Also Author Up: WFDB Applications Guide Please e-mail your comments and suggestions to webmaster@physionet.org , or post them to: PhysioNet MIT Room E25-505A 77 Massachusetts Avenue Cambridge, MA 02139 USA Updated 10 June 2022

Table of Contents Name Description Format 8 Format 16 Format 24 Format 32 Format 61 Format 80 Format 160 Format 212 Format 310 Format 311 Formats 508, 516, and 524 See Also Author Up: WFDB Applications Guide Please e-mail your comments and suggestions to webmaster@physionet.org , or post them to: PhysioNet MIT Room E25-505A 77 Massachusetts Avenue Cambridge, MA 02139 USA Updated 10 June 2022

Table of Contents Name Description Format 8 Format 16 Format 24 Format 32 Format 61 Format 80 Format 160 Format 212 Format 310 Format 311 Formats 508, 516, and 524 See Also Author Up: WFDB Applications Guide Please e-mail your comments and suggestions to webmaster@physionet.org , or post them to: PhysioNet MIT Room E25-505A 77 Massachusetts Avenue Cambridge, MA 02139 USA Updated 10 June 2022

Name Description Format 8 Format 16 Format 24 Format 32 Format 61 Format 80 Format 160 Format 212 Format 310 Format 311 Formats 508, 516, and 524 See Also Author Up: WFDB Applications Guide Please e-mail your comments and suggestions to webmaster@physionet.org , or post them to: PhysioNet MIT Room E25-505A 77 Massachusetts Avenue Cambridge, MA 02139 USA Updated 10 June 2022

Up: WFDB Applications Guide Please e-mail your comments and suggestions to webmaster@physionet.org , or post them to: PhysioNet MIT Room E25-505A 77 Massachusetts Avenue Cambridge, MA 02139 USA Updated 10 June 2022

Please e-mail your comments and suggestions to webmaster@physionet.org , or post them to: PhysioNet MIT Room E25-505A 77 Massachusetts Avenue Cambridge, MA 02139 USA Updated 10 June 2022

PhysioNet MIT Room E25-505A 77 Massachusetts Avenue Cambridge, MA 02139 USA Updated 10 June 2022
