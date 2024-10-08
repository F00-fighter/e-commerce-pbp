document.addEventListener("DOMContentLoaded", function() {
    const removeForms = document.querySelectorAll('.remove-from-cart-form');

    removeForms.forEach(form => {
        form.addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent the default form submission

            const productId = this.getAttribute('data-product-id');
            const csrfToken = this.querySelector('input[name="csrfmiddlewaretoken"]').value;

            // Send the AJAX request to remove the product from the cart
            fetch(`/remove_from_cart/${productId}/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrfToken
                }
            })
            .then(response => response.json())
            .then(data => {
                if (data.status === 'success') {
                    // Remove the product item from the DOM
                    this.closest('.cart-item').remove();

                    // Update total items count
                    const totalItemsElement = document.querySelector('.cart-summary p:first-child');
                    totalItemsElement.textContent = `Total Items: ${data.total_items}`;

                    // Update total price displayed
                    const totalPriceElement = document.querySelector('.cart-summary p:nth-child(2)');
                    totalPriceElement.textContent = `Estimated total $${data.total_price.toFixed(2)}`;

                    // Check if cart is empty
                    if (data.total_items === 0) {
                        document.querySelector('.cart-items').innerHTML = '<p>Your cart is empty!</p>';
                          // Remove the cart summary div
                        document.querySelector('.cart-summary').remove();
                    }

                    console.log('Product removed from cart successfully!');
                } else {
                    console.error('Error removing product from cart:', data.message);
                }
            })
            .catch(error => {
                console.error('Fetch error:', error);
            });
        });
    });
});
