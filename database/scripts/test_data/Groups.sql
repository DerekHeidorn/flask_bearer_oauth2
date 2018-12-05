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
	person_id, user_uuid)
	VALUES (1, '4e5d14ab-e91e-49b3-9c61-795748c41e09');
INSERT INTO public.tb_group_manager(
	manager_id, group_id, person_id, manager_from_ts)
	VALUES (1, 1, 1, CURRENT_DATE-2);
-- f55b7b25-6ef5-4727-9645-7564fb777f21		Wasp						Janet van Dyne
INSERT INTO public.tb_person(
	person_id, user_uuid)
	VALUES (10, 'f55b7b25-6ef5-4727-9645-7564fb777f21');
INSERT INTO public.tb_membership(
	membership_id, group_id, person_id, membership_from_ts)
	VALUES (10, 1, 10, CURRENT_DATE-2);
-- e4176c50-9e84-49d3-a2b7-f8773d57fb9b		Hulk						Dr. Robert Bruce Banner
INSERT INTO public.tb_person(
	person_id, user_uuid)
	VALUES (11, 'e4176c50-9e84-49d3-a2b7-f8773d57fb9b');
INSERT INTO public.tb_membership(
	membership_id, group_id, person_id, membership_from_ts)
	VALUES (11, 1, 11, CURRENT_DATE-2);
-- 29ef21b2-825f-4d49-a654-df9dd2295630		Scarlet Witch				Wanda Maximoff
INSERT INTO public.tb_person(
	person_id, user_uuid)
	VALUES (12, '29ef21b2-825f-4d49-a654-df9dd2295630');
INSERT INTO public.tb_membership(
	membership_id, group_id, person_id, membership_from_ts)
	VALUES (12, 1, 12, CURRENT_DATE-2);
-- 5fa2a30d-403c-4ae8-b3fa-5dd207ef926b		Vision						Victor Shade
INSERT INTO public.tb_person(
	person_id, user_uuid)
	VALUES (13, '5fa2a30d-403c-4ae8-b3fa-5dd207ef926b');
INSERT INTO public.tb_membership(
	membership_id, group_id, person_id, membership_from_ts)
	VALUES (13, 1, 13, CURRENT_DATE-2);
-- b130cdd5-e09c-471f-b3df-da80413d58d5		Black Widow					Natasha Alianovna Romanoff
INSERT INTO public.tb_person(
	person_id, user_uuid)
	VALUES (14, 'b130cdd5-e09c-471f-b3df-da80413d58d5');
INSERT INTO public.tb_membership(
	membership_id, group_id, person_id, membership_from_ts)
	VALUES (14, 1, 14, CURRENT_DATE-2);
-- b8919fd0-0379-4fe3-b81e-4d06f079ce1f		Falcon						Samuel "Snap" Thomas Wilson
INSERT INTO public.tb_person(
	person_id, user_uuid)
	VALUES (15, 'b8919fd0-0379-4fe3-b81e-4d06f079ce1f');
INSERT INTO public.tb_membership(
	membership_id, group_id, person_id, membership_from_ts)
	VALUES (15, 1, 15, CURRENT_DATE-2);
-- 48667be7-9b99-4353-af8d-814b4c308b15		Captain Marvel				Monica Rambeau
INSERT INTO public.tb_person(
	person_id, user_uuid)
	VALUES (16, '48667be7-9b99-4353-af8d-814b4c308b15');
INSERT INTO public.tb_membership(
	membership_id, group_id, person_id, membership_from_ts)
	VALUES (16, 1, 16, CURRENT_DATE-2);
-- d627b053-7986-41ab-9065-f37fec698148		War Machine					James Rupert "Rhodey" Rhodes
INSERT INTO public.tb_person(
	person_id, user_uuid)
	VALUES (17, 'd627b053-7986-41ab-9065-f37fec698148');
INSERT INTO public.tb_membership(
	membership_id, group_id, person_id, membership_from_ts)
	VALUES (17, 1, 17, CURRENT_DATE-2);
-- 179c80b3-a6f4-4c39-9edd-f38db0c7d0af		Spider-Man					Peter Benjamin Parker
INSERT INTO public.tb_person(
	person_id, user_uuid)
	VALUES (18, '179c80b3-a6f4-4c39-9edd-f38db0c7d0af');
INSERT INTO public.tb_membership(
	membership_id, group_id, person_id, membership_from_ts)
	VALUES (18, 1, 18, CURRENT_DATE-2);
-- a787b4e4-b09d-4d08-9073-2b47c8abbe5b		Ant-Man						Scott Lang
INSERT INTO public.tb_person(
	person_id, user_uuid)
	VALUES (19, 'a787b4e4-b09d-4d08-9073-2b47c8abbe5b');
INSERT INTO public.tb_membership(
	membership_id, group_id, person_id, membership_from_ts)
	VALUES (19, 1, 19, CURRENT_DATE-2);

	
-- ========================================================================================================
INSERT INTO public.tb_group(
            group_id, group_uuid, grptyp_cd, group_name, group_de, group_private_fl)
    VALUES (2, '84a7c3e2-d810-4439-836c-94002d9f4b0b', 'SP', 'Brown Coats', 'Browncoats were soldiers who fought for the Independent Planets, who lost to the Union of Allied Planets in the Unification War.', False);
-- a10541a9-46f4-49ae-97f4-625bc92b5f7c		Malcolm Reynolds					Firefly
INSERT INTO public.tb_person(
	person_id, user_uuid)
	VALUES (20, 'a10541a9-46f4-49ae-97f4-625bc92b5f7c');
INSERT INTO public.tb_group_manager(
	manager_id, group_id, person_id, manager_from_ts)
	VALUES (20, 2, 20, CURRENT_DATE-2);
-- 8ead1ce9-8867-4523-a84e-a1cf920038df		Zoe Washburne				Firefly
INSERT INTO public.tb_person(
	person_id, user_uuid)
	VALUES (21, '8ead1ce9-8867-4523-a84e-a1cf920038df');
INSERT INTO public.tb_membership(
	membership_id, group_id, person_id, membership_from_ts)
	VALUES (21, 2, 21, CURRENT_DATE-2);
-- bb3985d3-9d2f-49c7-8304-a8271330f762		Hoban "Wash" Washburne		Firefly
INSERT INTO public.tb_person(
	person_id, user_uuid)
	VALUES (22, 'bb3985d3-9d2f-49c7-8304-a8271330f762');
INSERT INTO public.tb_membership(
	membership_id, group_id, person_id, membership_from_ts)
	VALUES (22, 2, 22, CURRENT_DATE-2);
-- ac08889e-1c82-4e4e-8912-8e7c95b81a25		Inara Serra					Firefly
INSERT INTO public.tb_person(
	person_id, user_uuid)
	VALUES (23, 'ac08889e-1c82-4e4e-8912-8e7c95b81a25');
INSERT INTO public.tb_membership(
	membership_id, group_id, person_id, membership_from_ts)
	VALUES (23, 2, 23, CURRENT_DATE-2);
-- e6abb20f-75f7-43b2-8be6-421876ff4db4		Jayne Cobb					Firefly
INSERT INTO public.tb_person(
	person_id, user_uuid)
	VALUES (24, 'e6abb20f-75f7-43b2-8be6-421876ff4db4');
INSERT INTO public.tb_membership(
	membership_id, group_id, person_id, membership_from_ts)
	VALUES (24, 2, 24, CURRENT_DATE-2);
-- d9c83075-6efa-4554-9ab1-891ab6472950		Kaylee Frye					Firefly
INSERT INTO public.tb_person(
	person_id, user_uuid)
	VALUES (25, 'd9c83075-6efa-4554-9ab1-891ab6472950');
INSERT INTO public.tb_membership(
	membership_id, group_id, person_id, membership_from_ts)
	VALUES (25, 2, 25, CURRENT_DATE-2);
-- 53271313-d6a6-41a4-b733-a2c450834e07		Simon Tam					Firefly
INSERT INTO public.tb_person(
	person_id, user_uuid)
	VALUES (26, '53271313-d6a6-41a4-b733-a2c450834e07');
INSERT INTO public.tb_membership(
	membership_id, group_id, person_id, membership_from_ts)
	VALUES (26, 2, 26, CURRENT_DATE-2);
-- 3e1bef3b-562c-4c0c-a1b2-123c1385a1d4		River Tam					Firefly
INSERT INTO public.tb_person(
	person_id, user_uuid)
	VALUES (27, '3e1bef3b-562c-4c0c-a1b2-123c1385a1d4');
INSERT INTO public.tb_membership(
	membership_id, group_id, person_id, membership_from_ts)
	VALUES (27, 2, 27, CURRENT_DATE-2);
-- 441fa406-54c1-45b5-b33d-981b7197f277		Derrial Book				Firefly
INSERT INTO public.tb_person(
	person_id, user_uuid)
	VALUES (28, '441fa406-54c1-45b5-b33d-981b7197f277');
INSERT INTO public.tb_membership(
	membership_id, group_id, person_id, membership_from_ts)
	VALUES (28, 2, 28, CURRENT_DATE-2);

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
	person_id, user_uuid)
	VALUES (40, '121461d4-a78b-4bbb-9471-9cf8233fdc78');
INSERT INTO public.tb_group_manager(
	manager_id, group_id, person_id, manager_from_ts)
	VALUES (40, 4, 40, CURRENT_DATE-2);
-- c64ea92c-757b-4846-a385-15ee2febb2e2		Ada Wong					Resident Evil
INSERT INTO public.tb_person(
	person_id, user_uuid)
	VALUES (41, 'c64ea92c-757b-4846-a385-15ee2febb2e2');
INSERT INTO public.tb_membership(
	membership_id, group_id, person_id, membership_from_ts)
	VALUES (41, 4, 41, CURRENT_DATE-2);
-- 0ec0aeb8-8f3b-4d51-a3a0-a862cfcf0f96		Albert Wesker				Resident Evil
INSERT INTO public.tb_person(
	person_id, user_uuid)
	VALUES (42, '0ec0aeb8-8f3b-4d51-a3a0-a862cfcf0f96');
INSERT INTO public.tb_membership(
	membership_id, group_id, person_id, membership_from_ts)
	VALUES (42, 4, 42, CURRENT_DATE-2);
-- 68d3d343-d5cd-4d46-8cf7-f8707c46a148		Chris Redfield				Resident Evil
INSERT INTO public.tb_person(
	person_id, user_uuid)
	VALUES (43, '68d3d343-d5cd-4d46-8cf7-f8707c46a148');
INSERT INTO public.tb_membership(
	membership_id, group_id, person_id, membership_from_ts)
	VALUES (43, 4, 43, CURRENT_DATE-2);
-- bfaec952-7b06-4791-a321-02a925ff59b4		Claire Redfield				Resident Evil
INSERT INTO public.tb_person(
	person_id, user_uuid)
	VALUES (44, 'bfaec952-7b06-4791-a321-02a925ff59b4');
INSERT INTO public.tb_membership(
	membership_id, group_id, person_id, membership_from_ts)
	VALUES (44, 4, 44, CURRENT_DATE-2);
-- d81dc597-ed99-46a7-846f-6495898b40c9		Jill Valentine				Resident Evil
INSERT INTO public.tb_person(
	person_id, user_uuid)
	VALUES (45, 'd81dc597-ed99-46a7-846f-6495898b40c9');
-- ac6e6270-87eb-4be7-b3ce-385d9a7a2057		Leon Scott Kennedy			Resident Evil
INSERT INTO public.tb_person(
	person_id, user_uuid)
	VALUES (46, 'ac6e6270-87eb-4be7-b3ce-385d9a7a2057');
INSERT INTO public.tb_membership(
	membership_id, group_id, person_id, membership_from_ts)
	VALUES (46, 4, 46, CURRENT_DATE-2);
-- 78f59ccd-7dcf-4b85-8251-5bc1ba8f9b51		Rebecca Chambers			Resident Evil
INSERT INTO public.tb_person(
	person_id, user_uuid)
	VALUES (47, '78f59ccd-7dcf-4b85-8251-5bc1ba8f9b51');
INSERT INTO public.tb_membership(
	membership_id, group_id, person_id, membership_from_ts)
	VALUES (47, 4, 47, CURRENT_DATE-2);
	
-- ========================================================================================================	
INSERT INTO public.tb_group(
            group_id, group_uuid, grptyp_cd, group_name, group_de, group_private_fl)
    VALUES (5, '00b2c66d-35b0-48ac-8039-31e67c7bc34c', 'FI', 'Company ABC Workout Group', 'Employees interesting in fitness and health.', False);

-- d71b920a-04a9-44d3-beda-a736601a64c5', 'Joe.Group.Subscribed@foo.com.invali
INSERT INTO public.tb_person(
	person_id, user_uuid)
	VALUES (50, 'd71b920a-04a9-44d3-beda-a736601a64c5');
INSERT INTO public.tb_group_manager(
	manager_id, group_id, person_id, manager_from_ts)
	VALUES (50, 5, 50, CURRENT_DATE-2);
-- 14468f27-44e8-4fc3-8cc6-3a48c80fd5aa', 'Joe.Subscribed@foo.com.invali
INSERT INTO public.tb_person(
	person_id, user_uuid)
	VALUES (51, '14468f27-44e8-4fc3-8cc6-3a48c80fd5aa');
INSERT INTO public.tb_membership(
	membership_id, group_id, person_id, membership_from_ts)
	VALUES (51, 5, 51, CURRENT_DATE-2);
-- c95802ac-e465-11e8-9f32-f2801f1b9fd1', 'Joe.Customer@foo.com.invali
INSERT INTO public.tb_person(
	person_id, user_uuid)
	VALUES (52, 'c95802ac-e465-11e8-9f32-f2801f1b9fd1');
INSERT INTO public.tb_membership(
	membership_id, group_id, person_id, membership_from_ts)
	VALUES (52, 5, 52, CURRENT_DATE-2);
	
-- ========================================================================================================
INSERT INTO public.tb_group(
            group_id, group_uuid, grptyp_cd, group_name, group_de, group_private_fl)
    VALUES (6, '5491f5fd-c9ef-4f0e-9137-183c91d98b38', 'FI', 'Legion of Doom', 'The Legion of Doom is a group of supervillains ', TRUE);

-- 14468f27-44e8-4fc3-8cc6-3a48c80fd5aa', 'Joe.Subscribed@foo.com.invali
INSERT INTO public.tb_group_manager(
	manager_id, group_id, person_id, manager_from_ts)
	VALUES (51, 6, 51, CURRENT_DATE-2);
-- 21ce38c2-5456-40ac-a880-2b8477684a15 - Legion of Doom - Lex_Luthor
INSERT INTO public.tb_person(
	person_id, user_uuid)
	VALUES (60, '21ce38c2-5456-40ac-a880-2b8477684a15');
INSERT INTO public.tb_group_manager(
	manager_id, group_id, person_id, manager_from_ts)
	VALUES (60, 6, 60, CURRENT_DATE-2);
-- 53e491f9-96b3-495f-8fd6-a6d0aa54e0fc - Legion of Doom - Brainiac
INSERT INTO public.tb_person(
	person_id, user_uuid)
	VALUES (61, '53e491f9-96b3-495f-8fd6-a6d0aa54e0fc');
INSERT INTO public.tb_membership(
	membership_id, group_id, person_id, membership_from_ts)
	VALUES (61, 6, 61, CURRENT_DATE-2);
-- 0785e9e4-c80e-4f70-9c73-51fd1c63a142 - Legion of Doom - Bizarro
INSERT INTO public.tb_person(
	person_id, user_uuid)
	VALUES (62, '0785e9e4-c80e-4f70-9c73-51fd1c63a142');
INSERT INTO public.tb_membership(
	membership_id, group_id, person_id, membership_from_ts)
	VALUES (62, 6, 62, CURRENT_DATE-2);
-- 71dfe7fc-7279-46d9-a1ff-b6227d69aa73 - Legion of Doom - Captain_Cold
INSERT INTO public.tb_person(
	person_id, user_uuid)
	VALUES (63, '71dfe7fc-7279-46d9-a1ff-b6227d69aa73');
INSERT INTO public.tb_membership(
	membership_id, group_id, person_id, membership_from_ts)
	VALUES (63, 6, 63, CURRENT_DATE-2);
-- 157b3c6c-c56f-467b-8311-2202a066c531 - Legion of Doom - Gorilla_Grodd
INSERT INTO public.tb_person(
	person_id, user_uuid)
	VALUES (64, '157b3c6c-c56f-467b-8311-2202a066c531');
INSERT INTO public.tb_membership(
	membership_id, group_id, person_id, membership_from_ts)
	VALUES (64, 6, 64, CURRENT_DATE-2);
-- 1ed78d12-82c0-4eb6-bde8-b8413f9406f3 - Legion of Doom - Riddler
INSERT INTO public.tb_person(
	person_id, user_uuid)
	VALUES (65, '1ed78d12-82c0-4eb6-bde8-b8413f9406f3');
INSERT INTO public.tb_membership(
	membership_id, group_id, person_id, membership_from_ts)
	VALUES (65, 6, 65, CURRENT_DATE-2);
-- 5d7d2422-17e2-4613-9a5a-645675a4999a - Legion of Doom - Scarecrow
INSERT INTO public.tb_person(
	person_id, user_uuid)
	VALUES (66, '5d7d2422-17e2-4613-9a5a-645675a4999a');
INSERT INTO public.tb_membership(
	membership_id, group_id, person_id, membership_from_ts)
	VALUES (66, 6, 66, CURRENT_DATE-2);