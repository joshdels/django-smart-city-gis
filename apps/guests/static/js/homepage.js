document.addEventListener("DOMContentLoaded", () => {
    const heroImage = document.querySelector(".hero-images");

    const images = [
        "/static/images/webgis5.jpeg",
        "/static/images/autocad.jpg",
        "/static/images/QGIS-residus.jpg",
        "/static/images/webgis_3.png",
        "/static/images/buildings.png",
        "/static/images/clup.jpg",
        "/static/images/coding.png",
        "/static/images/coding2.png",
        "/static/images/model-builder.jpg",
        "/static/images/db.png",
        "/static/images/city-planning.jpg",
        
    ];

    let current = 0;

    heroImage.classList.add("zoom");

    setInterval(() => {
        heroImage.style.opacity = "0";

        setTimeout(() => {
            current = (current + 1) % images.length;
            heroImage.src = images[current];
            heroImage.style.opacity = "1";
        }, 500);
    }, 5000);
});