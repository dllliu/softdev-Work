#### Cool Stuff
* Data can be linked between tables based on field values.
* data types: TEXT, INTEGER, REAL, NUMERIC, BLOB
* ex: `CREATE TABLE <name> (<column name> <data type>, ...)`
* ex: `INSERT INTO <tbl_name> VALUES ( <field 1>, <field 2> ...)`
* To show all fields for each entry (record) in table tbl_name, use SELECT * FROM <tbl_name>;
* have to use cursor to trigger db events
* .commit() saves, .close() closes db
* use DROP TABLE if exists <tb_name> to avoid identifer errors