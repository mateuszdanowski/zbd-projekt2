

-- :k
-- :from
-- :to
-- :category


explain analyze SELECT SUM(value:k) FROM foreign_data WHERE date BETWEEN :'from' AND :'to';
explain analyze SELECT SUM(value:k) FROM local_data WHERE date BETWEEN :'from' AND :'to';
explain analyze SELECT SUM(value:k) FROM cstore_data WHERE date BETWEEN :'from' AND :'to';



-- SELECT SUM(value1) FROM foreign_data WHERE date BETWEEN '2020-01-05' AND '2022-01-08';
-- SELECT SUM(value1) FROM local_data WHERE date BETWEEN '2020-01-05' AND '2022-01-08';
-- SELECT SUM(value1) FROM cstore_data WHERE date BETWEEN '2020-01-05' AND '2022-01-08';

-- psql_run_queries_template = "psql -v to_date={} -v category={} -f {} -o {}"