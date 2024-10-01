document.addEventListener("DOMContentLoaded", function() {
    const forms = document.querySelectorAll('.add-to-cart-form');

    forms.forEach(form => {
        form.addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent the default form submission

            const productId = this.getAttribute('data-product-id');
            const csrfToken = this.querySelector('input[name="csrfmiddlewaretoken"]').value;

            // Send the AJAX request to add the product to the cart
            fetch(`/add_to_cart/${productId}/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrfToken
                },
                body: JSON.stringify({ product_id: productId }) // Optional payload
            })
            .then(response => {
                if (response.ok) {
                    // Optionally, update cart display or show a notification
                    console.log('Product added to cart successfully!');

                    // Update the cart count
                    updateCartCount();
                } else {
                    console.error('Error adding product to cart.');
                }
            })
            .catch(error => {
                console.error('Fetch error:', error);
            });
        });
    });

    // Function to update the cart count
    function updateCartCount() {
        const cartCountElement = document.getElementById('cart-count');
        const currentCount = parseInt(cartCountElement.textContent) || 0; // Get current count or default to 0
        cartCountElement.textContent = currentCount + 1; // Increment count
    }
});
