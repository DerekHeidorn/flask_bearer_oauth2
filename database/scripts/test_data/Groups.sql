ALTER SEQUENCE public.tb_group_group_id_seq RESTART WITH 500;
ALTER SEQUENCE public.tb_group_manager_manager_id_seq RESTART WITH 500;
ALTER SEQUENCE public.tb_membership_membership_id_seq RESTART WITH 500;
ALTER SEQUENCE public.tb_person_person_id_seq RESTART WITH 500;


-- ========================================================================================================
INSERT INTO public.tb_group(
            group_id, group_uuid, grptyp_cd, group_name, group_de, group_private_fl)
    VALUES (1, 'fbaa6765-bf50-40a8-bb29-a32ce07ef3d9', 'SP', 'The Avengers Group', 'A group of super heroes to help save the world!', False);
-- 4e5d14ab-e91e-49b3-9c61-795748c41e09		Iron Man					Tony Stark
INSERT INTO public.tb_person(
	person_id, user_uuid, nick_name)
	VALUES (1, '4e5d14ab-e91e-49b3-9c61-795748c41e09', 'Iron Man');
INSERT INTO public.tb_group_manager(
	manager_id, group_id, person_id, manager_from_ts, manager_to_ts)
	VALUES (1, 1, 1, CURRENT_DATE-2, null);
-- f55b7b25-6ef5-4727-9645-7564fb777f21		Wasp						Janet van Dyne
INSERT INTO public.tb_person(
	person_id, user_uuid, nick_name)
	VALUES (10, 'f55b7b25-6ef5-4727-9645-7564fb777f21', 'Wasp');
INSERT INTO public.tb_membership(
	membership_id, group_id, person_id, membership_from_ts, membership_to_ts)
	VALUES (10, 1, 10, CURRENT_DATE-2, null);
-- e4176c50-9e84-49d3-a2b7-f8773d57fb9b		Hulk						Dr. Robert Bruce Banner
INSERT INTO public.tb_person(
	person_id, user_uuid, nick_name)
	VALUES (11, 'e4176c50-9e84-49d3-a2b7-f8773d57fb9b', 'Hulk');
INSERT INTO public.tb_membership(
	membership_id, group_id, person_id, membership_from_ts, membership_to_ts)
	VALUES (11, 1, 11, CURRENT_DATE-2, null);
-- 29ef21b2-825f-4d49-a654-df9dd2295630		Scarlet Witch				Wanda Maximoff
INSERT INTO public.tb_person(
	person_id, user_uuid, nick_name)
	VALUES (12, '29ef21b2-825f-4d49-a654-df9dd2295630', 'Scarlet Witch');
INSERT INTO public.tb_membership(
	membership_id, group_id, person_id, membership_from_ts, membership_to_ts)
	VALUES (12, 1, 12, CURRENT_DATE-2, null);
-- 5fa2a30d-403c-4ae8-b3fa-5dd207ef926b		Vision						Victor Shade
INSERT INTO public.tb_person(
	person_id, user_uuid, nick_name)
	VALUES (13, '5fa2a30d-403c-4ae8-b3fa-5dd207ef926b', 'Vision');
INSERT INTO public.tb_membership(
	membership_id, group_id, person_id, membership_from_ts, membership_to_ts)
	VALUES (13, 1, 13, CURRENT_DATE-2, null);
-- b130cdd5-e09c-471f-b3df-da80413d58d5		Black Widow					Natasha Alianovna Romanoff
INSERT INTO public.tb_person(
	person_id, user_uuid, nick_name)
	VALUES (14, 'b130cdd5-e09c-471f-b3df-da80413d58d5', 'Black Widow');
INSERT INTO public.tb_membership(
	membership_id, group_id, person_id, membership_from_ts, membership_to_ts)
	VALUES (14, 1, 14, CURRENT_DATE-2, null);
-- b8919fd0-0379-4fe3-b81e-4d06f079ce1f		Falcon						Samuel "Snap" Thomas Wilson
INSERT INTO public.tb_person(
	person_id, user_uuid, nick_name)
	VALUES (15, 'b8919fd0-0379-4fe3-b81e-4d06f079ce1f', 'Falcon');
INSERT INTO public.tb_membership(
	membership_id, group_id, person_id, membership_from_ts, membership_to_ts)
	VALUES (15, 1, 15, CURRENT_DATE-2, null);
-- 48667be7-9b99-4353-af8d-814b4c308b15		Captain Marvel				Monica Rambeau
INSERT INTO public.tb_person(
	person_id, user_uuid, nick_name)
	VALUES (16, '48667be7-9b99-4353-af8d-814b4c308b15', 'Captain Marvel');
INSERT INTO public.tb_membership(
	membership_id, group_id, person_id, membership_from_ts, membership_to_ts)
	VALUES (16, 1, 16, CURRENT_DATE-2, null);
-- d627b053-7986-41ab-9065-f37fec698148		War Machine					James Rupert "Rhodey" Rhodes
INSERT INTO public.tb_person(
	person_id, user_uuid, nick_name)
	VALUES (17, 'd627b053-7986-41ab-9065-f37fec698148', 'War Machine');
INSERT INTO public.tb_membership(
	membership_id, group_id, person_id, membership_from_ts, membership_to_ts)
	VALUES (17, 1, 17, CURRENT_DATE-2, null);
-- 179c80b3-a6f4-4c39-9edd-f38db0c7d0af		Spider-Man					Peter Benjamin Parker
INSERT INTO public.tb_person(
	person_id, user_uuid, nick_name)
	VALUES (18, '179c80b3-a6f4-4c39-9edd-f38db0c7d0af', 'Spider-Man');
INSERT INTO public.tb_membership(
	membership_id, group_id, person_id, membership_from_ts, membership_to_ts)
	VALUES (18, 1, 18, CURRENT_DATE-2, null);
-- a787b4e4-b09d-4d08-9073-2b47c8abbe5b		Ant-Man						Scott Lang
INSERT INTO public.tb_person(
	person_id, user_uuid, nick_name)
	VALUES (19, 'a787b4e4-b09d-4d08-9073-2b47c8abbe5b', 'Ant-Man');
INSERT INTO public.tb_membership(
	membership_id, group_id, person_id, membership_from_ts, membership_to_ts)
	VALUES (19, 1, 19, CURRENT_DATE-2, null);

	
-- ========================================================================================================
INSERT INTO public.tb_group(
            group_id, group_uuid, grptyp_cd, group_name, group_de, group_private_fl)
    VALUES (2, '84a7c3e2-d810-4439-836c-94002d9f4b0b', 'SP', 'Brown Coats', 'Browncoats were soldiers who fought for the Independent Planets, who lost to the Union of Allied Planets in the Unification War.', False);
-- a10541a9-46f4-49ae-97f4-625bc92b5f7c		Malcolm Reynolds					Firefly
INSERT INTO public.tb_person(
	person_id, user_uuid, nick_name)
	VALUES (20, 'a10541a9-46f4-49ae-97f4-625bc92b5f7c', 'Captain Reynolds');
INSERT INTO public.tb_group_manager(
	manager_id, group_id, person_id, manager_from_ts, manager_to_ts)
	VALUES (20, 2, 20, CURRENT_DATE-2, null);
-- 8ead1ce9-8867-4523-a84e-a1cf920038df		Zoe Washburne				Firefly
INSERT INTO public.tb_person(
	person_id, user_uuid, nick_name)
	VALUES (21, '8ead1ce9-8867-4523-a84e-a1cf920038df', 'Zoe');
INSERT INTO public.tb_membership(
	membership_id, group_id, person_id, membership_from_ts, membership_to_ts)
	VALUES (21, 2, 21, CURRENT_DATE-2, null);
-- bb3985d3-9d2f-49c7-8304-a8271330f762		Hoban "Wash" Washburne		Firefly
INSERT INTO public.tb_person(
	person_id, user_uuid, nick_name)
	VALUES (22, 'bb3985d3-9d2f-49c7-8304-a8271330f762', 'Wash');
INSERT INTO public.tb_membership(
	membership_id, group_id, person_id, membership_from_ts, membership_to_ts)
	VALUES (22, 2, 22, CURRENT_DATE-2, null);
-- ac08889e-1c82-4e4e-8912-8e7c95b81a25		Inara Serra					Firefly
INSERT INTO public.tb_person(
	person_id, user_uuid, nick_name)
	VALUES (23, 'ac08889e-1c82-4e4e-8912-8e7c95b81a25', 'Inara');
INSERT INTO public.tb_membership(
	membership_id, group_id, person_id, membership_from_ts, membership_to_ts)
	VALUES (23, 2, 23, CURRENT_DATE-2, null);
-- e6abb20f-75f7-43b2-8be6-421876ff4db4		Jayne Cobb					Firefly
INSERT INTO public.tb_person(
	person_id, user_uuid, nick_name)
	VALUES (24, 'e6abb20f-75f7-43b2-8be6-421876ff4db4', 'Gunner');
INSERT INTO public.tb_membership(
	membership_id, group_id, person_id, membership_from_ts, membership_to_ts)
	VALUES (24, 2, 24, CURRENT_DATE-2, null);
-- d9c83075-6efa-4554-9ab1-891ab6472950		Kaylee Frye					Firefly
INSERT INTO public.tb_person(
	person_id, user_uuid, nick_name)
	VALUES (25, 'd9c83075-6efa-4554-9ab1-891ab6472950', 'Kaylee');
INSERT INTO public.tb_membership(
	membership_id, group_id, person_id, membership_from_ts, membership_to_ts)
	VALUES (25, 2, 25, CURRENT_DATE-2, null);
-- 53271313-d6a6-41a4-b733-a2c450834e07		Simon Tam					Firefly
INSERT INTO public.tb_person(
	person_id, user_uuid, nick_name)
	VALUES (26, '53271313-d6a6-41a4-b733-a2c450834e07', 'Simon');
INSERT INTO public.tb_membership(
	membership_id, group_id, person_id, membership_from_ts, membership_to_ts)
	VALUES (26, 2, 26, CURRENT_DATE-2, null);
-- 3e1bef3b-562c-4c0c-a1b2-123c1385a1d4		River Tam					Firefly
INSERT INTO public.tb_person(
	person_id, user_uuid, nick_name)
	VALUES (27, '3e1bef3b-562c-4c0c-a1b2-123c1385a1d4', 'River');
INSERT INTO public.tb_membership(
	membership_id, group_id, person_id, membership_from_ts, membership_to_ts)
	VALUES (27, 2, 27, CURRENT_DATE-2, null);
-- 441fa406-54c1-45b5-b33d-981b7197f277		Derrial Book				Firefly
INSERT INTO public.tb_person(
	person_id, user_uuid, nick_name)
	VALUES (28, '441fa406-54c1-45b5-b33d-981b7197f277', 'Bishop');
INSERT INTO public.tb_membership(
	membership_id, group_id, person_id, membership_from_ts, membership_to_ts)
	VALUES (28, 2, 28, CURRENT_DATE-2, null);

-- ========================================================================================================	
INSERT INTO public.tb_group(
            group_id, group_uuid, grptyp_cd, group_name, group_de, group_private_fl)
    VALUES (3, 'c574ec5b-8a51-4eb5-b4a2-ba84fa27a85a', 'FI', 'Fitness Pal Members', 'Members of the website', False);

-- ========================================================================================================
INSERT INTO public.tb_group(
            group_id, group_uuid, grptyp_cd, group_name, group_de, group_private_fl)
    VALUES (4, '91a94eb2-3412-4a0e-b84b-645e1451830e', 'SP', 'Zombie Apocalypse Preparation Group', 'A group planning on getting ready for the zombie Apocalypse.', False);

-- 121461d4-a78b-4bbb-9471-9cf8233fdc78		Janus Prospero (Alice)				Resident Evil
INSERT INTO public.tb_person(
	person_id, user_uuid, nick_name)
	VALUES (40, '121461d4-a78b-4bbb-9471-9cf8233fdc78', 'Alice');
INSERT INTO public.tb_group_manager(
	manager_id, group_id, person_id, manager_from_ts, manager_to_ts)
	VALUES (40, 4, 40, CURRENT_DATE-2, null);
-- c64ea92c-757b-4846-a385-15ee2febb2e2		Ada Wong					Resident Evil
INSERT INTO public.tb_person(
	person_id, user_uuid, nick_name)
	VALUES (41, 'c64ea92c-757b-4846-a385-15ee2febb2e2', 'Ada');
INSERT INTO public.tb_membership(
	membership_id, group_id, person_id, membership_from_ts, membership_to_ts)
	VALUES (41, 4, 41, CURRENT_DATE-2, null);
-- 0ec0aeb8-8f3b-4d51-a3a0-a862cfcf0f96		Albert Wesker				Resident Evil
INSERT INTO public.tb_person(
	person_id, user_uuid, nick_name)
	VALUES (42, '0ec0aeb8-8f3b-4d51-a3a0-a862cfcf0f96', 'Albert');
INSERT INTO public.tb_membership(
	membership_id, group_id, person_id, membership_from_ts, membership_to_ts)
	VALUES (42, 4, 42, CURRENT_DATE-2, null);
-- 68d3d343-d5cd-4d46-8cf7-f8707c46a148		Chris Redfield				Resident Evil
INSERT INTO public.tb_person(
	person_id, user_uuid, nick_name)
	VALUES (43, '68d3d343-d5cd-4d46-8cf7-f8707c46a148', 'Chris');
INSERT INTO public.tb_membership(
	membership_id, group_id, person_id, membership_from_ts, membership_to_ts)
	VALUES (43, 4, 43, CURRENT_DATE-2, null);
-- bfaec952-7b06-4791-a321-02a925ff59b4		Claire Redfield				Resident Evil
INSERT INTO public.tb_person(
	person_id, user_uuid, nick_name)
	VALUES (44, 'bfaec952-7b06-4791-a321-02a925ff59b4', 'Claire');
INSERT INTO public.tb_membership(
	membership_id, group_id, person_id, membership_from_ts, membership_to_ts)
	VALUES (44, 4, 44, CURRENT_DATE-2, null);
-- d81dc597-ed99-46a7-846f-6495898b40c9		Jill Valentine				Resident Evil
INSERT INTO public.tb_person(
	person_id, user_uuid, nick_name)
	VALUES (45, 'd81dc597-ed99-46a7-846f-6495898b40c9', 'JV');
INSERT INTO public.tb_membership(
	membership_id, group_id, person_id, membership_from_ts, membership_to_ts)
	VALUES (45, 4, 45, CURRENT_DATE-10, CURRENT_DATE-1);
-- ac6e6270-87eb-4be7-b3ce-385d9a7a2057		Leon Scott Kennedy			Resident Evil
INSERT INTO public.tb_person(
	person_id, user_uuid, nick_name)
	VALUES (46, 'ac6e6270-87eb-4be7-b3ce-385d9a7a2057', 'Scott');
INSERT INTO public.tb_membership(
	membership_id, group_id, person_id, membership_from_ts, membership_to_ts)
	VALUES (46, 4, 46, CURRENT_DATE-2, null);
-- 78f59ccd-7dcf-4b85-8251-5bc1ba8f9b51		Rebecca Chambers			Resident Evil
INSERT INTO public.tb_person(
	person_id, user_uuid, nick_name)
	VALUES (47, '78f59ccd-7dcf-4b85-8251-5bc1ba8f9b51', 'Becca');
INSERT INTO public.tb_membership(
	membership_id, group_id, person_id, membership_from_ts, membership_to_ts)
	VALUES (47, 4, 47, CURRENT_DATE-2, null);
	
-- ========================================================================================================	
INSERT INTO public.tb_group(
            group_id, group_uuid, grptyp_cd, group_name, group_de, group_private_fl)
    VALUES (5, '00b2c66d-35b0-48ac-8039-31e67c7bc34c', 'FI', 'Company ABC Workout Group', 'Employees interesting in fitness and health.', False);

-- d71b920a-04a9-44d3-beda-a736601a64c5', 'Joe.Group.Subscribed@foo.com.invali
INSERT INTO public.tb_person(
	person_id, user_uuid, nick_name)
	VALUES (50, 'd71b920a-04a9-44d3-beda-a736601a64c5', 'Joe.Group');
INSERT INTO public.tb_group_manager(
	manager_id, group_id, person_id, manager_from_ts, manager_to_ts)
	VALUES (50, 5, 50, CURRENT_DATE-2, null);
-- 14468f27-44e8-4fc3-8cc6-3a48c80fd5aa', 'Joe.Subscribed@foo.com.invali
INSERT INTO public.tb_person(
	person_id, user_uuid, nick_name)
	VALUES (51, '14468f27-44e8-4fc3-8cc6-3a48c80fd5aa', 'Joe.Subscribed');
INSERT INTO public.tb_membership(
	membership_id, group_id, person_id, membership_from_ts, membership_to_ts)
	VALUES (51, 5, 51, CURRENT_DATE-2, null);
-- c95802ac-e465-11e8-9f32-f2801f1b9fd1', 'Joe.Customer@foo.com.invali
INSERT INTO public.tb_person(
	person_id, user_uuid, nick_name)
	VALUES (52, 'c95802ac-e465-11e8-9f32-f2801f1b9fd1', 'Joe.Customer');
INSERT INTO public.tb_membership(
	membership_id, group_id, person_id, membership_from_ts, membership_to_ts)
	VALUES (52, 5, 52, CURRENT_DATE-2, null);
	
