# Public demo deployment

After the deployment workflow is merged, a repository administrator must open Settings → Pages → Build and deployment → Source and choose GitHub Actions. Then open Actions → Publish public demo → Run workflow on main. If the workflow triggered before configuration, run it again. Verify the published URL in the deployment job and visit it in a private browser window. Expected URL: https://fredoncyber.github.io/small-business-ai-enablement/ (not verified until deployment succeeds).

Only four web assets are published. No pilot records or private data belong in the repository. Public visitors should use fictional or approved sanitized inputs. No API key, analytics or live AI inference is included. GitHub hosting and browser/clipboard behavior remain outside the application's control.

## Acceptance checks
- Load the page in a private window and confirm styles and scripts load.
- Load both fictional scenarios, generate prompts, edit an input and confirm the old prompt clears.
- Verify default estimate: 15 minutes saved, 50% reduction, 5 hours/month, $125 gross, $105 net.
- Verify a slower assisted process reports negative savings.
- Clear all fields; check keyboard navigation, narrow screen layout and clipboard fallback.
- Confirm no application request transmits entered data.
