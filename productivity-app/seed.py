from app import create_app, db
from models import User, Task
from faker import Faker

fake = Faker()
app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    users = []
    for _ in range(3):
        u = User(username=fake.unique.user_name())
        u.set_password("password123")
        db.session.add(u)
        users.append(u)
    db.session.commit()

    for user in users:
        for _ in range(5):
            task = Task(
                title=fake.sentence(nb_words=4),
                description=fake.paragraph(),
                completed=fake.boolean(),
                user_id=user.id
            )
            db.session.add(task)
    db.session.commit()

    print("Seeded 3 users with 5 tasks each.")
    for u in users:
        print(f"  username: {u.username} | password: password123")