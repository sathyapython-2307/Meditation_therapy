// Add click event listeners to service cards
    document.addEventListener('DOMContentLoaded', function() {
        const serviceCards = document.querySelectorAll('.service-card');
        const mainContainer = document.getElementById('mainContainer');
        const familyTherapySection = document.getElementById('familyTherapySection');

        // Check URL for section=family
        const params = new URLSearchParams(window.location.search);
        if (params.get('section') === 'family') {
            mainContainer.style.display = 'none';
            familyTherapySection.style.display = 'block';
            window.scrollTo({ top: 0, behavior: 'smooth' });
        }

        serviceCards.forEach(card => {
            card.addEventListener('click', function(e) {
                e.preventDefault();
                const serviceType = this.getAttribute('data-service');
                // Show family therapy section when family service is clicked
                if (serviceType === 'family') {
                    mainContainer.style.display = 'none';
                    familyTherapySection.style.display = 'block';
                    window.scrollTo({ top: 0, behavior: 'smooth' });
                }
            });
        });
    });
    function goBack() {
        const mainContainer = document.getElementById('mainContainer');
        const familyTherapySection = document.getElementById('familyTherapySection');
        familyTherapySection.style.display = 'none';
        mainContainer.style.display = 'block';
        window.scrollTo({ top: 0, behavior: 'smooth' });
    }
