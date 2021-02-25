import pandas as pd


def district_school(row):
    #  inconsistency in data -> M. st./M. prefix
    return row['Gmina'].replace('M. st. ', '').replace('M. ', '')


def voivodeship(row):
    return row['Województwo'].replace('WOJ. ', '').lower()


def get_school_data(file_path=school_path):
    """Read xlsx file with school data

    Keyword arguments:
    file_path -- path to the xlsx file (default: school_path)

    Returns:
    school_dataframe -- DataFrame with school data
    or
    error message
    """
    try:
        school_dataframe = pd.read_excel(file_path, skiprows=[1], index_col=0)

        school_dataframe['SchoolType'] = school_dataframe['Nazwa typu']
        school_dataframe['Students'] = school_dataframe['Uczniowie, wychow., słuchacze']
        school_dataframe['Teachers'] = school_dataframe['Nauczyciele pełnozatrudnieni'] + school_dataframe[
            'Nauczyciele niepełnozatrudnieni (stos.pracy)']
        school_dataframe['District'] = school_dataframe.apply(district_school, axis=1)
        school_dataframe['DistrictType'] = school_dataframe['Typ gminy']
        school_dataframe['Voivodeship'] = school_dataframe.apply(voivodeship, axis=1)
        school_dataframe['SchoolName'] = school_dataframe['Nazwa szkoły, placówki']

        #  inconsistency in data -> Ostrowice stopped being a district in 2019
        school_dataframe = school_dataframe[school_dataframe.District != 'Ostrowice']

        return school_dataframe[['District', 'SchoolType', 'Students', 'Teachers', 'DistrictType', 'Voivodeship']]

    except Exception as e:
        print(repr(e))


def age(row):
    return int(row.Id) if row.Id.isnumeric() else None


def district(row):
    if row.Code == '':
        return None
    #  inconsistency in data - Łódź/Poznań/Wrocław have additional suffixes
    for city in ['Łódź', 'Poznań', 'Wrocław']:
        if row.Id.startswith(f'{city}-'):
            return city

    #  inconsistency in data - Warszawa's districts
    if row.Id in {'Ochota', 'Włochy', 'Targówek', 'Rembertów', 'Wola', 'Śródmieście', 'Białołęka',
                  'Praga-Południe', 'Bemowo', 'Żoliborz', 'Mokotów', 'Praga-Północ', 'Wilanów',
                  'Ursynów', 'Wawer', 'Wesoła', 'Ursus'}:
        return 'Warszawa'

    return row.Id


def district_type(row):
    if isinstance(row.UrbanTotal, int) and isinstance(row.RuralTotal, int):
        return 'M-Gm'
    if isinstance(row.UrbanTotal, int):
        return 'M'
    if isinstance(row.RuralTotal, int):
        return 'Gm'
    raise Exception()


def get_inhabitants_data(file_path=inhabitants_path):
    """Read xls file with inhabitants data

    Keyword arguments:
    file_path -- path to the xls file (default: inhabitants_path)

    Returns:
    school_dataframe -- DataFrame with inhabitants data
    or
    error message
    """
    try:
        inhabitants_dataframe = []
        for voivodeship, df in pd.read_excel(file_path, skiprows=5, header=[0, 1], sheet_name=None).items():
            df.columns = ['Id', 'Code', 'Total', 'Man', 'Woman',
                          'UrbanTotal', 'UrbanMan', 'UrbanWoman',
                          'RuralTotal', 'RuralMan', 'RuralWoman', 'XYZ']

            df = df.applymap(lambda s: s.strip() if isinstance(s, str) else s)

            df['Age'] = df.apply(age, axis=1)
            df['District'] = df.apply(district, axis=1).fillna(method='ffill')
            df['DistrictType'] = df.apply(district_type, axis=1)
            voivodeship = voivodeship.lower()
            #  inconsistency in data -> śląskie/śląske
            df['Voivodeship'] = 'śląskie' if voivodeship == 'śląske' else voivodeship

            inhabitants_dataframe.append(
                df[~df.Age.isnull()][['District', 'DistrictType', 'Voivodeship', 'Age', 'Total']])
            inh_data = pd.concat(inhabitants_dataframe)
            inhabitants_data = inh_data.groupby(['District', 'DistrictType', 'Voivodeship', 'Age']).agg({'Total': 'sum'})
            inhabitants_data.reset_index(inplace=True)
        return inhabitants_data

    except Exception as e:
        print(repr(e))
