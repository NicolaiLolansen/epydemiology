import pkg_resources

try:
    pkg_resources.get_distribution('numpy')
except pkg_resources.DistributionNotFound:
    numpyPresent = False
    print("Error: Numpy package not available.")
else:
    numpyPresent = True
    import numpy as np


try:
    pkg_resources.get_distribution('pandas')
except pkg_resources.DistributionNotFound:
    pandasPresent = False
    print("Error: Pandas package not available.")
else:
    pandasPresent = True
    import pandas as pd


try:
    pkg_resources.get_distribution('matplotlib')
except pkg_resources.DistributionNotFound:
    matplotlibPresent = False
    print("Error: Matplotlib package not available.")
else:
    matplotlibPresent = True
    import matplotlib.pyplot as plt


try:
    pkg_resources.get_distribution('scipy')
except pkg_resources.DistributionNotFound:
    scipyPresent = False
    print("Error: Scipy package not available.")
else:
    scipyPresent = True
    from scipy.stats import norm


try:
    pkg_resources.get_distribution('statsmodels')
except pkg_resources.DistributionNotFound:
    statsmodelsPresent = False
    print("Error: Statsmodels package not available.")
else:
    statsmodelsPresent = True
    import statsmodels.formula.api as smf
    import statsmodels.api as sm


import re


# Import minor epydemiology functions from other epydemiology files
# -----------------------------------------------------------------
# In order to use the phjDefineSuffixDict() function from a different .py file in the
# same package, it seems that we need to import that function explicitly. This can be
# done using the same format as in the __init__.py file e.g.:
#     from .pythonFileName import functionName
# Where the pythonFileName is a file in the same package.
# For more details, see tutorial at https://www.youtube.com/watch?v=0oTh1CXRaQ0.

from .phjRROR import phjOddsRatio
from .phjCalculateProportions import phjDefineSuffixDict
from .phjCalculateProportions import phjGetYErrors
from .phjExtFuncs import getJenksBreaks



# ==============
# Main functions
# ==============
#
def phjViewLogOdds(phjTempDF,
                   phjBinaryDepVarName = None,
                   phjContIndepVarName = None,
                   phjCaseValue = 1,
                   phjMissingValue = 'missing',
                   phjNumberOfCategoriesInt = 5,
                   phjNewCategoryVarName = None,
                   phjCategorisationMethod = 'jenks',   # Need to be able to pass a list of cut-off values here as well.
                   phjGroupNameVar = None,
                   phjAlpha = 0.05,
                   phjPrintResults = False):
    
    # In several functions, it's useful to have access to a dict containing column headings
    # and suffixes used in a variety of situations.
    phjSuffixDict = phjDefineSuffixDict()
    
    # Create a name for the new categorical variable by replacing all spaces with underscores
    # and adding the suffix to indicate that a continuous variable has been converted to a category.
    if phjNewCategoryVarName is None:
        phjNewCategoryVarName = phjSuffixDict['joinstr'].join([phjContIndepVarName.replace(' ','_'),
                                                               phjSuffixDict['categorisedvar']])
    
    
    # Convert a continuous variable at a categorical variable using a variety of methods.
    # If phjReturnBreaks = True then function also returns a list of the break points
    # for the continuous variable.
    phjTempDF, phjBreaks = phjCategoriseContinuousVariable(phjTempDF = phjTempDF,
                                                           phjContinuousVarName = phjContIndepVarName,
                                                           phjMissingValue = phjMissingValue,
                                                           phjNumberOfCategoriesInt = phjNumberOfCategoriesInt,
                                                           phjNewCategoryVarName = phjNewCategoryVarName,
                                                           phjCategorisationMethod = phjCategorisationMethod,
                                                           phjReturnBreaks = True,
                                                           phjPrintResults = phjPrintResults)
    
    # If the breaks have been calculated (and the continuous variable categorised successfully)
    # then plot the graph of logodds against mid-points
    if phjBreaks is not None:
        # The following DF contains an index that may be numeric.
        phjOR = phjOddsRatio(phjTempDF = phjTempDF,
                             phjCaseVarName = phjBinaryDepVarName,
                             phjCaseValue = phjCaseValue,
                             phjRiskFactorVarName = phjNewCategoryVarName,
                             phjRiskFactorBaseValue = 1)
        
        phjOR[phjSuffixDict['logodds']] = np.log(phjOR[phjSuffixDict['odds']])
        
        # Calculate log odds using logistic regression and retrieve the se from the statistical model
        phjSE = phjCalculateLogOddsSE(phjTempDF = phjTempDF,
                                      phjAlpha = phjAlpha,
                                      phjPrintResults = phjPrintResults)
        
        # Join to phjOR dataframe
        phjOR = phjOR.join(phjSE)
        
        
        # Calculate lower and upper limits assuming normal distribution
        phjRelCoef = norm.ppf(1 - (phjAlpha/2))
        
        phjOR[phjSuffixDict['joinstr'].join([phjSuffixDict['cisuffix'],
                                             phjSuffixDict['cilowlim']])] = phjOR[phjSuffixDict['logodds']] - (phjRelCoef * phjOR[phjSuffixDict['stderr']])
        
        phjOR[phjSuffixDict['joinstr'].join([phjSuffixDict['cisuffix'],
                                             phjSuffixDict['ciupplim']])] = phjOR[phjSuffixDict['logodds']] + (phjRelCoef * phjOR[phjSuffixDict['stderr']])
        
        
        # Calculae midpoints of categories
        phjOR[phjSuffixDict['catmidpoints']] = [((phjBreaks[i] + phjBreaks[i+1]) / 2) for i in range(len(phjBreaks) - 1)]
        
        
        # Plot log odds against midpoints of categories
        phjYErrors = phjGetYErrors(phjTempDF = phjOR,
                                   phjCategoriesToPlotList = phjOR.index.tolist(),
                                   phjParameterValue = 'logodds',
                                   phjGroupVarName = None,
                                   phjGroupLevelsList = None,
                                   phjAlpha = phjAlpha,
                                   phjPrintResults = phjPrintResults)
        
        ax = phjOR.plot(x = 'catMidpoints',
                        y = 'logodds',
                        kind = 'line',
                        yerr = phjYErrors,
                        capsize = 4,
                        title = 'Log-odds against mid-points of category')
        ax.set_ylabel("Log odds")
        ax.set_xlabel(phjNewCategoryVarName)
    
    else:
        phjOR = None
    
    if phjPrintResults == True:
        print('\nOdds ratio dataframe')
        print(phjOR)

    return phjOR




# ====================
# Supporting functions
# ====================

def phjCalculateLogOddsSE(phjTempDF,
                          phjAlpha = 0.05,
                          phjPrintResults = False):
    
    
    # Get a list of the terms used to head columns in summary tables
    phjSuffixDict = phjDefineSuffixDict(phjAlpha = phjAlpha)


    # Run a logistic regression mode with no constant term (in patsy package, the -1 removes the constant term)
    phjLogisticRegressionResults = smf.glm(formula='binDepVar ~ C(categoricalVar) -1',
                                           data=phjTempDF,
                                           family = sm.families.Binomial(link = sm.genmod.families.links.logit)).fit()
    
    if phjPrintResults == True:
        print('\nResults of logistic regression model')
        print(phjLogisticRegressionResults.summary())
    
    # Extract group codes from index of logistic regression results table.
    # The index values have the structure: varName[level].
    # Extract just the bit contained in square brackets:
    
    # i. Define and compile regex
    phjRegex = re.compile('\[(?P<group_index>\w+)\]$')
    
    # ii. Extract std err data from model
    phjSEResultsDF = pd.DataFrame(phjLogisticRegressionResults.bse)
    
    # iii. Rename column heading and generate a new index and replace the old one.
    phjSEResultsDF.columns = [phjSuffixDict['stderr']]

    # The following list comprehension steps through each index and extracts the regex
    # group (in this case, the bit between the square brackets)
    phjNewIndex = [re.search(phjRegex,i).group('group_index') for i in phjSEResultsDF.index]
    
    # ...and the extracted bits are converted to ints if possible
    for n,j in enumerate(phjNewIndex):
        try:
            phjNewIndex[n] = int(j)
        except ValueError:
            phjNewIndex[n] = j
            
    phjSEResultsDF.index = phjNewIndex
    
    
    return phjSEResultsDF




def phjCategoriseContinuousVariable(phjTempDF,
                                    phjContinuousVarName = None,
                                    phjMissingValue = 'missing',
                                    phjNumberOfCategoriesInt = 5,
                                    phjNewCategoryVarName = None,
                                    phjCategorisationMethod = 'jenks',
                                    phjReturnBreaks = False,
                                    phjPrintResults = False):
    
    
    if phjCategorisationMethod == 'jenks':
        
        phjBreaks = phjImplementGetBreaks(phjTempDF = phjTempDF,
                                          phjContinuousVarName = phjContinuousVarName,
                                          phjMissingValue = phjMissingValue,
                                          phjNumberOfCategoriesInt = phjNumberOfCategoriesInt,
                                          phjPrintResults = phjPrintResults)
        
        # Cut data series based on Jenks breaks
        phjTempDF[phjNewCategoryVarName] = pd.cut(phjTempDF[phjContinuousVarName],
                                                  bins = phjBreaks,
                                                  labels = False)
        
        if phjPrintResults == True:
            print('Category quantile bins (Jenks) = ',phjBreaks)

    
    elif phjCategorisationMethod == 'quantile':
        
        # Cut data series based on quantiles / number of required bins
        phjTempDF[phjNewCategoryVarName], phjBreaks = pd.cut(phjTempDF[phjContinuousVarName],
                                                             bins = phjNumberOfCategoriesInt,
                                                             retbins = True,
                                                             labels = False)
        
        if phjPrintResults == True:
            print('Category quantile bins = ',phjBreaks)
    
    
    else:
        print('The selected method to calculate category boundaries has not yet been implemented. The variable has not be categorised.')
        phjBreaks = None
    
    if phjReturnBreaks == True:
        return phjTempDF,phjBreaks
    else:
        return phjTempDF




def phjImplementGetBreaks(phjTempDF,
                          phjContinuousVarName = None,
                          phjMissingValue = 'missing',
                          phjNumberOfCategoriesInt = 5,
                          phjCategorisationMethod = 'jenks',
                          phjPrintResults = False):
    
    phjTempSer = phjTempDF[phjContinuousVarName].replace('missing',np.nan).dropna(axis = 0)
    
    if phjCategorisationMethod == 'jenks':
        if len(phjTempSer.index) <= 1000:
            phjBreaks = getJenksBreaks(np.array(phjTempSer),
                                       phjNumberOfCategoriesInt)
        
        else:
            phjBreaks = getJenksBreaks(np.array(phjTempSer.sample(1000)),
                                       phjNumberOfCategoriesInt)
            # As the breaks were calculated from a sample, the last value
            # may be smaller than the maximum. Hence, when categorising the
            # continuous variable in the original dataframe, there would be a
            # small number of individuals who wouldn't appear in any category.
            # Replace the end values of the break list with values that are
            # slightly bigger or smaller (0.1%) than the maximum or minimum.
            # This is the same procedure used by pandas.cut() method.
            phjBreaks[0] = phjTempSer.min() * 0.999
            phjBreaks[-1] = phjTempSer.max() * 1.001
    
    else:
        print('The selected method to calculate category boundaries has not yet been implemented.')
        phjBreaks = None
    
    return phjBreaks




if __name__ == '__main__':
    main()
