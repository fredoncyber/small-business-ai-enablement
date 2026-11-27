# Browser demonstration (v0.2)

Download or clone the repository, then open `web/index.html` in a modern browser. If local file restrictions prevent scripts or clipboard access, run `python3 -m http.server 8000 --bind 127.0.0.1 --directory web` from the repository root and open http://127.0.0.1:8000. Stop with Ctrl+C.

## Five-minute walkthrough
1. Load the fictional customer example and build a prompt. Show the missing Saturday hours and human approval requirement.
2. Copy into an approved AI tool and inspect its response; correct unsupported claims before sending.
3. Load the fictional operations example. Generate a prompt with unknowns and review points.
4. Calculate the default illustrative estimate: 30 vs 15 minutes, 20 monthly tasks, $25/hour, $20 monthly tool cost. Estimated net labor value: $105/month, not verified cash savings.
5. Try a slower assisted process and confirm negative results; clear inputs.

## Boundaries
No model call, analytics, storage, integrations or automatic sends. Prompt instructions are not a technical guarantee against hallucination or injection. Clipboard and third-party AI services are outside app control. Use sanitized data and human review.

## Validation
Run `node --test web/core.test.js` with Node 22 and `python3 -m unittest discover -s tests -v`. CI tests core functions and CLI commands; manual browser walkthrough is separate. No real client deployment or outcomes claimed.
