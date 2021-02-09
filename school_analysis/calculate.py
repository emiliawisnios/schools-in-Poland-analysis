import numpy as np
import pandas as pd


def students_per_teacher_minimum(school_dataframe):
    school_dataframe.drop(school_dataframe[school_dataframe['Teachers'] == 0].index, inplace=True)
    school_dataframe['Average_min'] = school_dataframe['Students']/school_dataframe['Teachers']
    school_dataframe.replace(np.inf, -1, inplace=True)
    school_dataframe.replace(np.nan, -1, inplace=True)
    school_dataframe = school_dataframe.round(2)
    districts_and_type = school_dataframe.groupby(['District', 'SchoolType'])['Average_min'].min()
    return districts_and_type


def students_per_teacher_maximum(school_dataframe):
    school_dataframe.drop(school_dataframe[school_dataframe['Teachers'] == 0].index, inplace=True)
    school_dataframe['Average_max'] = school_dataframe['Students']/school_dataframe['Teachers']
    school_dataframe.replace(np.inf, -1, inplace=True)
    school_dataframe.replace(np.nan, -1, inplace=True)
    school_dataframe = school_dataframe.round(2)
    districts_and_type = school_dataframe.groupby(['District', 'SchoolType'])['Average_max'].max()
    return districts_and_type


def students_per_teacher_average(school_dataframe):
    school_dataframe.drop(school_dataframe[school_dataframe['Teachers'] == 0].index, inplace=True)
    districts_and_type = school_dataframe.groupby(['District', 'SchoolType']).agg({'Students': 'sum',
                                                                                       'Teachers': 'sum'})
    districts_and_type['Average'] = districts_and_type['Students']/ districts_and_type['Teachers']
    districts_and_type.replace(np.inf, -1, inplace=True)
    districts_and_type.replace(np.nan, -1, inplace=True)
    districts_and_type = districts_and_type.round(2)
    districts_and_type_drop = districts_and_type.drop(['Students', 'Teachers'], axis=1)
    return districts_and_type_drop



def students_per_teacher_minimum_per_DistrictType(school_dataframe):
    school_dataframe.drop(school_dataframe[school_dataframe['Teachers'] == 0].index, inplace=True)
    school_dataframe['Average_min'] = school_dataframe['Students']/school_dataframe['Teachers']
    school_dataframe.replace(np.inf, -1, inplace=True)
    school_dataframe.replace(np.nan, -1, inplace=True)
    school_dataframe = school_dataframe.round(2)
    districts_and_type = school_dataframe.groupby(['DistrictType', 'SchoolType'])['Average_min'].min()
    return districts_and_type



def students_per_teacher_maximum_per_DistrictType(school_dataframe):
    school_dataframe.drop(school_dataframe[school_dataframe['Teachers'] == 0].index, inplace=True)
    school_dataframe['Average_max'] = school_dataframe['Students']/school_dataframe['Teachers']
    school_dataframe.replace(np.inf, -1, inplace=True)
    school_dataframe.replace(np.nan, -1, inplace=True)
    school_dataframe = school_dataframe.round(2)
    districts_and_type = school_dataframe.groupby(['DistrictType', 'SchoolType'])['Average_max'].max()
    return districts_and_type


def students_per_teacher_average_per_DistrictType(school_dataframe):
    school_dataframe.drop(school_dataframe[school_dataframe['Teachers'] == 0].index, inplace=True)
    districts_and_type = school_dataframe.groupby(['DistrictType', 'SchoolType']).agg({'Students': 'sum',
                                                                                       'Teachers': 'sum'})
    districts_and_type['Average'] = districts_and_type['Students']/ districts_and_type['Teachers']
    districts_and_type.replace(np.inf, -1, inplace=True)
    districts_and_type.replace(np.nan, -1, inplace=True)
    districts_and_type = districts_and_type.round(2)
    districts_and_type_drop = districts_and_type.drop(['Students', 'Teachers'], axis=1)
    return districts_and_type_drop
