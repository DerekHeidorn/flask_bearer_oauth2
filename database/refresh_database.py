
from subprocess import Popen, PIPE


def refresh_database():
    print("refreshDatabase...")
    database_uri = 'postgresql://postgres:P$F$xs+n?5+Ug3AU5PTe3q@localhost/groups'

    files = ['scripts/wipe_database.sql',
             'scripts/tables.sql',
             'scripts/data_codetables.sql',
             'scripts/test_data/TB_CONFIG.sql'
			 ]

    for f in files:
        psql_cmd = ["psql", "-f", f, "-a", database_uri]
        process = Popen(psql_cmd, stdout=PIPE)
        process.communicate()
        process.wait()


if __name__ == "__main__":
    refresh_database()
