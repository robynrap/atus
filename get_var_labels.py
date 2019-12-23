
import json
import numpy as np
import pandas as pd
import xmltodict

def get_var_labels(atus_xml_file_name_string): 
    
    """
    Takes the file name of an ATUS XML file. 
    Returns pandas dataframe with categorical variable names, labels, and corresponding values.
    """
    
    # Importing XML file and saving as JSON
    with open(atus_xml_file_name_string) as fd:
        xml_json = xmltodict.parse(fd.read())

    # Saving number of variables in the ATUS data file
    n_vars = len(xml_json['codeBook']['dataDscr']['var'])

    # Creating empty dataframe
    df = pd.DataFrame(data = {'var_name': [], 'value': [], 'label': []})

    # Looping through JSON to create dataframe
    for x in range(0, n_vars): 
        try: 
            label_length = len(xml_json['codeBook']['dataDscr']['var'][x]['catgry'])

            for i in range(0,label_length):
                value = xml_json['codeBook']['dataDscr']['var'][x]['catgry'][i]['catValu']
                label = xml_json['codeBook']['dataDscr']['var'][x]['catgry'][i]['labl']
                var_name = xml_json['codeBook']['dataDscr']['var'][x]['@ID']
                df.loc[len(df)] = [var_name, label, value]

        except: 
            pass

    return df 

