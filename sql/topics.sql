select corpus, topic_id, title, name, coalesce(name, title) display
    from foiarchive.topics
    order by corpus, name;