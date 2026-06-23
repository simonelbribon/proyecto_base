import json
import psycopg2
from src.seme.publisher import EventPublisher
from src.seme.models import SEMEEvent


class PostgresPublisher(EventPublisher):
    def __init__(self, conn):
        self.conn = conn

    def publish(self, event: SEMEEvent) -> None:
        with self.conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO seme_events (
                    id,
                    type,
                    input,
                    output,
                    trace,
                    timestamp
                )
                VALUES (%s, %s, %s, %s, %s, %s)
                """,
                (
                    event.id,
                    event.type,
                    json.dumps(event.input),
                    json.dumps(event.output),
                    json.dumps(event.trace),
                    event.timestamp,
                )
            )
        self.conn.commit()
