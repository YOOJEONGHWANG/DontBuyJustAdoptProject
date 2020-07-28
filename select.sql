-- SQLite
select * FROM animalinfo where ("종료(반환)" != status AND "종료(방사)" != status) AND (noticeend>=20160101)

create table animalinfo2 (regnum INT, noticeend INT, age INT, color TEXT, animal TEXT, species TEXT, neuteryn TEXT, sex TEXT, feature TEXT, weight REAL, status TEXT);

INSERT INTO animalinfo2(regnum, noticeend, age, color, animal, species,  neuteryn, sex, feature, weight, status)
select * FROM animalinfo where ("종료(반환)" != status AND "종료(방사)" != status) AND (noticeend>=20160101);

DELETE from animalinfo2 where (noticeend<20200701 AND status='보호중');
SELECT count(*) FROM animalinfo2;

DELETE from animalinfo2 where (animal like '%기타축종%' ); 

SELECT * FROM animalinfo2 where species ='';
SELECT * FROM animalinfo2 order by noticeend DESC; 

DELETE FROM animalinfo2 where status='종료(미포획)';

DELETE from animalinfo2 where species='닭';

SELECT DISTINCT feature FROM animalinfo2;
select * from animalinfo2 where age is NULL;