# Free-tier limits and the read cycle (R6, ADR-04)

Study Room Sniper · Isaam Memon · 11/8/26

## What has to fit

- The reader polls every room at least once every 2 minutes (QR-02), at no more than 20 library requests per minute (QR-05).
- Everything must cost nothing (CON-03), so the app and database run on managed free tiers (ADR-04).
- Risk R6: a free tier that sleeps when idle, or runs out of hours, requests or emails, would stop that cycle.

## Providers checked

| Provider | Idle sleep? | Monthly hours / quota | Scheduled jobs? | Breaks the 2-minute cycle? | Source (date checked) |
| --- | --- | --- | --- | --- | --- |
| Render (free web service) — app host | Yes: spins down after 15 min with no inbound traffic; ~1 min to wake | 750 free instance hours per workspace/month (one 24/7 service ≈ 720 h); all free services suspended if exceeded | Cron Jobs are paid ($1/month minimum per cron service), so they break CON-03. An in-process timer doesn't count as inbound traffic | Yes on its own: the timer stops when the service sleeps. No if an external trigger calls it every 2 min (see Cloudflare row). Render may also restart free services at any time (QR-02 risk) | render.com/docs/free; render.com/docs/cronjobs (8 Nov 2026) |
| Cloudflare Workers (free) — scheduler | No (no always-on server; runs per trigger) | 100,000 requests/day; 10 ms CPU per run; 5 Cron Triggers per account | Yes: Cron Triggers, 1-minute minimum | No: 720 runs/day, under 1% of quota. Each run calls Render's /cycle endpoint, which also keeps Render awake | developers.cloudflare.com/workers/platform/limits (8 Nov 2026) |
| Oracle Cloud Always Free VM — fallback | No sleep, but an instance idle for 7 days can be stopped/reclaimed (thresholds reported at <20% p95 CPU, network and memory) | Always Free: up to 4 Arm OCPUs total, 200 GB block storage | Yes: ordinary cron/systemd on the VM | No for timing. A light poller may look "idle", so reclamation is the risk | docs.oracle.com/en-us/iaas/Content/FreeTier/resourceref.htm (8 Nov 2026) |
| Resend (email) | n/a | 100 emails/day, 3,000/month; each To/CC/BCC recipient counts as one email | n/a | Yes at 100 recipients if each gets ≥1 alert/day; at QR-01's 200 active watches, almost certainly | resend.com/pricing; resend.com/docs/knowledge-base/what-is-resend-pricing (8 Nov 2026) |

## Finding

Render's free web service fits only when paired with a Cloudflare Workers Cron Trigger that calls it every 2 minutes. On its own, Render spins down after 15 minutes with no inbound traffic, and its own cron jobs cost $1/month (breaks CON-03). The external call keeps the service awake, uses about 720 of its 750 free hours a month, and uses under 1% of Cloudflare's 100,000 requests/day. GitHub Actions (5-minute minimum, often delayed) and Koyeb (sleeps after 1 hour idle) do not fit. For the database, use Supabase: Neon would run out of free compute hours under a 2-minute cycle, and Render's free Postgres expires after 30 days.

## Recommendation

R6 status: **closed**. Render (app) + Cloudflare Workers cron (scheduler) + Supabase (database) keeps the 2-minute read cycle at zero cost, so no change request to QR-02 is needed. Oracle Cloud Always Free is the fallback if Render proves unreliable. Two leftover risks go in the register:
- Render may restart free services at any time. The 14-day QR-02 trial will show whether this matters.
- Resend's free cap is 100 emails/day. The live service would hit it with about 100 students getting one alert a day, and QR-01's load of 200 active watches would go past it. Spread the 100-release QR-01 test over two days or send it to one test inbox.