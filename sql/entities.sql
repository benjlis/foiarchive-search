select entity_id, entity, entgroup, wikidata_id, doc_cnt, instance_cnt
    from entities
    order by entgroup, doc_cnt desc;
    