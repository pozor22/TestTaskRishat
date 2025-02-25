document.addEventListener("DOMContentLoaded", function() {
    const buyButton = document.getElementById("buy-button");

    buyButton.addEventListener("click", async function() {
        try {
            const response = await fetch(`/buy/${itemId}/`);
            if (!response.ok) {
                throw new Error(`Ошибка HTTP: ${response.status}`);
            }
            const data = await response.json();

            const stripe = Stripe(stripePublicKey);
            stripe.redirectToCheckout({ sessionId: data.session_id });
        } catch (error) {
            console.error("Ошибка при покупке:", error);
        }
    });
});