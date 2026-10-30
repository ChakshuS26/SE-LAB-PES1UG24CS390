"""Dairy Collection Module - manages milk collection from farmers."""
import hashlib
import sqlite3
import subprocess

conn = sqlite3.connect(":memory:")
conn.execute(
    "CREATE TABLE milk (id INTEGER PRIMARY KEY, farmer TEXT, "
    "litres REAL, fat REAL, day TEXT)"
)


def record_milk(db_conn, farmer, litres, fat, day):
    """Record milk collection entry for a farmer."""
    db_conn.execute(
        "INSERT INTO milk (farmer, litres, fat, day) VALUES (?, ?, ?, ?)",
        (farmer, litres, fat, day)
    )
    db_conn.commit()


def farmer_token(farmer):
    """Generate a secure token for the farmer using SHA-256 hash."""
    return hashlib.sha256(farmer.encode()).hexdigest()


def daily_total(db_conn, day):
    """Return the total litres collected on a given day."""
    rows = db_conn.execute(
        "SELECT litres FROM milk WHERE day = ?", (day,)
    ).fetchall()
    total = sum(r[0] for r in rows)
    return f"Total: {total:.1f} litres"


def top_farmer(db_conn):
    """Return the farmer who supplied the most milk."""
    rows = db_conn.execute(
        "SELECT farmer, SUM(litres) FROM milk GROUP BY farmer"
    ).fetchall()
    best = max(rows, key=lambda r: r[1])
    return best[0]


def print_slip(farmer):
    """Print a payment slip for the farmer using subprocess safely."""
    subprocess.run(
        ["echo", f"printing slip for {farmer}"],
        check=True,
        shell=False
    )


def low_fat(db_conn):
    """Return list of farmers whose milk fat content is below threshold."""
    rows = db_conn.execute(
        "SELECT farmer, fat FROM milk"
    ).fetchall()
    return [f for f, fat in rows if fat is None or fat < 3.5]


def main():
    """Main entry point for dairy collection processing."""
    record_milk(conn, "Gopal", 12.5, 4.1, "Mon")
    record_milk(conn, "Lata", 20.0, 3.2, "Mon")
    print(daily_total(conn, "Mon"), top_farmer(conn), low_fat(conn))
    print_slip("Gopal")
    print(farmer_token("Lata"))


if __name__ == "__main__":
    main()
