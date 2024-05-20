class SqlRepo:
    # organizasyona ait çalışanların giriş çıkıi bilgilerini filtreler
    organization_sql: str = """
            select jsonb_agg(tt) from (
                    select unique_id,
                    utc::date,  
                    coalesce(to_char(min(in_time)::timestamp, 'HH24:MI'), 'NULL')     as in_time,
                    coalesce(to_char(max(el.out_time)::timestamp, 'HH24:MI'), 'NULL') as out_time
                from employee_log el
                    where el.utc::date between %s and %s
                    and organization_id = %s
                    group by unique_id, el.utc::date
                                      )tt;
            """
