const Razorpay = require("razorpay");

module.exports = async function handler(req, res) {
  if (req.method !== "POST") {
    res.status(405).json({ error: "Method not allowed" });
    return;
  }

  const { name, email } = req.body || {};
  if (!name || !email) {
    res.status(400).json({ error: "Name and email are required" });
    return;
  }

  const instance = new Razorpay({
    key_id: process.env.RAZORPAY_KEY_ID,
    key_secret: process.env.RAZORPAY_KEY_SECRET,
  });

  try {
    const order = await instance.orders.create({
      amount: 499900, // ₹4,999 in paise — fixed here, never taken from the client
      currency: "INR",
      receipt: "launchpad_" + Date.now(),
      notes: { name, email },
    });
    res.status(200).json({
      order_id: order.id,
      key_id: process.env.RAZORPAY_KEY_ID,
      amount: order.amount,
    });
  } catch (err) {
    console.error("create-order failed", err);
    res.status(500).json({ error: "Could not create order" });
  }
};
