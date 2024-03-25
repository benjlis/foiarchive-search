select corpus, title, begin_date, end_date, 
       doc_cnt, pg_cnt, word_cnt, topic_cnt
    from foiarchive.corpora
    order by corpus;
