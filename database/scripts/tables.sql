


-- ranks(id, name, lower_rank_id, higher_rank_id, description)
-- guilds(id, name, gold_amount)
-- characters(id, name)
-- memberships(id, character_id, guild_id, rank_id, description)

  -- ===================================================================

CREATE TABLE public.TB_GROUP_TYP_CD
   (	
		GRPTYP_CD character varying(2) NOT NULL, 
		GRPTYP_DE character varying(20) NOT NULL, 
		CONSTRAINT PKTB_GROUP_TYP_CD PRIMARY KEY (GRPTYP_CD)
	);

  -- ===================================================================

CREATE TABLE public.TB_PERSON (
	PERSON_ID serial NOT NULL, -- System-generated ID for a Group.
    USER_UUID uuid NOT NULL,
    NICK_NAME character varying(100) NOT NULL, 
    CONSTRAINT PKTB_PERSON PRIMARY KEY (PERSON_ID)
);
  
  -- ===================================================================
  
CREATE TABLE public.TB_GROUP (
  GROUP_ID serial NOT NULL, -- System-generated ID for a Group.
  GROUP_UUID uuid NOT NULL,
  GROUP_NAME character varying(100) NOT NULL, 
  CONSTRAINT PKTB_GROUP PRIMARY KEY (GROUP_ID)
);
  
CREATE INDEX IDX_GROUP_NAME
  ON public.TB_GROUP
  USING btree
  (lower(GROUP_NAME::text) COLLATE pg_catalog.default);
  
  -- =====================================================================

CREATE TABLE public.TB_MEMBERSHIP (
	MEMBERSHIP_ID serial NOT NULL, -- System-generated ID for a Group.
    PERSON_ID integer NOT NULL,
    GROUP_ID integer NOT NULL,
    MEMBERSHIP_FROM_TS timestamp without time zone NOT NULL,
	MEMBERSHIP_TO_TS timestamp without time zone NOT NULL,
    CONSTRAINT PKTB_MEMBERSHIP PRIMARY KEY (MEMBERSHIP_ID),
	CONSTRAINT TB_MEMBERSHIP_TO_TB_PERSON FOREIGN KEY (PERSON_ID) REFERENCES public.TB_PERSON (PERSON_ID), 
	CONSTRAINT TB_MEMBERSHIP_TO_TB_GROUP FOREIGN KEY (GROUP_ID) REFERENCES public.TB_GROUP (GROUP_ID)
);

-- =======================================================================


CREATE TABLE public.TB_GROUP_MANAGER (
	MANAGER_ID serial NOT NULL, -- System-generated ID for a Group.
    GROUP_ID integer NOT NULL,
    PERSON_ID integer NOT NULL,
    MANAGER_FROM_TS timestamp without time zone NOT NULL,
	MANAGER_TO_TS timestamp without time zone NOT NULL,
	CONSTRAINT PKTB_GROUP_MANAGER PRIMARY KEY (MANAGER_ID),
	CONSTRAINT TB_GROUP_MANAGER_TO_TB_PERSON FOREIGN KEY (PERSON_ID) REFERENCES public.TB_PERSON (PERSON_ID), 
	CONSTRAINT TB_GROUP_MANAGER_TO_TB_GROUP FOREIGN KEY (GROUP_ID) REFERENCES public.TB_GROUP (GROUP_ID)
);
  -- ===================================================================
   
CREATE TABLE public.TB_PERSON_TITLE (
    PERSON_ID integer NOT NULL,
    TITLE character varying(100) NOT NULL,
    MANAGER_FROM_TS timestamp without time zone NOT NULL,
	MANAGER_TO_TS timestamp without time zone NOT NULL,
	CONSTRAINT PKTB_PERSON_TITLE PRIMARY KEY (PERSON_ID, TITLE),
	CONSTRAINT TB_PERSON_TITLE_TO_TB_PERSON FOREIGN KEY (PERSON_ID) REFERENCES public.TB_PERSON (PERSON_ID)
);
   
  -- ===================================================================   


  CREATE TABLE public.TB_CONFIG
   (	
	CFGPRM_KEY character varying(100) NOT NULL, 
	CFGPRM_VAL character varying(100) NOT NULL,	
	CFGPRM_DE character varying(300) NOT NULL, 
	 CONSTRAINT XPKTB_CONFIG PRIMARY KEY (CFGPRM_KEY)
	) 
	 ;


   COMMENT ON COLUMN public.TB_CONFIG.CFGPRM_DE IS 'Description or comments for a configurable system parameter';
   COMMENT ON COLUMN public.TB_CONFIG.CFGPRM_VAL IS 'Parameter value for a configurable system parameter';
   COMMENT ON COLUMN public.TB_CONFIG.CFGPRM_KEY IS 'ID name for a configurable parameter value';   
   COMMENT ON TABLE public.TB_CONFIG  IS 'Table for holding configurable system parameters.';

  -- ===================================================================  















