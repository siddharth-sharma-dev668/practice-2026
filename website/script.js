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

  // Scroll-reveal
  var revealTargets = document.querySelectorAll("[data-reveal]");
  if ("IntersectionObserver" in window) {
    var observer = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add("is-visible");
            observer.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.12 }
    );
    revealTargets.forEach(function (el) { observer.observe(el); });
  } else {
    revealTargets.forEach(function (el) { el.classList.add("is-visible"); });
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
