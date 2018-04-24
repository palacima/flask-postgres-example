from app import db, Stadium

stadium1 = Stadium(0, 'Levi\'s Stadium', '49ers')
stadium2 = Stadium(1, 'AT&T Park', 'Giants')
stadium3 = Stadium(2, 'Nats Park', 'Nationals')

db.session.add_all([stadium1, stadium2, stadium3])
db.session.commit()
