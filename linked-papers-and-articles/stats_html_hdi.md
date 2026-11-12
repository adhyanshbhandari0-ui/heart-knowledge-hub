# stats.html#hdi

**Source:** https://neuropsychology.github.io/NeuroKit/functions/stats.html

---

x ( Union[list, np.array, pd.Series] ) – Vectors of values.

x ( Union[list, np.array, pd.Series] ) – Vectors of values.

y ( Union[list, np.array, pd.Series] ) – Vectors of values.

y ( Union[list, np.array, pd.Series] ) – Vectors of values.

method ( str ) – Correlation method. Can be one of "pearson" , "spearman" , "kendall" .

method ( str ) – Correlation method. Can be one of "pearson" , "spearman" , "kendall" .

show ( bool ) – Draw a scatterplot with a regression line.

show ( bool ) – Draw a scatterplot with a regression line.

x ( Union[list, np.array, pd.Series] ) – A vector of values.

x ( Union[list, np.array, pd.Series] ) – A vector of values.

desired_length ( int ) – The amount of values in the returned density estimation.

desired_length ( int ) – The amount of values in the returned density estimation.

bandwidth ( float ) – Passed to the method argument from the density_bandwidth() function.

bandwidth ( float ) – Passed to the method argument from the density_bandwidth() function.

show ( bool ) – Display the density plot.

show ( bool ) – Display the density plot.

**kwargs – Additional arguments to be passed to density_bandwidth() .

**kwargs – Additional arguments to be passed to density_bandwidth() .

x – The x axis of the density estimation. y – The y axis of the density estimation.

x – The x axis of the density estimation.

x – The x axis of the density estimation.

y – The y axis of the density estimation.

y – The y axis of the density estimation.

Compute distance using different metrics.

X ( array or DataFrame ) – A dataframe of values.

X ( array or DataFrame ) – A dataframe of values.

method ( str ) – The method to use. One of "mahalanobis" or "mean" for the average distance from the
mean.

method ( str ) – The method to use. One of "mahalanobis" or "mean" for the average distance from the
mean.

array – Vector containing the distance values.

Compute the Highest Density Interval (HDI) of a distribution. All points within this interval
have a higher probability density than points outside the interval. The HDI can be used in the
context of uncertainty characterisation of posterior distributions (in the Bayesian farmework)
as Credible Interval (CI). Unlike equal-tailed intervals that typically exclude 2.5% from each
tail of the distribution and always include the median, the HDI is not equal-tailed and
therefore always includes the mode(s) of posterior distributions.

x ( Union[list, np.array, pd.Series] ) – A vector of values.

x ( Union[list, np.array, pd.Series] ) – A vector of values.

ci ( float ) – Value of probability of the (credible) interval - CI (between 0 and 1) to be estimated.
Default to .95 (95%).

ci ( float ) – Value of probability of the (credible) interval - CI (between 0 and 1) to be estimated.
Default to .95 (95%).

show ( bool ) – If True , the function will produce a figure.

show ( bool ) – If True , the function will produce a figure.

**kwargs ( Line2D properties ) – Other arguments to be passed to nk.density() .

**kwargs ( Line2D properties ) – Other arguments to be passed to nk.density() .

float(s) – The HDI low and high limits. fig – Distribution plot.

Median Absolute Deviation: a “robust” version of standard deviation

x ( Union[list, np.array, pd.Series] ) – A vector of values.

x ( Union[list, np.array, pd.Series] ) – A vector of values.

constant ( float ) – Scale factor. Use 1.4826 for results similar to default R.

constant ( float ) – Scale factor. Use 1.4826 for results similar to default R.

https://en.wikipedia.org/wiki/Median_absolute_deviation

https://en.wikipedia.org/wiki/Median_absolute_deviation

Rescale a numeric variable to a new range.

data ( Union[list, np.array, pd.Series] ) – Raw data.

data ( Union[list, np.array, pd.Series] ) – Raw data.

to ( list ) – New range of values of the data after rescaling. Must be a list or tuple of two values. If
more values, the function will assume it is another signal and will derive the min and max
from it.

to ( list ) – New range of values of the data after rescaling. Must be a list or tuple of two values. If
more values, the function will assume it is another signal and will derive the min and max
from it.

scale ( list ) – A list or tuple of two values specifying the actual range
of the data. If None , the minimum and the maximum of the
provided data will be used.

scale ( list ) – A list or tuple of two values specifying the actual range
of the data. If None , the minimum and the maximum of the
provided data will be used.

Performs a standardization of data (Z-scoring), i.e., centering and scaling, so that the data is
expressed in terms of standard deviation (i.e., mean = 0, SD = 1) or Median Absolute Deviance
(median = 0, MAD = 1).

data ( Union[list, np.array, pd.Series] ) – Raw data.

data ( Union[list, np.array, pd.Series] ) – Raw data.

robust ( bool ) – If True , centering is done by substracting the median from the variables and dividing
it by the median absolute deviation (MAD). If False , variables are standardized by
substracting the mean and dividing it by the standard deviation (SD).

robust ( bool ) – If True , centering is done by substracting the median from the variables and dividing
it by the median absolute deviation (MAD). If False , variables are standardized by
substracting the mean and dividing it by the standard deviation (SD).

window ( int ) – Perform a rolling window standardization, i.e., apply a standardization on a window of the
specified number of samples that rolls along the main axis of the signal. Can be used for
complex detrending.

window ( int ) – Perform a rolling window standardization, i.e., apply a standardization on a window of the
specified number of samples that rolls along the main axis of the signal. Can be used for
complex detrending.

**kwargs ( optional ) – Other arguments to be passed to pandas.rolling() .

**kwargs ( optional ) – Other arguments to be passed to pandas.rolling() .

Visualize a distribution with density, histogram, boxplot and rugs plots all at once.

Performs clustering of data using different algorithms.

kmedoids : k-medoids clustering, a more stable version of k-means.

kmedoids : k-medoids clustering, a more stable version of k-means.

aahc : Atomize and Agglomerate Hierarchical Clustering. Computationally heavy.

aahc : Atomize and Agglomerate Hierarchical Clustering. Computationally heavy.

data ( np.ndarray ) – Matrix array of data (E.g., an array (channels, times) of M/EEG data).

data ( np.ndarray ) – Matrix array of data (E.g., an array (channels, times) of M/EEG data).

method ( str ) – The algorithm for clustering. Can be one of "kmeans" (default), "kmod" , "kmedoids" , "pca" , "ica" , "aahc" , "hierarchical" , "spectral" , "mixture" , "mixturebayesian" .

method ( str ) – The algorithm for clustering. Can be one of "kmeans" (default), "kmod" , "kmedoids" , "pca" , "ica" , "aahc" , "hierarchical" , "spectral" , "mixture" , "mixturebayesian" .

n_clusters ( int ) – The desired number of clusters.

n_clusters ( int ) – The desired number of clusters.

random_state ( Union[int, numpy.random.RandomState] ) – The RandomState for the random number generator. Defaults to None , in which case a
different random state is chosen each time this function is called.

random_state ( Union[int, numpy.random.RandomState] ) – The RandomState for the random number generator. Defaults to None , in which case a
different random state is chosen each time this function is called.

optimize ( bool ) – Optimized method in Poulsen et al. (2018) for the k -means modified method.

optimize ( bool ) – Optimized method in Poulsen et al. (2018) for the k -means modified method.

**kwargs – Other arguments to be passed into sklearn functions.

**kwargs – Other arguments to be passed into sklearn functions.

clustering ( DataFrame ) – Information about the distance of samples from their respective clusters. clusters ( np.ndarray ) – Coordinates of cluster centers, which has a shape of n_clusters x n_features. info ( dict ) – Information about the number of clusters, the function and model used for clustering.

clustering ( DataFrame ) – Information about the distance of samples from their respective clusters.

clustering ( DataFrame ) – Information about the distance of samples from their respective clusters.

clusters ( np.ndarray ) – Coordinates of cluster centers, which has a shape of n_clusters x n_features.

clusters ( np.ndarray ) – Coordinates of cluster centers, which has a shape of n_clusters x n_features.

info ( dict ) – Information about the number of clusters, the function and model used for clustering.

info ( dict ) – Information about the number of clusters, the function and model used for clustering.

Park, H. S., & Jun, C. H. (2009). A simple and fast algorithm for K-medoids
clustering. Expert systems with applications, 36(2), 3336-3341.

Park, H. S., & Jun, C. H. (2009). A simple and fast algorithm for K-medoids
clustering. Expert systems with applications, 36(2), 3336-3341.

Find the optimal number of clusters based on different indices of quality of fit.

data ( np.ndarray ) – An array (channels, times) of M/EEG data.

data ( np.ndarray ) – An array (channels, times) of M/EEG data.

method ( str ) – The clustering algorithm to be passed into nk.cluster() .

method ( str ) – The clustering algorithm to be passed into nk.cluster() .

n_max ( int ) – Runs the clustering alogrithm from 1 to n_max desired clusters in nk.cluster() with
quality metrices produced for each cluster number.

n_max ( int ) – Runs the clustering alogrithm from 1 to n_max desired clusters in nk.cluster() with
quality metrices produced for each cluster number.

show ( bool ) – Plot indices normalized on the same scale.

show ( bool ) – Plot indices normalized on the same scale.

**kwargs – Other arguments to be passed into nk.cluster() and nk.cluster_quality() .

**kwargs – Other arguments to be passed into nk.cluster() and nk.cluster_quality() .

DataFrame – The different quality scores for each number of clusters: Score_Silhouette Score_Calinski Score_Bouldin Score_VarianceExplained Score_GAP Score_GAPmod Score_GAP_diff Score_GAPmod_diff

DataFrame – The different quality scores for each number of clusters:

Compute quality of the clustering using several metrics.

data ( np.ndarray ) – A matrix array of data (e.g., channels, sample points of M/EEG data)

data ( np.ndarray ) – A matrix array of data (e.g., channels, sample points of M/EEG data)

clustering ( DataFrame ) – Information about the distance of samples from their respective clusters, generated from cluster() .

clustering ( DataFrame ) – Information about the distance of samples from their respective clusters, generated from cluster() .

clusters ( np.ndarray ) – Coordinates of cluster centers, which has a shape of n_clusters x n_features, generated
from cluster() .

clusters ( np.ndarray ) – Coordinates of cluster centers, which has a shape of n_clusters x n_features, generated
from cluster() .

info ( dict ) – Information about the number of clusters, the function and model used for clustering,
generated from cluster() .

info ( dict ) – Information about the number of clusters, the function and model used for clustering,
generated from cluster() .

n_random ( int ) – The number of random initializations to cluster random data for calculating the GAP
statistic.

n_random ( int ) – The number of random initializations to cluster random data for calculating the GAP
statistic.

random_state ( None, int, numpy.random.RandomState or numpy.random.Generator ) – Seed for the random number generator. See for misc.check_random_state for further information.

random_state ( None, int, numpy.random.RandomState or numpy.random.Generator ) – Seed for the random number generator. See for misc.check_random_state for further information.

**kwargs – Other argument to be passed on, for instance GFP as 'sd' in microstates.

**kwargs – Other argument to be passed on, for instance GFP as 'sd' in microstates.

individual ( DataFrame ) – Indices of cluster quality scores for each sample point. general ( DataFrame ) – Indices of cluster quality scores for all clusters.

individual ( DataFrame ) – Indices of cluster quality scores for each sample point.

individual ( DataFrame ) – Indices of cluster quality scores for each sample point.

general ( DataFrame ) – Indices of cluster quality scores for all clusters.

general ( DataFrame ) – Indices of cluster quality scores for all clusters.

Tibshirani, R., Walther, G., & Hastie, T. (2001). Estimating the number of clusters in a
data set via the gap statistic. Journal of the Royal Statistical Society: Series B
(Statistical Methodology), 63(2), 411-423.

Tibshirani, R., Walther, G., & Hastie, T. (2001). Estimating the number of clusters in a
data set via the gap statistic. Journal of the Royal Statistical Society: Series B
(Statistical Methodology), 63(2), 411-423.

Mohajer, M., Englmeier, K. H., & Schmid, V. J. (2011). A comparison of Gap statistic
definitions with and without logarithm function. arXiv preprint arXiv:1103.4767.

Mohajer, M., Englmeier, K. H., & Schmid, V. J. (2011). A comparison of Gap statistic
definitions with and without logarithm function. arXiv preprint arXiv:1103.4767.

Also specific and direct access functions can be used, such as fit_mse() , fit_rmse() and fit_r2() .

y ( Union[list, np.array, pd.Series] ) – The response variable (the y axis).

y ( Union[list, np.array, pd.Series] ) – The response variable (the y axis).

y_predicted ( Union[list, np.array, pd.Series] ) – The fitted data generated by a model.

y_predicted ( Union[list, np.array, pd.Series] ) – The fitted data generated by a model.

n_parameters ( int ) – Number of model parameters (for the degrees of freedom used in R2).

n_parameters ( int ) – Number of model parameters (for the degrees of freedom used in R2).

dict – A dictionary containing different indices of fit error.

Performs a LOWESS (LOcally WEighted Scatter-plot Smoother) regression.

y ( Union[list, np.array, pd.Series] ) – The response variable (the y axis).

y ( Union[list, np.array, pd.Series] ) – The response variable (the y axis).

X ( Union[list, np.array, pd.Series] ) – Explanatory variable (the x axis). If None , will treat y as a continuous signal (useful
for smoothing).

X ( Union[list, np.array, pd.Series] ) – Explanatory variable (the x axis). If None , will treat y as a continuous signal (useful
for smoothing).

alpha ( float ) – The parameter which controls the degree of smoothing, which corresponds to the proportion
of the samples to include in local regression.

alpha ( float ) – The parameter which controls the degree of smoothing, which corresponds to the proportion
of the samples to include in local regression.

order ( int ) – Degree of the polynomial to fit. Can be 1 or 2 (default).

order ( int ) – Degree of the polynomial to fit. Can be 1 or 2 (default).

array – Prediction of the LOESS algorithm. dict – Dictionary containing additional information such as the parameters ( order and alpha ).

array – Prediction of the LOESS algorithm.

array – Prediction of the LOESS algorithm.

dict – Dictionary containing additional information such as the parameters ( order and alpha ).

dict – Dictionary containing additional information such as the parameters ( order and alpha ).

signal_smooth , signal_detrend , fit_error

https://simplyor.netlify.com/loess-from-scratch-in-python-animation.en-us/

https://simplyor.netlify.com/loess-from-scratch-in-python-animation.en-us/

Performs a polynomial regression of given order.

X ( Union[list, np.array, pd.Series] ) – The values to classify.

X ( Union[list, np.array, pd.Series] ) – The values to classify.

n_clusters ( int ) – Number of components to look for.

n_clusters ( int ) – Number of components to look for.

pd.DataFrame – DataFrame containing the probability of belonging to each cluster. dict – Dictionary containing additional information such as the parameters ( n_clusters() ).

pd.DataFrame – DataFrame containing the probability of belonging to each cluster.

pd.DataFrame – DataFrame containing the probability of belonging to each cluster.

dict – Dictionary containing additional information such as the parameters ( n_clusters() ).

dict – Dictionary containing additional information such as the parameters ( n_clusters() ).

Performs a polynomial regression of given order.

y ( Union[list, np.array, pd.Series] ) – The response variable (the y axis).

y ( Union[list, np.array, pd.Series] ) – The response variable (the y axis).

X ( Union[list, np.array, pd.Series] ) – Explanatory variable (the x axis). If None , will treat y as a continuous signal.

X ( Union[list, np.array, pd.Series] ) – Explanatory variable (the x axis). If None , will treat y as a continuous signal.

order ( int ) – The order of the polynomial. 0, 1 or > 1 for a baseline, linear or polynomial fit,
respectively. Can also be "auto" , in which case it will attempt to find the optimal
order to minimize the RMSE.

order ( int ) – The order of the polynomial. 0, 1 or > 1 for a baseline, linear or polynomial fit,
respectively. Can also be "auto" , in which case it will attempt to find the optimal
order to minimize the RMSE.

method ( str ) – If "raw" (default), compute standard polynomial coefficients. If "orthogonal" ,
compute orthogonal polynomials (and is equivalent to R’s poly default behavior).

method ( str ) – If "raw" (default), compute standard polynomial coefficients. If "orthogonal" ,
compute orthogonal polynomials (and is equivalent to R’s poly default behavior).

array – Prediction of the regression. dict – Dictionary containing additional information such as the parameters ( order ) used and the coefficients ( coefs ).

dict – Dictionary containing additional information such as the parameters ( order ) used and the coefficients ( coefs ).

dict – Dictionary containing additional information such as the parameters ( order ) used and the coefficients ( coefs ).

signal_detrend , fit_error , fit_polynomial_findorder

Any function appearing below this point is not explicitly part of the documentation and should be added. Please open an issue if there is one.

Bandwidth Selection for Density Estimation

Bandwidth selector for density() estimation. See bw_method argument in scipy.stats.gaussian_kde() .

The "KernSmooth" method is adapted from the dpik() function from the KernSmooth R
package. In this case, it estimates the optimal AMISE bandwidth using the direct plug-in method
with 2 levels for the Parzen-Rosenblatt estimator with Gaussian kernel.

x ( Union[list, np.array, pd.Series] ) – A vector of values.

x ( Union[list, np.array, pd.Series] ) – A vector of values.

method ( float ) – The bandwidth of the kernel. The larger the values, the smoother the estimation. Can be a
number, or "scott" or "silverman" (see bw_method argument in scipy.stats.gaussian_kde() ), or "KernSmooth" .

method ( float ) – The bandwidth of the kernel. The larger the values, the smoother the estimation. Can be a
number, or "scott" or "silverman" (see bw_method argument in scipy.stats.gaussian_kde() ), or "KernSmooth" .

resolution ( int ) – Only when method="KernSmooth" . The number of equally-spaced points over which binning
is performed to obtain kernel functional approximation (see gridsize argument in KernSmooth::dpik() ).

resolution ( int ) – Only when method="KernSmooth" . The number of equally-spaced points over which binning
is performed to obtain kernel functional approximation (see gridsize argument in KernSmooth::dpik() ).

Jones, W. M. (1995). Kernel Smoothing, Chapman & Hall.

Jones, W. M. (1995). Kernel Smoothing, Chapman & Hall.

Find the optimal order for polynomial fitting. Currently, the only method implemented is
RMSE minimization.

y ( Union[list, np.array, pd.Series] ) – The response variable (the y axis).

y ( Union[list, np.array, pd.Series] ) – The response variable (the y axis).

X ( Union[list, np.array, pd.Series] ) – Explanatory variable (the x axis). If ‘None’, will treat y as a continuous signal.

X ( Union[list, np.array, pd.Series] ) – Explanatory variable (the x axis). If ‘None’, will treat y as a continuous signal.

max_order ( int ) – The maximum order to test.

max_order ( int ) – The maximum order to test.

y = np.cos(np.linspace(start=0, stop=10, num=100))

nk.fit_polynomial_findorder(y, max_order=10)
