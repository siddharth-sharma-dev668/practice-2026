# Interview Launchpad — sales website

Static sales page + Razorpay checkout + auto-delivery email. Deployed on Vercel from this folder.

## One-time setup (all done in your own browser, your own accounts)

1. **Connect to Vercel:** vercel.com → New Project → Import the `lauchpad` GitHub repo → set **Root Directory** to `website` → Deploy. No password needed, it's GitHub OAuth.
2. **Razorpay:** sign in at dashboard.razorpay.com → Settings → API Keys → generate a **test mode** key pair first. Copy the Key ID and Key Secret.
3. **Brevo (email sending):** sign up at brevo.com (free tier, no domain purchase needed) → Senders → add and verify `launchpadinterview@gmail.com` as a single sender → Settings → SMTP & API → create an API key.
4. **Set environment variables** in Vercel: Project → Settings → Environment Variables. Add all five, then redeploy:

   | Name | Value |
   |---|---|
   | `RAZORPAY_KEY_ID` | from Razorpay dashboard |
   | `RAZORPAY_KEY_SECRET` | from Razorpay dashboard |
   | `BREVO_API_KEY` | from Brevo dashboard |
   | `SENDER_EMAIL` | `launchpadinterview@gmail.com` |
   | `NOTIFY_EMAIL` | `launchpadinterview@gmail.com` |

## Testing before going live

1. With Razorpay **test-mode** keys still in place, open the deployed Vercel URL, fill the buy form, and pay with a [Razorpay test card](https://razorpay.com/docs/payments/payments/test-card-details/).
2. Confirm the success message appears, and that both the buyer email and the owner-notification email actually arrive (check Brevo's dashboard logs if not).
3. Only after that works end to end: switch the Razorpay dashboard from test mode to live mode, generate **live** API keys, and replace `RAZORPAY_KEY_ID`/`RAZORPAY_KEY_SECRET` in Vercel with the live values.

## Updating the product file later

If `product/app/index.html` changes, rebuild the zip (see `product/README.md`) and copy the new zip over `website/dist/interview-launchpad.zip`, then push — Vercel redeploys automatically.
