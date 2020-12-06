DROP FOREIGN TABLE foreign_data;
DROP TABLE local_data;
DROP FOREIGN TABLE cstore_data;

CREATE FOREIGN TABLE foreign_data ()
SERVER csv_file_server
OPTIONS ( filename :'csv_name', format 'csv' );

CREATE TABLE local_data();

CREATE FOREIGN TABLE cstore_data ()
SERVER cstore_server;

SELECT create_columns_for_foreign('foreign_data', :col_count);
SELECT load_csv_to_table('local_data', :'csv_name', :col_count);
SELECT load_csv_to_table('cstore_data', :'csv_name', :col_count);

analyze foreign_data;
analyze local_data;
analyze cstore_data;