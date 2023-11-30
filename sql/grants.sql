create role foiarchive_gui with login;
alter role foiarchive_gui password :'pswd';
alter role foiarchive_gui set search_path to foiarchive,public;
-- alter role :uni set search_path to default;
alter role foiarchive_gui connnetion limit 10;
grant web_anon to foiarchive_gui;

grant select on mosaic.docs_oct73 mosaic_gui;
grant select on mosaic.classifications to mosaic_gui;
grant select on mosaic.corpora to mosaic_gui;
