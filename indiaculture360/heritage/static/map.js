

  // Animation for timeline items when they come into view
        document.addEventListener('DOMContentLoaded', function() {
            const timelineItems = document.querySelectorAll('.timeline-item');
            
            const observer = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        entry.target.style.animationPlayState = 'running';
                    }
                });
            }, { threshold: 0.3 });
            
            timelineItems.forEach(item => {
                observer.observe(item);
            });
            
            // Animation for story cards
            const storyCards = document.querySelectorAll('.story-card');
            
            const cardObserver = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        entry.target.style.animationPlayState = 'running';
                    }
                });
            }, { threshold: 0.2 });
            
            storyCards.forEach(card => {
                cardObserver.observe(card);
            });
        });
         document.addEventListener('DOMContentLoaded', function() {
            const animatedElements = document.querySelectorAll('.mission-content, .mission-image, .value-card, .team-member');
            
            const observer = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        entry.target.style.animationPlayState = 'running';
                    }
                });
            }, { threshold: 0.2 });
            
            animatedElements.forEach(element => {
                observer.observe(element);
            });
        });
        // Active navigation link
        document.querySelectorAll('.nav-links-contact a').forEach(link => {
            if(link.textContent === 'Contact') {
                link.classList.add('active');
                link.style.color = 'var(--accent)';
            }
        });


        // mission JavaScript//
          // Simple animation for mission cards when they come into view
        document.addEventListener('DOMContentLoaded', function() {
            const missionCards = document.querySelectorAll('.mission-card');
            
            const observer = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        entry.target.style.animation = 'mission-fadeInUp 1s ease forwards';
                        observer.unobserve(entry.target);
                    }
                });
            }, { threshold: 0.1 });
            
            missionCards.forEach(card => {
                observer.observe(card);
            });
        });