select entity_id, entity, entgroup, wikidata_id, doc_cnt, entity entity_dropdown_str
    from entities
    order by entgroup, doc_cnt desc;
