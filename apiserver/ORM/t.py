class User():
    id=1
    name='wt'
    money=2000


def save(entity):
    sql='insert into %s(%s) value (%s)'
    table=entity.__class__.__name__.lower()
    colname=','.join([col for col in entity.__dict__])
    colplaceholders=','.join(["%%(%s)s"%col for col in entity.__dict__])
    sql=sql%(table,colname,colplaceholders)


if __name__ == '__main__':
    u1=User()
    u1.name='jack'
    u1.money=900










