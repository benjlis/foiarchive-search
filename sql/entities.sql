select entity_id, entity, entgroup, wikidata_id, doc_cnt,
       case when wikidata_id is null then entity || ' (' || doc_cnt || ')' 
            else entity || ' (' || doc_cnt || ', '|| wikidata_id || ')' 
       end entity_dropdown_str
    from entities
    order by entgroup, doc_cnt desc;
