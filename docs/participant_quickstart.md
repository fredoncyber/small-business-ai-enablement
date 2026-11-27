# Participant quickstart — draft a safe customer reply
1. Pick a repeated question, such as "Can I book on Saturday?"
2. Identify business-approved facts. If Saturday hours are unknown, leave them unknown.
3. Run `python3 src/toolkit.py inquiry --question 'Can I book on Saturday?' --facts examples/approved_business_facts.txt` or use the equivalent template in `prompts/customer_inquiry.md`.
4. Review the resulting text; enter only sanitized, approved inputs into an organization-approved AI tool.
5. Check the output for invented claims and incorrect details. Have a person approve it before sending.
6. Time the whole process **including review**. Record it privately, compare with the manual baseline, and improve the instructions.
