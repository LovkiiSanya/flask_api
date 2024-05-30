import peewee as pw
from playhouse.migrate import PostgresqlMigrator, migrate


my_db = pw.PostgresqlDatabase("courses_db",
                              host="127.0.0.1",
                              user="admin",
                              password="root")

migrator = PostgresqlMigrator(my_db)

with my_db.atomic():
    migrate(
        migrator.add_column('usercourse', 'is_deleted', pw.BooleanField(default=False)),
        migrator.add_column('usertable', 'is_deleted', pw.BooleanField(default=False)),
        migrator.add_column('coursestable', 'is_deleted', pw.BooleanField(default=False))
    )
