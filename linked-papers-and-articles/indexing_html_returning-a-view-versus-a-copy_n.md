# indexing.html#returning-a-view-versus-a-copy\n

**Source:** https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html

---

The axis labeling information in pandas objects serves many purposes:

Identifies data (i.e. provides metadata ) using known indicators,
important for analysis, visualization, and interactive console display.

Identifies data (i.e. provides metadata ) using known indicators,
important for analysis, visualization, and interactive console display.

Enables automatic and explicit data alignment.

Enables automatic and explicit data alignment.

Allows intuitive getting and setting of subsets of the data set.

Allows intuitive getting and setting of subsets of the data set.

In this section, we will focus on the final point: namely, how to slice, dice,
and generally get and set subsets of pandas objects. The primary focus will be
on Series and DataFrame as they have received more development attention in
this area.

The Python and NumPy indexing operators [] and attribute operator . provide quick and easy access to pandas data structures across a wide range
of use cases. This makes interactive work intuitive, as there’s little new
to learn if you already know how to deal with Python dictionaries and NumPy
arrays. However, since the type of the data to be accessed isn’t known in
advance, directly using standard operators has some optimization limits. For
production code, we recommended that you take advantage of the optimized
pandas data access methods exposed in this chapter.

See the MultiIndex / Advanced Indexing for MultiIndex and more advanced indexing documentation.

See the cookbook for some advanced strategies.

Object selection has had a number of user-requested additions in order to
support more explicit location based indexing. pandas now supports three types
of multi-axis indexing.

.loc is primarily label based, but may also be used with a boolean array. .loc will raise KeyError when the items are not found. Allowed inputs are: A single label, e.g. 5 or 'a' (Note that 5 is interpreted as a label of the index. This use is not an integer position along the
index.). A list or array of labels ['a', 'b', 'c'] . A slice object with labels 'a':'f' (Note that contrary to usual Python
slices, both the start and the stop are included, when present in the
index! See Slicing with labels and Endpoints are inclusive .) A boolean array (any NA values will be treated as False ). A callable function with one argument (the calling Series or DataFrame) and
that returns valid output for indexing (one of the above). A tuple of row (and column) indices whose elements are one of the
above inputs. See more at Selection by Label .

.loc is primarily label based, but may also be used with a boolean array. .loc will raise KeyError when the items are not found. Allowed inputs are:

A single label, e.g. 5 or 'a' (Note that 5 is interpreted as a label of the index. This use is not an integer position along the
index.).

A single label, e.g. 5 or 'a' (Note that 5 is interpreted as a label of the index. This use is not an integer position along the
index.).

A list or array of labels ['a', 'b', 'c'] .

A list or array of labels ['a', 'b', 'c'] .

A slice object with labels 'a':'f' (Note that contrary to usual Python
slices, both the start and the stop are included, when present in the
index! See Slicing with labels and Endpoints are inclusive .)

A slice object with labels 'a':'f' (Note that contrary to usual Python
slices, both the start and the stop are included, when present in the
index! See Slicing with labels and Endpoints are inclusive .)

A boolean array (any NA values will be treated as False ).

A boolean array (any NA values will be treated as False ).

A callable function with one argument (the calling Series or DataFrame) and
that returns valid output for indexing (one of the above).

A callable function with one argument (the calling Series or DataFrame) and
that returns valid output for indexing (one of the above).

A tuple of row (and column) indices whose elements are one of the
above inputs.

A tuple of row (and column) indices whose elements are one of the
above inputs.

.iloc is primarily integer position based (from 0 to length-1 of the axis), but may also be used with a boolean
array. .iloc will raise IndexError if a requested
indexer is out-of-bounds, except slice indexers which allow
out-of-bounds indexing.  (this conforms with Python/NumPy slice semantics).  Allowed inputs are: An integer e.g. 5 . A list or array of integers [4, 3, 0] . A slice object with ints 1:7 . A boolean array (any NA values will be treated as False ). A callable function with one argument (the calling Series or DataFrame) and
that returns valid output for indexing (one of the above). A tuple of row (and column) indices whose elements are one of the
above inputs. See more at Selection by Position , Advanced Indexing and Advanced
Hierarchical .

.iloc is primarily integer position based (from 0 to length-1 of the axis), but may also be used with a boolean
array. .iloc will raise IndexError if a requested
indexer is out-of-bounds, except slice indexers which allow
out-of-bounds indexing.  (this conforms with Python/NumPy slice semantics).  Allowed inputs are:

A boolean array (any NA values will be treated as False ).

A boolean array (any NA values will be treated as False ).

A callable function with one argument (the calling Series or DataFrame) and
that returns valid output for indexing (one of the above).

A callable function with one argument (the calling Series or DataFrame) and
that returns valid output for indexing (one of the above).

A tuple of row (and column) indices whose elements are one of the
above inputs.

A tuple of row (and column) indices whose elements are one of the
above inputs.

See more at Selection by Position , Advanced Indexing and Advanced
Hierarchical .

.loc , .iloc , and also [] indexing can accept a callable as indexer. See more at Selection By Callable . Note Destructuring tuple keys into row (and column) indexes occurs before callables are applied, so you cannot return a tuple from
a callable to index both rows and columns.

.loc , .iloc , and also [] indexing can accept a callable as indexer. See more at Selection By Callable .

Destructuring tuple keys into row (and column) indexes occurs before callables are applied, so you cannot return a tuple from
a callable to index both rows and columns.

Getting values from an object with multi-axes selection uses the following
notation (using .loc as an example, but the following applies to .iloc as
well). Any of the axes accessors may be the null slice : . Axes left out of
the specification are assumed to be : , e.g. p.loc['a'] is equivalent to p.loc['a', :] .

As mentioned when introducing the data structures in the last section , the primary function of indexing with [] (a.k.a. __getitem__ for those familiar with implementing class behavior in Python) is selecting out
lower-dimensional slices. The following table shows return type values when
indexing pandas objects with [] :

DataFrame with columns corresponding to [colname]

DataFrame with columns corresponding to list_of_colnames

The same principle applies to label-based selection with .loc : a
list-like of labels preserves the corresponding axis (so df.loc[:, ["A"]] returns a DataFrame , even when the list contains a
single label), while a scalar label reduces the axis when labels on that
axis are unique (so df.loc[:, "A"] typically returns a Series ; if "A" is duplicated on the axis, a DataFrame is returned instead).
See Selection by label for details.

Here we construct a simple time series data set to use for illustrating the
indexing functionality:

None of the indexing functionality is time series specific unless
specifically stated.

Thus, as per above, we have the most basic indexing using [] :

You can pass a list of columns to [] to select columns in that order.
If a column is not contained in the DataFrame, an exception will be
raised. Multiple columns can also be set in this manner:

You may find this useful for applying a transform (in-place) to a subset of the
columns.

pandas aligns all AXES when setting Series and DataFrame from .loc .

This will not modify df because the column alignment is before value assignment.

The correct way to swap column values is by using raw values:

However, pandas does not align AXES when setting Series and DataFrame from .iloc because .iloc operates by position.

This will modify df because the column alignment is not done before value assignment.

DataFrame.select() returns a DataFrame with the requested columns in the
given order, similar to passing a list of columns to [] . As a method, it
can be used within a chain of operations. Columns can be given as individual
arguments or as a single list:

In addition to existing columns, computed columns can be included via pandas.col() expressions or callables. A positional expression keeps the
name of the underlying column, while a keyword argument names the resulting
column. Later arguments can refer to columns computed earlier in the same call:

A computed column with the same name as an existing column replaces it for
later arguments. It does not replace a column that was already selected, so
the result can contain duplicate column labels:

You may access an index on a Series or  column on a DataFrame directly
as an attribute:

You can use this access only if the index element is a valid Python identifier, e.g. s.1 is not allowed.
See here for an explanation of valid identifiers .

You can use this access only if the index element is a valid Python identifier, e.g. s.1 is not allowed.
See here for an explanation of valid identifiers .

The attribute will not be available if it conflicts with an existing method name, e.g. s.min is not allowed, but s['min'] is possible.

The attribute will not be available if it conflicts with an existing method name, e.g. s.min is not allowed, but s['min'] is possible.

Similarly, the attribute will not be available if it conflicts with any of the following list: index , major_axis , minor_axis , items .

Similarly, the attribute will not be available if it conflicts with any of the following list: index , major_axis , minor_axis , items .

In any of these cases, standard indexing will still work, e.g. s['1'] , s['min'] , and s['index'] will
access the corresponding element or column.

In any of these cases, standard indexing will still work, e.g. s['1'] , s['min'] , and s['index'] will
access the corresponding element or column.

If you are using the IPython environment, you may also use tab-completion to
see these accessible attributes.

You can also assign a dict to a row of a DataFrame :

You can use attribute access to modify an existing element of a Series or column of a DataFrame, but be careful;
if you try to use attribute access to create a new column, it creates a new attribute rather than a
new column and will this raise a UserWarning :

The most robust and consistent way of slicing ranges along arbitrary axes is
described in the Selection by Position section
detailing the .iloc method. For now, we explain the semantics of slicing using the [] operator.

When the Series has float indices, slicing will select by position.

With Series, the syntax works exactly as with an ndarray, returning a slice of
the values and the corresponding labels:

With DataFrame, slicing inside of [] slices the rows . This is provided
largely as a convenience since it is such a common operation.

.loc is strict when you present slicers that are not compatible (or convertible) with the index type. For example
using integers in a DatetimeIndex . These will raise a TypeError .

String likes in slicing can be convertible to the type of the index and lead to natural slicing.

pandas provides a suite of methods in order to have purely label based indexing . This is a strict inclusion based protocol.
Every label asked for must be in the index, or a KeyError will be raised.
When slicing, both the start bound AND the stop bound are included , if present in the index.
Integers are valid labels, but they refer to the label and not the position .

The .loc attribute is the primary access method. The following are valid inputs:

A single label, e.g. 5 or 'a' (Note that 5 is interpreted as a label of the index. This use is not an integer position along the index.).

A single label, e.g. 5 or 'a' (Note that 5 is interpreted as a label of the index. This use is not an integer position along the index.).

A list or array of labels ['a', 'b', 'c'] .

A list or array of labels ['a', 'b', 'c'] .

A slice object with labels 'a':'f' . Note that contrary to usual Python
slices, both the start and the stop are included, when present in the
index! See Slicing with labels .

A slice object with labels 'a':'f' . Note that contrary to usual Python
slices, both the start and the stop are included, when present in the
index! See Slicing with labels .

For getting a cross section using a label (equivalent to df.xs('a') ):

NA values in a boolean array propagate as False :

When using .loc with slices, if both the start and the stop labels are
present in the index, then elements located between the two (including them)
are returned:

If the index is sorted, and can be compared against start and stop labels,
then slicing will still work as expected, by selecting labels which rank between the two:

However, if at least one of the two is absent and the index is not sorted, an
error will be raised (since doing otherwise would be computationally expensive,
as well as potentially ambiguous for mixed type indexes). For instance, in the
above example, s.loc[1:6] would raise KeyError .

For the rationale behind this behavior, see Endpoints are inclusive .

Also, if the index has duplicate labels and either the start or the stop label is duplicated,
an error will be raised. For instance, in the above example, s.loc[2:5] would raise a KeyError .

For more information about duplicate labels, see Duplicate Labels .

When using a slice with a step, such as .loc[start:stop:step] , note that start and stop are interpreted as labels , while step is applied over
the positional index within that label range. This means a stepped slice
will behave differently than using the labels range(start, stop, step) when
the index is not contiguous integers.

For example, in a Series with a non-contiguous integer index:

The first applies step across positional locations between the start/stop
labels. The second selects each label directly.

Similarly, with a string-based index, the behavior is identical:

In both cases, start and stop determine the label boundaries (inclusive),
while step skips positions within that range, regardless of the index type.

pandas provides a suite of methods in order to get purely integer based indexing . The semantics follow closely Python and NumPy slicing. These are 0-based indexing. When slicing, the start bound is included , while the upper bound is excluded . Trying to use a non-integer, even a valid label will raise an IndexError .

The .iloc attribute is the primary access method. The following are valid inputs:

A tuple of row (and column) indexes, whose elements are one of the
above types.

A tuple of row (and column) indexes, whose elements are one of the
above types.

For getting a cross section using an integer position (equiv to df.xs(1) ):

Out of range slice indexes are handled gracefully just as in Python/NumPy.

Note that using slices that go out of bounds can result in
an empty axis (e.g. an empty DataFrame being returned).

A single indexer that is out of bounds will raise an IndexError .
A list of indexers where any element is out of bounds will raise an IndexError .

.loc , .iloc , and also [] indexing can accept a callable as indexer.
The callable must be a function with one argument (the calling Series or DataFrame) that returns valid output for indexing.

For .iloc indexing, returning a tuple from the callable is
not supported, since tuple destructuring for row and column indexes
occurs before applying callables.

You can use callable indexing in Series .

Using these methods / indexers, you can chain data selection operations
without using a temporary variable.

Combining positional and label-based indexing #

If you wish to get the 0th and the 2nd elements from the index in the ‘A’ column, you can do:

This can also be expressed using .iloc , by explicitly getting locations on the indexers, and using positional indexing to select things.

For getting multiple indexers, using .get_indexer :

The idiomatic way to achieve selecting potentially not-found elements is via .reindex() . See also the section on reindexing .

Alternatively, if you want to select only valid keys, the following is idiomatic and efficient; it is guaranteed to preserve the dtype of the selection.

Having a duplicated index will raise for a .reindex() :

Generally, you can intersect the desired labels with the current
axis, and then reindex.

However, this would still raise if your resulting index is duplicated.

A random selection of rows or columns from a Series or DataFrame with the sample() method. The method will sample rows by default, and accepts a specific number of rows/columns to return, or a fraction of rows.

By default, sample will return each row at most once, but one can also sample with replacement
using the replace option:

By default, each row has an equal probability of being selected, but if you want rows
to have different probabilities, you can pass the sample function sampling weights as weights . These weights can be a list, a NumPy array, or a Series, but they must be of the same length as the object you are sampling. Missing values will be treated as a weight of zero, and inf values are not allowed. If weights do not sum to 1, they will be re-normalized by dividing all weights by the sum of the weights. For example:

When applied to a DataFrame, you can use a column of the DataFrame as sampling weights
(provided you are sampling rows and not columns) by simply passing the name of the column
as a string.

sample also allows users to sample columns instead of rows using the axis argument.

Finally, one can also set a seed for sample ’s random number generator using the random_state argument, which will accept either an integer (as a seed) or a NumPy RandomState object.

The .loc/[] operations can perform enlargement when setting a non-existent key for that axis.

In the Series case this is effectively an appending operation.

A DataFrame can be enlarged on either axis via .loc .

This is like an append operation on the DataFrame .

Since indexing with [] must handle a lot of cases (single-label access,
slicing, boolean indexing, etc.), it has a bit of overhead in order to figure
out what you’re asking for. If you only want to access a scalar value, the
fastest way is to use the at and iat methods, which are implemented on
all of the data structures.

Similarly to loc , at provides label based scalar lookups, while, iat provides integer based lookups analogously to iloc

You can also set using these same indexers.

at previously could enlarge the object in-place if the indexer was missing,
but this behavior is deprecated. Use .loc instead for setting values with
new keys:

Another common operation is the use of boolean vectors to filter the data.
The operators are: | for or , & for and , and ~ for not .
These must be grouped by using parentheses, since by default Python will
evaluate an expression such as df['A'] > 2 & df['B'] < 3 as df['A'] > (2 & df['B']) < 3 , while the desired evaluation order is (df['A'] > 2) & (df['B'] < 3) .

Using a boolean vector to index a Series works exactly as in a NumPy ndarray:

You may select rows from a DataFrame using a boolean vector the same length as
the DataFrame’s index (for example, something derived from one of the columns
of the DataFrame):

List comprehensions and the map method of Series can also be used to produce
more complex criteria:

With the choice methods Selection by Label , Selection by Position ,
and Advanced Indexing you may select along more than one axis using boolean vectors combined with other indexing expressions.

While loc supports two kinds of boolean indexing, iloc only supports indexing with a
boolean array. If the indexer is a boolean Series , an error will be raised. For instance,
in the following example, df.iloc[s.values, 1] is ok. The boolean indexer is an array.
But df.iloc[s, 1] would raise ValueError .

DataFrame.filter() and Series.filter() also accept a boolean mask
through the cond keyword, keeping the rows where the mask is True. A Series mask is aligned on the index; any other array-like must have
the same length as the index.

cond may also be a callable that returns a boolean mask, or an expression
created with pandas.col() . These two forms may be passed positionally,
which is convenient in a method chain where the intermediate object has no
name:

Pass axis=1 to filter columns instead of rows:

Missing values in the mask are treated as False by default, matching df[mask] for a mask with nullable boolean dtype. Pass na=True to keep
the corresponding rows instead, or na="raise" to raise an error:

Consider the isin() method of Series , which returns a boolean
vector that is true wherever the Series elements exist in the passed list.
This allows you to select rows where one or more columns have values you want:

The same method is available for Index objects and is useful for the cases
when you don’t know which of the sought labels are in fact present:

In addition to that, MultiIndex allows selecting a separate level to use
in the membership check:

DataFrame also has an isin() method.  When calling isin , pass a set of
values as either an array or dict.  If values is an array, isin returns
a DataFrame of booleans that is the same shape as the original DataFrame, with True
wherever the element is in the sequence of values.

Oftentimes you’ll want to match certain values with certain columns.
Just make values a dict where the key is the column, and the value is
a list of items you want to check for.

To return the DataFrame of booleans where the values are not in the original DataFrame,
use the ~ operator:

Combine DataFrame’s isin with the any() and all() methods to
quickly select subsets of your data that meet a given criteria.
To select a row where each column meets its own criterion:

Selecting values from a Series with a boolean vector generally returns a
subset of the data. To guarantee that selection output has the same shape as
the original data, you can use the where method in Series and DataFrame .

To return a Series of the same shape as the original:

Selecting values from a DataFrame with a boolean criterion now also preserves
input data shape. where is used under the hood as the implementation.
The code below is equivalent to df.where(df < 0) .

In addition, where takes an optional other argument for replacement of
values where the condition is False, in the returned copy.

You may wish to set values based on some boolean criteria.
This can be done intuitively like so:

where returns a modified copy of the data.

The signature for DataFrame.where() differs from numpy.where() .
Roughly df1.where(m, df2) is equivalent to np.where(m, df1, df2) .

Furthermore, where aligns the input boolean condition (ndarray or DataFrame),
such that partial selection with setting is possible. This is analogous to
partial setting via .loc (but on the contents rather than the axis labels).

Where can also accept axis and level parameters to align the input when
performing the where .

This is equivalent to (but faster than) the following.

where can accept a callable as condition and other arguments. The function must
be with one argument (the calling Series or DataFrame) and that returns valid output
as condition and other argument.

mask() is the inverse boolean operation of where .

Setting with enlargement conditionally using numpy() #

An alternative to where() is to use numpy.where() .
Combined with setting a new column, you can use it to enlarge a DataFrame where the
values are determined conditionally.

Consider you have two choices to choose from in the following DataFrame. And you want to
set a new column color to ‘green’ when the second column has ‘Z’.  You can do the
following:

If you have multiple conditions, you can use numpy.select() to achieve that.  Say
corresponding to three conditions there are three choice of colors, with a fourth color
as a fallback, you can do the following.

DataFrame objects have a query() method that allows selection using an expression.

You can get the value of the frame where column b has values
between the values of columns a and c . For example:

Do the same thing but fall back on a named index if there is no column
with the name a .

If instead you don’t want to or cannot name your index, you can use the name index in your query expression:

If the name of your index overlaps with a column name, the column name is
given precedence. For example,

You can still use the index in a query expression by using the special
identifier ‘index’:

If for some reason you have a column named index , then you can refer to
the index as ilevel_0 as well, but at this point you should consider
renaming your columns to something less ambiguous.

You can also use the levels of a DataFrame with a MultiIndex as if they were columns in the frame:

If the levels of the MultiIndex are unnamed, you can refer to them using
special names:

The convention is ilevel_0 , which means “index level 0” for the 0th level
of the index .

A use case for query() is when you have a collection of DataFrame objects that have a subset of column names (or index
levels/names) in common. You can pass the same query to both frames without having to specify which frame you’re interested in querying

query() Python versus pandas Syntax Comparison #

Slightly nicer by removing the parentheses (comparison operators bind tighter
than & and | ):

Pretty close to how you might write it on paper:

query() also supports special use of Python’s in and not in comparison operators, providing a succinct syntax for calling the isin method of a Series or DataFrame .

You can combine this with other expressions for very succinct queries:

Note that in and not in are evaluated in Python, since numexpr has no equivalent of this operation. However, only the in / not in expression itself is evaluated in vanilla Python. For example, in the
expression

(b + c + d) is evaluated by numexpr and then the in operation is evaluated in plain Python. In general, any operations that can
be evaluated using numexpr will be.

Special use of the == operator with list objects #

Comparing a list of values to a column using == / != works similarly
to in / not in .

You can negate boolean expressions with the word not or the ~ operator.

Of course, expressions can be arbitrarily complex too:

DataFrame.query() using numexpr is slightly faster than Python for
large frames.

You will only see the performance benefits of using the numexpr engine
with DataFrame.query() if your frame has more than approximately 100,000
rows.

This plot was created using a DataFrame with 3 columns each containing
floating point values generated using numpy.random.randn() .

If you want to identify and remove duplicate rows in a DataFrame,  there are
two methods that will help: duplicated and drop_duplicates . Each
takes as an argument the columns to use to identify duplicated rows.

duplicated returns a boolean vector whose length is the number of rows, and which indicates whether a row is duplicated.

duplicated returns a boolean vector whose length is the number of rows, and which indicates whether a row is duplicated.

By default, the first observed row of a duplicate set is considered unique, but
each method has a keep parameter to specify targets to be kept.

keep='first' (default): mark / drop duplicates except for the first occurrence.

keep='first' (default): mark / drop duplicates except for the first occurrence.

keep='last' : mark / drop duplicates except for the last occurrence.

keep='last' : mark / drop duplicates except for the last occurrence.

keep=False : mark  / drop all duplicates.

keep=False : mark  / drop all duplicates.

Also, you can pass a list of columns to identify duplications.

To drop duplicates by index value, use Index.duplicated then perform slicing.
The same set of options are available for the keep parameter.

Each of Series or DataFrame have a get method which can return a
default value.

Looking up values by index/column labels #

Sometimes you want to extract a set of values given a sequence of row labels
and column labels, this can be achieved by pandas.factorize and NumPy indexing.

For heterogeneous column types, we subset columns to avoid unnecessary NumPy conversions:

For homogeneous column types, it is fastest to skip column subsetting and go directly to NumPy:

Formerly this could be achieved with the dedicated DataFrame.lookup method
which was deprecated in version 1.2.0 and removed in version 2.0.0.

The pandas Index class and its subclasses can be viewed as
implementing an ordered multiset . Duplicates are allowed.

Index also provides the infrastructure necessary for
lookups, data alignment, and reindexing. The easiest way to create an Index directly is to pass a list or other sequence to Index :

If no dtype is given, Index tries to infer the dtype from the data.
It is also possible to give an explicit dtype when instantiating an Index :

You can also pass a name to be stored in the index:

The name, if set, will be shown in the console display:

Indexes are “mostly immutable”, but it is possible to set and change their name attribute. You can use the rename , set_names to set these attributes
directly, and they default to returning a copy.

See Advanced Indexing for usage of MultiIndexes.

set_names , set_levels , and set_codes also take an optional level argument

The two main operations are union and intersection .
Difference is provided via the .difference() method.

Also available is the symmetric_difference operation, which returns elements
that appear in either idx1 or idx2 , but not in both. This is
equivalent to the Index created by idx1.difference(idx2).union(idx2.difference(idx1)) ,
with duplicates dropped.

The resulting index from a set operation will be sorted in ascending order.

When performing Index.union() between indexes with different dtypes, the indexes
must be cast to a common dtype. Typically, though not always, this is object dtype. The
exception is when performing a union between integer and float data. In this case, the
integer values are converted to float

Even though Index can hold missing values ( NaN ), it should be avoided
if you do not want any unexpected results. For example, some operations
exclude missing values implicitly.

Index.fillna fills missing values with specified scalar value.

Occasionally you will load or create a data set into a DataFrame and want to
add an index after you’ve already done so. There are a couple of different
ways.

DataFrame has a set_index() method which takes a column name
(for a regular Index ) or a list of column names (for a MultiIndex ).
To create a new, re-indexed DataFrame:

The append keyword option allow you to keep the existing index and append
the given columns to a MultiIndex:

Other options in set_index allow you not drop the index columns.

As a convenience, there is a new function on DataFrame called reset_index() which transfers the index values into the
DataFrame’s columns and sets a simple integer index.
This is the inverse operation of set_index() .

The output is more similar to a SQL table or a record array. The names for the
columns derived from the index are the ones stored in the names attribute.

You can use the level keyword to remove only a portion of the index:

reset_index takes an optional parameter drop which if true simply
discards the index, instead of putting index values in the DataFrame’s columns.

You can assign a custom index to the index attribute:

Why does assignment fail when using chained indexing? #

Copy-on-Write is the new default with pandas 3.0.
This means that chained indexing will never work.
See this section for more context.

When assigning a Series to a DataFrame column, pandas performs automatic alignment
based on index labels. This is a fundamental behavior that can be surprising to
new users who might expect positional assignment.

Series values are matched to DataFrame rows by index label

Series values are matched to DataFrame rows by index label

Position/order in the Series doesn’t matter

Position/order in the Series doesn’t matter

Missing index labels result in NaN values

Missing index labels result in NaN values

This behavior is consistent across df[col] = series and df.loc[:, col] = series

This behavior is consistent across df[col] = series and df.loc[:, col] = series

You can think of this as reindexing the Series to the DataFrame index before
assignment (for example, df[col] = series.reindex(df.index) ).

# Create a DataFrame
df = pd.DataFrame({‘values’: [1, 2, 3]}, index=[‘x’, ‘y’, ‘z’])

# Series with matching indices (different order)
s1 = pd.Series([10, 20, 30], index=[‘z’, ‘x’, ‘y’])
df[‘aligned’] = s1  # Aligns by index, not position
print(df)

# Series with partial index match
s2 = pd.Series([100, 200], index=[‘x’, ‘z’])
df[‘partial’] = s2  # Missing ‘y’ gets NaN
print(df)

# Series with non-matching indices
s3 = pd.Series([1000, 2000], index=[‘a’, ‘b’])
df[‘nomatch’] = s3  # All values become NaN
print(df)

#Avoiding Confusion:
#If you want positional assignment instead of index alignment:
# reset the Series index to match DataFrame index
df[‘s1_values’] = s1.reindex(df.index)

While index alignment is consistent between df[col] = value and df.loc[:, col] = value (see the previous section), the two forms differ in
how they treat the column’s existing dtype:

df[col] = value replaces the column. The new column’s dtype is
inferred from value , regardless of what dtype the old column had.

df[col] = value replaces the column. The new column’s dtype is
inferred from value , regardless of what dtype the old column had.

df.loc[:, col] = value (and df.iloc[:, i] = value ) sets the values
in place in the existing column. The original dtype is preserved, and the
assignment will raise TypeError if value is not compatible with it.

df.loc[:, col] = value (and df.iloc[:, i] = value ) sets the values
in place in the existing column. The original dtype is preserved, and the
assignment will raise TypeError if value is not compatible with it.

This is most visible for ExtensionDtype columns
such as category , Int64 , boolean , or string , where the
replacing form silently drops the extension dtype:

The same distinction applies to nullable numeric and boolean dtypes:

Use df.loc[:, col] = value (or .iloc ) when you want to update every
value of an existing column while keeping its dtype.
