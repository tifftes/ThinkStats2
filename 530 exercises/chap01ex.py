"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2010 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function, division

import sys
import numpy as np
import thinkstats2
import nsfg

#READ RESPONDENT FILE
def ReadFemResp(dct_file='2002FemResp.dct',
                dat_file='2002FemResp.dat.gz',
                nrows=None):
    """Reads the NSFG respondent data.

    dct_file: string file name
    dat_file: string file name

    returns: DataFrame
    """
    dct = thinkstats2.ReadStataDct(dct_file)
    df = dct.ReadFixedWidth(dat_file, compression='gzip', nrows=nrows)
    CleanFemResp(df)
    return df

def CleanFemResp(df):
    """Recodes variables from the respondent frame.

    df: DataFrame
    """
    pass

def ValidatePregnum(resp):
    """Validate pregnum in the respondent file.

    resp: respondent DataFrame
    """
    #READ PREGNANCY DATAFRAME
    #REFERRED TO EX 1-1 IN [3]
    resp = nsfg.ReadFemPreg()
    
    # make the map from caseid to list of pregnancy indices
    #GIVEN IN EXERCISE INSTRUCTIONS
    #REFERRED TO EX 1-1 IN [13]
    preg_map = nsfg.MakePregMap(preg)
    
    # iterate through the respondent pregnum series
    for index, pregnum in resp.pregnum.iteritems():
        caseid = resp.caseid[index]
        indices = preg_map[caseid]

        # check that pregnum from the respondent file equals
        # the number of records in the pregnancy file
        if len(indices) != pregnum:
            print(caseid, len(indices), pregnum)
            return False

    return True


def main():
    """Tests the functions in this module.

    script: string script name
    """
    # read and validate the respondent file
    resp = ReadFemResp()
    #DISPLAY PREGNUM  AND VALUE COUNT OF 
    assert(len(resp) == 7643)
    assert(resp.pregnum.value_counts()[1] == 1267)

    # validate that the pregnum column in `resp` matches the number
    # REMOVED PREG BC ONLY ASKING FOR RESP FILE
    assert(ValidatePregnum(resp))

    #MADE A COPY OF NSFG.PY AND MAIN FUNCTION ONLY HAD PRINT ALL TESTS PASSED W/O %
    #FOUND THESE LINES OF CODE BELOW IN ORIGINAL chap01ex.py GITHUB/THINKSTATS2/CODE FILE
    print('%s: All tests passed.' % script)


if __name__ == '__main__':
    main(*sys.argv)


