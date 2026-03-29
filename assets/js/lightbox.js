
document.addEventListener('DOMContentLoaded', () => {
    const galleryItems = document.querySelectorAll('.gallery-item');
    const modal = document.querySelector('.lightbox-modal');
    const modalImg = modal.querySelector('.lightbox-content img');
    const closeModal = modal.querySelector('.lightbox-close');

    galleryItems.forEach(item => {
        item.addEventListener('click', (e) => {
            e.preventDefault();
            modalImg.src = e.target.src;
            modal.classList.add('visible');
        });
    });

    closeModal.addEventListener('click', () => {
        modal.classList.remove('visible');
    });

    modal.addEventListener('click', (e) => {
        if (e.target === modal) {
            modal.classList.remove('visible');
        }
    });
});
