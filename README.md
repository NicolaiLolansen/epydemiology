# epydemiology
Library of python code for epidemiologists – eventually.

## A. Installation
```python
pip install epydemiology as epy
```
## B. Usage

The following functions are available:

**1. [Load data from a named Excel cell range into a Pandas dataframe](https://github.com/lvphj/epydemiology/wiki/Load-data-from-a-named-Excel-cell-range-into-a-Pandas-dataframe)**

```python
myDF = epy.phjReadDataFromExcelNamedCellRange()
```

**2. To load data from a MySQL or SQL SERVER database into a Pandas dataframe**

```python
myDF = epy.phjGetDataFromDatabase()
```

**3. To load text from a text file (e.g. a SQL query or regular expression) into a Python variable as a single string**

```python
myString = epy.phjReadTextFromFile()
```

**4. To convert columns of binary data to a square matrix containing co-occurrences**

```python
myArr = epy.phjBinaryVarsToSquareMatrix()
```

**5. To clean a column of UK postcodes in a Pandas dataframe**

```python
myDF = epy.phjCleanUKPostcodeVariable()
```

**6. To generate a matched or unmatched case-control dataset (without replacement) from Pandas dataframes**

```python
myDF = epy.phjGenerateCaseControlDataset()
```

**7. To select matched or unmatched case-control data (without replacement) from Pandas dataframes**

```python
myDF = epy.phjSelectCaseControlDataset()
```
**8. To calculate and plot a series of binomial proportions**

```python
myDF = epy.phjCalculateBinomialProportions()
```
**9. To calculate and plot multinomial proportions**

```python
myDF = epy.phjCalculateMultinomialProportions()
```

**10. To calculate odds and odds ratios for case-control studies for data stored in Pandas dataframe**

```python
myDF = epy.phjOddsRatio()
```

**11. To calculate relative risks for cross-sectional or longitudinal studies for data stored in Pandas dataframe**

```python
myDF = epy.phjRelativeRisk()
```

**12. Categorise a continuous variable using predefined breaks, quantiles or optimised break positions**

```python
myDF = epy.phjCategoriseContinuousVariable()
```
or, if phjReturnBreaks is set to True:
```python
myDF,myBreaks = epy.phjCategoriseContinuousVariable()
```

**13. To view a plot of log odds against mid-points of categories of a continuous variable**

```python
myOddRatioTable = epy.phjViewLogOdds()
```
---
## C. Details of functions
### 1. phjReadDataFromExcelNamedCellRange()

```python
df = phjReadDataFromExcelNamedCellRange(phjExcelPathAndFileName = None,
                                        phjExcelCellRangeName = None,
                                        phjDatetimeFormat = "%Y-%m-%d %H:%M:%S",
                                        phjMissingValue = "missing",
                                        phjHeaderRow = False,
                                        phjPrintResults = False)
```

Python function to read data from a named cell range in an Excel workbook.

#### Description

This function can be used to import data from a named range in a Microsoft Excel workbook. The function receives the full path and filename of the Excel document, together with the name of the named cell range of interest, and returns the data as a Pandas dataframe.

#### Function parameters
1. **phjExcelPathAndFilename**

   The full path and filename of the Microsoft Excel workbook.

2. **phjExcelCellRangeName**

   The name of the cell range of interest. It is import to ensure that the name range only occurs once in the workbook.

3. **phjDatetimeFormat** (default = "%Y-%m-%d %H:%M:%S")

   The datatime format that will be used to interpret columns containing date (and time) data.

4. **phjMissingValue** (default = "missing")

   A string or code that is used to replace empty cells.

5. **phjHeaderRow** (default = False)

   Indicates whether the cell range has a header row. If so, the values in the first row of the cell range are used as the headings of the dataframe columns; otherwise, the columns are given default, generic names.

6. **phjPrintResults** (default = False)

   Print the imported results.

#### Exceptions raised

None.

#### Returns

Pandas dataframe containing data read from named cell range.

#### Other notes

None.

#### Example

An example of the function in use is given below. An Excel workbook named 'myWorkbook.xlsx' is stored on the Desktop. The workbook contains several individual worksheets, one of which contains a named cell range called 'myCellRange', the first row of which contains the names of the columns. The data can be imported into a Pandas dataframe using:

```python
# The following libraries are imported automatically but are incuded here for completeness.
import pandas as pd
import openpyxl
import epydemiology as epy

myTempDF = epy.phjReadDataFromExcelNamedCellRange(phjExcelPathAndFileName = '/Users/username/Desktop/myWorkbook.xlsx',
                                                  phjExcelCellRangeName = 'myCellRange',
                                                  phjDatetimeFormat = "%Y-%m-%d %H:%M:%S",
                                                  phjMissingValue = "missing",
                                                  phjHeaderRow = True,
                                                  phjPrintResults = False)

```
---
### 2. phjGetDataFromDatabase()

```python
df = phjGetDataFromDatabase(phjQueryStr = None,
                            phjQueryPathAndFileName = None,
                            phjPrintResults = False)
```

Python function to read data from a MySQL or SQL SERVER database.

#### Description

The function is used to query MySQL or SQL SERVER databases using an SQL query that can be entered as a string or is stored as a text file. As the function runs, the user will be prompted to enter all other required parameters including server address, username and password details. A maximum of three attempts allowed to enter correct login information. The password is entered and remains securely obscured on-screen.

#### Function parameters

1. **phjQueryStr**

   A string representing a SELECT...FROM query.
   A query entered as a text file (below) is given preference over a query entered as a string.

2. **phjQueryPathAndFilename**

   The full path and filename of the SQL text file containing the SQL query.
   A query entered as a text file (below) is given preference over a query entered as a string.
   
2. **phjPrintResults** (default = False)

   Print the imported results.

#### Exceptions raised

None.

#### Returns

Pandas dataframe containing data read from database.

#### Other notes

None.

#### Example

An example of the function in use is given below. If the SQL query to be used to query a SQL SERVER database is saved as a text file named 'theSQLQueryFile.mssql' on the Desktop, the function can be used to import returned data using:

```python
# The following libraries are imported automatically but are incuded here for completeness.
import re
import getpass
import pandas as pd
import pymysql
import pymssql
import epydemiology as epy

myTempDF = epy.phjQueryPathAndFilename(phjQueryPathAndFile = '/Users/username/Desktop/theSQLQueryFile.mssql',
                                       phjPrintResults = True)
```
---
### 3. phjReadTextFromFile()

```python
myStr = phjReadTextFromFile(phjFilePathAndName = None,
                            maxAttempts = 3,
                            phjPrintResults = False)
```

#### Description

This function can be used to read text from a text file.

#### Function parameters

1. **phjFilePathAndName**

   The full path and name of the text file to read. The text file does not need to end with the prefix '.txt'. This is the function that is used to read SQL queries from text files in the phjGetDataFromDatabase() function.

#### Exceptions raised

   None.

#### Returns

   A string containing the contents of the text file.

#### Other notes

   None.

#### Example

```python
myStr = phjReadTextFromFile(phjFilePathAndName = '/Users/username/Desktop/myTextFile.txt',
                            maxAttempts = 3,
                            phjPrintResults = False)


```
---
### 4. phjBinaryVarsToSquareMatrix()

```python
arr = phjBinaryVarsToSquareMatrix(phjDataDF,
                                  phjColumnNamesList,
                                  phjOutputFormat = 'arr',
                                  phjPrintResults = False)
```

Function to produce a Numpy array from a group of binary variables to show co-occurrence.

#### Description

This function takes a number of variables containing binary data and returns a Numpy array representing a square matrix that shows co-occurrence of positive variables.

#### Function parameters

1. **phjDataDF**
    Pandas dataframe

2. **phjColumnNamesList**
    A list of variable names contained in the dataframe that contains binary data.
    
3. **phjOutputFormat** (default = 'arr')
    Output format. Default is a Numpy array ('arr'). Alternative is 'df' to return a Pandas dataframe.
    
4. **phjPrintResults** (default = False)

Print verbose output during execution of scripts. If running on Jupyter-Notebook, setting ```phjPrintResults = True``` causes a lot a output and can cause problems connecting to kernel. It is recommended to set ```phjPrintResults = False``` routinely to avoid possible problems when using Jupyter-notebook.

#### Exceptions raised

None.

#### Returns

By default, function returns a Numpy array of a square matrix (phjOutputFormat = 'arr'). Matrix can be returned as a Pandas dataframe (phjOutputFormat = 'df').

#### Other notes

None.

#### Example

```python
import pandas as pd

rawDataDF = pd.DataFrame({'a':[0,1,1,1,0,0,1,0],
                          'b':[1,1,0,0,1,0,0,1],
                          'c':[0,0,1,0,1,1,1,1],
                          'd':[1,0,0,0,1,0,0,0],
                          'e':[1,0,0,0,0,1,0,0]})

columns = ['a','b','c','d','e']

phjMatrix = epy.phjBinaryVarsToSquareMatrix(phjDataDF = rawDataDF,
                                            phjColumnNamesList = columns,
                                            phjOutputFormat = 'arr',
                                            phjPrintResults = False)
                                        
print(phjMatrix)
```

Output:

```
[[1 1 2 0 0]
 [1 0 2 2 1]
 [2 2 0 1 1]
 [0 2 1 0 1]
 [0 1 1 1 0]]
```
---
### 5. phjCleanUKPostcodeVariable()

```python
df = phjCleanUKPostcodeVariable(phjCleanUKPostcodeVariable(phjTempDF,
                                phjRealPostcodeSer = None,
                                phjOrigPostcodeVarName = 'postcode',
                                phjNewPostcodeVarName = 'postcodeClean',
                                phjNewPostcodeStrLenVarName = 'postcodeCleanStrLen',
                                phjPostcodeCheckVarName = 'postcodeCheck',
                                phjMissingValueCode = 'missing',
                                phjMinDamerauLevenshteinDistanceVarName = 'minDamLevDist',
                                phjBestAlternativesVarName = 'bestAlternatives',
                                phjPostcode7VarName = 'postcode7',
                                phjPostcodeAreaVarName = 'postcodeArea',
                                phjSalvageOutwardPostcodeComponent = True,
                                phjCheckByOption = 'format',
                                phjDropExisting = False,
                                phjPrintResults = True)

```

Python function to clean and extract correctly formatted postcode data.

#### Description

In many situations, postcodes are added to a database field to record people's addresses. However, when entering postcodes by hand or transcribing from written notes, it is often the case that postcodes are entered incorrectly due to typing errors or because the postcode in question is not fully known. Consequently, a variable containing postcode information will contain many correct postcodes but also many incorrect or partial data points. This function seeks to extract correctly formatted postcodes and to correct some commonly occurring transcription errors in order to produce a correctly-formatted postcode. In addition, in situations where just the outward component (first half) of the postcode is recorded, the function will attempt to salvage just the outward component. Finally, the function extracts the postcode area (first 1 or 2 letters) of the postcode. The cleaned postcode (with no spaces and in 7-character format), the outward and inward components of the postcode and the postcode areas are all stored in new variables that are added to the original dataframe.

This function uses one of two methods to extract postcode information:

1. checking the postcode is correctly 'formatted' using a regex;
  
2. comparing the postcode to a database of all known postcodes and, if the postcode does not exist, determining the most likely alternatives based on Damerau-Levenshtein distance and on the physical position of inserted or transposed characters on the keyboard.

The regex used to determine whether postcodes are correctly formatted is a modified version of a regex published at https://en.wikipedia.org/wiki/Talk:Postcodes_in_the_United_Kingdom (accessed 22 Mar 2016). (This page is also stored locally as a PDF entitled, "Talk/Postcodes in the United Kingdom - Wikipedia, the free encyclopedia".)

The function takes, as two of its arguments, a Pandas dataframe containing a column of postcode data, and the name of that postcode column. It returns the same dataframe with some additional, postcode-related columns. The additional columns returned are:

1. 'postcodeClean' (column name is user-defined through phjNewPostcodeVarName argument)

   This variable will contain the correctly formatted components of the postcode, either the whole postcode or the outward component (first half of postcode). Postcodes that are incorrectly formatted or have been entered as missing values will contain the missing value code (e.g. 'missing').

2. 'postcodeFormatCheck' (column name is user-defined through phjPostcodeFormatCheckVarName argument)

   This is a binary variable that contains True if a correctly formatted postcode component can be extracted, either the whole postcode or the outward component only. Otherwise, it contains False.

3. 'postcode7' (column name is user-defined through the phjPostcode7VarName argument)

   This variable contains correctly formatted complete postcodes in 7-character format. For postcodes that contain 5 letters, the outward and inward components will be separated by 2 spaces; for postcodes that contain 6 letters, the outward and inward components will be separated by 1 space; and postcodes that contain 7 letters will contain no spaces. This format of postcodes is often used in postcode lookup tables.

4. 'postcodeOutward' (defined as a group name in the regular expression and, therefore, not user-definable)

   This variable contains the outward component of the postcode (first half of postcode). It is possible that this variable may contain a correctly-formatted postcode string (2 to 4 characters) whilst the variable containing the inward postcode string contains the missing vaue code. 

5. 'postcodeInward' (defined as a group name in the regular expression and, therefore, not user-definable)

   This variable contains the inward component of the postcode (second half of postcode). It is possible that this variable may contain a missing value whilst the postcodeOutward variable contains a correctly-formatted postcode string (2 to 4 characters).

6. 'phjPostcodeArea' (column name is user-defined through the phjPostcodeAreaVarName argument)

   This variable contains the postcode area (first one or two letters) taken from correctly formatted outward postcode components.


If postcodes are checked using a regex, the functions proceeds as follows:

1. Postcodes data is cleaned by removing all spaces and punctuation marks and converting all letters to uppercase. Missing values and strings that cannot possibly be a postcode (e.g. all numeric data) are converted to the missing value code. The cleaned strings are stored temporarily in the postcodeClean variable.

2. Correctly formatted postcodes (in postcodeClean column) are identified using the regular expression and the postcodeFormatCheck is set to True. Outward and inward components are extracted and stored in the relevant columns.

3. Postcodes that are incorrectly formatted undergo an error-correction step where common typos and mis-transcriptions are corrected. After this process, the format of the corrected postcode is checked again using the regex and the postcodeFormatCheck variable set to True if necessary. Outward and inward components are extracted and stored in the relevant columns.

4. If the phjSalvageOutwardPostcodeComponent arugment is set to True (default), the function attempts to salvage just the outward postcode component. The postcode string in the postcodeClean variable are tested using the outward component of the regex to determine if the first 2 to 4 characters represent a correctly formatted outward component of a postcode. If so, postcodeFormatCheck is set to True and the partial string is extracted and stored in the postcodeOutward column.

5. Common typos and mis-transcriptions are corrected once again and the string tested against the regex to determine if the first 2 to 4 characters represent a correctly formatted outward component of a postcode. If so, postcodeFormatCheck is set to True and the partial string is extracted and stored in the postcodeOutward column.

6. For any postcode strings that have not been identified as a complete or partial match to the postcode regex, the postcodeClean variable is set to the missing value code.

7. The postcode area is extracted from the outwardPostcode variable and stored in the postcodeArea variable.

8. The function returns the dataframe containing the additional columns.

If postcodes are checked against a list of correct postcodes, the functions proceeds in a similar way except incorrect postcodes are compared with correct postcodes using the Damarau-Levenshtein distance, weighted bfor the physical distance of inserted or transponsed character on a standard QWERTY keyboard.

#### Function parameters

The function takes the following parameters:

1. **phjTempDF**

   Pandas dataframe containing a variable that contains postcode information.
  
2. **phjRealPostcodeSer** (default = None)

   If the postcodes are to be compared to real postcodes, this variable should refer to a Pandas Series of genuine postcodes.

3. **phjOrigPostcodeVarName** (default = 'postcode')

   The name of the variable that contains postcode information.

4. **phjNewPostcodeVarName** (default = 'postcodeClean')

   The name of the variable that the function creates that will contain 'cleaned' postcode data. The postcodes stored in this column will contain no whitespace. Therefore, A1 2BC will be entered as A12BC. Also, the 'cleaned' postcode may only be the outward component if that is the only corrected formatted data. If the use wants to view only complete postcodes, use phjPostcode7VarName. Strings where no valid postcode data has been extracted will be stored as missing value string.

5. **phjNewPostcodeStrLenVarName** (default = 'postcodeCleanStrLen')

   Name of the variable that will be created to contain the length of the postcode.
  
6. **phjPostcodeCheckVarName** (default = 'postcodeCheck')

   A binary variable that the function will create that indicates whether the whole postcode (or, if only 2 to 4 characters are entered, the outward component of the postcode) is either correctly formatted or matches the list of real postcodes supplied, depending on what what requested.

7. **phjMissingValueCode** (default = 'missing')

   String used to indicate a missing value. This can not be np.nan because DataFrame.update() function does not undate NaN values.
  
8. **phjMinDamerauLevenshteinDistanceVarName** (default = 'minDamLevDist')

   Name of variable that will be created to contain the DL distance.
  
9. **phjBestAlternativesVarName** (default = 'bestAlternatives')

   Name of variable that will be created to contain best (or closest matching) postcodes from the list of real postcodes.
  
10. **phjPostcode7VarName** (default = 'postcode7')

   The name of the variable that the function creates that will contain 'cleaned' postcode data in 7-character format. Postcodes can contain 5 to 7 characters. In those postcodes that consist of 5 characters, the outward and inward components will be separated by 2 spaces, in those postcodes that consist of 6 characters, the outward and inward components will be separated by 1 spaces, and in those postcodes that consist of 7 characters there will be no spaces. This format is commonly used in lookup tables that link postcodes to other geographical information.

11. **phjPostcodeAreaVarName** (default = 'postcodeArea')

   The name of the variable that the function creates that will contain the postcode area (the first 1, 2 or, in very rare cases, 3 letters).

12. **phjSalvageOutwardPostcodeComponent** (default = True)

   Indicates whether user wants to attempt to salvage some outward postcode components from postcode strings.
  
13. **phjCheckByOption** (default = 'format')

   Select method to use to check postcodes. The default is 'format' and checks the format of the postcode using a regular expression. The alternative is 'dl' which calculates the Damarau-Levenshtein distance from each postcode in the list of supplied postcodes and chooses the closest matches based on the DL distance and the disctance of inserted or trasposed characters based on physical distance on a standard QWERTY keyboard.
  
14. **phjDropExisting** (default = False)

   If set to True, the function will automatically drop any pre-existing columns that have the same name as those columns that need to be created. If set to False, the function will halt.

15. **phjPrintResults** (default = False)

   If set to True, the function will print information to screen as it proceeds.

#### Exceptions raised

None.

#### Returns

By default, function returns the original dataframe with added columns containing postcode data.

#### Other notes

The regex used to check the format of postcodes is given below and is a modification of the regex found at https://en.wikipedia.org/wiki/Talk:Postcodes_in_the_United_Kingdom (accessed 22 Mar 2016). The regex was modified slightly to allow for optional space between first and second parts of postcode (even though, in this library, all the whitespace is removed before comparing with the regex). Also, the original did not find old Norwich postcodes of the form NOR number-number-letter nor old Newport postcodes of form NPT number-letter-letter. The regex was changed so it consisted of two named components recognising the outward (first half) and inward (second half) of the postcode which could be compiled into a single regex, separated by whitespace (if required).

```python
postcodeOutwardRegex = '''(?P<postcodeOutward>(?:^GIR(?=\s*0AA$)) |                 # Identifies special postcode GIR 0AA
                                              (?:^NOR(?=\s*[0-9][0-9][A-Z]$)) |     # Identifies old Norwich postcodes of format NOR number-number-letter
                                              (?:^NPT(?=\s*[0-9][A-Z][A-Z]$)) |     # Identifies old Newport (South Wales) postcodes of format NPT number-letter-letter
                                              (?:^(?:(?:A[BL]|B[ABDFHLNRSTX]?|C[ABFHMORTVW]|D[ADEGHLNTY]|E[HNX]?|F[KY]|G[LUY]?|H[ADGPRSUX]|I[GMPV]|JE|K[ATWY]|L[ADELNSU]?|M[EKL]?|N[EGNPRW]?|O[LX]|P[AEHLOR]|R[GHM]|S[AEGKLMNOPRSTY]?|T[ADFNQRSW]|UB|W[ADFNRSV]|YO|ZE)[1-9]?[0-9] |  # Identifies stardard outward code e.g. L4, L12, CH5, CH64
                                                  (?:(?:E|N|NW|SE|SW|W)1|EC[1-4]|WC[12])[A-HJKMNPR-Y]|(?:SW|W)(?:[1-9]|[1-9][0-9])|EC[1-9][0-9]|WC99))    # Identifies the odd London-based postcodes
                           )'''

postcodeInwardRegex = '''(?P<postcodeInward>(?<=NOR)(?:\s*[0-9][0-9][A-Z]$) |      # Picks out the unusual format of old Norwich postcodes (including leading space)
                                            (?:[0-9][ABD-HJLNP-UVW-Z]{2}$)         # Picks out standard number-letter-letter end of postcode
                         )'''
```

#### Example

```python
# Create a test dataframe that contains a postcode variable and some other empty variables
# that have the same names as the new variables that will be created. Setting the 'phjDropExisting'
# variable to true will automatically drop pre-existing variables before running the function.
# Some of the variables in the test dataframe are not duplicated and are present to show that the
# function preserves those variables in tact.

import numpy as np
import pandas as pd
import re

# Create test dataframe
myTestPostcodeDF = pd.DataFrame({'postcode': ['NP45DG',
                                              'CH647TE',
                                              'CH5 4HE',
                                              'GIR 0AA',
                                              'NOT NOWN',
                                              'GIR0AB',
                                              'NOR12A',
                                              'no idea',
                                              'W1A 1AA',
                                              'missin',
                                              'NP4  OGH',
                                              'P012 OLL',
                                              'p01s',
                                              'ABCD',
                                              '',
                                              'ab123cd',
                                              'un-known',
                                              'B1    INJ',
                                              'AB123CD',
                                              'No idea what the postcode is',
                                              '    ???NP4-5DG_*#   '],
                                 'pcdClean': np.nan,
                                 'pcd7': np.nan,
                                 'postcodeOutward': np.nan,
                                 'someOtherCol': np.nan})

# Run function to extract postcode data
print('\nStart dataframe\n===============\n')
print(myTestPostcodeDF)
print('\n')

myTestPostcodeDF = epy.phjCleanUKPostcodeVariable(phjTempDF = myTestPostcodeDF,
                                                  phjRealPostcodeSer = None,
                                                  phjOrigPostcodeVarName = 'postcode',
                                                  phjNewPostcodeVarName = 'pcdClean',
                                                  phjNewPostcodeStrLenVarName = 'pcdCleanStrLen',
                                                  phjPostcodeCheckVarName = 'pcdFormatCheck',
                                                  phjMissingValueCode = 'missing',
                                                  phjMinDamerauLevenshteinDistanceVarName = 'minDamLevDist',
                                                  phjBestAlternativesVarName = 'bestAlternatives',
                                                  phjPostcode7VarName = 'pcd7',
                                                  phjPostcodeAreaVarName = 'pcdArea',
                                                  phjSalvageOutwardPostcodeComponent = True,
                                                  phjCheckByOption = 'format',
                                                  phjDropExisting = True,
                                                  phjPrintResults = True)

print('\nReturned dataframe\n==================\n')
print(myTestPostcodeDF)

```
```
OUTPUT
======

Start dataframe
===============

    pcd7  pcdClean                      postcode  postcodeOutward  \
0    NaN       NaN                        NP45DG              NaN   
1    NaN       NaN                       CH647TE              NaN   
2    NaN       NaN                       CH5 4HE              NaN   
3    NaN       NaN                       GIR 0AA              NaN   
4    NaN       NaN                      NOT NOWN              NaN   
5    NaN       NaN                        GIR0AB              NaN   
6    NaN       NaN                        NOR12A              NaN   
7    NaN       NaN                       no idea              NaN   
8    NaN       NaN                       W1A 1AA              NaN   
9    NaN       NaN                        missin              NaN   
10   NaN       NaN                      NP4  OGH              NaN   
11   NaN       NaN                      P012 OLL              NaN   
12   NaN       NaN                          p01s              NaN   
13   NaN       NaN                          ABCD              NaN   
14   NaN       NaN                                            NaN   
15   NaN       NaN                       ab123cd              NaN   
16   NaN       NaN                      un-known              NaN   
17   NaN       NaN                     B1    INJ              NaN   
18   NaN       NaN                       AB123CD              NaN   
19   NaN       NaN  No idea what the postcode is              NaN   
20   NaN       NaN              ???NP4-5DG_*#                 NaN   

    someOtherCol  
0            NaN  
1            NaN  
2            NaN  
3            NaN  
4            NaN  
5            NaN  
6            NaN  
7            NaN  
8            NaN  
9            NaN  
10           NaN  
11           NaN  
12           NaN  
13           NaN  
14           NaN  
15           NaN  
16           NaN  
17           NaN  
18           NaN  
19           NaN  
20           NaN  


Column 'pcdClean' needs to be added to the dataframe but the variable already exists; the pre-existing column has been reset.
Column 'pcd7' needs to be added to the dataframe but the variable already exists; the pre-existing column has been reset.
Column 'postcodeOutward' needs to be added to the dataframe but the variable already exists; the pre-existing column has been reset.
                        postcode pcdClean pcdFormatCheck     pcd7
0                         NP45DG   NP45DG           True  NP4 5DG
1                        CH647TE  CH647TE           True  CH647TE
2                        CH5 4HE   CH54HE           True  CH5 4HE
3                        GIR 0AA   GIR0AA           True  GIR 0AA
4                       NOT NOWN  missing          False      NaN
5                         GIR0AB   GIR0AB          False      NaN
6                         NOR12A   NOR12A           True  NOR 12A
7                        no idea   NO1DEA          False      NaN
8                        W1A 1AA   W1A1AA           True  W1A 1AA
9                         missin  missing          False      NaN
10                      NP4  OGH   NP40GH           True  NP4 0GH
11                      P012 OLL  PO120LL           True  PO120LL
12                          p01s     PO15          False      NaN
13                          ABCD     ABCD          False      NaN
14                                missing          False      NaN
15                       ab123cd  AB123CD          False      NaN
16                      un-known  missing          False      NaN
17                     B1    INJ    B11NJ           True  B1  1NJ
18                       AB123CD  AB123CD          False      NaN
19  No idea what the postcode is  missing          False      NaN
20              ???NP4-5DG_*#      NP45DG           True  NP4 5DG

Returned dataframe
==================

                        postcode  someOtherCol pcdClean pcdFormatCheck  \
0                         NP45DG           NaN   NP45DG           True   
1                        CH647TE           NaN  CH647TE           True   
2                        CH5 4HE           NaN   CH54HE           True   
3                        GIR 0AA           NaN   GIR0AA           True   
4                       NOT NOWN           NaN  missing          False   
5                         GIR0AB           NaN  missing          False   
6                         NOR12A           NaN   NOR12A           True   
7                        no idea           NaN  missing          False   
8                        W1A 1AA           NaN   W1A1AA           True   
9                         missin           NaN  missing          False   
10                      NP4  OGH           NaN   NP40GH           True   
11                      P012 OLL           NaN  PO120LL           True   
12                          p01s           NaN     PO15           True   
13                          ABCD           NaN  missing          False   
14                                         NaN  missing          False   
15                       ab123cd           NaN     AB12           True   
16                      un-known           NaN  missing          False   
17                     B1    INJ           NaN    B11NJ           True   
18                       AB123CD           NaN     AB12           True   
19  No idea what the postcode is           NaN  missing          False   
20              ???NP4-5DG_*#              NaN   NP45DG           True   

       pcd7 postcodeOutward postcodeInward pcdArea  
0   NP4 5DG             NP4            5DG      NP  
1   CH647TE            CH64            7TE      CH  
2   CH5 4HE             CH5            4HE      CH  
3   GIR 0AA             GIR            0AA     GIR  
4       NaN             NaN            NaN     NaN  
5       NaN             NaN            NaN     NaN  
6   NOR 12A             NOR            12A     NOR  
7       NaN             NaN            NaN     NaN  
8   W1A 1AA             W1A            1AA       W  
9       NaN             NaN            NaN     NaN  
10  NP4 0GH             NP4            0GH      NP  
11  PO120LL            PO12            0LL      PO  
12      NaN            PO15            NaN      PO  
13      NaN             NaN            NaN     NaN  
14      NaN             NaN            NaN     NaN  
15      NaN            AB12            NaN      AB  
16      NaN             NaN            NaN     NaN  
17  B1  1NJ              B1            1NJ       B  
18      NaN            AB12            NaN      AB  
19      NaN             NaN            NaN     NaN  
20  NP4 5DG             NP4            5DG      NP

```
---
### 6. phjGenerateCaseControlDataset()

```python
df = phjGenerateCaseControlDataset(phjAllDataDF,
                                   phjConsultationIDVarName,
                                   phjPatientIDVarName,
                                   phjCasesDF,
                                   phjMatchingVariablesList = None,
                                   phjControlsPerCaseInt = 1,
                                   phjScreeningRegexStr = None,
                                   phjScreeningRegexPathAndFileName = None,
                                   phjFreeTextVarName = None,
                                   phjControlType = 'consultation',
                                   phjConsultationDateVarName = None,
                                   phjAggDict = None,
                                   phjPrintResults = False)
```

### 7. phjSelectCaseControlDataset()

```python
df = epy.phjSelectCaseControlDataset(phjCasesDF,
                                     phjPotentialControlsDF,
                                     phjUniqueIdentifierVarName,
                                     phjMatchingVariablesList = None,
                                     phjControlsPerCaseInt = 1,
                                     phjPrintResults = False)
```

Python functions to randomly select and generate matched or unmatched case-control datasets.

#### Description

These two functions are closely related. In fact, the phjGenerateCaseControlDataset() function calls the phjSelectCaseControlDataset() function as part of the data selection process but both functions can be used independently. In essence, the difference between them is that the phjSelectCaseControlDataset() function takes as arguments two dataframes, one containing all the data that can be used as potential controls and the other containing a list of cases and returns a skeletel, bare-bones dataframe containing the unique IDs of cases and controls together with case/control status and, in the case of matched controls, the group membership. This dataframe needs to be merged with original data to retrieve all the original variables. The phjGenerateCaseControlDataset() function, in contrast, seeks to automate the entire process. It takes a dataframe of all data and a list of cases and returns either a consultation-based or patient-based case-control dataset that contains all the original variables.

##### General workflow

These functions were written to streamline a commonly-encountered workflow in our research group, namely the need to randomly select matched or unmatched controls from a large dataset having screened and confirmed the identification of cases. The controls that are selected to go with cases could be either consultation controls (i.e. a random selection of consultations from any animals not represented in the cases dataset) or patient controls (i.e. a random selection of animals that are not represented in the case dataset). In the latter case, consultation-specific information needs to be collapsed on patient ID to produce patient-based information.

It is assumed the cases and controls are ideally* stored in the same flat-file dataframe having the following basic structure:
 
 ```
 | consultID |       date | patientID | match | freetext | var2 | var3 |
 |-----------|------------|-----------|-------|----------|------|------|
 |      1001 | 2017-01-23 |      7324 |  catA |        a |  454 |  low |
 |      1002 | 2017-01-25 |      7324 |  catB |        b |  345 |  low |
 |      1003 | 2017-01-29 |      7324 |  catA |        c |  879 |  low |
 |      1004 | 2017-02-05 |      9767 |  catB |        a |  276 |  mid |
 |      1005 | 2017-02-11 |      9767 |  catB |        b |  478 |  mid |
 |      1006 | 2017-02-28 |      3452 |  catA |        c |  222 |  mid |
 |      1007 | 2017-03-23 |      5322 |  catA |        a |  590 |   hi |
 |      1008 | 2017-03-23 |      5322 |  catB |        b |  235 |   hi |
 |      1009 | 2017-04-02 |      5322 |  catB |        c |  657 |   hi |
 etc.
 ```
 
 * Cases that are not part of the whole dataset can be provided as a dataframe but the extra columns in the dataframe (i.e. other variables) need to be the same as the columns in the dataset containing 'all' the data from which the controls will be selected.
 
The following provides a brief description of the workflow used to identify and generate case-control datasets.

1. IDENTIFY CASES
The first step – prior to using these functions – is to identify cases within the data set.
* The whole database (or a partial excerpt) is downloaded and stored in a pandas dataframe. The data set consists of consultation ID, date of consultation, patient ID, freetext clinical narrative, variables to be used for matching (if required) and any other variables of interest.
* Potential cases are identified using a screening regex applied to the freetext clinical narrative.
* The researcher manually reads consultations of potenial cases to confirm that they are cases. The consultation numbers of confirmed cases are recorded either alone or as a slice of the dataframe.

2. IDENTIFY POTENIAL CONTROLS
The potential controls may be drawn from a larger range of data than was used to select the cases. As a result, it is important that the potential controls do not include any consultations that would have been identified as cases had they been included in the initial screening of cases.
   
• Identify all consultations that would have been identified as a potential CASE using the screen regex and identify the corresponding patient ID.

* Identify all corresponding patient IDs for consultations identified as confirmed cases.

* Remove all consultations from confirmed and potential case patients (regardless of whether the individual consultation was positive or negative. If a patient has one consultation where the regex identifies a match, all consultations from that animal should be excluded from the list of potential controls. The remaining consultations are, therefore, potential cases.

3. SELECT CONTROL DATASET
* Select suitable controls from the dataframe of potential controls, either unmatched or matched on give variables. The controls can be either consultation controls (where individual consultations are selected from the dataframe) or patient controls (where patients are selected).

* When selecting patient controls, it is necessary to collapse the consultation-based dataframe down to a patient-based on patient ID. A default, a collapsed dataframe will contain a 'count' variable to indicate how many consultations were recorded for each patient, the dates of the first and last consultations, and the last recorded entry for all other variables. This can, however, be altered as necessary.

4. MERGE CASE-CONTROL DATASET WITH ORIGINAL DATAFRAMES
The initial selection of case control dataset returns and minimalist dataframe that contains the bare minimum variables to be able to make the selection. After the case-control dataframe has been selected, it is necessary to merge with the original dataframe to return a complete dataset that contains all the original variables.

##### POINTS TO NOTE
* Collapsing a consultation-based dataframe to a patient-based dataframe requires a lot of computer processing that can be slow. As a result collapsing the consultation-based dataframe to a patient-based dataframe is only done after the controls have been selected; this ensures that only an minimal amount of computer processing is required to collapse the dataset.

* The list of confirmed cases can be passed to the function either as a list (or series) with not other variables, or as a dataframe which contains several variables, one of which is the consultation ID or patient ID (depending on whether the required control dataset consists of consultations or patients).

* Two dataframes need to be passed to the functions, one is a dataframe of 'ALL' data (including all necessary variables) and the other is a dataframe (or series or list) of confirmed cases. If the confirmed cases are all included in the dataframe of 'ALL' data then the final returned dataset (containing all the necessary other variables of interest) will be recreated from the dataframe of 'ALL' data. This means that any edits included in the dataframe of confirmed cases will be lost in favour of recreating the data from source. However, if the dataframe of cases contains some consultations or patients that are not included in the original dataframe then the returned dataframe will contain the data included in confirmed cases dataframe.

##### Selecting consultation controls

There are two main functions that can be used to create a case-control dataset:

1. phjGenerateCaseControlDataset()

   This function ultimates calls the phjSelectCaseControlDataset() function but it also attempts to automate a large proportion of the required pre- and post-production faffing around. For example, the function will determine whether a consultation-based or patient-based dataset is required, it will generate the dataframe of potential controls automatically and will merge the skeleton dataframe returned by phjSelectCaseControlDataset() function to produce a dataframe that is complete with all the variables that were included in the original dataframes.

2. phjSelectCaseControlDataset()

   This function takes, as arguments, two dataframes, one of confirmed cases and the other of potential controls. It then returns a 'skeleton' dataframe containing the minimal number of variables (e.g. ID, case/control and group membership (if a matched control set was required). It will be necessary to merge this skeleton with appropriate dataframes to produce a complete case-control dataset that contains all the necessary variables required for further analysis.

#### phjGenerateCaseControlDataset()

This function tries to deliver a complete solution for selecting controls for use in case-control studies.

##### Function parameters

##### Exceptions raised

None

##### Returns

##### Other notes

As mentioned previously, there are some limitions that should be recognised when passing case data. It is, therefore, important to pass suitable case data. The function should be passed a full dataframe containing 'ALL' the data. In fact, some of the confirmed cases need not be included in the dataframe of 'ALL' data (but there some limitations if this is the case). The requested case-control dataset can be either 'consultation-based' or 'patient-based'. In each of these cases, the confirmed cases can be passed in one of several formats (but, in some situations, returning a valid case-control dataset may not be feasible).

1. Consultation-based dataset requested
* Cases passed as a SERIES of consultation ID numbers, all of which are included in the dataframe of 'ALL' data.
   SUCCESS. Returned dataframe will contain variables reconstructed from 'ALL' data.

* Cases passed as a SERIES of consultation ID numbers, some of which are not included in the dataframe of 'ALL' data.
   FAILED. Required variables missing for some cases.

* Cases passed as a DATAFRAME containing several variables, one of which is the CONSULTATION ID and all consultations are a subset of the consultations in the dataframe of 'ALL' data.
   SUCCESS

* Cases passed as a DATAFRAME containing several variables, one of which is the CONSULTATION ID but not all consultations are included in the dataframe of 'ALL' data.
   FAILED

* Cases passed as a DATAFRAME containing all the same variables as included in the 'ALL' dataframe. Not all consultations are included in the dataframe of 'ALL' data.
   SUCCESS

2. Patient-based dataset requested
* Cases passed as a SERIES of case PATIENT IDs that are a subset of the information in the dataframe of 'ALL' data.
   SUCCESS

* Cases passed as a SERIES of case PATIENT IDs that are NOT a subset of the information in the dataframe of 'ALL' data (e.g. there may be extra rows).
   FAILED

* Cases passed as a DATAFRAME containing several variables, one of which is the PATIENT ID and all patients are a subset of the patients in the dataframe of 'ALL' data.
   SUCCESS

* Cases passed as a DATAFRAME containing several variables, one of which is the PATIENT ID but not all patients are a subset of the patients in the dataframe of 'ALL' data.
   FAILED

* Cases passed as a DATAFRAME containing numerous variables, one of which is the PATIENT ID and all patients are a subset of the patients in the dataframe of 'ALL' data. The variables are the same as those that will be produced when the consultation dataframe is collapsed based on patient ID data.
   SUCCESS

* Cases passed as a DATAFRAME containing numerous variables, one of which is the PATIENT ID but the patients are NOT a subset of the patients in the dataframe of 'ALL' data. The variables are the same as those that will be produced when the consultation dataframe is collapsed based on patient ID data.
   SUCCESS

#### phjSelectCaseControlDataset()

The phjSelectCaseControlDataset() function can be used independently to select case-control datasets from the SAVSNET database. It receives, as parameters, two Pandas dataframes, one containing known cases and, the other, potential controls. For unmatched controls, the algorithm selects the requested number of random controls from the database whilst for matched controls, the algorithm steps through each case in turn and selects the relevant number of control subjects from the second dataframe, matching on the list of variables provided as an argument to the function. The function then adds the details of the case and the selected controls to a separate, pre-defined dataframe before moving onto the next case.

Initially, the phjSelectCaseControlDataset() function calls phjParameterCheck() to check that passed parameters meet specified criteria (e.g. ensure lists are lists and ints are ints etc.). If all requirements are met, phjParameterCheck() returns True and phjSelectCaseControlDataset() continues.

The function requires a parameter called phjMatchingVariablesList. If this parameter is None (the default), an unmatched case-control dataset is produced. If, however, the parameter is a list of variable names, the function will return a dataset where controls have been matched on the variables in the list.

The phjSelectCaseControlDataset() function proceeds as follows:

1. Creates an empty dataframe in which selected cases and controls will be stored.
2. Steps through each case in the phjCasesDF dataframe, one at a time.
3. Gets data from matched variables for the case and store in a dict
4. Creates a mask for the controls dataframe to select all controls that match the cases in the matched variables
5. Applies mask to controls dataframe and count number of potential matches
6. Adds cases and controls to dataframe (through call to phjAddRecords() function)
7. Removes added control records from potential controls database so single case cannot be selected more than once
8. Returns Pandas dataframe containing list of cases and controls. This dataframe only contains columns for unique identifier, case and group id. It will, therefore need to be merged with the full database to get and additional required columns.

##### Function parameters

The function takes the following parameters:

1. **phjCasesDF**

   Pandas dataframe containing list of cases.
  
2. **phjPotentialControlsDF**

   Pandas dataframe containing a list of potential control cases.
  
3. **phjUniqueIdentifierVarName**

   Name of variable that acts as a unique identifier (e.g. consulations ID number would be a good example). N.B. In some cases, the consultation number is not unique but has been entered several times in the database, sometimes in very quick succession (ms). Data must be cleaned to ensure that the unique identifier variable is, indeed, unique.
  
4. **phjMatchingVariablesList** (Default = None)

   List of variable names for which the cases and controls should be matched. Must be a list. The default is None.
  
5. **phjControlsPerCaseInt** (Default = 1)

   Number of controls that should be selected per case.
  
6. **phjPrintResults** (Default= False)

   Print verbose output during execution of scripts. If running on Jupyter-Notebook, setting PrintResults = True causes a lot a output and can cause problems connecting to kernel.

##### Exceptions raised

None

##### Returns

Pandas dataframe containing a column containing the unique identifier variable, a column containing case/control identifier and – for matched case-control studies – a column containing a group identifier. The returned dataframe will need to be left-joined with another dataframe that contains additional required variables.

##### Other notes

Setting phjPrintResults = True can cause problems when running script on Jupyiter-Notebook.

#### Examples

Examples of the functions in use are given below:

```python
import pandas as pd
import epydemiology as epy

casesDF = pd.DataFrame({'animalID':[1,2,3,4,5],'var1':[43,45,34,45,56],'sp':['dog','dog','dog','dog','dog']})
potControlsDF = pd.DataFrame({'animalID':[11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30],
                              'var1':[34,54,34,23,34,45,56,67,56,67,78,98,65,54,34,76,87,56,45,34],
                              'sp':['dog','cat','dog','dog','cat','dog','cat','dog','cat','dog',
                                    'dog','dog','dog','cat','dog','cat','dog','dog','dog','cat']})

print("This dataframe contains all the cases of disease\n")
print(casesDF)
print("\n")
print("This dataframe contains all the animals you could potentially use as controls\n")
print(potControlsDF)
print("\n")

# Selecting unmatched controls
unmatchedDF = epy.phjSelectCaseControlDataset(phjCasesDF = casesDF,
                                              phjPotentialControlsDF = potControlsDF,
                                              phjUniqueIdentifierVarName = 'animalID',
                                              phjMatchingVariablesList = None,
                                              phjControlsPerCaseInt = 2,
                                              phjPrintResults = False)

print(unmatchedDF)
print("\n")

# Selecting controls that are matched to cases on variable 'sp'
matchedDF = epy.phjSelectCaseControlDataset(phjCasesDF = casesDF,
                                            phjPotentialControlsDF = potControlsDF,
                                            phjUniqueIdentifierVarName = 'animalID',
                                            phjMatchingVariablesList = ['sp'],
                                            phjControlsPerCaseInt = 2,
                                            phjPrintResults = False)

print(matchedDF)

```

Output

```
This dataframe contains all the cases of disease

   animalID   sp  var1
0         1  dog    43
1         2  dog    45
2         3  dog    34
3         4  dog    45
4         5  dog    56


This dataframe contains all the animals you could potentially use as controls

    animalID   sp  var1
0         11  dog    34
1         12  cat    54
2         13  dog    34
3         14  dog    23
4         15  cat    34
5         16  dog    45
6         17  cat    56
7         18  dog    67
8         19  cat    56
9         20  dog    67
10        21  dog    78
11        22  dog    98
12        23  dog    65
13        24  cat    54
14        25  dog    34
15        26  cat    76
16        27  dog    87
17        28  dog    56
18        29  dog    45
19        30  cat    34


UNMATCHED CONTROLS

    case  animalID
0      1         1
1      1         2
2      1         3
3      1         4
4      1         5
5      0        22
6      0        13
7      0        30
8      0        18
9      0        25
10     0        28
11     0        14
12     0        15
13     0        24
14     0        19


MATCHED CONTROLS

   animalID group case   sp
0         1     0    1  dog
1        28     0    0  dog
2        16     0    0  dog
3         2     1    1  dog
4        25     1    0  dog
5        27     1    0  dog
6         3     2    1  dog
7        21     2    0  dog
8        11     2    0  dog
9         4     3    1  dog
10       18     3    0  dog
11       14     3    0  dog
12        5     4    1  dog
13       22     4    0  dog
14       29     4    0  dog
```

---
### 8. phjCalculateBinomialProportions()
```python
df = phjCalculateBinomialProportions(phjTempDF,
                                     phjColumnsList = None,
                                     phjSuccess = 'yes',
                                     phjGroupVarName = None,
                                     phjMissingValue = 'missing',
                                     phjBinomialConfIntMethod = 'normal',
                                     phjAlpha = 0.05,
                                     phjPlotProportions = True,
                                     phjGroupsToPlotList = 'all',
                                     phjSortProportions = False,
                                     phjGraphTitle = None,
                                     phjPrintResults = False)
```
### 9. phjCalculateMultinomialProportions()
```python
df = phjCalculateMultinomialProportions(phjTempDF,
                                       phjCategoryVarName = None,
                                       phjGroupVarName = None,
                                       phjMissingValue = 'missing',
                                       phjMultinomialConfIntMethod = 'goodman',
                                       phjAlpha = 0.05,
                                       phjPlotRelFreq = True,
                                       phjCategoriesToPlotList = 'all',
                                       phjGroupsToPlotList = 'all',   # Currently not implemented
                                       phjGraphTitle = None,
                                       phjPrintResults = False)

```

#### Description

The above two functions – ``` phjCalculateBinomialProportions() and phjCalculateMultinomialProportions() ``` – are closely related and will be discussed and described together.

The functions can be used to rapidly summarise and visualise two common-encountered (at least, in my research) types of data. The first summarises data which consists of rows of records (representing individuals) and a series of binomial (dummy-esque) variables indicating whether a characteristic is present or absent (see below). These are not true dummy variables because categories are not necessarily mutually exclusive and each variable is considered as an individual characteristic. The confidence intervals for each category are calculated as individual binomial intervals (using StatsModels functions).

The second data structure consists of rows of data (representing individuals) and a single variable which contains numerous categories. In this case, all the categories are mutually exclusive. The proportions (or relative frequencies) are calculated for each category level and the confidence intervals are calculated as multinomial intervals (using StatsModels functions).

The series of binomial data might take the form shown on the left whilst the multinomial dataset might take the form shown on the right below:

```
Binomial data structure                                   Multinomial data structure
------------------------------------------------          ------------------------------
| id |    group  |       A |       B |       C |          | id |    group  |  category |
|----|-----------|---------|---------|---------|          |----|-----------|-----------|
|  1 |     case  |     yes |      no |     yes |          |  1 |     case  |    np.nan |
|  2 |     case  |     yes |  np.nan |     yes |          |  2 |     case  |   spaniel |
|  3 |  control  |      no | missing |     yes |          |  3 |     case  |   missing |
|  4 |     case  |      no |     yes |  np.nan |          |  4 |  control  |   terrier |
|  5 |  control  |      no |     yes |      no |          |  5 |  control  |    collie |
|  6 |  control  |      no |     yes |     yes |          |  6 |     case  |  labrador |
|  7 |     case  |      no |     yes |     yes |          |  7 |     case  |  labrador |
|  8 |     case  |     yes |      no |     yes |          |  8 |     case  |    collie |
|  9 |  control  | missing |      no |      no |          |  9 |  control  |   spaniel |
| 10 |     case  |     yes |      no |      no |          | 10 |  control  |   spaniel |
------------------------------------------------          | 11 |  control  |  labrador |
                                                          | 12 |  control  |    collie |
                                                          | 13 |     case  |   terrier |
                                                          | 14 |     case  |   terrier |
                                                          | 15 |     case  |   terrier |
                                                          | 16 |  control  |    collie |
                                                          | 17 |  control  |  labrador |
                                                          | 18 |  control  |  labrador |
                                                          | 19 |  control  |  labrador |
                                                          | 20 |     case  |   spaniel |
                                                          | 21 |     case  |   spaniel |
                                                          | 22 |     case  |    collie |
                                                          | 23 |     case  |    collie |
                                                          | 24 |     case  |    collie |
                                                          | 25 |   np.nan  |   terrier |
                                                          | 26 |   np.nan  |   spaniel |
                                                          ------------------------------

```

In both datasets, missing values can be entered either as np.nan or as a missing value string such as 'missing' which is then defined when the function is called.

These example datasets can be produced using the following Python code:

```python
import numpy as np
import pandas as pd

binomDataDF = pd.DataFrame({'id':[1,2,3,4,5,6,7,8,9,10],
                            'group':['case','case','control','case','control','control','case','case','control','case'],
                            'A':['yes','yes','no','no','no','no','no','yes','missing','yes'],
                            'B':['no',np.nan,'missing','yes','yes','yes','yes','no','no','no'],
                            'C':['yes','yes','yes',np.nan,'no','yes','yes','yes','no','no']})

multinomDataDF = pd.DataFrame({'id':[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26],
                               'group':['case','case','case','control','control','case','case','case','control','control','control','control','case','case','case','control','control','control','control','case','case','case','case','case',np.nan,np.nan],
                               'category':[np.nan,'spaniel','missing','terrier','collie','labrador','labrador','collie','spaniel','spaniel','labrador','collie','terrier','terrier','terrier','collie','labrador','labrador','labrador','spaniel','spaniel','collie','collie','collie','terrier','spaniel']})
```

The output summary tables in each case would be very similar:

```
    Summary table for multinomial proportions
    
    |---------|---------------|---------------|---------------|---------------|
    |         |    case_count | control_count |     case_prop |  control_prop |
    |---------|---------------|---------------|---------------|---------------|
    | spaniel |               |               |               |               |
    |---------|---------------|---------------|---------------|---------------|
    | terrier |               |               |               |               |
    |---------|---------------|---------------|---------------|---------------|
    | labrador|               |               |               |               |
    |---------|---------------|---------------|---------------|---------------|
    | collie  |               |               |               |               |
    |---------|---------------|---------------|---------------|---------------|
    
    * The 'count' columns give the absolute counts.
      The 'prop' columns give the proportion of the total.
    
    
    Summary table for binomial proportions
    
    |-----|---------------|-----------------|---------------|---------------|---------------|---------------|
    |     |  case_success | control_success |    case_total | control_total |     case_prop |  control_prop |
    |-----|---------------|-----------------|---------------|---------------|---------------|---------------|
    |   A |               |                 |               |               |               |               |
    |-----|---------------|-----------------|---------------|---------------|---------------|---------------|
    |   B |               |                 |               |               |               |               |
    |-----|---------------|-----------------|---------------|---------------|---------------|---------------|
    |   C |               |                 |               |               |               |               |
    |-----|---------------|-----------------|---------------|---------------|---------------|---------------|
    
    * The 'success' columns give the number of 'successes' in each variable.
      The 'total' columns give the total number of rows (missing values excluded) for each variable.
      The 'prop' columns give the proportion of successes.
```

The confidence intervals (either binomial or multinomial) are added to the table as separate columns containing lower and upper limits.

And the data would be plotted in a similar fashion (although the method used to calculate the error bars would be different).

```
     R  |           |-|                                 |           |-|             
     e  |           |/|-|                               |           |/|-|           |/| case
     l  |     |-|   |/| |           |-|               P |     |-|   |/| |           
        |     | |   |/| |           |/|-|             r |     | |   |/| |           | | control
     F  |   |-| |   |/| |     |-|   |/| |       OR    o |   |-| |   |/| |     |-|   
     r  |   |/| |   |/| |   |-| |   |/| |             p |   |/| |   |/| |   |-| |   
     e  |   |/| |   |/| |   |/| |   |/| |               |   |/| |   |/| |   |/| |   
     q  |-----------------------------------            |---------------------------
             spn     ter     lab     col                      A       B       C

```

#### Function parameters

**phjCalculateBinomialProportions() function**

The phjCalculateBinomialProportions() function takes the following parameters:

1. **phjTempDF**

   The Pandas dataframe containing the data to be analysed. The dataframe does not need to be sliced before use because the data columns that need to be used are defined in the function arguments.

2. **phjColumnsList** (default = None)

   A list of the columns that need to be analyses. Each of these columns should be binary variables and should contain only binary data. Missing values (either in the form of a specified missing value or a np.nan value will be removed before analysis).

3. **phjSuccess** (default = 'yes')

   The text string or value that is used to indicate a positive value or a 'success'. The default assumes that data will be coded as 'yes' or 'no'.

4. **phjGroupVarName** (default = None)

   It is likely that some analyses will need to summarise data over two distinct categories (e.g. 'case' and 'control' data may be summarised separately). This varialble should contain the column heading for the variable that defines group membership. The default is None. If phjGroupVarName is None, the whole dataset is analysed as a single group.

5. **phjMissingValue** (default = 'missing')

   The text string or value that indicates a success.

6. **phjBinomialConfIntMethod** (default = 'normal')

   This argument defines the method to be used to calculate the binomial confidence intervals. The options available are those that can be handled by the statsmodel.stats.proporotion proportion_confint() method. The default is 'normal' but the full list of options (taken from the statsmodels website) are:
   1. `normal` : asymptotic normal approximation
   2. `agresti_coull` : Agresti-Coull interval
   3. `beta` : Clopper-Pearson interval based on Beta distribution
   4. `wilson` : Wilson Score interval
   5. `jeffreys` : Jeffreys Bayesian Interval
   6. `binom_test` : experimental, inversion of binom_test

7. **phjAlpha** (default = 0.05)

   The desired value for alpha; the default is 0.05 (which leads to the calculation of 95% confidence intervals.

8. **phjPlotProportions** (default = True)

   Determines whether a bar chart of proportions (with errors bars) is plotted.

9. **phjGroupsToPlotList** (default = 'all')

   The data may be calculated for numerous groups but it may not be desired for the plot to display all groups. This argument is a list of groups which should be displayed in the plot.

10. **phjSortProportions** (default = False)

   If only a single group is plotted, this argument indicates whether the columns should be sorted. Default is 'False' but other options are 'asc' or desc'.

11. **phjGraphTitle** (default = None)

   The title of the graph.

12. **phjPrintResults** (default = False)

   Indicates whehter the results should be printed to screed as the function progresses.



**phjCalculateMultinomialProportions() function**

The phjCalculateMultinomialProportions() function takes the following parameters:

1. **phjTempDF**

   The Pandas dataframe containing the data to be analysed. The dataframe does not need to be sliced before use because the data columns that need to be used are defined in the function arguments.

2. **phjCategoryVarName** (default = None)

   The name of the column that defines category.

3. **phjGroupVarName** (default = None)

   It is likely that some analysis will need to summarise data over two distinct categories (e.g. 'case' and 'control' data may be summarised separately). This varialble should contain the column heading for the variable that defines group membership. The default is None. If phjGroupVarName is None, the whole dataset is analysed as a single group.


4. **phjMissingValue** (default = 'missing')

   The text string or value that indicates a success.

5. **phjMultinomialConfIntMethod** (default = 'goodman')

   This argument defines the method to be used to calculate the multinomial confidence intervals. The options available are those that can be handled by the statsmodel.stats.proporotion multinomial_proportions_confint() method. The default is 'normal' but the full list of options (taken from the statsmodels website) are:
   1. `goodman`: based on a chi-squared approximation, valid if all values in `counts` are greater or equal to 5
   2. `sison-glaz`: less conservative than `goodman`, but only valid if `counts` has 7 or more categories (``len(counts) >= 7``)

6. **phjAlpha** (default = 0.05)

   The desired value for alpha; the default is 0.05 (which leads to the calculation of 95% confidence intervals.

7. **phjPlotRelFreq** (default = True)

   Determines whether a bar chart of proportions (with errors bars) is plotted.

8. **phjCategoriesToPlotList** (default = 'all')

  A list of column names that should be plotted on a bar chart.

9. **phjGroupsToPlotList** (default = 'all')

   The data may be calculated for numerous groups but it may not be desired for the plot to display all groups. This argument is a list of groups which should be displayed in the plot.

10. **phjGraphTitle** (default = None)

   The title of the graph.

11. **phjPrintResults** (default = False)

   Indicates whehter the results should be printed to screed as the function progresses.

#### Exceptions raised

None

#### Returns

These functions both return Pandas dataframes containing a table of proportions and confidence intervals.

#### Other notes

None

#### Example

An example of the function in use is given below:

```python
# Example calculating binomial proportions (using phjCaculateBinomialProportions() function)
# ========================================

phjTempDF = pd.DataFrame({'group':['g1','g1','g2','g1','g2','g2','g1','g1','g2','g1'],
                          'A':['yes','yes','no','no','no','no','no','yes',np.nan,'yes'],
                          'B':['no',np.nan,np.nan,'yes','yes','yes','yes','no','no','no'],
                          'C':['yes','yes','yes',np.nan,'no','yes','yes','yes','no','no']})

print(phjTempDF)
print('\n')

phjPropDF = epy.phjCalculateBinomialProportions(phjTempDF = phjTempDF,
                                                phjColumnsList = ['A','B','C'],
                                                phjSuccess = 'yes',
                                                phjGroupVarName = 'group',
                                                phjMissingValue = 'missing',
                                                phjBinomialConfIntMethod = 'normal',
                                                phjAlpha = 0.05,
                                                phjPlotProportions = True,
                                                phjGroupsToPlotList = 'all',
                                                phjSortProportions = True,
                                                phjGraphTitle = None,
                                                phjPrintResults = False)

print(phjPropDF)
```

```python
# Example of calculating multinomial proportions (using phjCalculateMultinomialProportions() function)
# ==============================================

phjTempDF = pd.DataFrame({'group':['case','case','case','control','control','case','case','case','control','control','control','control','case','case','case','control','control','control','control','case','case','case','case','case',np.nan,np.nan],
                          'category':[np.nan,'spaniel','missing','terrier','collie','labrador','labrador','collie','spaniel','spaniel','labrador','collie','terrier','terrier','terrier','collie','labrador','labrador','labrador','spaniel','spaniel','collie','collie','collie','terrier','spaniel'],
                          'catint':[1,2,3,2,3,2,1,2,1,2,3,2,3,2,3,1,2,3,2,3,2,3,2,3,1,2]})

print(phjTempDF)
print('\n')

phjRelFreqDF = epy.phjCalculateMultinomialProportions(phjTempDF = phjTempDF,
                                                      phjCategoryVarName = 'category',
                                                      phjGroupVarName = 'group',
                                                      phjMissingValue = 'missing',
                                                      phjMultinomialConfIntMethod = 'goodman',
                                                      phjAlpha = 0.05,
                                                      phjPlotRelFreq = True,
                                                      phjCategoriesToPlotList = 'all',
                                                      phjGroupsToPlotList = 'all',   # Currently not implemented
                                                      phjGraphTitle = 'Relative frequencies (Goodman CI)',
                                                      phjPrintResults = True)

print(phjRelFreqDF)

```
---
### 10. phjOddsRatio()

```python
df = phjOddsRatio(phjTempDF,
                  phjCaseVarName,
                  phjCaseValue,
                  phjRiskFactorVarName,
                  phjRiskFactorBaseValue)
```

#### Description

This function can be used to calculate odds ratios and 95% confidence intervals for case-control studies. The function is passed a Pandas dataframe containing the data together with the name of the 'case' variable and the name of the potential risk factor variable. The function returns a Pandas dataframe based on a 2 x 2 or n x 2 contingency table together with columns containing the odds, odds ratios and 95% confidence intervals (Woolf). Rows that contain a missing value in either the case variable or the risk factor variable are removed before calculations are made.

#### Function parameters

The function takes the following parameters:

1. **phjTempDF**

   This is a Pandas dataframe that contains the data to be analysed. One of the columns should be a variable that indicates whether the row is a case or a control.

2. **phjCaseVarName**

   Name of the variable that indicates whether the row is a case or a control.

3. **phjCaseValue**

   The value used in phjCaseVarName variable to indicate a case (e.g. True, yes, 1, etc.)

4. **phjRiskFactorVarName**

   The name of the potential risk factor to be analysed. This needs to be a categorical variable.

5. **phjRiskFactorBaseValue**

   The level or stratum of the potential risk factor that will be used as the base level in the calculation of odds ratios.

#### Exceptions raised

None.

#### Returns

Pandas dataframe containing a cross-tabulation of the case and risk factor varible. In addition, odds, odds ratios and 95% confidence interval (Woolf) of the odds ratio is presented.

#### Other notes

None.

#### Example

An example of the function in use is given below:

```python
import pandas as pd
import epydemiology as epy

tempDF = pd.DataFrame({'caseN':[1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0],
                       'caseA':['y','y','y','y','y','y','y','y','n','n','n','n','n','n','n','n','n','n','n','n'],
                       'catN':[1,2,3,2,3,4,3,2,3,4,3,2,1,2,1,2,3,2,3,4],
                       'catA':['a','a','b','b','c','d','a','c','c','d','a','b','c','a','d','a','b','c','a','d'],
                       'floatN':[1.2,4.3,2.3,4.3,5.3,4.3,2.4,6.5,4.5,7.6,5.6,5.6,4.8,5.2,7.4,5.4,6.5,5.7,6.8,4.5]})

phjORTable = epy.phjOddsRatio( phjTempDF = tempDF,
                               phjCaseVarName = 'caseA',
                               phjCaseValue = 'y',
                               phjRiskFactorVarName = 'catA',
                               phjRiskFactorBaseValue = 'a')

pd.options.display.float_format = '{:,.3f}'.format

print(phjORTable)
```

Output

```
caseA  y  n  odds    or       95pcCI_Woolf
catA                                      
a      3  4 0.750 1.000                ---
b      2  2 1.000 1.333  [0.1132, 15.7047]
c      2  3 0.667 0.889   [0.0862, 9.1622]
d      1  3 0.333 0.444   [0.0295, 6.7031]
```
---
### 11. phjRelativeRisk()

```python
df = phjRelativeRisk(phjTempDF,
                     phjCaseVarName,
                     phjCaseValue,
                     phjRiskFactorVarName,
                     phjRiskFactorBaseValue)
```

#### Description

This function can be used to calculate relative risk (risk ratios) and 95% confidence intervals for cross-sectional and longitudinal (cohort) studies. The function is passed a Pandas dataframe containing the data together with the name of the 'case' variable and the name of the potential risk factor variable. The function returns a Pandas dataframe based on a 2 x 2 or n x 2 contingency table together with columns containing the risk, risk ratios and 95% confidence intervals. Rows that contain a missing value in either the case variable or the risk factor variable are removed before calculations are made.

#### Function parameters

The function takes the following parameters:

1. **phjTempDF**

   This is a Pandas dataframe that contains the data to be analysed. One of the columns should be a variable that indicates whether the row has disease (diseased) or not (healthy).

2. **phjCaseVarName**

   Name of the variable that indicates whether the row has disease or is healthy.

3. **phjCaseValue**

   The value used in phjCaseVarName variable to indicate disease (e.g. True, yes, 1, etc.)

4. **phjRiskFactorVarName**

   The name of the potential risk factor to be analysed. This needs to be a categorical variable.

5. **phjRiskFactorBaseValue**

   The level or stratum of the potential risk factor that will be used as the base level in the calculation of odds ratios.

#### Exceptions raised

None

#### Returns

Pandas dataframe containing a cross-tabulation of the disease status and risk factor varible. In addition, risk, relative risk and 95% confidence interval of the relative risk is presented.

#### Other notes

None

#### Example

An example of the function in use is given below:

```python
import pandas as pd
import epydemiology as epy

# Pretend this came from a cross-sectional study (even though it's the same example data as used for the case-control study above.
tempDF = pd.DataFrame({'caseN':[1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0],
                       'caseA':['y','y','y','y','y','y','y','y','n','n','n','n','n','n','n','n','n','n','n','n'],
                       'catN':[1,2,3,2,3,4,3,2,3,4,3,2,1,2,1,2,3,2,3,4],
                       'catA':['a','a','b','b','c','d','a','c','c','d','a','b','c','a','d','a','b','c','a','d'],
                       'floatN':[1.2,4.3,2.3,4.3,5.3,4.3,2.4,6.5,4.5,7.6,5.6,5.6,4.8,5.2,7.4,5.4,6.5,5.7,6.8,4.5]})

phjRRTable = epy.phjRelativeRisk( phjTempDF = tempDF,
                                  phjCaseVarName = 'caseA',
                                  phjCaseValue = 'y',
                                  phjRiskFactorVarName = 'catA',
                                  phjRiskFactorBaseValue = 'a')

pd.options.display.float_format = '{:,.3f}'.format

print(phjRRTable)
```

Output

```
caseA  y  n  risk    rr            95pcCI
catA                                     
a      3  4 0.429 1.000               ---
b      2  2 0.500 1.167  [0.3177, 4.2844]
c      2  3 0.400 0.933  [0.2365, 3.6828]
d      1  3 0.250 0.583  [0.0872, 3.9031]
```
---

### 12. phjCategoriseContinuousVariable()

```python
df,list = phjCategoriseContinuousVariable(phjTempDF,
                                          phjContinuousVarName = None,
                                          phjMissingValue = 'missing',
                                          phjNumberOfCategoriesInt = 5,
                                          phjNewCategoryVarName = None,
                                          phjCategorisationMethod = 'jenks',
                                          phjReturnBreaks = True,
                                          phjPrintResults = False)
```
or
```
df = phjCategoriseContinuousVariable(phjTempDF,
                                     phjContinuousVarName = None,
                                     phjMissingValue = 'missing',
                                     phjNumberOfCategoriesInt = 5,
                                     phjNewCategoryVarName = None,
                                     phjCategorisationMethod = 'jenks',
                                     phjReturnBreaks = False,
                                     phjPrintResults = False)
```
#### Description

#### Function parameters

#### Exceptions raised

None

#### Returns

Pandas dataframe containing a tabulation of the log odds for a categorised variable.

#### Other notes

Check:
1. The extreme values in the list of breaks are extended by a small percentage to make sure they include all values. Check whether these are the values that are actually returned as a list from the function.
2. When calculating the Jenks breaks, the process can be very slow. Jenks breaks are therefore calculated on a random sample taken from the dataframe. The lowest and highest values are replaced by the data minimum and maximum (possibly extended by a small percentage as in 1. above).

#### Example

An example of the function in use is given below:

```python
# Define example dataset
phjTempDF = pd.DataFrame({'binDepVar':['yes']*50000 + ['no']*50000,
                          'riskFactorCont':np.random.uniform(0,1,100000)})

with pd.option_context('display.max_rows', 10, 'display.max_columns', 5):
    print(phjTempDF)

    
# Categorise a continuous variable
phjTempDF, phjBreaksList = epy.phjCategoriseContinuousVariable(phjTempDF = phjTempDF,
                                                               phjContinuousVarName = 'riskFactorCont',
                                                               phjMissingValue = 'missing',
                                                               phjNumberOfCategoriesInt = 6,
                                                               phjNewCategoryVarName = 'catVar',
                                                               phjCategorisationMethod = 'jenks',
                                                               phjReturnBreaks = True,
                                                               phjPrintResults = False)

with pd.option_context('display.max_rows', 10, 'display.max_columns', 5):
    print('\nCategorised variable')
    print(phjTempDF)
    print('\n')
    print('Breaks')
    print(phjBreaksList)
```
Output
```
      binDepVar  riskFactorCont
0           yes        0.268203
1           yes        0.871220
2           yes        0.501282
3           yes        0.858652
4           yes        0.723276
...         ...             ...
99995        no        0.943760
99996        no        0.953255
99997        no        0.080429
99998        no        0.091481
99999        no        0.925220

[100000 rows x 2 columns]

Categorised variable
      binDepVar  riskFactorCont  catVar
0           yes        0.268203       1
1           yes        0.871220       5
2           yes        0.501282       3
3           yes        0.858652       5
4           yes        0.723276       4
...         ...             ...     ...
99995        no        0.943760       5
99996        no        0.953255       5
99997        no        0.080429       0
99998        no        0.091481       0
99999        no        0.925220       5

[100000 rows x 3 columns]


Breaks
[1.1083476758642629e-05, 0.16544335416294453, 0.32239443898189324, 0.48614660309506053, 0.65418653301496088, 0.83115022562356933, 1.0009938172219826]
```
---

### 13. phjViewLogOdds()

```python
df = phjViewLogOdds(phjTempDF,
                    phjBinaryDepVarName = None,
                    phjContIndepVarName = None,
                    phjCaseValue = 1,
                    phjMissingValue = 'missing',
                    phjNumberOfCategoriesInt = 5,
                    phjNewCategoryVarName = None,
                    phjCategorisationMethod = 'jenks',
                    phjGroupNameVar = None,
                    phjAlpha = 0.05,
                    phjPrintResults = False)
```
#### Description

#### Function parameters

#### Exceptions raised

None

#### Returns

Pandas dataframe containing a tabulation of the log odds for a categorised variable.

#### Other notes

See comments relating to phjCategoriseContinuousVariable() function.

#### Example

An example of the function in use is given below:

```python
# Define example dataset
phjTempDF = pd.DataFrame({'binDepVar':['yes']*50000 + ['no']*50000,
                          'riskFactorCont':np.random.uniform(0,1,100000)})

with pd.option_context('display.max_rows', 10, 'display.max_columns', 5):
    print(phjTempDF)

    
# View log odds
phjTempDF = phjViewLogOdds(phjTempDF = phjTempDF,
                           phjBinaryDepVarName = 'binDepVar',
                           phjContIndepVarName = 'riskFactorCont',
                           phjCaseValue = 'yes',
                           phjMissingValue = 'missing',
                           phjNumberOfCategoriesInt = 8,
                           phjNewCategoryVarName = 'categoricalVar',
                           phjCategorisationMethod = 'quantile',
                           phjGroupNameVar = None,
                           phjPrintResults = False)

with pd.option_context('display.max_rows', 10, 'display.max_columns', 10):
    print(phjTempDF)
```
Output
```
                 yes    no      odds        or      95pcCI_Woolf   logodds  \
categoricalVar                                                               
0               6371  6385  0.997807  1.018299  [0.9693, 1.0698] -0.002195   
1               6184  6311  0.979876  1.000000               --- -0.020329   
2               6334  6313  1.003326  1.023932  [0.9745, 1.0758]  0.003321   
3               6239  6299  0.990475  1.010816  [0.9619, 1.0622] -0.009571   
4               6254  6123  1.021395  1.042371  [0.9918, 1.0955]  0.021169   
5               6155  6276  0.980720  1.000861  [0.9524, 1.0518] -0.019468   
6               6190  6133  1.009294  1.030022  [0.9800, 1.0826]  0.009251   
7               6273  6160  1.018344  1.039258  [0.9889, 1.0922]  0.018178   

                      se  95CI_llimit  95CI_ulimit  catMidpoints  
categoricalVar                                                    
0               0.017708    -0.036902     0.032512      0.062007  
1               0.017893    -0.055399     0.014741      0.187506  
2               0.017784    -0.031536     0.038178      0.312504  
3               0.017862    -0.044579     0.025437      0.437502  
4               0.017978    -0.014068     0.056406      0.562501  
5               0.017939    -0.054628     0.015692      0.687499  
6               0.018017    -0.026061     0.044563      0.812497  
7               0.017937    -0.016979     0.053335      0.937496  
```
---
