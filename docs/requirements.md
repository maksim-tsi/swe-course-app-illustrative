# User requirements — grooming appointment example

**Status:** initial teaching requirements, before W1 implementation. All people, pets, and appointments used in demonstrations are synthetic. The studio has **three groomers, two interchangeable rooms, and four services**. All groomers can perform all four services. These constraints are product inputs, not evidence that any scheduling code exists.

## Users and goals

- **Dog owner:** find a suitable appointment, book it, understand whether the operation succeeded, and cancel or later reschedule it.
- **Studio operator (instructor demonstration):** inspect the schedule, understand resource use and rejected requests, and recover a known version and synthetic records.

## Initial user requirements

| ID | User-visible need | Earliest stage |
|---|---|---|
| UR-01 | See the four named services, fixed durations, and bookable starts in the studio's local time. | W2 |
| UR-02 | Request one service and start time; receive an unambiguous accepted or rejected result and booking reference. | W2 |
| UR-03 | Never receive a confirmed booking that overlaps another active booking for its assigned groomer or room. A booking occupies both resources for its entire interval. | W2 |
| UR-04 | Cancel an owned booking; a repeated cancellation reports its existing state without releasing resources twice. | W1 contract; W2 persisted path |
| UR-05 | Understand pending, success, unavailable-dependency, validation, and conflict outcomes without relying on colour alone; retry safely after an uncertain result. | W2 |
| UR-06 | Reproduce setup, startup, and ordinary checks from recorded dependencies and non-secret configuration. | W2 |
| UR-07 | Use criteria-based functional and structural checks to judge the early release; gather one documented feedback item. | W3 |
| UR-08 | Reschedule an owned booking as one bounded operation; failure leaves the original booking valid and does not reserve another resource. | W4 |
| UR-09 | Demonstrate allowed and denied changes at the application's trust boundary, plus rollback and data restore against synthetic records. | W5 |
| UR-10 | Show a checked maintenance change and a course-accessible release with reproducible operating and handover instructions. | W6 |

## Bounded scheduling assumptions

The initial model uses one studio time zone, one teaching week, fixed opening hours, starts on a 30-minute grid, and four fixed service durations that are multiples of 30 minutes. The proposed example catalogue is Bath (30 min), Basic Groom (60 min), Full Groom (90 min), and Puppy Introduction (30 min). The instructor can revise labels before W1; the four-service cardinality remains fixed. The application chooses the lowest numbered available groomer and room deterministically. No customer choice of groomer, specialist qualifications, room types, recurring appointments, payments, or notifications are required. W1 must record timing and allocation assumptions in an ADR before code relies on them.

For the teaching path, owners use synthetic booking references and an ownership proof defined in the stage specification. No real identity or customer information is stored. Before any internet-facing deployment, the instructor must decide and verify access controls for the demonstration endpoint; this baseline does not claim production authentication.

## Quality constraints

- Preserve booking state on rejected or repeated operations; avoid double allocation and double release.
- Keep the backend/client boundary explicit, testable, and small enough to explain in class.
- Record actual limitations: accessibility observations are bounded, tests do not prove absence of defects, and SQLite transaction behaviour must be tested rather than assumed.
- Make the result reproducible using ordinary free project tools. No model or paid service is required to run the application or its required checks.

See [specification plan](specification-plan.md) for the decisions still to define and [test plan](test-plan.md) for coverage intentions.
