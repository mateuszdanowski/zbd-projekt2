-- INIT LOCAL TABLES
create or replace function public.load_csv_to_table
(
    target_table text,
    csv_path text,
    values_col_count integer
)

returns void as $$

declare iter integer;

begin

    execute format('alter table %s add column date date;', target_table);
    execute format('alter table %s add column category text;', target_table);

    for iter in 1..values_col_count
    loop
        execute format('alter table %s add column value%s integer;', target_table, iter);
    end loop;

    execute format('copy %s from %L with delimiter '','' quote ''"'' csv ', target_table, csv_path);

end;

$$ language plpgsql;


-- INIT FOREIGN TABLE
create or replace function public.create_columns_for_foreign
(
    target_table text,
    values_col_count integer
)

returns void as $$

declare iter integer;

begin

    execute format('alter table %s add column date date;', target_table);
    execute format('alter table %s add column category text;', target_table);

    for iter in 1..values_col_count
    loop
        execute format('alter table %s add column value%s integer;', target_table, iter);
    end loop;

end;

$$ language plpgsql;



