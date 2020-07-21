# Current Covid Cases of any country

from covid import Covid

covid = Covid()
cases = covid.get_status_by_country_name("Bangladesh")

for i in cases:
    print(i, ':', cases[i])

active_cases = covid.get_total_active_cases()
print("Affected countries :", covid.list_countries())
print("Total -", active_cases, "worldwide.")