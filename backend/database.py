import aiosqlite

DB_PATH = "fitness_data.db"

async def init_db() -> None:
    """Initialize the DB connection and create exercises table"""
    async with aiosqlite.connect(DB_PATH) as connection:
        init_fitness_table_query = """
            CREATE TABLE IF NOT EXISTS exercises (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT NOT NULL,
                exercise TEXT NOT NULL,
                type TEXT NOT NULL,
                sets INTEGER NOT NULL,
                reps INTEGER,
                time INTEGER,
                notes TEXT
            );
        """

        await connection.execute(init_fitness_table_query)
        await connection.commit()


async def add_exercise(date, exercise, type, sets, reps, time=0, notes=""):
    async with aiosqlite.connect(DB_PATH) as connection:
        add_exercise_query = """INSERT INTO exercises 
                                (date, exercise, type, sets, reps, time, notes)
                                VALUES (?, ?, ?, ?, ?, ?, ?)"""
        await connection.execute(add_exercise_query, (date, exercise, type, sets, reps, time, notes))
        await connection.commit()


async def delete_exercise(id):
    async with aiosqlite.connect(DB_PATH) as connection:
        delete_exercise_query = """DELETE FROM exercises where id=?"""
        await connection.execute(delete_exercise_query, (id, ))
        await connection.commit()


async def update_exercise(id, date, exercise, type, sets, reps, time=0, notes=""):
    async with aiosqlite.connect(DB_PATH) as connection:
        update_exercise_query = """UPDATE exercises SET date=?, exercise=?, type=?,
                                sets=?, reps=?, time=?, notes=?
                                WHERE id=?"""
        await connection.execute(update_exercise_query, (date, exercise, type, sets, reps, time, notes, id))
        await connection.commit()


async def delete_all():
    pass

async def fetch_all():
    pass