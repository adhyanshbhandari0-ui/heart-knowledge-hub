# 
    "In this example, we will try to approximate this Skin Conductance Response (SCR) using a [gamma distribution

**Source:** https://en.wikipedia.org/wiki/Gamma_distribution

---

In probability theory and statistics , the gamma distribution is a versatile two- parameter family of continuous probability distributions . [ 1 ] The exponential distribution , Erlang distribution , and chi-squared distribution are special cases of the gamma distribution. [ 2 ] There are two equivalent parameterizations in common use:

With a shape parameter α and a scale parameter θ

With a shape parameter α and a rate parameter ⁠ β = 1 / θ ⁠

In each of these forms, both parameters are positive real numbers.

The distribution has important applications in various fields, including econometrics , Bayesian statistics , and life testing. [ 3 ] In econometrics, the ( α , θ ) parameterization is common for modeling waiting times, such as the time until death, where it often takes the form of an Erlang distribution for integer α values. Bayesian statisticians prefer the ( α , β ) parameterization, utilizing the gamma distribution as a conjugate prior for several inverse scale parameters, facilitating analytical tractability in posterior distribution computations.

The gamma distribution is the maximum entropy probability distribution (both with respect to a uniform base measure and a 1 / x base measure) for a random variable X for which E [ X ] = αθ = α / β is fixed and greater than zero, and E [ln X ] = ψ ( α ) + ln θ = ψ ( α ) − ln β is fixed ( ψ is the digamma function ). [ 4 ]

The parameterization with α and θ appears to be more common in econometrics and other applied fields, where the gamma distribution is frequently used to model waiting times. For instance, in life testing , the waiting time until death is a random variable that is frequently modeled with a gamma distribution. See Hogg and Craig [ 5 ] for an explicit motivation.

The parameterization with α and β is more common in Bayesian statistics , [ 6 ] where the gamma distribution is used as a conjugate prior distribution for various types of inverse scale (rate) parameters, such as the λ of an exponential distribution or a Poisson distribution [ 7 ] – or for that matter, the β of the gamma distribution itself. The closely related inverse-gamma distribution is used as a conjugate prior for scale parameters, such as the variance of a normal distribution .

If α is a positive integer , then the distribution represents an Erlang distribution ; i.e., the sum of α independent exponentially distributed random variables , each of which has a mean of θ .

Characterization using shape α and rate β

The gamma distribution can be parameterized in terms of a shape parameter α and an inverse scale parameter β = 1/ θ , called a rate parameter . A random variable X that is gamma-distributed with shape α and rate β is denoted

The corresponding probability density function in the shape-rate parameterization is

f ( x ; α , β ) = x α − 1 e − β x β α Γ ( α ) for x > 0 α , β > 0 ,

where Γ ( α ) is the gamma function .
For all positive integers, Γ ( α ) = ( α − 1 ) ! .

The cumulative distribution function is the regularized gamma function:

F ( x ; α , β ) = ∫ 0 x f ( u ; α , β ) d u = γ ( α , β x ) Γ ( α ) ,

where γ ( α , β x ) is the lower incomplete gamma function .

If α is a positive integer (i.e., the distribution is an Erlang distribution ), the cumulative distribution function has the following series expansion: [ 8 ]

F ( x ; α , β ) = 1 − ∑ i = 0 α − 1 ( β x ) i i ! e − β x = e − β x ∑ i = α ∞ ( β x ) i i ! .

Characterization using shape α and scale θ

A random variable X that is gamma-distributed with shape α and scale θ is denoted by

The probability density function using the shape-scale parametrization is

f ( x ; α , θ ) = x α − 1 e − x / θ θ α Γ ( α ) for x > 0 and α , θ > 0.

Here Γ( α ) is the gamma function evaluated at α .

The cumulative distribution function is the regularized gamma function:

F ( x ; α , θ ) = ∫ 0 x f ( u ; α , θ ) d u = γ ( α , x θ ) Γ ( α ) ,

where γ ( α , x θ ) is the lower incomplete gamma function .

It can also be expressed as follows, if α is a positive integer (i.e., the distribution is an Erlang distribution ): [ 8 ]

F ( x ; α , θ ) = 1 − ∑ i = 0 α − 1 1 i ! ( x θ ) i e − x / θ = e − x / θ ∑ i = α ∞ 1 i ! ( x θ ) i .

Both parametrizations are common because either can be more convenient depending on the situation.

The mean of gamma distribution is given by the product of its shape and scale parameters: μ = α θ = α / β The variance is: σ 2 = α θ 2 = α / β 2 The square root of the inverse shape parameter gives the coefficient of variation : σ / μ = α − 0.5 = 1 / α

The skewness of the gamma distribution only depends on its shape parameter, α , and it is equal to 2 / α .

Unlike the mode and the mean, which have readily calculable formulas based on the parameters, the median does not have a closed-form equation. The median for this distribution is the value ν such that 1 Γ ( α ) θ α ∫ 0 ν x α − 1 e − x / θ d x = 1 2 .

A rigorous treatment of the problem of determining an asymptotic expansion and bounds for the median of the gamma distribution was handled first by Chen and Rubin, who proved that (for θ = 1 ) α − 1 3 < ν ( α ) < α , where μ ( α ) = α is the mean and ν ( α ) is the median of the Gamma ( α , 1 ) distribution. [ 9 ] For other values of the scale parameter, the mean scales to μ = α θ , and the median bounds and approximations would be similarly scaled by θ .

K. P. Choi found the first five terms in a Laurent series asymptotic approximation of the median by comparing the median to Ramanujan's θ function . [ 10 ] Berg and Pedersen found more terms: [ 11 ] ν ( α ) = α − 1 3 + 8 405 α − 1 + 184 25 515 α − 2 + 2248 3 444 525 α − 3 − 19 006 408 15 345 358 875 α − 4 − 𝒪 ( α − 5 ) + ⋯

Partial sums of these series are good approximations for high enough α ; they are not plotted in the figure, which is focused on the low- α region that is less well approximated.

Berg and Pedersen also proved many properties of the median, showing that it is a convex function of α , [ 12 ] and that the asymptotic behavior near α = 0 is ν ( α ) ≈ e − γ 2 − 1 / α (where γ is the Euler–Mascheroni constant ), and that for all α > 0 the median is bounded by α 2 − 1 / α < ν ( α ) < k e − 1 / 3 k . [ 11 ]

A closer linear upper bound, for α ≥ 1 only, was provided in 2021 by Gaunt and Merkle, [ 13 ] relying on the Berg and Pedersen result that the slope of ν ( α ) is everywhere less than 1: ν ( α ) ≤ α − 1 + log ⁡ 2 for α ≥ 1 (with equality at α = 1 )
which can be extended to a bound for all α > 0 by taking the max with the chord shown in the figure, since the median was proved convex. [ 12 ]

An approximation to the median that is asymptotically accurate at high α and reasonable down to α = 0.5 or a bit lower follows from the Wilson–Hilferty transformation : ν ( α ) = α ( 1 − 1 9 α ) 3 which goes negative for α < 1 / 9 .

In 2021, Lyon proposed several approximations of the form ν ( α ) ≈ 2 − 1 / α ( A + B α ) .  He conjectured values of A and B for which this approximation is an asymptotically tight upper or lower bound for all α > 0 . [ 14 ] In particular, he proposed these closed-form bounds, which he proved in 2023: [ 15 ]

ν L ∞ ( α ) = 2 − 1 / α ( log ⁡ 2 − 1 3 + α ) is a lower bound, asymptotically tight as α → ∞ ν U ( α ) = 2 − 1 / α ( e − γ + α ) is an upper bound, asymptotically tight as α → 0

Lyon also showed (informally in 2021, rigorously in 2023) two other lower bounds that are not closed-form expressions , including this one involving the gamma function , based on solving the integral expression substituting 1 for e − x : ν ( α ) > ( 2 Γ ( α + 1 ) ) − 1 / α (approaching equality as k → 0 )
and the tangent line at α = 1 where the derivative was found to be ν ′ ( 1 ) ≈ 0.9680448 : ν ( α ) ≥ ν ( 1 ) + ( α − 1 ) ν ′ ( 1 ) (with equality at k = 1 ) ν ( α ) ≥ log ⁡ 2 + ( α − 1 ) [ γ − 2 Ei ⁡ ( − log ⁡ 2 ) − log ⁡ log ⁡ 2 ] where Ei is the exponential integral . [ 14 ] [ 15 ]

Additionally, he showed that interpolations between bounds could provide excellent approximations or tighter bounds to the median, including an approximation that is exact at α = 1 (where ν ( 1 ) = log ⁡ 2 ) and has a maximum relative error less than 0.6%.  Interpolated approximations and bounds are all of the form ν ( α ) ≈ g ~ ( α ) ν L ∞ ( α ) + ( 1 − g ~ ( α ) ) ν U ( α ) where g ~ is an interpolating function running monotonially from 0 at low α to 1 at high α , approximating an ideal, or exact, interpolator g ( α ) : g ( α ) = ν U ( α ) − ν ( α ) ν U ( α ) − ν L ∞ ( α ) For the simplest interpolating function considered, a first-order rational function g ~ 1 ( α ) = α b 0 + α the tightest lower bound has b 0 = 8 405 + e − γ log ⁡ 2 − log 2 2 2 e − γ − log ⁡ 2 + 1 3 − log ⁡ 2 ≈ 0.143472 and the tightest upper bound has b 0 = e − γ − log ⁡ 2 + 1 3 1 − e − γ π 2 12 ≈ 0.374654 The interpolated bounds are plotted (mostly inside the yellow region) in the log–log plot shown.  Even tighter bounds are available using different interpolating functions, but not usually with closed-form parameters like these. [ 14 ]

If X i has a Gamma( α i , θ ) distribution for i = 1, 2, ..., N (i.e., all distributions have the same scale parameter θ ), then

∑ i = 1 N X i ∼ G a m m a ( ∑ i = 1 N α i , θ )

For the cases where the X i are independent but have different scale parameters, see Mathai [ 16 ] or Moschopoulos. [ 17 ]

The gamma distribution exhibits infinite divisibility .

c X ∼ G a m m a ( α , c θ ) , by moment generating functions,

X ∼ G a m m a ( α , β ) (shape-rate parameterization)

Indeed, we know that if X is an exponential r.v. with rate β , then cX is an exponential r.v. with rate β / c ; the same thing is valid with Gamma variates (and this can be checked using the moment-generating function , see, e.g., these notes , 10.4-(ii)): multiplication by a positive constant c divides the rate (or, equivalently, multiplies the scale).

The gamma distribution is a two-parameter exponential family with natural parameters α − 1 and −1/ θ (equivalently, α − 1 and − β ), and natural statistics X and ln X .

If the shape parameter α is held fixed, the resulting one-parameter family of distributions is a natural exponential family .

where ψ is the digamma function .  Likewise,

This can be derived using the exponential family formula for the moment generating function of the sufficient statistic , because one of the sufficient statistics of the gamma distribution is ln x .

H ⁡ ( X ) = E ⁡ [ − ln ⁡ p ( X ) ] = E ⁡ [ − α ln ⁡ β + ln ⁡ Γ ( α ) − ( α − 1 ) ln ⁡ X + β X ] = α − ln ⁡ β + ln ⁡ Γ ( α ) + ( 1 − α ) ψ ( α ) .

In the α , θ parameterization, the information entropy is given by

H ⁡ ( X ) = α + ln ⁡ θ + ln ⁡ Γ ( α ) + ( 1 − α ) ψ ( α ) .

The Kullback–Leibler divergence (KL-divergence), of Gamma( α p , β p ) ("true" distribution) from Gamma( α q , β q ) ("approximating" distribution) is given by [ 18 ]

D K L ( α p , β p ; α q , β q ) = ( α p − α q ) ψ ( α p ) − log ⁡ Γ ( α p ) Γ ( α q ) + α q log ⁡ β p β q + α p ( β q β p − 1 ) .

Written using the α , θ parameterization, the KL-divergence of Gamma( α p , θ p ) from Gamma( α q , θ q ) is given by

D K L ( α p , θ p ; α q , θ q ) = ( α p − α q ) ψ ( α p ) − log ⁡ Γ ( α p ) Γ ( α q ) + α q log ⁡ θ q θ p + α p ( θ p θ q − 1 ) .

The Laplace transform of the gamma PDF, which is related to the moment-generating function , is

F ( s ) = E ⁡ [ e − s X ] = 1 ( 1 + θ s ) α = ( β β + s ) α

(where X is a random variable distributed as Gamma ⁡ ( α , θ ) , or equivalently Gamma ⁡ ( α , β ) ).

The full width at half maximum of a unimodal probability distribution is the difference between the two values of the support that produce an output of half the function's maximum value when evaluated by the distribution's probability density function . For the gamma distribution with shape parameter α > 1 , the FWHM is [ 19 ]

F W H M = ( α − 1 ) θ [ W 0 ( − 2 − 1 / ( α − 1 ) e ) − W − 1 ( − 2 − 1 / ( α − 1 ) e ) ]

When α = 1 , the gamma distribution reduces to an exponential distribution , whose FWHM is

When α < 1 , the gamma distribution has no finite mode and therefore no well-defined FWHM.

Let X 1 , X 2 , … , X n be n independent and identically distributed random variables following an exponential distribution with rate parameter β , then ∑ i X i ∼ Gamma ⁡ ( n , β ) where n is the shape parameter and β is the rate, and X ¯ = 1 n ∑ i X i ∼ Gamma ⁡ ( n , n β ) .

If X ~ Gamma(1, β ) (in the shape–rate parametrization), then X has an exponential distribution with rate parameter β . In the shape-scale parametrization, X ~ Gamma(1, θ ) has an exponential distribution with rate parameter 1/ θ .

If X ~ Gamma( ν /2, 2) (in the shape–scale parametrization), then X is identical to χ 2 ( ν ) , the chi-squared distribution with ν degrees of freedom. Conversely, if Q ~ χ 2 ( ν ) and c is a positive constant, then cQ ~ Gamma( ν /2, 2 c ) .

If θ = 1/ α , one obtains the Schulz-Zimm distribution , which is most prominently used to model polymer chain lengths.

If α is an integer , the gamma distribution is an Erlang distribution and is the probability distribution of the waiting time until the α -th "arrival" in a one-dimensional Poisson process with intensity 1/ θ . If

If X has a Maxwell–Boltzmann distribution with parameter a , then

If X ~ Gamma( α , θ ) , then exp ⁡ X follows a log-gamma distribution. [ 20 ]

If X ~ Gamma( α , θ ) , then log ⁡ X follows an exponential-gamma (abbreviated exp-gamma) distribution. [ 21 ] It is sometimes incorrectly referred to as the log-gamma distribution. [ 22 ] Formulas for its mean and variance are in the section #Logarithmic expectation and variance .

If X ~ Gamma( α , θ ) , then X follows a generalized gamma distribution with parameters p = 2 , d = 2 α , and a = θ . [ citation needed ]

More generally, if X ~ Gamma( α , θ ) , then X q for q > 0 follows a generalized gamma distribution with parameters p = 1/ q , d = α / q , and a = θ q .

If X ~ Gamma( α , θ ) with shape α and scale θ , then 1/ X ~ Inv-Gamma( α , θ −1 ) (see Inverse-gamma distribution for derivation).

Parametrization 1: If X k ∼ Γ ( α k , θ k ) are independent, then α 2 θ 2 X 1 α 1 θ 1 X 2 ∼ F ( 2 α 1 , 2 α 2 ) , or equivalently, X 1 X 2 ∼ β ′ ( α 1 , α 2 , 1 , θ 1 θ 2 )

Parametrization 2: If X k ∼ Γ ( α k , β k ) are independent, then α 2 β 1 X 1 α 1 β 2 X 2 ∼ F ( 2 α 1 , 2 α 2 ) , or equivalently, X 1 X 2 ∼ β ′ ( α 1 , α 2 , 1 , β 2 β 1 )

If X ~ Gamma( α , θ ) and Y ~ Gamma( β , θ ) are independently distributed, then X /( X + Y ) has a beta distribution with parameters α and β , and X /( X + Y ) is independent of X + Y , which is Gamma( α + β , θ ) -distributed.

If X n ∼ Beta ( α , n β ) and Y n = n X n , then Y n converges in distribution to Gamma ( α , β ) defined under parametrization 2.

If X i ~ Gamma( α i , 1) are independently distributed, then the vector ( X 1 / S , ..., X n / S ) , where S = X 1 + ... + X n , follows a Dirichlet distribution with parameters α 1 , ..., α n .

For large α the gamma distribution converges to normal distribution with mean μ = αθ and variance σ 2 = αθ 2 .

The gamma distribution is the conjugate prior for the precision of the normal distribution with known mean .

The matrix gamma distribution and the Wishart distribution are multivariate generalizations of the gamma distribution (samples are positive-definite matrices rather than positive real numbers).

The gamma distribution is a special case of the generalized gamma distribution , the generalized integer gamma distribution , and the generalized inverse Gaussian distribution .

Among the discrete distributions, the negative binomial distribution is sometimes considered the discrete analog of the gamma distribution.

Tweedie distributions – the gamma distribution is a member of the family of Tweedie exponential dispersion models .

For the shape-scale parameterization x | θ ∼ Γ ( α , θ ) , if the scale parameter θ ∼ I G ( b , 1 ) where I G denotes the Inverse-gamma distribution , then the marginal distribution x ∼ β ′ ( α , b ) where β ′ denotes the Beta prime distribution .

If the shape parameter of the gamma distribution is known, but the inverse-scale parameter is unknown, then a gamma distribution for the inverse scale forms a conjugate prior. The compound distribution , which results from integrating out the inverse scale, has a closed-form solution known as the compound gamma distribution . [ 23 ]

If, instead, the shape parameter is known but the mean is unknown, with the prior of the mean being given by another gamma distribution, then it results in K-distribution .

The likelihood function for N iid observations ( x 1 , ..., x N ) is

L ( α , θ ) = ∏ i = 1 N f ( x i ; α , θ )

from which we calculate the log-likelihood function

ℓ ( α , θ ) = ( α − 1 ) ∑ i = 1 N ln ⁡ x i − ∑ i = 1 N x i θ − N α ln ⁡ θ − N ln ⁡ Γ ( α )

Finding the maximum with respect to θ by taking the derivative and setting it equal to zero yields the maximum likelihood estimator of the θ parameter, which equals the sample mean x ¯ divided by the shape parameter α :

Substituting this into the log-likelihood function gives

ℓ ( α ) = ( α − 1 ) ∑ i = 1 N ln ⁡ x i − N α − N α ln ⁡ ∑ i x i α N − N ln ⁡ Γ ( α )

We need at least two samples: N ≥ 2 , because for N = 1 , the function ℓ ( α ) increases without bounds as α → ∞ . For α > 0 , it can be verified that ℓ ( α ) is strictly concave , by using inequality properties of the polygamma function . Finding the maximum with respect to α by taking the derivative and setting it equal to zero yields

ln ⁡ α − ψ ( α ) = ln ⁡ ( 1 N ∑ i = 1 N x i ) − 1 N ∑ i = 1 N ln ⁡ x i = ln ⁡ x ¯ − ln ⁡ x ‾

where ψ is the digamma function and ln ⁡ x ‾ is the sample mean of ln x . There is no closed-form solution for α . The function is numerically very well behaved, so if a numerical solution is desired, it can be found using, for example, Newton's method . An initial value of k can be found either using the method of moments , or using the approximation

ln ⁡ α − ψ ( α ) ≈ 1 2 α ( 1 + 1 6 α + 1 )

s = ln ⁡ ( 1 N ∑ i = 1 N x i ) − 1 N ∑ i = 1 N ln ⁡ x i = ln ⁡ x ¯ − ln ⁡ x ‾

which is within 1.5% of the correct value. [ 24 ] An explicit form for the Newton–Raphson update of this initial guess is: [ 25 ]

α ← α − ln ⁡ α − ψ ( k ) − s 1 α − ψ ′ ( α ) .

At the maximum-likelihood estimate ( α ̂ , θ ̂ ) , the expected values for x and ln ⁡ x agree with the empirical averages: α ̂ θ ̂ = x ¯ and ψ ( α ̂ ) + ln ⁡ θ ̂ = ln ⁡ x ‾ .

For data, ( x 1 , … , x N ) , that is represented in a floating point format that underflows to 0 for values smaller than ε , the logarithms that are needed for the maximum-likelihood estimate will cause failure if there are any underflows. If we assume the data was generated by a gamma distribution with cdf F ( x ; α , θ ) , then the probability that there is at least one underflow is: Pr ⁡ ( underflow ) = 1 − ( 1 − F ( ε ; α , θ ) ) N This probability will approach 1 for small α and  large N . For example, at α = 1 0 − 2 , N = 1 0 4 and ε = 2.25 × 1 0 − 308 , Pr ⁡ ( underflow ) ≈ 0.9998 . A workaround is to instead have the data in logarithmic format.

In order to test an implementation of a maximum-likelihood estimator that takes logarithmic data as input, it is useful to be able to generate non-underflowing logarithms of random gamma variates, when α < 1 . Following the implementation in scipy.stats.loggamma , this can be done as follows: [ 26 ] sample Y ∼ Gamma ( α + 1 , θ ) and U ∼ Uniform independently. Then the required logarithmic sample is Z = ln ⁡ ( Y ) + ln ⁡ ( U ) / α , so that exp ⁡ ( Z ) ∼ Gamma ( k , θ ) .

There exist consistent closed-form estimators of α and θ that are derived from the likelihood of the generalized gamma distribution . [ 27 ]

α ̂ = N ∑ i = 1 N x i N ∑ i = 1 N x i ln ⁡ x i − ∑ i = 1 N x i ∑ i = 1 N ln ⁡ x i

θ ̂ = 1 N 2 ( N ∑ i = 1 N x i ln ⁡ x i − ∑ i = 1 N x i ∑ i = 1 N ln ⁡ x i )

Using the sample mean of x , the sample mean of ln x , and the sample mean of the product x ·ln x simplifies the expressions to:

α ̂ = x ¯ θ ̂ θ ̂ = x ln ⁡ x ‾ − x ¯ ln ⁡ x ‾ .

If the rate parameterization is used, the estimate of β ̂ = 1 / θ ̂ .

These estimators are not strictly maximum likelihood estimators, but are instead referred to as mixed type log-moment estimators. They have however similar efficiency as the maximum likelihood estimators.

Although these estimators are consistent, they have a small bias. A bias-corrected variant of the estimator for the scale θ is

A bias correction for the shape parameter α is given as [ 28 ]

α ~ = α ̂ − 1 N ( 3 α ̂ − 2 3 ( α ̂ 1 + α ̂ ) − 4 5 α ̂ ( 1 + α ̂ ) 2 )

With known α and unknown θ , the posterior density function for theta (using the standard scale-invariant prior for θ ) is

Pr ⁡ ( θ ∣ α , x 1 , … , x N ) ∝ 1 θ ∏ i = 1 N f ( x i ; α , θ )

y ≡ ∑ i = 1 N x i , Pr ⁡ ( θ ∣ α , x 1 , … , x N ) = C ( x i ) θ − N α − 1 e − y / θ

where the C (integration) constant does not depend on θ . The form of the posterior density reveals that 1 / θ is gamma-distributed with shape parameter Nα + 2 and rate parameter y . Integration with respect to θ can be carried out using a change of variables to find the integration constant

∫ 0 ∞ θ − N α − 1 + m e − y / θ d θ = ∫ 0 ∞ x N α − 1 − m e − x y d x = y − ( N α − m ) Γ ( N α − m )

The moments can be computed by taking the ratio ( m by m = 0 )

E ⁡ [ x m ] = Γ ( N α − m ) Γ ( N α ) y m

which shows that the mean ± standard deviation estimate of the posterior distribution for θ is

y N α − 1 ± y 2 ( N α − 1 ) 2 ( N α − 2 ) .

In Bayesian inference , the gamma distribution is the conjugate prior to many likelihood distributions: the Poisson , exponential , normal (with known mean), Pareto , gamma with known shape σ , inverse gamma with known shape parameter, and Gompertz with known scale parameter.

The gamma distribution's conjugate prior is: [ 29 ]

p ( α , θ ∣ p , q , r , s ) = 1 Z p α − 1 e − θ − 1 q Γ ( α ) r θ α s ,

where Z is the normalizing constant with no closed-form solution.
The posterior distribution can be found by updating the parameters as follows:

p ′ = p ∏ i x i , q ′ = q + ∑ i x i , r ′ = r + n , s ′ = s + n ,

where n is the number of observations, and x i is the i -th observation from the gamma distribution.

Consider a sequence of events, with the waiting time for each event being an exponential distribution with rate β . Then the waiting time for the n -th event to occur is the gamma distribution with integer shape α = n . This construction of the gamma distribution allows it to model a wide variety of phenomena where several sub-events, each taking time with exponential distribution, must happen in sequence for a major event to occur. [ 30 ] Examples include the waiting time of cell-division events , [ 31 ] number of compensatory mutations for a given mutation, [ 32 ] waiting time until a repair is necessary for a hydraulic system, [ 33 ] and so on.

In biophysics, the dwell time between steps of a molecular motor like ATP synthase is nearly exponential at constant ATP concentration, revealing that each step of the motor takes a single ATP hydrolysis. If there were n ATP hydrolysis events, then it would be a gamma distribution with degree n. [ 34 ]

The gamma distribution has been used to model the size of insurance claims [ 35 ] and rainfalls. [ 36 ] This means that aggregate insurance claims and the amount of rainfall accumulated in a reservoir are modelled by a gamma process – much like the exponential distribution generates a Poisson process .

The gamma distribution is also used to model errors in multi-level Poisson regression models because a mixture of Poisson distributions with gamma-distributed rates has a known closed form distribution, called negative binomial .

In wireless communication, the gamma distribution is used to model the multi-path fading of signal power; [ citation needed ] see also Rayleigh distribution and Rician distribution .

In oncology , the age distribution of cancer incidence often follows the gamma distribution, wherein the shape and scale parameters predict, respectively, the number of driver events and the time interval between them. [ 37 ] [ 38 ]

In neuroscience , the gamma distribution is often used to describe the distribution of inter-spike intervals . [ 39 ] [ 40 ]

In bacterial gene expression where protein production can occur in bursts, the copy number of a given protein often follows the gamma distribution, where the shape and scale parameters are, respectively, the mean number of bursts per cell cycle and the mean number of protein molecules produced per burst. [ 41 ]

In genomics , the gamma distribution was applied in peak calling step (i.e., in recognition of signal) in ChIP-chip [ 42 ] and ChIP-seq [ 43 ] data analysis.

In Bayesian statistics, the gamma distribution is widely used as a conjugate prior . It is the conjugate prior for the precision (i.e. inverse of the variance) of a normal distribution . It is also the conjugate prior for the exponential distribution .

In phylogenetics , the gamma distribution is the most commonly used approach to model among-sites rate variation [ 44 ] when maximum likelihood , Bayesian , or distance matrix methods are used to estimate phylogenetic trees. Phylogenetic analyzes that use the gamma distribution to model rate variation estimate a single parameter from the data because they limit consideration to distributions where α = β . This parameterization means that the mean of this distribution is 1 and the variance is 1/ α . Maximum likelihood and Bayesian methods typically use a discrete approximation to the continuous gamma distribution. [ 45 ] [ 46 ]

Given the scaling property above, it is enough to generate gamma variables with θ = 1 , as we can later convert to any value of β with a simple division.

Suppose we wish to generate random variables from Gamma( n + δ , 1) , where n is a non-negative integer and 0 < δ < 1 . Using the fact that a Gamma(1, 1) distribution is the same as an Exp(1) distribution, and noting the method of generating exponential variables , we conclude that if U is uniformly distributed on (0, 1], then −ln U is distributed Gamma(1, 1) (i.e. inverse transform sampling ). Now, using the " α -addition" property of gamma distribution, we expand this result:

where U k are all uniformly distributed on (0, 1] and independent . All that is left now is to generate a variable distributed as Gamma( δ , 1) for 0 < δ < 1 and apply the " α -addition" property once more. This is the most difficult part.

Random generation of gamma variates is discussed in detail by Devroye, [ 47 ] : 401–428 noting that none are uniformly fast for all shape parameters. For small values of the shape parameter, the algorithms are often not valid. [ 47 ] : 406 For arbitrary values of the shape parameter, one can apply the Ahrens and Dieter [ 48 ] modified acceptance-rejection method Algorithm GD (shape α ≥ 1 ), or transformation method [ 49 ] when 0 < α < 1 . Also see Cheng and Feast Algorithm GKM 3 [ 50 ] or Marsaglia's squeeze method. [ 51 ]

The following is a version of the Ahrens-Dieter acceptance–rejection method : [ 48 ]

Generate U , V and W as iid uniform (0, 1] variates.

If U ≤ e e + δ then ξ = V 1 / δ and η = W ξ δ − 1 . Otherwise, ξ = 1 − ln ⁡ V and η = W e − ξ .

A summary of this is θ ( ξ − ∑ i = 1 ⌊ α ⌋ ln ⁡ U i ) ∼ Γ ( α , θ ) where ⌊ α ⌋ is the integer part of α , ξ is generated via the algorithm above with δ = { α } (the fractional part of α ) and the U k are all independent.

While the above approach is technically correct, Devroye notes that it is linear in the value of α and generally is not a good choice. Instead, he recommends using either rejection-based or table-based methods, depending on context. [ 47 ] : 401–428

For example, Marsaglia's simple transformation-rejection method relying on one normal variate X and one uniform variate U : [ 26 ]

If v > 0 and ln ⁡ U < X 2 2 + d − d v + d ln ⁡ v return d v , else go back to step 2.

With 1 ≤ a = α generates a gamma distributed random number in time that is approximately constant with α .  The acceptance rate does depend on α , with an acceptance rate of 0.95, 0.98, and 0.99 for α = 1, 2, and 4.  For α < 1 , one can use γ α = γ 1 + α U 1 / α to boost k to be usable with this method.

In Matlab numbers can be generated using the function gamrnd() , which uses the α , θ representation.

↑ "Gamma distribution" . Britannica . 6 June 2026.

↑ Weisstein, Eric W. "Gamma Distribution" . mathworld.wolfram.com . Archived from the original on 2024-05-28 . Retrieved 2024-10-09 .

↑ "Gamma Distribution | Gamma Function | Properties | PDF" . Archived from the original on 2024-06-13 . Retrieved 2024-10-09 . [ self-published source? ]

↑ Park, Sung Y.; Bera, Anil K. (June 2009). "Maximum entropy autoregressive conditional heteroskedasticity model". Journal of Econometrics . 150 (2): 219– 230. Bibcode : 2009JEcon.150..219P . doi : 10.1016/j.jeconom.2008.12.014 .

↑ Hogg, R. V. ; Craig, A. T. (1978). Introduction to Mathematical Statistics (4th ed.). New York: Macmillan. pp. Remark 3.3.1. ISBN 0-02-355710-9 .

↑ Gelman, Andrew; Carlin, John B.; Stern, Hal S.; Dunson, David B.; Vehtari, Aki; Rubin, Donald B. (2013). Bayesian Data Analysis . pp. 576– 577. doi : 10.1201/b16018 . ISBN 978-0-429-11307-9 .

↑ Gopalan, Prem; Hofman, Jake M.; Blei, David M. (2013). "Scalable Recommendation with Poisson Factorization". arXiv : 1311.1704 [ cs.IR ].

1 2 Papoulis, Athanasios; Pillai, S. Unnikrishna (2002). Probability, Random Variables, and Stochastic Processes . McGraw-Hill. ISBN 978-0-07-112256-6 . [ page needed ]

↑ Chen, Jeesen; Rubin, Herman (October 1986). "Bounds for the difference between median and mean of gamma and poisson distributions". Statistics & Probability Letters . 4 (6): 281– 283. doi : 10.1016/0167-7152(86)90044-1 .

↑ Choi, K. P. (May 1994). "On the medians of gamma distributions and an equation of Ramanujan". Proceedings of the American Mathematical Society . 121 (1): 245– 251. doi : 10.1090/S0002-9939-1994-1195477-8 .

1 2 Berg, Christian; Pedersen, Henrik L. (2006). "The Chen-Rubin Conjecture in a Continuous Setting" . Methods and Applications of Analysis . 13 (1): 63– 88. doi : 10.4310/MAA.2006.v13.n1.a4 .

1 2 Berg, Christian; Pedersen, Henrik L. (2006). "Convexity of the median in the gamma distribution". arXiv : math/0609442 .

↑ Gaunt, Robert E.; Merkle, Milan (January 2021). "On bounds for the mode and median of the generalized hyperbolic and related distributions". Journal of Mathematical Analysis and Applications . 493 (1) 124508. arXiv : 2002.01884 . doi : 10.1016/j.jmaa.2020.124508 .

1 2 3 Lyon, Richard F. (13 May 2021). "On closed-form tight bounds and approximations for the median of a gamma distribution" . PLOS One . 16 (5) e0251626. arXiv : 2011.04060 . Bibcode : 2021PLoSO..1651626L . doi : 10.1371/journal.pone.0251626 . PMC 8118309 . PMID 33984053 .

1 2 Lyon, Richard F. (13 May 2021). "Tight bounds for the median of a gamma distribution" . PLOS One . 18 (9) e0288601. doi : 10.1371/journal.pone.0288601 . PMC 10490949 . PMID 37682854 .

↑ Mathai, A. M. (December 1982). "Storage capacity of a dam with gamma type inputs". Annals of the Institute of Statistical Mathematics . 34 (3): 591– 597. doi : 10.1007/BF02481056 .

↑ Moschopoulos, P. G. (1985). "The distribution of the sum of independent gamma random variables". Annals of the Institute of Statistical Mathematics . 37 (3): 541– 544. Bibcode : 1985AnISM..37..541M . doi : 10.1007/BF02481123 .

↑ Penny, W. D. "KL-Divergences of Normal, Gamma, Dirichlet, and Wishart densities" .

↑ LoPrete, Anthony; Burge, Johannes (August 2026). "Bandwidth of gamma-distribution-shaped functions via Lambert W function" . Statistics & Probability Letters . 235 110707. doi : 10.1016/j.spl.2026.110707 . PMC 13246144 . PMID 42267171 .

↑ "LogGammaDistribution—Wolfram Language Documentation" .

↑ "ExpGammaDistribution—Wolfram Language Documentation" .

↑ "scipy.stats.loggamma — SciPy v1.8.0 Manual" . docs.scipy.org .

↑ Dubey, Satya D. (December 1970). "Compound gamma, beta and F distributions". Metrika . 16 (1): 27– 31. doi : 10.1007/BF02613934 .

↑ Minka, Thomas P. (2002). "Estimating a Gamma distribution" (PDF) .

↑ Choi, S. C.; Wette, R. (1969). "Maximum Likelihood Estimation of the Parameters of the Gamma Distribution and Their Bias". Technometrics . 11 (4): 683– 690. doi : 10.1080/00401706.1969.10490731 .

1 2 Marsaglia, G.; Tsang, W. W. (2000). "A simple method for generating gamma variables". ACM Transactions on Mathematical Software . 26 (3): 363– 372. doi : 10.1145/358407.358414 .

↑ Ye, Zhi-Sheng; Chen, Nan (3 April 2017). "Closed-Form Estimators for the Gamma Distribution Derived From Likelihood Equations". The American Statistician . 71 (2): 177– 181. doi : 10.1080/00031305.2016.1209129 .

↑ Louzada, Francisco; Ramos, Pedro L.; Ramos, Eduardo (3 April 2019). "A Note on Bias of Closed-Form Estimators for the Gamma Distribution Derived From Likelihood Equations". The American Statistician . 73 (2): 195– 199. doi : 10.1080/00031305.2018.1513376 . hdl : 11449/184543 .

↑ Fink, Daniel (May 1995). A Compendium of Conjugate Priors (PDF) (Report).

↑ Jessica., Scheiner, Samuel M., 1956- Gurevitch (2001). "13. Failure-time analysis" . Design and analysis of ecological experiments . Oxford University Press. ISBN 0-19-513187-8 . OCLC 43694448 . {{ cite book }} :  CS1 maint: multiple names: authors list ( link ) CS1 maint: numeric names: authors list ( link )

↑ Golubev, A. (March 2016). "Applications and implications of the exponentially modified gamma distribution as a model for time variabilities related to cell proliferation and gene expression". Journal of Theoretical Biology . 393 : 203– 217. Bibcode : 2016JThBi.393..203G . doi : 10.1016/j.jtbi.2015.12.027 . PMID 26780652 .

↑ Poon, Art; Davis, Bradley H; Chao, Lin (July 2005). "The Coupon Collector and the Suppressor Mutation" . Genetics . 170 (3): 1323– 1332. doi : 10.1534/genetics.104.037259 . PMC 1451182 . PMID 15879511 .

↑ Vineyard, Michael; Amoako-Gyampah, Kwasi; Meredith, Jack R (July 1999). "Failure rate distributions for flexible manufacturing systems: An empirical study". European Journal of Operational Research . 116 (1): 139– 155. doi : 10.1016/s0377-2217(98)00096-4 .

↑ Rief, Matthias; Rock, Ronald S.; Mehta, Amit D.; Mooseker, Mark S.; Cheney, Richard E.; Spudich, James A. (15 August 2000). "Myosin-V stepping kinetics: A molecular model for processivity" . Proceedings of the National Academy of Sciences . 97 (17): 9482– 9486. Bibcode : 2000PNAS...97.9482R . doi : 10.1073/pnas.97.17.9482 . PMC 16890 . PMID 10944217 .

↑ Boland, Philip J. (2007). Statistical and Probabilistic Methods in Actuarial Science . p. 43. doi : 10.1201/9781584886969 . ISBN 978-0-429-14557-5 .

↑ Wilks, Daniel S. (1990). "Maximum Likelihood Estimation for the Gamma Distribution Using Data Containing Zeros" . Journal of Climate . 3 (12): 1495– 1501. Bibcode : 1990JCli....3.1495W . doi : 10.1175/1520-0442(1990)003 < 1495:MLEFTG > 2.0.CO ; 2 . JSTOR 26196366 .

↑ Belikov, Aleksey V. (22 September 2017). "The number of key carcinogenic events can be predicted from cancer incidence" . Scientific Reports . 7 (1) 12170. Bibcode : 2017NatSR...712170B . doi : 10.1038/s41598-017-12448-7 . PMC 5610194 . PMID 28939880 .

↑ Belikov, Aleksey V.; Vyatkin, Alexey; Leonov, Sergey V. (6 August 2021). "The Erlang distribution approximates the age distribution of incidence of childhood and young adulthood cancers" . PeerJ . 9 e11976. Bibcode : 2021PeerJ...911976B . doi : 10.7717/peerj.11976 . PMC 8351573 . PMID 34434669 .

↑ Robson, J. G.; Troy, J. B. (December 1987). "Nature of the maintained discharge of Q, X, and Y retinal ganglion cells of the cat". Journal of the Optical Society of America A . 4 (12): 2301– 2307. Bibcode : 1987JOSAA...4.2301R . doi : 10.1364/josaa.4.002301 . PMID 3430217 .

↑ Wright, M.C.M.; Winter, I.M.; Forster, J.J.; Bleeck, S. (November 2014). "Response to best-frequency tone bursts in the ventral cochlear nucleus is governed by ordered inter-spike interval statistics". Hearing Research . 317 : 23– 32. doi : 10.1016/j.heares.2014.09.006 . PMID 25261771 .

↑ Friedman, Nir; Cai, Long; Xie, X. Sunney (19 October 2006). "Linking Stochastic Dynamics to Population Distribution: An Analytical Framework of Gene Expression". Physical Review Letters . 97 (16) 168302. Bibcode : 2006PhRvL..97p8302F . doi : 10.1103/PhysRevLett.97.168302 . PMID 17155441 .

↑ Reiss, David J.; Facciotti, Marc T.; Baliga, Nitin S. (February 2008). "Model-based deconvolution of genome-wide DNA binding". Bioinformatics . 24 (3): 396– 403. doi : 10.1093/bioinformatics/btm592 . PMID 18056063 .

↑ Mendoza-Parra, Marco-Antonio; Nowicka, Malgorzata; Van Gool, Wouter; Gronemeyer, Hinrich (2013). "Characterising ChIP-seq binding patterns by model-based peak shape deconvolution" . BMC Genomics . 14 (1): 834. doi : 10.1186/1471-2164-14-834 . PMC 4046686 . PMID 24279297 .

↑ Yang, Ziheng (September 1996). "Among-site rate variation and its impact on phylogenetic analyses". Trends in Ecology & Evolution . 11 (9): 367– 372. Bibcode : 1996TEcoE..11..367Y . doi : 10.1016/0169-5347(96)10041-0 . PMID 21237881 .

↑ Yang, Ziheng (September 1994). "Maximum likelihood phylogenetic estimation from DNA sequences with variable rates over sites: Approximate methods". Journal of Molecular Evolution . 39 (3): 306– 314. Bibcode : 1994JMolE..39..306Y . doi : 10.1007/BF00160154 . PMID 7932792 .

↑ Felsenstein, Joseph (October 2001). "Taking Variation of Evolutionary Rates Between Sites into Account in Inferring Phylogenies". Journal of Molecular Evolution . 53 ( 4– 5): 447– 455. Bibcode : 2001JMolE..53..447F . doi : 10.1007/s002390010234 . PMID 11675604 .

1 2 3 Devroye, Luc (1986). Non-Uniform Random Variate Generation . doi : 10.1007/978-1-4613-8643-8 . ISBN 978-1-4613-8645-2 .

1 2 Ahrens, J. H.; Dieter, U (January 1982). "Generating gamma variates by a modified rejection technique" . Communications of the ACM . 25 (1): 47– 54. doi : 10.1145/358315.358390 . See Algorithm GD, p. 53.

↑ Ahrens, J. H.; Dieter, U. (September 1974). "Computer methods for sampling from gamma, beta, poisson and bionomial distributions". Computing . 12 (3): 223– 246. Bibcode : 1974Compu..12..223A . doi : 10.1007/BF02293108 .

↑ Cheng, R. C. H.; Feast, G. M. (1979). "Some Simple Gamma Variate Generators". Journal of the Royal Statistical Society. Series C (Applied Statistics) . 28 (3): 290– 295. doi : 10.2307/2347200 . JSTOR 2347200 .

↑ Marsaglia, George (1977). "The squeeze method for generating gamma variates". Computers & Mathematics with Applications . 3 (4): 321– 325. doi : 10.1016/0898-1221(77)90089-X .

"Gamma-distribution" , Encyclopedia of Mathematics , EMS Press, 2001 [1994]

Weisstein, Eric W. "Gamma distribution" . MathWorld .

ModelAssist (2017) Uses of the gamma distribution in risk modeling, including applied examples in Excel Archived 2017-05-09 at the Wayback Machine .

Exponential Hyperexponential Hypoexponential Logarithmic

Wishart Normal Inverse Normal-inverse Complex

Uniform distribution on a Stiefel manifold

Infinitely divisible probability distributions

Articles with self-published sources from July 2026

Wikipedia articles needing page number citations from July 2026

Articles with unsourced statements from September 2012

Articles with unsourced statements from May 2019
