import argparse
from os.path import isfile

from school_analysis.io.load import get_school_data, get_inhabitants_data
from school_analysis.calculate import students_per_teacher_per_district_type, students_per_teacher_per_district, \
    sum_of_students, percentage_of_students, students_per_school_by_year_by_district, \
    statistics_per_school_per_year_per_district, statistics_per_school_per_year_per_districttype, \
    students_per_teacher_minimum_per_districttype


def file_checker(filename):
    if not isfile(filename):
        raise argparse.ArgumentTypeError('File does not exists')
    return filename

def arguments_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('school_data', type=file_checker)
    parser.add_argument('arg.inhabitants_data', type=file_checker)
    return parser.parse_args()




if __name__ == '__main__':
    args = parse_arguments()

    school_dataframe = get_school_data(arg.school_data)
    inhabitants_data = get_inhabitants_data(arg.inhabitants_data)

    students_per_teacher_df = students_per_teacher_per_district(school_dataframe)
    students_per_teacher_df.to_csv('students_per_teacher_df.csv')

    students_per_teacher_per_dsttype_df = students_per_teacher_per_district_type(school_dataframe)
    students_per_teacher_per_dsttype_df.to_csv('students_per_teacher_per_dsttype_df.csv')

    students_in_total = sum_of_students(inhabitants_data)
    inhabitants_dataframe = percentage_of_students(inhabitants_data, students_in_total)

    statistic_dataframe = students_per_school_by_year_by_district(school_dataframe, inhabitants_dataframe)

    stats_per_district = statistics_per_school_per_year_per_district(statistic_dataframe)
    stats_per_district.to_csv('stats_per_district.csv')

    stats_per_districttype = statistics_per_school_per_year_per_districttype(statistic_dataframe)
    stats_per_districttype.to_csv('stats_per_districttype.csv')
