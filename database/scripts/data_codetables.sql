INSERT INTO public.tb_group_typ_cd(
            GRPTYP_CD, GRPTYP_DE)
    VALUES ('SP', 'Special Interest');

INSERT INTO public.tb_group_typ_cd(
            GRPTYP_CD, GRPTYP_DE)
    VALUES ('FI', 'Fitness');

Insert into TB_BATCH_JOB_STATUS_CD (BATJOBSTA_CD,BATJOBSTA_DE) values ('COMPLETED','Completed Successfully');
Insert into TB_BATCH_JOB_STATUS_CD (BATJOBSTA_CD,BATJOBSTA_DE) values ('FAILED','Failed');
Insert into TB_BATCH_JOB_STATUS_CD (BATJOBSTA_CD,BATJOBSTA_DE) values ('INPROGRESS','In Progress');
Insert into TB_BATCH_JOB_STATUS_CD (BATJOBSTA_CD,BATJOBSTA_DE) values ('ERRORS','Errors');
Insert into TB_BATCH_JOB_STATUS_CD (BATJOBSTA_CD,BATJOBSTA_DE) values ('DUPPROC','Duplicate Processs / Process Already Running');
Insert into TB_BATCH_JOB_STATUS_CD (BATJOBSTA_CD,BATJOBSTA_DE) values ('WARNINGS','Completed With Warnings');

Insert into tb_batch_job_cd (batjoc_cd, batjoc_de, batjoc_comment) values ('STATS','Application Statistics', 'Application Statistics');
