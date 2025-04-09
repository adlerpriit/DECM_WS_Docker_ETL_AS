with WDir as (
    select
        DateTime,
        WS10,
        case
            when WD10 >= 337.5 or WD10 < 22.5 then 'N'
            when WD10 >= 22.5 and WD10 < 67.5 then 'NE'
            when WD10 >= 67.5 and WD10 < 112.5 then 'E'
            when WD10 >= 112.5 and WD10 < 157.5 then 'SE'
            when WD10 >= 157.5 and WD10 < 202.5 then 'S'
            when WD10 >= 202.5 and WD10 < 247.5 then 'SW'
            when WD10 >= 247.5 and WD10 < 292.5 then 'W'
            when WD10 >= 292.5 and WD10 < 337.5 then 'NW'
            else 'Unknown'
        end as WD
    from
        {{ ref('airQ') }}
),
WDir_tbl as (
    select
        DateTime,
        AVG(case when WD = 'N' then WS10 else NULL end) as N,
        AVG(case when WD = 'NE' then WS10 else NULL end) as NE,
        AVG(case when WD = 'E' then WS10 else NULL end) as E,
        AVG(case when WD = 'SE' then WS10 else NULL end) as SE,
        AVG(case when WD = 'S' then WS10 else NULL end) as S,
        AVG(case when WD = 'SW' then WS10 else NULL end) as SW,
        AVG(case when WD = 'W' then WS10 else NULL end) as W,
        AVG(case when WD = 'NW' then WS10 else NULL end) as NW
    from
        WDir
    group by
        DateTime
)
select * from WDir_tbl