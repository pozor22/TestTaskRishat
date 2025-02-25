document.addEventListener("DOMContentLoaded", function() {
    const payButton = document.getElementById("pay-button");

    payButton.addEventListener("click", async function() {
        try {
            const response = await fetch(`/buy_order/${orderId}/`);
            if (!response.ok) {
                throw new Error(`Ошибка HTTP: ${response.status}`);
            }
            const data = await response.json();

            const stripe = Stripe(stripePublicKey);
            stripe.redirectToCheckout({ sessionId: data.session_id });
        } catch (error) {
            console.error("Ошибка при оплате:", error);
        }
    });
});
