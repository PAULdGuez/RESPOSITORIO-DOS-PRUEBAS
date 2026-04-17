# E2E Pipeline Flow

## Linear -> n8n -> Odoo

1. Linear sends webhook on issue change
2. n8n validates and forwards to Odoo
3. Odoo creates/updates project.task
4. Commits link via [GOJ-XXX] identifier
5. Cron generates AI Timesheet summary
