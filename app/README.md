# Application code

W1 adds a Python package under `app/grooming/` with an immutable synthetic `Booking` value and the pure `cancel` contract. Import it from the repository root as `from app.grooming import Booking, CancellationResult, cancel`. No application server, SQLite persistence, browser client or startup command exists yet; W2 will add those boundaries. Keep business rules out of future HTTP handlers and update the [specification plan](../docs/specification-plan.md) as behaviour is added.
