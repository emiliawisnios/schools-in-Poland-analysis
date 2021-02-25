import numpy as np
import pandas as pd


STUDENTS_AGES = {'Przedszkole': [3,6, '3-6'],
               'Szkoła podstawowa': [7,12, '7-12'],
               'Gimnazjum': [13,15, '13-15'],
               'Liceum ogólnokształcące': [16,18, '16-18'],
               'Szkoła policealna': [19, 24, '19-24']}


def students_per_teacher_per_district(school_dataframe):
    school_dataframe.drop(school_dataframe[school_dataframe['Teachers'] == 0].index, inplace=True)
    school_dataframe['Students_per_Teachers'] = school_dataframe['Students'] / school_dataframe['Teachers']
    school_dataframe_grouped = school_dataframe.groupby(
        ['District', 'SchoolType']).agg({'Students_per_Teachers': ['min', 'max', 'mean']})
    return school_dataframe_grouped


def students_per_teacher_per_district_type(school_dataframe):
    school_dataframe.drop(school_dataframe[school_dataframe['Teachers'] == 0].index, inplace=True)
    school_dataframe['Students_per_Teachers'] = school_dataframe['Students'] / school_dataframe['Teachers']
    school_dataframe_grouped = school_dataframe.groupby(
        ['DistrictType', 'SchoolType']).agg({'Students_per_Teachers': ['min', 'max', 'mean']})
    return school_dataframe_grouped


def sum_of_students(inhabitants_dataframe):
    district = []
    students_years = []
    number_of_students = []

    for index, row in inhabitants_dataframe.iterrows():
        if 3 <= row['Age'] <= 6:
            district.append(row['District'])
            students_years.append('3-6')
            number_of_students.append(row['Total'])
        elif 7 <= row['Age'] <= 12:
            district.append(row['District'])
            students_years.append('7-12')
            number_of_students.append(row['Total'])
        elif 13 <= row['Age'] <= 15:
            district.append(row['District'])
            students_years.append('13-15')
            number_of_students.append(row['Total'])
        elif 16 <= row['Age'] <= 18:
            district.append(row['District'])
            students_years.append('16-18')
            number_of_students.append(row['Total'])
        elif 19 <= row['Age'] <= 24:
            district.append(row['District'])
            students_years.append('19-24')
            number_of_students.append(row['Total'])
        else:
            pass

    d = {'District': district, 'Age': students_years, 'Number_of_students': number_of_students}
    df = pd.DataFrame(data=d)
    students_in_total = df.groupby(['District', 'Age']).agg({'Number_of_students': 'sum'})

    students_in_total.reset_index(inplace=True)
    return students_in_total


def percentage_of_students(inhabitants_dataframe, students_in_total):
    percent = []
    inhabitants_dataframe = inhabitants_dataframe[
        (inhabitants_dataframe['Age'] > 2) & (inhabitants_dataframe['Age'] < 25)]
    inhabitants_dataframe.to_csv('pojebane_dane.csv')
    for index, row in inhabitants_dataframe.iterrows():
        if 3 <= row['Age'] <= 6:
            correct_row = students_in_total[
                (students_in_total['District'] == row['District']) & (students_in_total[
                    'Age'] == '3-6')]
            sums = int(correct_row['Number_of_students'])
            number_of_stud = int(row['Total'])
            perc = round(number_of_stud / sums, 2)
            percent.append(perc)
        elif 7 <= row['Age'] <= 12:
            correct_row = students_in_total[
                (students_in_total['District'] == row['District']) & (students_in_total[
                    'Age'] == '7-12')]
            sums = int(correct_row['Number_of_students'])
            number_of_stud = int(row['Total'])
            perc = round(number_of_stud / sums, 2)
            percent.append(perc)
        elif 13 <= row['Age'] <= 15:
            correct_row = students_in_total[
                (students_in_total['District'] == row['District']) & (students_in_total[
                    'Age'] == '13-15')]
            sums = int(correct_row['Number_of_students'])
            number_of_stud = int(row['Total'])
            perc = round(number_of_stud / sums, 2)
            percent.append(perc)
        elif 16 <= row['Age'] <= 18:
            correct_row = students_in_total[
                (students_in_total['District'] == row['District']) & (students_in_total[
                    'Age'] == '16-18')]
            sums = int(correct_row['Number_of_students'])
            number_of_stud = int(row['Total'])
            perc = round(number_of_stud / sums, 2)
            percent.append(perc)
        elif 19 <= row['Age'] <= 24:
            correct_row = students_in_total[
                (students_in_total['District'] == row['District']) & (students_in_total[
                    'Age'] == '19-24')]
            sums = int(correct_row['Number_of_students'])
            number_of_stud = int(row['Total'])
            perc = round(number_of_stud / sums, 2)
            percent.append(perc)
        else:
            pass

    inhabitants_dataframe['Percentage'] = percent
    return inhabitants_dataframe


def students_per_school_by_year_by_district(school_dataframe, inhabitants_dataframe):
    school_dataframe = school_dataframe[school_dataframe['SchoolType'].isin(STUDENTS_AGES.keys())]
    data = []
    for index, row in school_dataframe.iterrows():
        if row['SchoolType'] == 'Przedszkole':
            for i in range(STUDENTS_AGES['Przedszkole'][0], STUDENTS_AGES['Przedszkole'][1]+1):
                temp_row = inhabitants_dataframe[
                    (inhabitants_dataframe['District'] == row['District']) & (inhabitants_dataframe['Age'] == i) & (
                            inhabitants_dataframe['DistrictType'] == row['DistrictType']) & (
                                inhabitants_dataframe['Voivodeship'] == row['Voivodeship'])]
                perc = temp_row['Percentage']
                if perc.size == 1:
                    number_of_stud = int(row['Students'])
                    perc = float(perc)
                    record = [row.SchoolType, row.Students, row.Teachers, row.District, row.DistrictType,
                              row.Voivodeship, 2018 - i, int(number_of_stud * perc)]
                    data.append(record)
        elif row['SchoolType'] == 'Szkoła podstawowa':
            for i in range(STUDENTS_AGES['Szkoła podstawowa'][0], STUDENTS_AGES['Szkoła podstawowa'][1]+1):
                temp_row = inhabitants_dataframe[
                    (inhabitants_dataframe['District'] == row['District']) & (inhabitants_dataframe['Age'] == i) & (
                            inhabitants_dataframe['DistrictType'] == row['DistrictType']) & (
                                inhabitants_dataframe['Voivodeship'] == row['Voivodeship'])]
                perc = temp_row['Percentage']
                if perc.size == 1:
                    number_of_stud = int(row['Students'])
                    perc = float(perc)
                    record = [row.SchoolType, row.Students, row.Teachers, row.District, row.DistrictType,
                              row.Voivodeship, 2018 - i, int(number_of_stud * perc)]
                    data.append(record)
        elif row['SchoolType'] == 'Gimnazjum':
            for i in range(STUDENTS_AGES['Gimnazjum'][0], STUDENTS_AGES['Gimnazjum'][1]+1):
                temp_row = inhabitants_dataframe[
                    (inhabitants_dataframe['District'] == row['District']) & (inhabitants_dataframe['Age'] == i) & (
                            inhabitants_dataframe['DistrictType'] == row['DistrictType']) & (
                                inhabitants_dataframe['Voivodeship'] == row['Voivodeship'])]
                perc = temp_row['Percentage']
                if perc.size == 1:
                    number_of_stud = int(row['Students'])
                    perc = float(perc)
                    record = [row.SchoolType, row.Students, row.Teachers, row.District, row.DistrictType,
                              row.Voivodeship, 2018 - i, int(number_of_stud * perc)]
                    data.append(record)

        elif row['SchoolType'] == 'Liceum ogólnokształcące':
            for i in range(STUDENTS_AGES['Liceum ogólnokształcące'][0], STUDENTS_AGES['Liceum ogólnokształcące'][1]+1):
                temp_row = inhabitants_dataframe[
                    (inhabitants_dataframe['District'] == row['District']) & (inhabitants_dataframe['Age'] == i) & (
                            inhabitants_dataframe['DistrictType'] == row['DistrictType']) & (
                                inhabitants_dataframe['Voivodeship'] == row['Voivodeship'])]
                perc = temp_row['Percentage']
                if perc.size == 1:
                    number_of_stud = int(row['Students'])
                    perc = float(perc)
                    record = [row.SchoolType, row.Students, row.Teachers, row.District, row.DistrictType,
                              row.Voivodeship, 2018 - i, int(number_of_stud * perc)]
                    data.append(record)
        elif row['SchoolType'] == 'Szkoła policealna':
            for i in range(STUDENTS_AGES['Szkoła policealna'][0], STUDENTS_AGES['Szkoła policealna'][1]+1):
                temp_row = inhabitants_dataframe[
                    (inhabitants_dataframe['District'] == row['District']) & (inhabitants_dataframe['Age'] == i) & (
                            inhabitants_dataframe['DistrictType'] == row['DistrictType']) & (
                                inhabitants_dataframe['Voivodeship'] == row['Voivodeship'])]
                perc = temp_row['Percentage']
                if perc.size == 1:
                    number_of_stud = int(row['Students'])
                    perc = float(perc)
                    record = [row.SchoolType, row.Students, row.Teachers, row.District, row.DistrictType,
                              row.Voivodeship, 2018 - i, int(number_of_stud * perc)]
                    data.append(record)

    statistic_dataframe = pd.DataFrame(data, columns=['SchoolType', 'Students', 'Teachers', 'District', 'DistrictType',
                                                      'Voivodeship', 'BirthYear', 'NumberofStudents'])

    return statistic_dataframe


def statistics_per_school_per_year_per_district(statistic_dataframe):
    statistic_dataframe.drop(statistic_dataframe[statistic_dataframe['NumberofStudents'] == 0].index, inplace=True)
    grouped_data = statistic_dataframe.groupby(['District', 'SchoolType', 'BirthYear']).agg(
        {'NumberofStudents': ['min', 'max', 'mean']})
    return grouped_data


def statistics_per_school_per_year_per_districttype(statistic_dataframe):
    statistic_dataframe.drop(statistic_dataframe[statistic_dataframe['NumberofStudents'] == 0].index, inplace=True)
    grouped_data = statistic_dataframe.groupby(['DistrictType', 'SchoolType', 'BirthYear']).agg(
        {'NumberofStudents': ['min', 'max', 'mean']})
    return grouped_data
