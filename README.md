# Small Business AI Enablement Toolkit

**Practical AI adoption · Measurable business outcomes · Responsible data handling**

> Independent portfolio project by [fredoncyber](https://github.com/fredoncyber). Not affiliated with or endorsed by OpenAI or its OpenWorks program.

## The problem
Small businesses often have repetitive customer questions, scattered operating notes, and limited time to prepare reports. This toolkit helps an owner identify one suitable task, create a reviewable AI-assisted draft, and compare the process before and after adoption.

## What works today (v0.2)
- **Browser toolkit:** Three interactive workflows with fictional examples, prompt copying and estimated labor-value calculations. See [browser demonstration](docs/browser_demo.md). Open `web/index.html` locally; no API key needed. The interface generates prompts, not AI responses.
- **Customer inquiry drafting:** Converts a sample customer question and an *approved* business facts file into a copy-and-paste prompt. It does **not** automatically send replies or invent business policies.
- **Operations briefing:** Turns approved event or job details into a prompt for an actionable checklist, with owner verification.
- **Business metrics:** Reads a CSV of task durations and produces before/after time-saved metrics. Example data are synthetic, not verified real-world results.
- **Readiness and privacy:** Plain-language assessment and redaction/review checklists.

No API key, account integration, or paid platform is needed for these starter workflows. The prompt drafts may be used in an AI tool approved by the business, with suitable account settings and a human reviewer.

## Quick start
```bash
python3 src/toolkit.py inquiry --question 'Can I pick up Saturday?' --facts examples/approved_business_facts.txt
python3 src/toolkit.py operations --details examples/program_details.txt
python3 src/toolkit.py metrics --csv examples/synthetic_time_study.csv
python3 -m unittest discover -s tests -v
```
Python 3.10+; standard library only. The program prints drafts and calculations; it never connects to or transmits data to an AI service.

## Public demonstration and community pilot
- [Public demo deployment instructions](docs/public_demo_setup.md) — hosting must be enabled and verified before advertising a live URL.
- [Community pilot plan](docs/community_pilot_plan.md) — proposed evaluation, not completed results.

## Community workshop
[90-minute workshop package](workshop/README.md) — facilitator guide, 12-slide outline, participant workbook, exercise key and evaluation form. Prepared, not yet delivered.

## Workflow
1. **Discover:** Fill in `templates/ai_readiness_assessment.md` with the owner.
2. **Select:** Identify one repetitive, low-risk task with an observable baseline.
3. **Prepare:** Confirm approved facts and remove private or regulated information.
4. **Draft:** Run a local prompt generator and paste into an approved AI tool.
5. **Review:** The owner verifies every claim; no automatic posting, sending, or business decisions.
6. **Measure:** Use `templates/pilot_measurement_log.csv` and the metrics command.
7. **Teach:** Use `docs/workshop_agenda.md` and `docs/participant_quickstart.md`.

## Evidence status
| Artifact | Status | Evidence |
|---|---|---|
| Prompt-generation scripts | Implemented | Source code and automated unit tests |
| Metric calculator | Implemented | Repeatable calculations with synthetic CSV |
| Business deployment | Not yet verified | Pilot documentation to be completed |
| Real productivity gains | Not yet measured | Baseline and post-pilot measurements required |
| Client testimonials | Not yet collected | Permission required |

See [demo walk-through](docs/demo_walkthrough.md), [pilot protocol](docs/pilot_protocol.md), and [privacy guidelines](docs/responsible_ai.md).

## Future releases (not yet implemented)
Customer support integrations, invoice extraction, live dashboard, connected Power Automate flows, and enterprise controls. They are not represented as completed features.

## License and use
MIT license. Templates and sample data are illustrative. Consult qualified advisers for regulatory or legal requirements. No customer or volunteer data should be placed in this repository.
