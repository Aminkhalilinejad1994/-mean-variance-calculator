import pandas as pd

def calculate_demographic_data(print_data=True):
    df = pd.read_csv('C:/Users/Shayan/OneDrive/Desktop/Data Analysis with Python/demographic_data_analyzer/adult.data.csv', header=None, names=[
        'age', 'workclass', 'fnlwgt', 'education', 'education-num',
        'marital-status', 'occupation', 'relationship', 'race', 'sex',
        'capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'salary'
    ])

    df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

    race_count = df['race'].value_counts()
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)
    percentage_bachelors = round((df['education'] == 'Bachelors').mean() * 100, 1)

    higher_edu = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    lower_edu = ~higher_edu

    higher_education_rich = round((df[higher_edu]['salary'] == '>50K').mean() * 100, 1)
    lower_education_rich = round((df[lower_edu]['salary'] == '>50K').mean() * 100, 1)

    min_work_hours = df['hours-per-week'].min()
    min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage_min_workers = round((min_workers['salary'] == '>50K').mean() * 100, 1)

    rich = df[df['salary'] == '>50K']
    country_rich_pct = (rich['native-country'].value_counts() / df['native-country'].value_counts()) * 100
    highest_earning_country = country_rich_pct.idxmax()
    highest_earning_country_percentage = round(country_rich_pct.max(), 1)

    india_rich = rich[rich['native-country'] == 'India']
    if not india_rich.empty:
        top_IN_occupation = india_rich['occupation'].value_counts().idxmax()
    else:
        top_IN_occupation = "No data"

    if print_data:
        print("Race count:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Rich percentage among min workers: {rich_percentage_min_workers}%")
        print("Highest earning country:", highest_earning_country)
        print("Highest earning country percentage:", highest_earning_country_percentage)
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage_min_workers': rich_percentage_min_workers,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }