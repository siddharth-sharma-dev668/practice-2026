const crypto = require("crypto");

module.exports = async function handler(req, res) {
  if (req.method !== "POST") {
    res.status(405).json({ error: "Method not allowed" });
    return;
  }

  const {
    razorpay_order_id,
    razorpay_payment_id,
    razorpay_signature,
    name,
    email,
  } = req.body || {};

  if (!razorpay_order_id || !razorpay_payment_id || !razorpay_signature || !name || !email) {
    res.status(400).json({ error: "Missing verification fields" });
    return;
  }

  const expected = crypto
    .createHmac("sha256", process.env.RAZORPAY_KEY_SECRET)
    .update(razorpay_order_id + "|" + razorpay_payment_id)
    .digest("hex");

  if (expected !== razorpay_signature) {
    res.status(400).json({ error: "Signature mismatch" });
    return;
  }

  const site = "https://" + req.headers.host;
  const downloadUrl = site + "/dist/interview-launchpad.zip";

  const buyerEmail = {
    sender: { email: process.env.SENDER_EMAIL, name: "Interview Launchpad" },
    to: [{ email: email, name: name }],
    subject: "Your Interview Launchpad download",
    htmlContent: buildBuyerEmailHtml(name, downloadUrl),
  };
  const ownerEmail = {
    sender: { email: process.env.SENDER_EMAIL, name: "Interview Launchpad" },
    to: [{ email: process.env.NOTIFY_EMAIL, name: "Sid" }],
    subject: "New sale: " + name,
    htmlContent:
      "<p>" + name + " (" + email + ") paid. Payment id: " + razorpay_payment_id +
      ", order id: " + razorpay_order_id + ", time: " + new Date().toISOString() + "</p>",
  };

  try {
    await Promise.all([sendBrevoEmail(buyerEmail), sendBrevoEmail(ownerEmail)]);
  } catch (err) {
    // A verified payment must never be reported as failed to the buyer over an
    // email-provider hiccup — log it, Sid checks Vercel logs if a buyer reports
    // no email arrived.
    console.error("brevo send failed", err);
  }

  res.status(200).json({ verified: true });
};

async function sendBrevoEmail(payload) {
  const resp = await fetch("https://api.brevo.com/v3/smtp/email", {
    method: "POST",
    headers: {
      "api-key": process.env.BREVO_API_KEY,
      "content-type": "application/json",
    },
    body: JSON.stringify(payload),
  });
  if (!resp.ok) {
    const text = await resp.text();
    throw new Error("Brevo send failed: " + resp.status + " " + text);
  }
}

function buildBuyerEmailHtml(name, downloadUrl) {
  return (
    '<div style="font-family:Arial,sans-serif;line-height:1.6;color:#1a1a1a">' +
    "<h2>Thanks, " + name + " — here's your Interview Launchpad</h2>" +
    '<p><a href="' + downloadUrl + '">Download the app (zip file)</a></p>' +
    "<p>Unzip it anywhere permanent, then open <code>index.html</code> in your browser. No account, no install.</p>" +
    "<p><strong>To book your free 45-minute debrief:</strong> just reply to this email with a few times that work for you. Two slots a week, so book early — redeem within 90 days.</p>" +
    "<p>14-day refund, no questions asked — reply to this email with your payment id if it's not useful.</p>" +
    "<p>— Sid</p>" +
    "</div>"
  );
}
