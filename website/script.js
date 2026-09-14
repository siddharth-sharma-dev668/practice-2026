(function () {
  "use strict";

  // Mobile nav toggle
  var navToggle = document.getElementById("nav-toggle");
  var siteNav = document.getElementById("site-nav");
  navToggle.addEventListener("click", function () {
    var isOpen = siteNav.classList.toggle("is-open");
    navToggle.setAttribute("aria-expanded", isOpen ? "true" : "false");
  });
  siteNav.querySelectorAll("a").forEach(function (link) {
    link.addEventListener("click", function () {
      siteNav.classList.remove("is-open");
      navToggle.setAttribute("aria-expanded", "false");
    });
  });

  // Hero diagnostic readout: one deliberate on-load moment, not a scroll effect.
  var readoutNum = document.getElementById("readout-num");
  var readoutFill = document.getElementById("readout-fill");
  var targetScore = 62;
  var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  if (readoutNum && readoutFill) {
    if (reduceMotion) {
      readoutNum.textContent = String(targetScore);
      readoutFill.style.width = targetScore + "%";
    } else {
      requestAnimationFrame(function () {
        readoutFill.style.width = targetScore + "%";
      });
      var start = null;
      var duration = 900;
      function tick(ts) {
        if (start === null) start = ts;
        var progress = Math.min((ts - start) / duration, 1);
        readoutNum.textContent = String(Math.round(progress * targetScore));
        if (progress < 1) requestAnimationFrame(tick);
      }
      requestAnimationFrame(tick);
    }
  }

  // Buy flow
  var form = document.getElementById("buy-form");
  var submitBtn = document.getElementById("buy-submit");
  var statusEl = document.getElementById("buy-status");

  function setStatus(text, kind) {
    statusEl.textContent = text;
    statusEl.className = "buy-status" + (kind ? " " + kind : "");
  }

  form.addEventListener("submit", function (e) {
    e.preventDefault();
    var name = document.getElementById("buy-name").value.trim();
    var email = document.getElementById("buy-email").value.trim();
    if (!name || !email) {
      setStatus("Please fill in both fields.", "error");
      return;
    }

    submitBtn.disabled = true;
    setStatus("Starting checkout…", "pending");

    fetch("/api/create-order", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ name: name, email: email }),
    })
      .then(function (res) {
        if (!res.ok) throw new Error("create-order-failed");
        return res.json();
      })
      .then(function (order) {
        var rzp = new Razorpay({
          key: order.key_id,
          order_id: order.order_id,
          amount: order.amount,
          currency: "INR",
          name: "Interview Launchpad",
          description: "App + live debrief + 12 months of updates",
          prefill: { name: name, email: email },
          theme: { color: "#3730a3" },
          handler: function (response) {
            setStatus("Verifying payment…", "pending");
            fetch("/api/verify-payment", {
              method: "POST",
              headers: { "Content-Type": "application/json" },
              body: JSON.stringify({
                razorpay_order_id: response.razorpay_order_id,
                razorpay_payment_id: response.razorpay_payment_id,
                razorpay_signature: response.razorpay_signature,
                name: name,
                email: email,
              }),
            })
              .then(function (res) {
                if (!res.ok) throw new Error("verify-failed");
                return res.json();
              })
              .then(function () {
                setStatus(
                  "Payment verified — check your email for your download link and booking instructions.",
                  "success"
                );
                form.reset();
              })
              .catch(function () {
                setStatus(
                  "Payment went through but we couldn't confirm it automatically. Email launchpadinterview@gmail.com with your payment id and we'll sort it out.",
                  "error"
                );
              })
              .finally(function () {
                submitBtn.disabled = false;
              });
          },
          modal: {
            ondismiss: function () {
              setStatus("Checkout closed. No payment was made.", "");
              submitBtn.disabled = false;
            },
          },
        });
        rzp.open();
      })
      .catch(function () {
        setStatus("Couldn't start checkout — please retry or email support.", "error");
        submitBtn.disabled = false;
      });
  });
})();
