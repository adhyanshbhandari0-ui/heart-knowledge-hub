# 
    "In this and following tutorials you will work with ECG data through the CardIO framework.\n",
    "\n",
    "We suggest loading ECG data from the 2017 PhysioNet/CinC Challenge database of short single lead ECG recording. \n",
    "\n",
    "The PhysioNet archive contains 8.528 ECGs in [wfdb

**Source:** https://www.physionet.org/physiotools/wpg/wpg_35.htm

---

The WFDB_Time type is defined as a signed integer type of at least 32
bits, which means that it can represent sample numbers up to 2,147,483,647.  By
default, WFDB_Time is defined as an alias for the standard C long int , and many existing applications have been written with the
assumption that WFDB_Time and long int are interchangeable.

However, it is quite possible for a record to be longer than 2,147,483,647
samples (about 25 days of recording at 1 kHz) and it is useful to be able
to process such records on machines where a long int is only 32 bits.

If you are using a modern C compiler, with WFDB library version 10.7.0 or
later, it is possible to define WFDB_Time as long long int instead of long int .  This lets your program work with sample numbers as
large as 9,223,372,036,854,775,807, even on a 32-bit machine.  To do this, add
the following line at the very beginning of your source file, before including ‘ <wfdb/wfdb.h> ’:

If your program consists of multiple ‘ *.c ’ files, be sure to do the same
for each file.  Alternatively, you can define this macro on the C compiler
command line (e.g., -DWFDB_LARGETIME if you are using gcc ).

When doing this, you will also need to ensure that your program handles large
time values consistently, by using the WFDB_Time data type rather than long or long long , using WFDB_TIME_MAX rather than LONG_MAX or LLONG_MAX , using WFDB_Pd_TIME rather than "ld" or "lld" , and so forth.
