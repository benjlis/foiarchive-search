select entity_id, entity, entgroup, wikidata_id, doc_cnt, 
       entity || ' (' || doc_cnt || ')' entity_dropdown_str
    from entities
    order by doc_cnt desc;
