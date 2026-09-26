"""W1's in-memory cancellation contract; persistence belongs to W2."""

from dataclasses import dataclass, replace
from enum import Enum


class CancellationResult(str, Enum):
    INVALID_INPUT = "InvalidInput"
    UNAUTHENTICATED = "Unauthenticated"
    FORBIDDEN = "Forbidden"
    ALREADY_CANCELLED = "AlreadyCancelled"
    TOO_LATE = "TooLate"
    CANCELLED = "Cancelled"


@dataclass(frozen=True)
class Booking:
    id: str
    owner_id: str
    start_minute: int
    duration_minutes: int
    groomer_id: int
    room_id: int
    status: str


def _is_int(value: object) -> bool:
    return type(value) is int


def _valid_booking(booking: object) -> bool:
    return (
        isinstance(booking, Booking)
        and isinstance(booking.id, str)
        and bool(booking.id.strip())
        and isinstance(booking.owner_id, str)
        and bool(booking.owner_id.strip())
        and _is_int(booking.start_minute)
        and _is_int(booking.duration_minutes)
        and booking.duration_minutes > 0
        and _is_int(booking.groomer_id)
        and 1 <= booking.groomer_id <= 3
        and _is_int(booking.room_id)
        and 1 <= booking.room_id <= 2
        and booking.status in ("active", "cancelled")
    )


def cancel(
    booking: Booking, actor_id: str | None, now_minute: int
) -> tuple[CancellationResult, Booking]:
    """Return a result and booking value without changing the input booking.

    Booking fields and the current minute are checked before authorization or state.
    Integer minutes share one teaching timeline; calendar conversion is outside W1.
    """
    if not _valid_booking(booking) or not _is_int(now_minute):
        return CancellationResult.INVALID_INPUT, booking
    if actor_id is None or (isinstance(actor_id, str) and not actor_id.strip()):
        return CancellationResult.UNAUTHENTICATED, booking
    if not isinstance(actor_id, str):
        return CancellationResult.INVALID_INPUT, booking
    if actor_id != booking.owner_id:
        return CancellationResult.FORBIDDEN, booking
    if booking.status == "cancelled":
        return CancellationResult.ALREADY_CANCELLED, booking
    if now_minute >= booking.start_minute:
        return CancellationResult.TOO_LATE, booking
    return CancellationResult.CANCELLED, replace(booking, status="cancelled")
