import os
import generator
from math import ceil

psql_init_template = "psql -f {}"
psql_create_tables_template = "psql -v csv_name={} -v col_count={} -f {}"
psql_run_queries_template = "psql -v k={} -v from={} -v to={} -v category={} -f {}"

init_scripts = ["init-fdw.sql", "init-functions.sql"]
create_tables_script = "create-tables.sql"
run_queries_script = "run-queries.sql"

for script in init_scripts:
    os.system(psql_init_template.format(script))


# Generate tables with different properties

csv_name_template = "/Users/mateuszdanowski/bazy-danych/data/{}-{}.csv"
result_template = "/Users/mateuszdanowski/bazy-danych/results/{}-{}.out"

output_file_template = "/Users/mateuszdanowski/bazy-danych/results/from{}-to{}-c{}-v{}.csv"

DEFAULT_DAYS = 1000
DEFAULT_CATEGORIES = 100
DEFAULT_VALUES = 100
DEFAULT_K = 100
DEFAULT_START_DATE = '2020-01-01'
DEFAULT_END_DATE = '2020-04-09'


CATEGORIES = [1, 10, 100, 1000]
VALUES = [1, 10, 100, 1000, 1598]
END_DATES = [('2020-01-01', 1), ('2020-01-10', 10), ('2020-04-09', 100), ('2022-09-26', 1000)]

# INTERVAL
for end_date, number_of_days in END_DATES:
    generator.write_csv(DEFAULT_DAYS, DEFAULT_CATEGORIES, DEFAULT_VALUES, 'interval', number_of_days)

    csv_name = csv_name_template.format('interval', number_of_days)
    result_filename = result_template.format('interval', number_of_days)
    os.system(psql_create_tables_template.format(csv_name, DEFAULT_VALUES, create_tables_script))
    os.system(psql_run_queries_template.format(DEFAULT_K, DEFAULT_START_DATE, end_date, DEFAULT_CATEGORIES, run_queries_script) + " | grep 'Exec' > {}".format(result_filename))


# VALUES
for values in VALUES:
    generator.write_csv(DEFAULT_DAYS, DEFAULT_CATEGORIES, values, 'values', values)

    csv_name = csv_name_template.format('values', values)
    result_filename = result_template.format('values', values)
    os.system(psql_create_tables_template.format(csv_name, values, create_tables_script))
    os.system(psql_run_queries_template.format(values, DEFAULT_START_DATE, DEFAULT_END_DATE, DEFAULT_CATEGORIES, run_queries_script) + " | grep 'Exec' > {}".format(result_filename))



# CATEGORIES
for categories in CATEGORIES:
    generator.write_csv(DEFAULT_DAYS, categories, DEFAULT_VALUES, 'categories', categories)

    csv_name = csv_name_template.format('categories', categories)
    result_filename = result_template.format('categories', categories)
    os.system(psql_create_tables_template.format(csv_name, DEFAULT_VALUES, create_tables_script))
    os.system(psql_run_queries_template.format(DEFAULT_K, DEFAULT_START_DATE, DEFAULT_END_DATE, categories, run_queries_script) + " | grep 'Exec' > {}".format(result_filename))






# for days in DAYS:
#     for categories in CATEGORIES:
#         for values in VALUES:


#             # generator.write_csv(days, categories, values)

#             csv_name = csv_name_template.format(days, categories, values)
#             os.system(psql_create_tables_template.format(csv_name, values, create_tables_script))

#             for date, number_of_days in END_DATES:

#                 _k = values
#                 _from = '2020-01-01'
#                 _to = date
#                 _category = ceil(categories / 26) * 'A'

#                 output_filename = output_file_template.format(_from, _to, categories, values)

#                 os.system(psql_run_queries_template.format(_k, _from, _to, _category, run_queries_script) + " | grep 'Exec' > {}".format(output_filename))
                


                # os.system("python3 ./format_res.py")
                # # result = result.split('\n')


                # print(result)
                # exit(0)




# Execute

# os.system(psql_.format(script))







# csv_name = "/Users/mateuszdanowski/bazy-danych/big-d1000-c10-v500.csv"
# col_count = 500
