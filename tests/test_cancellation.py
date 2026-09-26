"""Executable examples for the W1 UR-04 cancellation seam."""

import unittest
from dataclasses import replace

from app.grooming import Booking, CancellationResult, cancel


class CancellationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.booking = Booking(
            id="booking-1",
            owner_id="owner-1",
            start_minute=600,
            duration_minutes=60,
            groomer_id=1,
            room_id=2,
            status="active",
        )

    def assert_unchanged(self, booking: Booking, result: CancellationResult, **kwargs: object) -> None:
        actual_result, after = cancel(booking, **kwargs)
        self.assertEqual(actual_result, result)
        self.assertIs(after, booking)
        self.assertEqual(after, booking)

    def test_owner_cancels_before_start(self) -> None:
        result, after = cancel(self.booking, "owner-1", 599)
        self.assertEqual(result, CancellationResult.CANCELLED)
        self.assertEqual(after, replace(self.booking, status="cancelled"))
        self.assertEqual(self.booking.status, "active")
        self.assertIsNot(after, self.booking)

    def test_repeated_cancellation_preserves_entire_record(self) -> None:
        _, cancelled = cancel(self.booking, "owner-1", 599)
        self.assert_unchanged(
            cancelled,
            CancellationResult.ALREADY_CANCELLED,
            actor_id="owner-1",
            now_minute=600,
        )

    def test_invalid_booking_fields_are_rejected_before_authorization(self) -> None:
        invalid = (
            replace(self.booking, id=" "),
            replace(self.booking, owner_id=""),
            replace(self.booking, start_minute=True),
            replace(self.booking, duration_minutes=0),
            replace(self.booking, groomer_id=4),
            replace(self.booking, room_id=0),
            replace(self.booking, status="pending"),
        )
        for booking in invalid:
            with self.subTest(booking=booking):
                self.assert_unchanged(
                    booking,
                    CancellationResult.INVALID_INPUT,
                    actor_id=None,
                    now_minute=599,
                )

    def test_invalid_time_preserves_record(self) -> None:
        for now_minute in (True, "599"):
            with self.subTest(now_minute=now_minute):
                self.assert_unchanged(
                    self.booking,
                    CancellationResult.INVALID_INPUT,
                    actor_id="owner-1",
                    now_minute=now_minute,
                )

    def test_missing_actor_preserves_record(self) -> None:
        for actor_id in (None, "", "  "):
            with self.subTest(actor_id=actor_id):
                self.assert_unchanged(
                    self.booking,
                    CancellationResult.UNAUTHENTICATED,
                    actor_id=actor_id,
                    now_minute=599,
                )

    def test_malformed_actor_preserves_record(self) -> None:
        self.assert_unchanged(
            self.booking,
            CancellationResult.INVALID_INPUT,
            actor_id=42,
            now_minute=599,
        )

    def test_other_actor_preserves_record(self) -> None:
        self.assert_unchanged(
            self.booking,
            CancellationResult.FORBIDDEN,
            actor_id="owner-2",
            now_minute=599,
        )

    def test_at_start_and_after_start_are_too_late(self) -> None:
        for now_minute in (600, 601):
            with self.subTest(now_minute=now_minute):
                self.assert_unchanged(
                    self.booking,
                    CancellationResult.TOO_LATE,
                    actor_id="owner-1",
                    now_minute=now_minute,
                )

    def test_non_owner_does_not_learn_cancelled_state(self) -> None:
        cancelled = replace(self.booking, status="cancelled")
        self.assert_unchanged(
            cancelled,
            CancellationResult.FORBIDDEN,
            actor_id="owner-2",
            now_minute=599,
        )


if __name__ == "__main__":
    unittest.main()
